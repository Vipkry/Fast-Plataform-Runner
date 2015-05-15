from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.collision import *

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
personagem = Sprite("Imagens/Jogo/personagem_teste.png")
chao = Sprite("Imagens/Jogo/chao.png")
# Posições da corrida
chao.set_position(0, janela.height - chao.height)
personagem.set_position(10, janela.height - chao.height - personagem.height)
# Física
personagem_speed_Y = 250
personagem_speed_X = 300
altura_do_pulo = 100
altura_inicial = 0
botao_pulo = False


# Game loop
while True:
    # Mudando de tela
    if mouse.is_button_pressed(1) and mouse.is_over_object(logo) and menu == True:
        menu = False
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
        personagem.move_key_x(personagem_speed_X * janela.delta_time())
        # Pulo
        if teclado.key_pressed("UP"):
            altura_inicial = personagem.y
            botao_pulo = True
        if personagem.y >= altura_inicial - altura_do_pulo and botao_pulo == True:
            personagem.move_y(-personagem_speed_Y * janela.delta_time())
        # RENDER Jogo
        fundo_menu.draw()
        logo.draw()
        personagem.draw()
        chao.draw()

    janela.update()
