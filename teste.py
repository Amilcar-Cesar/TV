class Livro:
    def __init__(self, titulo, autor, num_paginas, genero):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
        self.genero  = genero


    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

meu_livro = Livro(titulo="Crepusculo", 
                  autor="stephanie",
                  num_paginas=200, 
                  genero="romance")


print("titulo do livro: ",meu_livro.get_titulo())

meu_livro.set_titulo(titulo="Lua Nova")

print("Novo titulo do livro: ", meu_livro.get_titulo())