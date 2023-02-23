import pyautogui
from tkinter import *

# função que move o mouse para as coordenadas especificadas
def mover_mouse():
    x = int(entrada_x.get())
    y = int(entrada_y.get())
    pyautogui.moveTo(x, y)

# cria a interface com duas entradas de texto para as coordenadas e um botão para mover o mouse
janela = Tk()
janela.title("Mover Mouse")

rotulo_x = Label(janela, text="Coordenada X:")
rotulo_x.pack()
entrada_x = Entry(janela)
entrada_x.pack()

rotulo_y = Label(janela, text="Coordenada Y:")
rotulo_y.pack()
entrada_y = Entry(janela)
entrada_y.pack()

botao = Button(janela, text="Mover Mouse", command=mover_mouse)
botao.pack()

janela.mainloop()
