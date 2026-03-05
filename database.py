"""
database.py — Form 25 VARPE
Funcionários = usuários do sistema (mesma tabela, com senha_hash e is_admin).
"""

import json
import sqlite3

from werkzeug.security import check_password_hash, generate_password_hash

DB_PATH = "form25.db"


# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def _add_column_if_missing(conn, table, column, definition):
    cols = [r[1] for r in conn.execute(f"PRAGMA table_info({table})").fetchall()]
    if column not in cols:
        conn.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")


# ─────────────────────────────────────────────────────────────────────────────
# init_db
# ─────────────────────────────────────────────────────────────────────────────

def init_db():
    conn = get_db()

    # ── Funcionários / Usuários ───────────────────────────────────────────────
    conn.execute("""
        CREATE TABLE IF NOT EXISTS funcionarios (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            nome       TEXT NOT NULL UNIQUE,
            senha_hash TEXT,
            is_admin   INTEGER DEFAULT 0,
            ativo      INTEGER DEFAULT 1,
            created_at TEXT DEFAULT (datetime('now','localtime'))
        )
    """)
    # Colunas extras para bases já existentes sem esses campos
    _add_column_if_missing(conn, "funcionarios", "senha_hash", "TEXT")
    _add_column_if_missing(conn, "funcionarios", "is_admin",   "INTEGER DEFAULT 0")

    # ── Registros ─────────────────────────────────────────────────────────────
    conn.execute("""
        CREATE TABLE IF NOT EXISTS registros (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente       TEXT,
            op            TEXT,
            ns            TEXT,
            modelo        TEXT,
            data          TEXT,
            producao      TEXT,
            responsavel   TEXT,
            respostas     TEXT DEFAULT '{}',
            created_at    TEXT DEFAULT (datetime('now','localtime')),
            updated_at    TEXT DEFAULT (datetime('now','localtime'))
        )
    """)
    _add_column_if_missing(conn, "registros", "encerrado",            "INTEGER DEFAULT 0")
    _add_column_if_missing(conn, "registros", "assinatura_qualidade", "TEXT")
    _add_column_if_missing(conn, "registros", "assinatura_producao",  "TEXT")
    _add_column_if_missing(conn, "registros", "criado_por_id",        "INTEGER")
    _add_column_if_missing(conn, "registros", "encerrado_em",         "TEXT")

    # ── Checklist dinâmico ────────────────────────────────────────────────────
    conn.execute("""
        CREATE TABLE IF NOT EXISTS secoes (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT NOT NULL UNIQUE,
            nome   TEXT NOT NULL,
            ordem  INTEGER DEFAULT 0,
            ativo  INTEGER DEFAULT 1
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS subsecoes (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            secao_id INTEGER NOT NULL REFERENCES secoes(id),
            codigo   TEXT NOT NULL UNIQUE,
            nome     TEXT NOT NULL,
            ordem    INTEGER DEFAULT 0,
            ativo    INTEGER DEFAULT 1
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS itens_checklist (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            secao_id    INTEGER REFERENCES secoes(id),
            subsecao_id INTEGER REFERENCES subsecoes(id),
            codigo      TEXT NOT NULL UNIQUE,
            descricao   TEXT NOT NULL,
            tem_medicao INTEGER DEFAULT 0,
            ordem       INTEGER DEFAULT 0,
            ativo       INTEGER DEFAULT 1
        )
    """)

    conn.commit()

    # ── Seeds ─────────────────────────────────────────────────────────────────
    _seed_funcionarios(conn)
    _seed_checklist(conn)

    conn.commit()
    conn.close()


def _seed_funcionarios(conn):
    count = conn.execute("SELECT COUNT(*) FROM funcionarios").fetchone()[0]
    if count == 0:
        # Cria Admin padrão
        conn.execute(
            "INSERT INTO funcionarios (nome, senha_hash, is_admin) VALUES (?, ?, 1)",
            ("Admin", generate_password_hash("admin123")),
        )
        # Funcionários padrão sem senha (serão definidas pelo admin)
        for nome in ["Eleomar", "Giovani", "Israel", "Marcos", "Ronaldo", "Wagner"]:
            conn.execute("INSERT INTO funcionarios (nome) VALUES (?)", (nome,))
    else:
        # Garante que exista pelo menos um Admin
        admin_count = conn.execute(
            "SELECT COUNT(*) FROM funcionarios WHERE is_admin=1"
        ).fetchone()[0]
        if admin_count == 0:
            conn.execute(
                "INSERT OR IGNORE INTO funcionarios (nome, senha_hash, is_admin) VALUES (?, ?, 1)",
                ("Admin", generate_password_hash("admin123")),
            )


