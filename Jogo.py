"""
    Fast! Platform Jumper.
    Precisa fazer:
        1º - Generalizar essa função do pulo para quando colidir com qualquer sprite
        2º - Fazer a gravidade como um método de uma classe (seja sprite ou uma nova classe)

"""
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *


class Character(Sprite):
    flag_pulo = False
    ja_pulou = False
    altura_inicial = 0
    altura_do_pulo = 100
    speed_X = 300
    speed_Y = 220
    def pulo(self, janela, teclado, chao):
        if teclado.key_pressed("UP"):
            if self.flag_pulo == False:  # Flag pra obter altura inicial apenas uma vez e executar o pulo novamente somente
                self.altura_inicial = self.y  # quando o personagem tocar o chão
                self.flag_pulo = True
        if self.y > self.altura_inicial - self.altura_do_pulo and self.flag_pulo and \
                        self.ja_pulou is False:  # Faz ir pra cima
            self.move_y(-self.speed_Y * janela.delta_time())
        elif self.flag_pulo:  # Faz ir pra baixo (só ativa se tiver pulado)
            self.move_y(self.speed_Y * janela.delta_time())
            self.ja_pulou = True
            if self.collided(chao):  # Para o pulo quando cai no chão
                self.flag_pulo = False
                self.ja_pulou = False


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

# Configurações
janela = Window(800, 600)
teclado = janela.get_keyboard()
mouse = janela.get_mouse()
# Configurações do menu
logo = GameImage("Imagens/Menu/logo_pequeno.png")
icone_jogo = GameImage("Imagens/Menu/jogo.png")
icone_loja = GameImage("Imagens/Menu/loja.png")
icone_records = GameImage("Imagens/Menu/records.png")
fundo_menu = GameImage("Imagens/Menu/fundo.png")
menu = True
# Posições do menu
espaco_padrao = 40
logo.set_position(janela.width / 2 - logo.width / 2 + espaco_padrao / 2, 0)
icone_jogo.set_position(janela.width / 2 - icone_jogo.width / 2, logo.height + espaco_padrao)
icone_loja.set_position(janela.width / 2 - icone_loja.width / 2,
                        logo.height + espaco_padrao + espaco_padrao / 4 + icone_jogo.height)
icone_records.set_position(janela.width / 2 - icone_records.width / 2,
                           janela.height - icone_records.height - espaco_padrao)
# Configurações da corrida
personagem = Character("Imagens/Jogo/personagem_teste.png")
chao = Chao()
# Posições da corrida
chao.set_position(0, janela.height - chao.height)



# Game loop
while True:
    # Mudando de tela
    if mouse.is_button_pressed(1) and mouse.is_over_object(icone_jogo) and menu:
        menu = False
        # posicionando o personagem aqui pois assim podemos jogar múlltiplas vezes após perder o jogo
        personagem.set_position(10, janela.height - chao.height - personagem.height)
    # Condição para saber em qual parte do jogo o jogador está (menu ou corrida)
    if menu:
        # RENDER Menu
        fundo_menu.draw()
        logo.draw()
        icone_jogo.draw()
        icone_loja.draw()
        icone_records.draw()

    else:
        # Input
        personagem.move_key_x(personagem.speed_X * janela.delta_time())
        # Pulo -> Agora tem que fazer isso virar uma função legal
        personagem.pulo(janela, teclado, chao)
        # Game over
        # Acontece quando o jogador cai ou bateem um dos espinhos
        if personagem.y > janela.height:
            menu = True

        # RENDER Jogo
        fundo_menu.draw()
        logo.draw()
        personagem.draw()
        chao.draw()

    janela.update()
