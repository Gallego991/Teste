import psycopg2


class Postg:

    def __init__(self, local, nome, usuario, senha, entrada):
        self.name = psycopg2.connect(host=local, dbname=nome, user=usuario, password=senha, port=entrada)

    def criardb(self, nomedb):
        sql = f"CREATE DATABASE {nomedb}"
        cur = self.name.cursor()
        cur.execute(sql)
        cur.commit()
        cur.close()

    def deletardb(self, nomedb):
        sql = f"DROP DATABASE IF EXISTS {nomedb}"
        cur = self.name.cursor()
        cur.execute(sql)
        cur.commit()
        cur.close()

    def criartab(self, nometab, variaves):
        sql = f"CREATE TABLE IF NOT EXISTS {nometab}({variaves})"
        cur = self.name.cursor()
        cur.execute(sql)
        cur.commit()
        cur.close()

    def deletartab(self, nometab):
        sql = f"DROP TABLE IF EXISTS {nometab}"
        cur = self.name.cursor()
        cur.execute(sql)
        cur.commit()
        cur.close()

    def adicionar(self, nometab, local, valores):
        sql = f"INSERT INTO {nometab}({local}) VALUES({valores})"
        cur = self.name.cursor()
        cur.execute(sql)
        cur.commit()
        cur.close()

    def atualizar(self, nometab, colval, local):
        sql = f"UPDATE {nometab} SET {colval} WHERE {local}"
        cur = self.name.cursor()
        cur.execute(sql)
        cur.commit()
        cur.close()

    def deletar(self, nometab, local):
        sql = f"DELETE FROM {nometab} WHERE {local}"
        cur = self.name.cursor()
        cur.execute(sql)
        cur.commit()
        cur.close()

    def ver(self, col, nametab, cond):
        if col == "":
            col = "*"
        if cond != "":
            sql = f"SELECT {col} FROM {nametab} WHERE {cond}"
        else:
            sql = f"SELECT {col} FROM {nametab}"
        cur = self.name.cursor()
        cur.execute(sql)
        imp = cur.fetchall()
        for linha in imp:
            print(linha)
        cur.close()

    def comando(self, sql):
        cur = self.name.cursor()
        cur.execute(sql)
        cur.commit()
        cur.close()

    def fechar(self):
        self.name.close()
