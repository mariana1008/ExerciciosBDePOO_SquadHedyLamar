# Classes com conceitos de classe, herança, propriedade, encapsulamento e classe abstrata
import sqlite3

from classe_usuario import Usuario

conexao = sqlite3.connect('banco_biblioteca.db')
print("Conexão bem-sucedida!")



class userAdmin(Usuario):
    def __init__(self, id, nome, telefone, nacionalidade):
        super().__init__(id, nome, telefone, nacionalidade, cargo="Administrador")

    def inserirUsuarioComum(self, id, nome, telefone, nacionalidade):
        # Criar um novo usuário comum
        novo_usuario = Usuario(id, nome, telefone, nacionalidade, cargo= "Comum")

        # Inserir o novo usuário no banco de dados
        novo_usuario.inserirUsuario()
        
admin = userAdmin(id=1, nome="Admin", telefone="123456789", nacionalidade="BR")
admin.inserirUsuarioComum(id=2, nome="Celena", telefone="454950999", nacionalidade="BR")

conexao.commit()
print("Comando executado com sucesso!")

conexao.close()