categorias = {
    'DESPESAS COM PESSOAL',
    'PRESTAÇÃO DE SERVIÇOS',
    'LOCAÇÃO DE MÁQUINAS/EQUIPAMENTOS',
    'DESPESAS CONSUMO',
    'MANUTENÇÃO',
    'CONSERVAÇÃO',
    'OBRAS NO CONDOMÍNIO E MELHORIAS',
    'DESPESAS ADMINISTRATIVAS',
    'IMOBILIZADO',
    'IMPOSTOS/TRIBUTOS/ENCARGOS',
    'TARIFAS BANCÁRIAS',
    'Receitas'
}

columns = [
    'descricao',
    'mes_ref',
    'mes_baixa',
    'tipo_pagamento',
    'nota_fiscal',
    'valor',
    'categoria'
]

mysqlDb = {
    'host':'localhost',
    'password':'',
    'user':'root',
    'db':'auditoria',
    'port':'3307'
}