def _seed_checklist(conn):
    count = conn.execute("SELECT COUNT(*) FROM secoes").fetchone()[0]
    if count > 0:
        return
    from checklist_data import CHECKLIST

    for ordem_s, secao in enumerate(CHECKLIST):
        cur = conn.execute(
            "INSERT INTO secoes (codigo, nome, ordem) VALUES (?, ?, ?)",
            (secao["id"], secao["nome"], ordem_s),
        )
        secao_db_id = cur.lastrowid

        if "subsecoes" in secao:
            for ordem_sub, sub in enumerate(secao["subsecoes"]):
                cur2 = conn.execute(
                    "INSERT INTO subsecoes (secao_id, codigo, nome, ordem) VALUES (?, ?, ?, ?)",
                    (secao_db_id, sub["id"], sub["nome"], ordem_sub),
                )
                sub_db_id = cur2.lastrowid
                for ordem_i, item in enumerate(sub["itens"]):
                    conn.execute(
                        """INSERT INTO itens_checklist
                           (secao_id, subsecao_id, codigo, descricao, tem_medicao, ordem)
                           VALUES (?, ?, ?, ?, ?, ?)""",
                        (secao_db_id, sub_db_id, item["id"], item["desc"],
                         1 if item.get("medicao") else 0, ordem_i),
                    )
        else:
            for ordem_i, item in enumerate(secao["itens"]):
                conn.execute(
                    """INSERT INTO itens_checklist
                       (secao_id, subsecao_id, codigo, descricao, tem_medicao, ordem)
                       VALUES (?, ?, ?, ?, ?, ?)""",
                    (secao_db_id, None, item["id"], item["desc"],
                     1 if item.get("medicao") else 0, ordem_i),
                )


# ─────────────────────────────────────────────────────────────────────────────
# Auth / Funcionários
# ─────────────────────────────────────────────────────────────────────────────

def verificar_login(nome, senha_plain):
    conn = get_db()
    row = conn.execute(
        "SELECT * FROM funcionarios WHERE nome=? AND ativo=1", (nome,)
    ).fetchone()
    conn.close()
    if not row:
        return None
    if not row["senha_hash"]:
        return None  # sem senha cadastrada
    if check_password_hash(row["senha_hash"], senha_plain):
        return dict(row)
    return None


