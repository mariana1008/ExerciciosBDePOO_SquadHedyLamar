class Book:
    def __init__(self, titulo, editora, autor, genero, exemplares):
        self.titulo = titulo
        self.editora = editora
        self.autor = autor
        self.genero = genero
        self.exemplares = exemplares

    def emprestar(self, usuario):
        if len(self.exemplares) > 0:
            exemplar = self.exemplares.pop()
            emprestimo = (exemplar, usuario)
            self.emprestimos.append(emprestimo)
            return emprestimo
        else:
            raise ValueError(f"Não há exemplares disponíveis para o livro {self.titulo}")   

    def devolver(self, emprestimo):
        if emprestimo.exemplar.livro == self:
            self.exemplares.append(emprestimo.exemplar)
            emprestimo.devolver()

    def __str__(self):
        return f"{self.titulo}, {self.autor}"    