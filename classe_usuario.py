from classe_abstrata import Biblioteca
import sqlite3

# Inicia conexão com o Banco de Dados
conexao = sqlite3.connect('banco_biblioteca.db')
cursor = conexao.cursor()

# Inicia classe Livro que herda de Bilioteca
class Usuario(Biblioteca):
    def __init__(self, id, nome, telefone, nacionalidade):
        super().__init__()
        self._id = id
        self._nome = nome
        self._telefone = telefone
        self._nacionalidade = nacionalidade

    # Verifica se já existe usuário com o mesmo nome e cadastra no sistema
    def cadastrar_usuario(self):
        cursor.execute("SELECT COUNT(*) FROM usuarios WHERE nome = ?", (self._nome,))
        resultado = cursor.fetchall()
        
        if resultado[0][0] > 0:
            print(f"Erro: Já existe um usuário com o nome '{self._nome}' no sistema.")
            return
        
        else:
            cursor.execute("INSERT INTO usuarios (nome, telefone, nacionalidade) VALUES (?, ?, ?)", (self._nome, self._telefone, self._nacionalidade))
            conexao.commit()
            self.id = cursor.lastrowid
            print(f"Usuário {self._nome} cadastrado com sucesso! ID: {self.id}")

    # Parte do método imprimir, mostra informações formatadas sobre o livro
    def imprimir(self):
        print(f"Informações do usuário(a) {self._nome}\n ID: {self._id}\nTelefone: {self._telefone}\nNacionalidade: {self._nacionalidade}")

    # Método especial __str__ que retorna uma representação formatada em string do objeto 
    def __str__(self):
        return f"Informações do usuário(a) {self.nome}\n ID: {self.id}\nTelefone: {self.telefone}\nNacionalidade: {self.nacionalidade}"


    def removerUsuarioPorId(id):
        cursor.execute('DELETE FROM usuarios where id=?',(id,))
        conexao.commit()

    def listarUsuarios():
        dados = cursor.execute('SELECT * FROM usuarios ORDER BY nome')
        for usuario in dados:
            print(usuario)
        conexao.commit()

    def removerUsuarios():
        cursor.execute('DELETE FROM usuarios')
        conexao.commit()
        
############################## TESTES

# ## Cria um usuário e cadastra no banco de dados (executar duas vezes)
# usuario1 = Usuario(id=1, nome="Maria", telefone="987654321", nacionalidade="Portuguesa")
# usuario1.cadastrar_usuario()

# ## Imprime informações do usuário
# usuario1.imprimir()

# Finaliza conexão com o Banco de Dados
conexao.close()