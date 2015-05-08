from PPlay.window import *
from PPlay.gameimage import *
# Configurações
janela = Window (800,600)
teclado = janela.get_keyboard()
# Configurações do menu
fundo_menu = GameImage("Imagens/")
# Game loop
while True:
    janela.update()
