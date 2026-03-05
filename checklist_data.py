FUNCIONARIOS = ["Eleomar", "Giovani", "Israel", "Marcos", "Ronaldo", "Wagner"]

CHECKLIST = [
    {
        "id": "1",
        "nome": "BÁSICO",
        "subsecoes": [
            {
                "id": "1.1",
                "nome": "ESTRUTURA / CHASSI",
                "itens": [
                    {"id": "1.1.1", "desc": "Verificar bases de sustentação"},
                    {"id": "1.1.2", "desc": "Limpeza em geral"},
                    {"id": "1.1.3", "desc": "Aparência da estrutura"},
                    {"id": "1.1.4", "desc": "Reforços adicionais já instalados conforme projeto"},
                    {"id": "1.1.5", "desc": "Furos e cavidades da estrutura"},
                    {"id": "1.1.6", "desc": "Proteções das arestas vivas"},
                    {"id": "1.1.7", "desc": "Encaixe de peças na estrutura (Almofada, placa de montagem)"},
                    {"id": "1.1.8", "desc": "Colocação de parafusos, arruelas e porcas em geral"},
                    {"id": "1.1.9", "desc": "Travamento dos parafusos em geral"},
                    {"id": "1.1.10", "desc": "Aparência dos conectores e cabos"},
                    {"id": "1.1.11", "desc": "Aparência de furos de fixação das chapas"},
                    {"id": "1.1.12", "desc": "Verificar se não falta nenhum componente"},
                ],
            },
            {
                "id": "1.2",
                "nome": "ACIONAMENTO PRINCIPAL",
                "itens": [
                    {"id": "1.2.1", "desc": "Posicionamento do transportador com relação à máquina"},
                    {"id": "1.2.2", "desc": "Espaçamento do transportador"},
                    {"id": "1.2.3", "desc": "Alinhamento do transportador"},
                    {"id": "1.2.4", "desc": "Nivelamento do transportador"},
                    {"id": "1.2.5", "desc": "Aparência das correntes e eixos"},
                    {"id": "1.2.6", "desc": "Ruído das correntes"},
                    {"id": "1.2.7", "desc": "Fixação dos mancais do transportador"},
                    {"id": "1.2.8", "desc": "Travamento de porcas dos mancais"},
                    {"id": "1.2.9", "desc": "Fixação do motor do transportador na campana"},
                    {"id": "1.2.10", "desc": "Fixação da polia motriz e movida"},
                    {"id": "1.2.11", "desc": "Travamento dos parafusos"},
                    {"id": "1.2.12", "desc": "Aparência dos puxadores da correia"},
                    {"id": "1.2.13", "desc": "Funcionamento do transportador"},
                    {"id": "1.2.14", "desc": "Verificar folga lateral do transportador"},
                    {"id": "1.2.15", "desc": "Verificar alinhamento e ruído do redutor"},
                    {"id": "1.2.16", "desc": "Testar funcionamento correto do transportador"},
                ],
            },
            {
                "id": "1.3",
                "nome": "ELEVADOR",
                "itens": [
                    {"id": "1.3.1", "desc": "Alinhamento e nivelamento das correias de tração"},
                    {"id": "1.3.2", "desc": "Posicionamento do elevador em relação ao transportador"},
                    {"id": "1.3.3", "desc": "Encaixe das guias nas correias"},
                    {"id": "1.3.4", "desc": "Nivelamento das guias"},
                    {"id": "1.3.5", "desc": "Fixação dos mancais"},
                    {"id": "1.3.6", "desc": "Ruído e aparência das correias"},
                    {"id": "1.3.7", "desc": "Travamento de porcas"},
                    {"id": "1.3.8", "desc": "Fixação do motor do elevador"},
                    {"id": "1.3.9", "desc": "Aparência do cilindro pneumático"},
                    {"id": "1.3.10", "desc": "Funcionamento do elevador"},
                    {"id": "1.3.11", "desc": "Testar sensores de confirmação de presença do produto"},
                ],
            },
            {
                "id": "1.4",
                "nome": "DISTRIBUIDOR",
                "itens": [
                    {"id": "1.4.1", "desc": "Posicionamento do distribuidor em relação ao transportador"},
                    {"id": "1.4.2", "desc": "Aparência do distribuidor"},
                    {"id": "1.4.3", "desc": "Alinhamento da manga de saída"},
                    {"id": "1.4.4", "desc": "Nivelamento do distribuidor"},
                    {"id": "1.4.5", "desc": "Encaixe das mangueiras"},
                    {"id": "1.4.6", "desc": "Fixação do cilindro pneumático"},
                    {"id": "1.4.7", "desc": "Travamento dos parafusos"},
                    {"id": "1.4.8", "desc": "Aparência e funcionamento da válvula pneumática"},
                    {"id": "1.4.9", "desc": "Identificação da mangueira, cilindro e conectores"},
                    {"id": "1.4.10", "desc": "Encaixe e identificação do conector solenóide"},
                    {"id": "1.4.11", "desc": "Testar funcionamento do distribuidor"},
                    {"id": "1.4.12", "desc": "Verificar sensores de confirmação de presença"},
                    {"id": "1.4.13", "desc": "Testar saídas do distribuidor"},
                    {"id": "1.4.14", "desc": "Verificar funcionamento correto da distribuição"},
                ],
            },
            {
                "id": "1.5",
                "nome": "REJEITO",
                "itens": [
                    {"id": "1.5.1", "desc": "Verificar se o sentido de rejeição está conforme ficha técnica"},
                    {"id": "1.5.2", "desc": "Fixação da pala (Quebrar cantos vivos)"},
                    {"id": "1.5.3", "desc": "Alinhamento da pala em relação ao transportador"},
                    {"id": "1.5.4", "desc": "Fixação do suporte do rejeito"},
                    {"id": "1.5.5", "desc": "Fixação do cilindro no suporte"},
                    {"id": "1.5.6", "desc": "Fixação da válvula do rejeito"},
                    {"id": "1.5.7", "desc": "Fixação do conector da solenoide"},
                    {"id": "1.5.8", "desc": "Fixação dos conectores em geral (Fluxo, silenciador, cotovelos)"},
                    {"id": "1.5.9", "desc": "Travamento dos parafusos em geral"},
                    {"id": "1.5.10", "desc": "Encaixe das mangueiras de ar (Sem vazamentos)"},
                    {"id": "1.5.11", "desc": "Etiqueta do cilindro pneumático colocada"},
                    {"id": "1.5.12", "desc": "Identificar mangueira, válvula, conectores e cilindro pneumático"},
                    {"id": "1.5.13", "desc": "Identificar conector, solenóide e cabo elétrico da válvula pneumática"},
                    {"id": "1.5.14", "desc": "Testar confirmação de rejeito"},
                    {"id": "1.5.15", "desc": "Verificar avanço/recuo suave do cilindro"},
                    {"id": "1.5.16", "desc": "Funcionamento do rejeito"},
                ],
            },
            {
                "id": "1.6",
                "nome": "MOTORES",
                "itens": [
                    {"id": "1.6.1", "desc": "Posicionamento dos motores com relação aos braços da máquina"},
                    {"id": "1.6.2", "desc": "Proteções dos eixos dos motores (tampas e/ou caixa de inox etc)"},
                    {"id": "1.6.3", "desc": "Ruído dos motores"},
                    {"id": "1.6.4", "desc": "Aparência dos motores"},
                    {"id": "1.6.5", "desc": "Ajustar eixos, chavetas e engrenagens"},
                    {"id": "1.6.6", "desc": "Alinhar (lateralmente) e fixar engrenagens motriz e movida"},
                    {"id": "1.6.7", "desc": "Verificar tensão da corrente (transmissão) dos motores"},
                    {"id": "1.6.8", "desc": "Verificar fixação dos motores na campana ou flange"},
                    {"id": "1.6.9", "desc": "Verificar fixação da tampa da caixa de passagem"},
                    {"id": "1.6.10", "desc": "Verificar fixação dos prensa cabos"},
                    {"id": "1.6.11", "desc": "Preencher Formulário com o número de série do motor"},
                ],
            },
            {
                "id": "1.7",
                "nome": "MONTAGEM E ACABAMENTO EXTERNO DO COFRE",
                "itens": [
                    {"id": "1.7.1", "desc": "Pintura em bom estado (Sem riscos, sem manchas e cor com mesma tonalidade)"},
                    {"id": "1.7.2", "desc": "Verificar acabamento do escovado ou polimento do armário de inox"},
                    {"id": "1.7.3", "desc": "Cortar pés do armário de máquina com bancada"},
                    {"id": "1.7.4", "desc": "Colar tampões dos pés do armário"},
                    {"id": "1.7.5", "desc": "Colocar pés que tenha no mínimo curso de +/- 35 milímetros"},
                    {"id": "1.7.6", "desc": "Fixar porcas dos pés do equipamento em geral"},
                    {"id": "1.7.7", "desc": "Colocar tampões na lateral do armário (Entrada de cabos)"},
                    {"id": "1.7.8", "desc": "Tampar todo e qualquer furo na lateral do armário"},
                    {"id": "1.7.9", "desc": "Colocar guarnição na porta do armário"},
                    {"id": "1.7.10", "desc": "Colocar puxador na porta do armário"},
                    {"id": "1.7.11", "desc": "Alinhar, fixar e travar dobradiças e fechos da porta do armário"},
                    {"id": "1.7.12", "desc": "Ajustar lingueta do fecho retirando folga (vibração) da porta do armário"},
                    {"id": "1.7.13", "desc": "Ajustar e fixar varão (cofre especial) da porta do armário"},
                    {"id": "1.7.14", "desc": "Colocar chave da porta do armário"},
                    {"id": "1.7.15", "desc": "Verificar estado e fixação das grelhas dos filtros"},
                    {"id": "1.7.16", "desc": "Colocar filtros limpos"},
                    {"id": "1.7.17", "desc": "Etiqueta marca Varpe colocada (Parte frontal do armário)"},
                    {"id": "1.7.18", "desc": "Etiquetas de dados de calibração colocadas"},
                    {"id": "1.7.19", "desc": "Etiqueta da certificação NR-12"},
                    {"id": "1.7.20", "desc": "Etiqueta da porta do painel colocada (Troca de Tensão e Atenção)"},
                    {"id": "1.7.21", "desc": "Etiquetas dos filtros colocadas"},
                    {"id": "1.7.22", "desc": "Etiqueta de tensão de entrada colocada (Alimentação)"},
                    {"id": "1.7.23", "desc": "Colocar todas as etiquetas padrão dos equipamentos NESTLÉ"},
                    {"id": "1.7.24", "desc": "Verificar posicionamento de cabos e conduítes"},
                    {"id": "1.7.25", "desc": "Verificar prensa cabos em geral se estão fixados e prensando"},
                    {"id": "1.7.26", "desc": "Pesar cofre depois de finalizado"},
                ],
            },
            {
                "id": "1.8",
                "nome": "ACABAMENTO INTERNO DO COFRE",
                "itens": [
                    {"id": "1.8.1", "desc": "Limpar armário (IMPORTANTÍSSIMO)"},
                    {"id": "1.8.2", "desc": "Verificar fixação da botoeira principal e tampa cega"},
                    {"id": "1.8.3", "desc": "Instalar ventilador da porta (dar acabamento no chicote)"},
                    {"id": "1.8.4", "desc": "Instalar sinaleiro (dar acabamento no chicote)"},
                    {"id": "1.8.5", "desc": "Colocar porta documentos na porta do armário"},
                    {"id": "1.8.6", "desc": "Colocar separador entre o armário e placa de montagem"},
                    {"id": "1.8.7", "desc": "Colocar e fixar placa de montagem elétrica (almofada) dentro do armário"},
                    {"id": "1.8.8", "desc": "Colocar ferrita de alimentação na base do armário"},
                    {"id": "1.8.9", "desc": "Colocar sílica"},
                ],
            },
        ],
    },
    {
        "id": "2",
        "nome": "DOCUMENTAÇÃO EM GERAL",
        "itens": [
            {"id": "2.1", "desc": "Colocar manuais no painel (Inversor, ar condicionado etc)"},
            {"id": "2.2", "desc": "Colocar Laudo NR-12"},
            {"id": "2.3", "desc": "Colocar certificado de calibração"},
            {"id": "2.4", "desc": "Colocar esquema elétrico (Verificar: Nº de páginas, cliente, Nº de série, Tensão de alimentação coerente com ficha técnica etc)"},
            {"id": "2.5", "desc": "IMPORTANTE: Para máquinas NESTLÉ deve estar incluso os manuais de todos os componentes"},
        ],
    },
    {
        "id": "3",
        "nome": "FUNCIONALIDADE DO EQUIPAMENTO EM GERAL",
        "itens": [
            {"id": "3.1", "desc": "Testar materiais de reposição (Motores, drives, placas PCI, etc.)"},
            {"id": "3.2", "desc": "Realizar a checagem dos contatos secos"},
            {"id": "3.3", "desc": "Testar linha de comando"},
            {"id": "3.4", "desc": "Fazer comprovação das luzes (Térmicos e Rede)"},
            {"id": "3.5", "desc": "Verificar funcionamento da tomada"},
            {"id": "3.6", "desc": "Verificar se a corrente nominal do disjuntor está de acordo com a corrente do motor", "medicao": True},
            {"id": "3.7", "desc": "Verificar funcionamento dos disjuntores térmicos (Ajustar corrente)", "medicao": True},
            {"id": "3.8", "desc": "Funcionamento do alarme sonoro e visual (Sinaleiro)"},
            {"id": "3.9", "desc": "Funcionamento de periféricos: USB, porta RS232, ethernet, saída de servo, alarme temperatura"},
            {"id": "3.10", "desc": "Testar saída nobreak (Opcional)"},
            {"id": "3.11", "desc": "Testar botoeira externa (Opcional)"},
            {"id": "3.12", "desc": "Transformador externo: Fixar, instalar e testar (Opcional)"},
        ],
    },
    {
        "id": "4",
        "nome": "DETALHES FINAL",
        "itens": [
            {"id": "4.1", "desc": "Limpar máquina (IMPORTANTÍSSIMO)"},
            {"id": "4.2", "desc": "IMPORTANTE: Tirar fotos detalhadas do equipamento"},
        ],
    },
    {
        "id": "5",
        "nome": "TESTE FINAL (PESAGEM)",
        "itens": [
            {"id": "5.1", "desc": "Realizar parametrização em geral do equipamento"},
            {"id": "5.2", "desc": "Realizar coletas de peso"},
            {"id": "5.3", "desc": "Testar rejeito"},
            {"id": "5.4", "desc": "Testar todos os opcionais do equipamento"},
            {"id": "5.5", "desc": "Preencher certificado de calibração"},
            {"id": "5.6", "desc": "Verificar a variação para 50 Hertz no caso de máquinas com variação automática"},
            {"id": "5.7", "desc": "Etiquetas de dados de calibração colocada preenchida"},
            {"id": "5.8", "desc": "Etiqueta NR-12 preenchida"},
        ],
    },
    {
        "id": "6",
        "nome": "BANDAS LATERAIS",
        "itens": [
            {"id": "6.1", "desc": "Alinhamento e nivelamento das Bandas laterais"},
            {"id": "6.2", "desc": "Verificar altura de trabalho com relação ao transportador"},
            {"id": "6.3", "desc": "Espaçamento entre as bandas (Abraçamento do produto)"},
            {"id": "6.4", "desc": "Verificar ruídos das correias e eixos"},
            {"id": "6.5", "desc": "Verificar uniformidade das correias (Sem ondulações)"},
            {"id": "6.6", "desc": "Verificar fixação dos mancais traseiro e dianteiro"},
            {"id": "6.7", "desc": "Verificar o giro das polias motora e motriz (Movimento suave e sem folga)"},
            {"id": "6.8", "desc": "Verificar se todas as peças que compõe as bandas estão na mesma: trava cilíndrica parte inferior, tensores, niveladores e porcas de contra aperto fixadas"},
            {"id": "6.9", "desc": "Travamento dos parafusos de regulagem colocados e fixados"},
            {"id": "6.10", "desc": "Fixar chapa da proteção das correias"},
            {"id": "6.11", "desc": "Travar porca dos pés do suporte das bandas"},
            {"id": "6.12", "desc": "Verificar alinhamento, fixação, posição, e vibração dos motores"},
            {"id": "6.13", "desc": "Verificar instalação elétrica (Acabamento de conduítes e tampa da caixa de ligação fixados)"},
            {"id": "6.14", "desc": "Verificar deslocamento lateral das bandas"},
            {"id": "6.15", "desc": "Verificar funcionamento do fuso e manivela (Movimento suave e sem folga)"},
            {"id": "6.16", "desc": "Verificar colocação da régua (PROJETO VARPE)"},
        ],
    },
    {
        "id": "7",
        "nome": "DETECTOR DE METAIS",
        "itens": [
            {"id": "7.1", "desc": "Verificar a existência dos manuais"},
            {"id": "7.2", "desc": "Verificar a existência dos corpos de prova"},
            {"id": "7.3", "desc": "Verificar a fixação do DM na estrutura"},
            {"id": "7.4", "desc": "Verificar as medidas do DM confere com a ficha técnica"},
            {"id": "7.5", "desc": "Verificar se o modelo do DM confere com a ficha técnica"},
            {"id": "7.6", "desc": "Realizar os testes com os corpos de prova"},
            {"id": "7.7", "desc": "Verificar a existência das tabelas (Características elétricas)"},
            {"id": "7.8", "desc": "Realizar Certificado de Calibração"},
        ],
    },
    {
        "id": "8",
        "nome": "PROTEÇÕES EXTERNAS (POLICARBONATO)",
        "itens": [
            {"id": "8.1", "desc": "Verificar se a espessura está de acordo com a ficha técnica"},
            {"id": "8.2", "desc": "Verificar fechamento e travamento das portas (Fechos e chaves)"},
            {"id": "8.3", "desc": "Verificar fixação dos embudos (Dobras uniformes)"},
            {"id": "8.4", "desc": "Verificar fixação tampas traseira, dianteira, superior, inferior, puxador, batentes, etc."},
            {"id": "8.5", "desc": "Verificar fixação dos sensores eletromecânico e/ou magnéticos"},
            {"id": "8.6", "desc": "Verificar a fixação dos sensores de confirmação de rejeito"},
            {"id": "8.7", "desc": "Retirar todo e qualquer canto vivo"},
            {"id": "8.8", "desc": "Verificar a existência de riscos, trincas e tonalidade de cor"},
            {"id": "8.9", "desc": "Dobradiças das portas devem estar fixa e intertravadas (Esquerda/Direita)"},
        ],
    },
    {
        "id": "9",
        "nome": "PROTEÇÕES IP-66",
        "itens": [
            {"id": "9.1", "desc": "Verificar fechamento, alinhamento e posicionamento da proteção de tela"},
            {"id": "9.2", "desc": "Verificar fechamento, alinhamento e posicionamento da proteção dos ventiladores"},
            {"id": "9.3", "desc": "Verificar fechamento, alinhamento e posicionamento da proteção dos motores"},
            {"id": "9.4", "desc": "Colocar proteção de tela nos equipamentos VITARELLA"},
            {"id": "9.5", "desc": "OBS: TODAS ESTAS PROTEÇÕES DEVEM SER HERMETICAMENTE FECHADAS"},
        ],
    },
    {
        "id": "10",
        "nome": "RAMPA",
        "itens": [
            {"id": "10.1", "desc": "Cortar tubos conforme desenho (Engenharia)"},
            {"id": "10.2", "desc": "Fixar tubos nos suportes de fixação"},
            {"id": "10.3", "desc": "Agregar todos os tubos e montar na maca da rampa"},
            {"id": "10.4", "desc": "Fixar rampa no chassi do equipamento"},
            {"id": "10.5", "desc": "Verificar se todos os parafusos estão apertados"},
            {"id": "10.6", "desc": "Montar os eixos e verificar se estão rodando livremente"},
            {"id": "10.7", "desc": "Verificar a existência da espuma de amortecimento no final da rampa"},
            {"id": "10.8", "desc": "Verificar inclinação e altura, conforme pedido na Ficha Técnica"},
            {"id": "10.9", "desc": "Verificar fixação da rampa no transportador"},
            {"id": "10.10", "desc": "Verificar se foi colocada as etiquetas"},
            {"id": "10.11", "desc": "Colocar pés que tenha no mínimo curso de +/- 35 milímetros"},
            {"id": "10.12", "desc": "Verificar a existência da ponteira na guia"},
            {"id": "10.13", "desc": "Pesar Rampa"},
        ],
    },
]


def get_all_item_ids():
    """Return a flat list of all item IDs."""
    ids = []
    for secao in CHECKLIST:
        if "subsecoes" in secao:
            for sub in secao["subsecoes"]:
                for item in sub["itens"]:
                    ids.append(item["id"])
        else:
            for item in secao["itens"]:
                ids.append(item["id"])
    return ids


def get_item_by_id(item_id):
    """Return an item dict by its ID."""
    for secao in CHECKLIST:
        if "subsecoes" in secao:
            for sub in secao["subsecoes"]:
                for item in sub["itens"]:
                    if item["id"] == item_id:
                        return item
        else:
            for item in secao["itens"]:
                if item["id"] == item_id:
                    return item
    return None