def listar_funcionarios(apenas_ativos=False):
    conn = get_db()
    if apenas_ativos:
        rows = conn.execute(
            "SELECT * FROM funcionarios WHERE ativo=1 ORDER BY is_admin DESC, nome"
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT * FROM funcionarios ORDER BY ativo DESC, is_admin DESC, nome"
        ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def obter_funcionario(func_id):
    conn = get_db()
    row = conn.execute("SELECT * FROM funcionarios WHERE id=?", (func_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def criar_funcionario(nome, senha_plain=None, is_admin=False):
    conn = get_db()
    try:
        senha_hash = generate_password_hash(senha_plain) if senha_plain else None
        conn.execute(
            "INSERT INTO funcionarios (nome, senha_hash, is_admin) VALUES (?, ?, ?)",
            (nome.strip(), senha_hash, 1 if is_admin else 0),
        )
        conn.commit()
        return True, None
    except Exception:
        return False, "Já existe um funcionário com esse nome."
    finally:
        conn.close()


def atualizar_funcionario(func_id, nome, ativo, is_admin=None, senha_plain=None):
    conn = get_db()
    try:
        if senha_plain and is_admin is not None:
            conn.execute(
                "UPDATE funcionarios SET nome=?, ativo=?, is_admin=?, senha_hash=? WHERE id=?",
                (nome.strip(), 1 if ativo else 0, 1 if is_admin else 0,
                 generate_password_hash(senha_plain), func_id),
            )
        elif senha_plain:
            conn.execute(
                "UPDATE funcionarios SET nome=?, ativo=?, senha_hash=? WHERE id=?",
                (nome.strip(), 1 if ativo else 0, generate_password_hash(senha_plain), func_id),
            )
        elif is_admin is not None:
            conn.execute(
                "UPDATE funcionarios SET nome=?, ativo=?, is_admin=? WHERE id=?",
                (nome.strip(), 1 if ativo else 0, 1 if is_admin else 0, func_id),
            )
        else:
            conn.execute(
                "UPDATE funcionarios SET nome=?, ativo=? WHERE id=?",
                (nome.strip(), 1 if ativo else 0, func_id),
            )
        conn.commit()
        return True, None
    except Exception:
        return False, "Já existe um funcionário com esse nome."
    finally:
        conn.close()


def funcionario_em_uso(func_id):
    conn = get_db()
    func = conn.execute("SELECT nome FROM funcionarios WHERE id=?", (func_id,)).fetchone()
    if not func:
        conn.close()
        return False
    nome = func["nome"]
    row = conn.execute(
        "SELECT COUNT(*) FROM registros WHERE respostas LIKE ?",
        (f'%"responsavel": "{nome}"%',),
    ).fetchone()
    # Também verifica marcado_por_id
    rows2 = conn.execute("SELECT respostas FROM registros").fetchall()
    conn.close()
    if row[0] > 0:
        return True
    for r in rows2:
        resp = json.loads(r["respostas"] or "{}")
        for v in resp.values():
            if v.get("marcado_por_id") == func_id:
                return True
    return False


def excluir_funcionario(func_id):
    conn = get_db()
    conn.execute("DELETE FROM funcionarios WHERE id=?", (func_id,))
    conn.commit()
    conn.close()


def inativar_funcionario(func_id):
    conn = get_db()
    conn.execute("UPDATE funcionarios SET ativo=0 WHERE id=?", (func_id,))
    conn.commit()
    conn.close()


# ─────────────────────────────────────────────────────────────────────────────
# Checklist dinâmico
# ─────────────────────────────────────────────────────────────────────────────

def listar_checklist_db():
    """Return nested checklist matching old CHECKLIST format (ativo only)."""
    conn = get_db()
    secoes = conn.execute(
        "SELECT * FROM secoes WHERE ativo=1 ORDER BY ordem, id"
    ).fetchall()
    result = []
    for secao in secoes:
        s = {"id": secao["codigo"], "nome": secao["nome"], "_db_id": secao["id"]}
        subs = conn.execute(
            "SELECT * FROM subsecoes WHERE secao_id=? AND ativo=1 ORDER BY ordem, id",
            (secao["id"],),
        ).fetchall()
        if subs:
            s["subsecoes"] = []
            for sub in subs:
                sub_d = {"id": sub["codigo"], "nome": sub["nome"],
                         "_db_id": sub["id"], "itens": []}
                itens = conn.execute(
                    "SELECT * FROM itens_checklist WHERE subsecao_id=? AND ativo=1 ORDER BY ordem, id",
                    (sub["id"],),
                ).fetchall()
                for item in itens:
                    sub_d["itens"].append({
                        "id": item["codigo"],
                        "desc": item["descricao"],
                        "medicao": bool(item["tem_medicao"]),
                        "_db_id": item["id"],
                    })
                s["subsecoes"].append(sub_d)
        else:
            itens = conn.execute(
                """SELECT * FROM itens_checklist
                   WHERE secao_id=? AND subsecao_id IS NULL AND ativo=1
                   ORDER BY ordem, id""",
                (secao["id"],),
            ).fetchall()
            s["itens"] = []
            for item in itens:
                s["itens"].append({
                    "id": item["codigo"],
                    "desc": item["descricao"],
                    "medicao": bool(item["tem_medicao"]),
                    "_db_id": item["id"],
                })
        result.append(s)
    conn.close()
    return result


def get_all_item_codes_db():
    conn = get_db()
    rows = conn.execute(
        "SELECT codigo FROM itens_checklist WHERE ativo=1"
    ).fetchall()
    conn.close()
    return [r["codigo"] for r in rows]


def get_item_desc_map():
    conn = get_db()
    rows = conn.execute(
        "SELECT codigo, descricao FROM itens_checklist WHERE ativo=1"
    ).fetchall()
    conn.close()
    return {r["codigo"]: r["descricao"] for r in rows}


# Seções
def listar_secoes(apenas_ativas=False):
    conn = get_db()
    q = ("SELECT * FROM secoes WHERE ativo=1 ORDER BY ordem, id" if apenas_ativas
         else "SELECT * FROM secoes ORDER BY ordem, id")
    rows = conn.execute(q).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def obter_secao(secao_id):
    conn = get_db()
    row = conn.execute("SELECT * FROM secoes WHERE id=?", (secao_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def criar_secao(codigo, nome, ordem):
    conn = get_db()
    try:
        conn.execute(
            "INSERT INTO secoes (codigo, nome, ordem) VALUES (?, ?, ?)",
            (codigo.strip(), nome.strip(), ordem),
        )
        conn.commit()
        return True, None
    except Exception:
        return False, "Código já existe."
    finally:
        conn.close()


def atualizar_secao(secao_id, nome, ordem, ativo):
    conn = get_db()
    conn.execute(
        "UPDATE secoes SET nome=?, ordem=?, ativo=? WHERE id=?",
        (nome.strip(), ordem, 1 if ativo else 0, secao_id),
    )
    conn.commit()
    conn.close()


# Subseções
def listar_subsecoes(secao_id=None, apenas_ativas=False):
    conn = get_db()
    conds, params = [], []
    if secao_id:
        conds.append("secao_id=?")
        params.append(secao_id)
    if apenas_ativas:
        conds.append("ativo=1")
    where = f"WHERE {' AND '.join(conds)}" if conds else ""
    rows = conn.execute(
        f"SELECT * FROM subsecoes {where} ORDER BY ordem, id", params
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def obter_subsecao(sub_id):
    conn = get_db()
    row = conn.execute("SELECT * FROM subsecoes WHERE id=?", (sub_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def criar_subsecao(secao_id, codigo, nome, ordem):
    conn = get_db()
    try:
        conn.execute(
            "INSERT INTO subsecoes (secao_id, codigo, nome, ordem) VALUES (?, ?, ?, ?)",
            (secao_id, codigo.strip(), nome.strip(), ordem),
        )
        conn.commit()
        return True, None
    except Exception:
        return False, "Código já existe."
    finally:
        conn.close()


def atualizar_subsecao(sub_id, nome, ordem, ativo):
    conn = get_db()
    conn.execute(
        "UPDATE subsecoes SET nome=?, ordem=?, ativo=? WHERE id=?",
        (nome.strip(), ordem, 1 if ativo else 0, sub_id),
    )
    conn.commit()
    conn.close()


# Itens
def listar_itens_admin(secao_id=None, subsecao_id=None):
    conn = get_db()
    conds, params = [], []
    if secao_id is not None:
        conds.append("secao_id=?")
        params.append(secao_id)
    if subsecao_id is not None:
        conds.append("subsecao_id=?")
        params.append(subsecao_id)
    where = f"WHERE {' AND '.join(conds)}" if conds else ""
    rows = conn.execute(
        f"SELECT * FROM itens_checklist {where} ORDER BY ordem, id", params
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def obter_item_checklist(item_id):
    conn = get_db()
    row = conn.execute("SELECT * FROM itens_checklist WHERE id=?", (item_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def criar_item_checklist(secao_id, subsecao_id, codigo, descricao, tem_medicao, ordem):
    conn = get_db()
    try:
        conn.execute(
            """INSERT INTO itens_checklist
               (secao_id, subsecao_id, codigo, descricao, tem_medicao, ordem)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (secao_id or None, subsecao_id or None, codigo.strip(),
             descricao.strip(), 1 if tem_medicao else 0, ordem),
        )
        conn.commit()
        return True, None
    except Exception:
        return False, "Código já existe."
    finally:
        conn.close()


def atualizar_item_checklist(item_id, descricao, tem_medicao, ordem, ativo):
    conn = get_db()
    conn.execute(
        "UPDATE itens_checklist SET descricao=?, tem_medicao=?, ordem=?, ativo=? WHERE id=?",
        (descricao.strip(), 1 if tem_medicao else 0, ordem, 1 if ativo else 0, item_id),
    )
    conn.commit()
    conn.close()


def item_checklist_em_uso(codigo):
    conn = get_db()
    rows = conn.execute("SELECT respostas FROM registros").fetchall()
    conn.close()
    for row in rows:
        respostas = json.loads(row["respostas"] or "{}")
        if codigo in respostas:
            return True
    return False


# ─────────────────────────────────────────────────────────────────────────────
# Registros
# ─────────────────────────────────────────────────────────────────────────────

def listar_registros(busca=None):
    conn = get_db()
    if busca:
        like = f"%{busca}%"
        rows = conn.execute(
            """SELECT r.*, f.nome as criado_por_nome
               FROM registros r LEFT JOIN funcionarios f ON r.criado_por_id = f.id
               WHERE r.cliente LIKE ? OR r.op LIKE ? OR r.ns LIKE ?
                  OR r.modelo LIKE ? OR r.responsavel LIKE ?
               ORDER BY r.id DESC""",
            (like, like, like, like, like),
        ).fetchall()
    else:
        rows = conn.execute(
            """SELECT r.*, f.nome as criado_por_nome
               FROM registros r LEFT JOIN funcionarios f ON r.criado_por_id = f.id
               ORDER BY r.id DESC"""
        ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def obter_registro(registro_id):
    conn = get_db()
    row = conn.execute(
        "SELECT * FROM registros WHERE id=?", (registro_id,)
    ).fetchone()
    conn.close()
    if row:
        r = dict(row)
        r["respostas"] = json.loads(r["respostas"] or "{}")
        return r
    return None


def criar_registro(dados, respostas, criado_por_id=None):
    conn = get_db()
    cur = conn.execute(
        """INSERT INTO registros
           (cliente, op, ns, modelo, data, producao, responsavel, respostas, criado_por_id)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            dados.get("cliente", ""),
            dados.get("op", ""),
            dados.get("ns", ""),
            dados.get("modelo", ""),
            dados.get("data", ""),
            dados.get("producao", ""),
            dados.get("responsavel", ""),
            json.dumps(respostas, ensure_ascii=False),
            criado_por_id,
        ),
    )
    conn.commit()
    novo_id = cur.lastrowid
    conn.close()
    return novo_id


def atualizar_registro(registro_id, dados, respostas):
    conn = get_db()
    conn.execute(
        """UPDATE registros
           SET cliente=?, op=?, ns=?, modelo=?, data=?, producao=?, responsavel=?,
               respostas=?, updated_at=datetime('now','localtime')
           WHERE id=?""",
        (
            dados.get("cliente", ""),
            dados.get("op", ""),
            dados.get("ns", ""),
            dados.get("modelo", ""),
            dados.get("data", ""),
            dados.get("producao", ""),
            dados.get("responsavel", ""),
            json.dumps(respostas, ensure_ascii=False),
            registro_id,
        ),
    )
    conn.commit()
    conn.close()


def excluir_registro(registro_id):
    conn = get_db()
    conn.execute("DELETE FROM registros WHERE id=?", (registro_id,))
    conn.commit()
    conn.close()


def encerrar_registro(registro_id, assin_qualidade, assin_producao):
    conn = get_db()
    conn.execute(
        """UPDATE registros
           SET encerrado=1, assinatura_qualidade=?, assinatura_producao=?,
               encerrado_em=datetime('now','localtime'),
               updated_at=datetime('now','localtime')
           WHERE id=?""",
        (assin_qualidade, assin_producao, registro_id),
    )
    conn.commit()
    conn.close()


def reabrir_registro(registro_id):
    conn = get_db()
    conn.execute("UPDATE registros SET encerrado=0 WHERE id=?", (registro_id,))
    conn.commit()
    conn.close()


def limpar_item_resposta(registro_id, codigo):
    conn = get_db()
    row = conn.execute("SELECT respostas FROM registros WHERE id=?", (registro_id,)).fetchone()
    if not row:
        conn.close()
        return
    respostas = json.loads(row["respostas"] or "{}")
    respostas.pop(codigo, None)
    conn.execute(
        "UPDATE registros SET respostas=? WHERE id=?",
        (json.dumps(respostas, ensure_ascii=False), registro_id),
    )
    conn.commit()
    conn.close()
