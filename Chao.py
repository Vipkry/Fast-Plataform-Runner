from PPlay.gameimage import *
class Chao (GameImage):
    def __init__(self):
        # Parent constructor must be called first
        gameobject.GameObject.__init__(self)

        # Loads image from the source
        # Carrega a imagem apenas de "chão" para que o chão comum seja padronizado e o código fique limpo
        self.file_name = "Imagens/Jogo/chao.png"
        self.image = pygame.image.load("Imagens/Jogo/chao.png")

        # Size
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height