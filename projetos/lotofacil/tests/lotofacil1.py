# tecnicamente um namespace para importar os outros modulos
# core, controls, gdi, misc, windows
import wx
import modules
import sys
import modules
import helpers

def main():

    # todos os app devem ter ao menos um objeto app
    app = wx.App()

    # é um widget que está no topo e é o pai de todos os outros widgets
    # ele, em si, não tem um pai
    # depois de criado é necessário chamar o método show() para exibi-lo

    # este widget é o mais importante porque pode conter qualquer outro widget
    # menos frame ou dialog

    # wxFrame possui bordas, titulo e uma area central de containeres
    # a barra e titulo são opcionais e podem ser removidos por flags

    # o construtor possui 7 parametros, o primeiro parametro não tem valor padrão
    # os outros 6, sim. O 3 primeiros são obrigatorios e outros, não
    # é possível no parametro style combinar opções
    # wx.DEFAULT_FRAME_STYLE is a set of default flags. wx.MINIMIZE_BOX |
    # wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION |
    # wx.CLOSE_BOX | wx.CLIP_CHILDREN

    # é possível especificar o tamanho da aplicação de duas formas
    # ou pelo construtor ou pelo método setSize
    frame = wx.Frame(None, -1, 'lotofacil.py', size=(500,500))

    # define a posição x, y da tela para centralizar a janela
    # posx = (helpers.get_width_height_monitor()[0] / 2) - (frame.GetSize()[0] / 2)
    # posy = (helpers.get_width_height_monitor()[1] / 2) - (frame.GetSize()[1] / 2)
    # frame.Move(posx, posy)
    frame.Centre()
    frame.Show()

    # posteriormente é chamado o mainLoop() o qual é um ciclo sem fim
    # é usado para pegar e disparar o que ocorrem durante o ciclo de vida
    # da aplicação
    app.MainLoop()


if __name__ == '__main__':

    main()

# http://zetcode.com/wxpython/firststeps/
