import mysql.connector

class MySQLConn():
    conn = None
    cursor = None
    def __init__(self,conexao):
        self.hots = conexao["host"]
        self.password = conexao["password"]
        self.user = conexao["user"]
        self.db = conexao["db"]
        self.port = conexao["port"]
        self.conn = self.conectar()
        self.cursor = self.conn.cursor()
    
    def conectar(self):
        conexao = mysql.connector.connect(
            host=self.hots,
            user=self.user,
            password=self.password,
            database=self.db,
            port=self.port
        )
        return conexao
        
    def salvar(self,sql,valores):
        
        try:
            self.cursor.execute(sql,valores)
            self.conn.commit()        
        except mysql.connector.ProgrammingError as err:
            self.conn.rollback()
            return err
        self.conn.close()
        return 'Registro inserido com sucesso'
    
    def select(self,sql):
        
        try:
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            if rs != None:
                #self.conn.close()
                return rs
            else:
                return None
        except mysql.connector.ProgrammingError as err:
            self.conn.close()
            return err
        
        
        
        

