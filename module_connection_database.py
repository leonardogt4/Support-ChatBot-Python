
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importa os módulos necessários 'MySQLdb'
import pymysql as database
#import time

# Define endereço do servidor, nome de usuário do bd, senha do usuário do bd e nome da base de dados
aServidor = "localhost"
aUsuario  = "MY_USER_DB"
aSenha    = "MY_PASSWORD_DB"
aBanco    = "chatbot_db"

try:
 
    db = database.connect(aServidor, aUsuario, aSenha, aBanco)
    cursor = db.cursor() # seta o cursor para a conexão
 
    sql = "SELECT * FROM perguntas"
    number_of_rows = cursor.execute(sql)
    print("Conexão realizada com sucesso!")
    print("Numero de registros lidos: " + str(number_of_rows))
    db.close();
    print("Conexão fechada!")
 
except database.DataError as e:
    print("DataError")
    print(e)
 
except database.InternalError as e:
    print("InternalError")
    print(e)
 
except database.IntegrityError as e:
    print("IntegrityError")
    print(e)
 
except database.OperationalError as e:
    print("OperationalError")
    print(e)
 
except database.NotSupportedError as e:
    print("NotSupportedError")
    print(e)
 
except database.ProgrammingError as e:
    print("ProgrammingError")
    print(e)
 
except :
    print("Unknown error occurred")
'''
# Função que executa os comandos SQL no banco
def Executa_SQL(pSQL):
  try:
    cursor.execute(pSQL)
    db.commit()
  except:
    print("Erro: Não foi possível executar o SQL")
    db.rollback()

# Função que executa comandos SQL (Select)
def Busca_SQL(pSQL):
  try:
    cursor.execute(pSQL)
    results = cursor.fetchall()
    return results
  except:
    print("Erro: Não foi possível buscar os dados")
    return 0


# Cria uma variavel com o SQL e chama a função passando como parametro o SQL
vSQL = "CREATE TABLE IF NOT EXISTS perguntas (codigo int not null auto_increment, descricao VARCHAR(255) NOT NULL, PRIMARY KEY (codigo))"
Executa_SQL(vSQL)

Executa_SQL("INSERT INTO perguntas(descricao) VALUES ('O que posso fazer para resolver o erro X')")

# Chama a função Busca_SQL passando o comando SQL como parâmetro
vResultado = Busca_SQL("SELECT * FROM perguntas")
for row in vResultado:
  # Lê cada coluna de cada linha retornada do SELECT, começando pela coluna 0
  codigo  = row[0]
  descricao = row[1]

print("Codigo : " + str(codigo))
print("Descricao : " + descricao)


# Fecha a conexão com o banco de dados
db.close()

time.sleep(3)'''


