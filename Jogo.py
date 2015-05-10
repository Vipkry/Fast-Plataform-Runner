from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

# Configurações
janela = Window(800, 600)
teclado = janela.get_keyboard()
mouse = janela.get_mouse()
# Configurações do menu
fundo_menu = GameImage("Imagens/menu_teste.png")
botao = Sprite("Imagens/botao_teste.png")
botao2 = Sprite("Imagens/botao_teste.png")
botao2.set_position(400, 300)
menu = True
# Configurações da corrida
fundo_corrida = GameImage("Imagens/jogo_teste.jpg")
# Game loop
while True:

    # Mudando de tela
    if mouse.is_button_pressed(1) and mouse.is_over_object(botao):
        menu = False

    # Condição para saber em qual parte do jogo o jogador está (menu ou corrida)
    if menu:
        fundo_menu.draw()
        botao.draw()
    else:
        fundo_corrida.draw()

    janela.update()
