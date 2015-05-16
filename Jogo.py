from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

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
# Física
personagem_speed_Y = 0
personagem_speed_X = 300
altura_do_pulo = 100
altura_inicial = 0
flag_pulo = False
ja_pulou = False

# Game loop
while True:
    # Mudando de tela
    if mouse.is_button_pressed(1) and mouse.is_over_object(icone_jogo) and menu == True:
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
        personagem.move_key_x(personagem_speed_X * janela.delta_time())
        # Pulo -> Agora tem que fazer isso virar uma função legal (miguel)
        if teclado.key_pressed("UP"):
            if flag_pulo == False:
                altura_inicial = personagem.y
                personagem_speed_Y = 220
                flag_pulo = True
        if personagem.y > altura_inicial - altura_do_pulo and flag_pulo == True and ja_pulou == False:
            personagem.move_y(-personagem_speed_Y * janela.delta_time())
        elif flag_pulo == True:
            personagem.move_y(personagem_speed_Y * janela.delta_time())
            ja_pulou = True
            if personagem.collided(chao):
                flag_pulo = False
                ja_pulou = False
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
