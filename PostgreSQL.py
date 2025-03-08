import psycopg2


class Postg:

    def __init__(self, local, nome, usuario, senha, entrada):
        self.name = psycopg2.connect(host=local, dbname=nome, user=usuario, password=senha, port=entrada)

    def criar(self, sql):
        cur = self.name.cursor()
        cur.execute(sql)
        cur.commit()
        cur.close()

    def ver(self, sql):
        cur = self.name.cursor()
        cur.execute(sql)
        imp = cur.fetchall()
        for linha in imp:
            print(linha)
        cur.close()

    def modificar(self, sql):
        cur = self.name.cursor()
        cur.commit()
        cur.close()

    def fechar(self):
        self.name.close()
