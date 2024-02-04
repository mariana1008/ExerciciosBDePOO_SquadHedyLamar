import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('banco')
print("Conexão bem-sucedida!")

# PAssando a conexão para uma nova variável
cursor = conexao.cursor()

# Envio das informações para o banco
conexao.commit()
print("Comando executado com sucesso!")


"""1. Criação de tabelas"""    

"""2. Inserção de Dados"""    

"""3. Consultas SQL"""    

"""4. Atualizações e exclusões"""    


conexao.close()