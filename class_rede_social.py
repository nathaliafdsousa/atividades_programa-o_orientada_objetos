 

class Usuario:
    def __init___(self,nome,senha,email,postagens,seguidores,id):
        self.nome = nome
        self.senha=senha
        self.email = email
        self.postagens = []
        self.seguidores = []
        self.id = id
    def adiccionar_postagem(self,postagem):
        self.postagens.append(postagem)
    
    def adicionar_amigo(self,seguidores):
        self.seguidores.append(seguidores)


class Postagem:

    def __init__(self,conteudo,comentarios,curtidas,autor):
        self.conteudo= conteudo
        self.autor = autor
        self.comentarios = []
        self.curtidas = []
    def adicionar_comentario(self,comentario):
        self.comentarios.append(comentario)

    def adicionar_curtida(self,curtida):
        self.curtidas.append(curtida)

class comentario:

    def __init__(self,autor,conteudo):
        self.autor= autor
        self.conteudo = conteudo
    def mostrar_comentarios(self):
        print(f"Comentários da postagem de {self.autor.nome}:")
        for comentario in self.comentarios:
            print(f"- {comentario.conteudo} por {comentario.autor.nome}") 

class curtida:
    def __init__(self,data_hora,autor):
        self.data_hora = data_hora
        self.autor= autor

    def registrar_curtida(self):
        print(f"Curtida registrada por {self.autor.nome} em {self.data_hora}")



        
        
    

