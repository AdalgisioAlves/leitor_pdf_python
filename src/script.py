from cmath import nan
import csv
import tabula
import pandas as pd
from .confs.conn import MySQLConn
from .confs.constantes import categorias,mysqlDb, columns


class Script():
    def __init__(self, file):
        self.file = file
        self.categorias = categorias
        self.categoria = 'Receitas'

    def pdf_to_db(self):
        f = self.file.split("\\")
        self.nome_file = f[4].split(".")[0]
        tb = tabula.read_pdf(self.file, java_options="-Dfile.encoding=UTF8",
                             pages='all', stream=True, multiple_tables=True)
        i = 0
        csv = []
        for item in tb:
            row_limpa = self.limpar_df(item)
            item = None
            for index, row in row_limpa.iterrows():
                row.dropna(axis=0, how='all')
                row = self.tratar_nan(row)
                self.get_categoria(row)
                if self.categoria != 'Receitas':
                    row.append(self.categoria)
                    if len(row) == 2 and row[0] != row[1]:
                        csv[len(csv) - 1][0] = csv[len(csv) - 1][0] + \
                            str(row[0])
                        i = i + 1
                    elif len(row) == 7:
                        csv.append(row)
                        i = i + 1
                    elif len(row) == 6:
                        
                        row_aux = []
                        mes_baixa = row[2].split(" ")
                        row_aux.append(row[0])
                        row_aux.append(row[1])
                        row_aux.append(mes_baixa[0])
                        mes_baixa.pop(0)
                        row_aux.append(" ".join(mes_baixa))
                        row_aux.append(row[3])
                        #row_aux.append('null')
                        row_aux.append(row[4])
                        row_aux.append(row[5])
                        csv.append(row_aux)
                        i = i + 1
                    elif len(row) == 5:
                        #descricao,mes_ref,mes_baixa,tipo_pagamento,nota_fiscal,valor,categoria
                        row_aux = []
                        mes_baixa = row[2].split(" ")
                        row_aux.append(row[0])
                        row_aux.append(row[1])
                        row_aux.append(mes_baixa[0])
                        mes_baixa.pop(0)
                        row_aux.append(" ".join(mes_baixa))
                        row_aux.append('null')
                        row_aux.append(row[3])                        
                        row_aux.append(row[4])
                        csv.append(row_aux)
                        i = i + 1
        salva = self.salvar_bd(csv)
        print(salva)

    def limpar_df(self, df):
        return df.replace('\r', '',  regex=True)

    def tratar_nan(self, df):
        values = [i for i in df if i != nan]
        i = 0
        ret = []
        for drow in values:
            if type(drow) != 'float' and str(drow) != 'nan':
                ret.append(drow)
        return ret

    def get_categoria(self, categoria):
        for valor in self.categorias:
            if str(categoria[0]) == str(valor):
                self.categoria = valor

    def gerar_csv(self, csv_data):
        f = open(self.nome_file + '.csv', 'w', newline='')
        w = csv.writer(f)
        cabacalho = ['id','descricao','mes_ref','mes_baixa','tipo_pagamento','valor','categoria','tipo_custo','categoria_2']
        w.writerow(cabacalho)
        for i in csv_data:
            #i[1] = i[1].replace("'"," ")
            w.writerow(i)
        f.close()

    def salvar_bd(self, row):
        if len(row) > 1:

            sql = "INSERT INTO auditoria.tb_despesas (descricao,mes_ref,mes_baixa,tipo_pagamento,nota_fiscal,valor,categoria) "
            sql = sql + " VALUES (%s, %s,%s, %s, %s, %s, %s)"
            for r in row:
                salva = MySQLConn(mysqlDb).salvar(sql, r)
                print(salva)

    def gerar_csv_bd(self):       
        sql = str("select * from vw_debitos_categorizado")                       
        debitos = MySQLConn(mysqlDb).select(sql)
        if debitos != None:
            self.gerar_csv(debitos)
        else:
            print("Banco de dados vazio")
        
