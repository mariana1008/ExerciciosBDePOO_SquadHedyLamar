# Classes com conceitos de classe, herança, propriedade, encapsulamento e classe abstrata
import sqlite3
from classe_emprestimo import emprestimo #importando classe_emprestimo
from classe_usuario import Usuario #importando classe_usuario

conexao = sqlite3.connect('banco_biblioteca.db')
print("Conexão bem-sucedida!")

class userAdmin(Usuario):
    def __init__(self, nome, telefone, nacionalidade):
        super().__init__(nome, telefone, nacionalidade, cargo="Administrador")

    def inserirUsuarioComum(self, nome, telefone, nacionalidade):
        # Criar um novo usuário comum
        novo_usuario = Usuario(nome, telefone, nacionalidade, cargo="comum")

        # Inserir o novo usuário no banco de dados
        self.inserirUsuario(novo_usuario.nome, novo_usuario.telefone, novo_usuario.nacionalidade, novo_usuario.cargo)
    #_________________________________________________________________________
    def atualizarUsuarioComum(self, nome, novo_telefone, nova_nacionalidade):
        # Obtém informações do usuário comum
        usuario_comum = self.obterUsuarioPorNome(nome)

        if usuario_comum:
            # Obtém o ID do usuário comum
            id_usuario_comum = usuario_comum[0]

            # Chama o método de atualização da classe base
            self.atualizarUsuario(nome, novo_telefone, nova_nacionalidade)
        else:
            print(f"Usuário com nome '{nome}' não encontrado.")
            
     #_______________________________________________________________________________
    def removerUsuarioPorId(self, id):
        # Chamar o método da classe base para realizar a exclusão
        super().removerUsuarioPorId(id)
#____________________________________________________________________________________      
        #def realizaremprestimo(self): #parte que chamariamos da classe_emprestimo 
                                  #para manipular os emprestimos e as devoluções
        
        


# ___________________________________________________________________________________
"área de teste de  usuario_admin"
if __name__ == "__main__":
    admin = userAdmin(nome="Admin", telefone="123456789", nacionalidade="BR")

    # teste Inserindo um usuário comum para teste ok
    #admin.inserirUsuario(nome="Sueli", telefone="4056328623", nacionalidade="BR", cargo="Comum")
    #admin.listarUsuarios()
        
        
    # Atualizando o usuário comum  teste ok
    #admin.atualizarUsuarioComum(nome="Sueli", novo_telefone="90023", nova_nacionalidade="BR")

    #excluir um usuario por id #teste ok
    #admin.removerUsuarioPorId(19)  # Substitua 1 pelo ID do usuário que deseja remover
    
    # teste ok excluir todos os usuarios (atenção, essa opção somente poderá ser realizada por alguem com cargo Master em suma TEM que aparecer um erro aqui.)
    # admin.removerUsuarios()
    # Listando todos os usuários
    admin.listarUsuarios()

conexao.commit()
print("Comando executado com sucesso!")

conexao.close()