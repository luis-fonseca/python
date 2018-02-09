# tecnicamente um namespace para importar os outros modulos
# core, controls, gdi, misc, windows
import wx

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
    frame = wx.Frame(None, -1, 'lotofacil.py')
    frame.Show()

    # posteriormente é chamado o mainLoop() o qual é um ciclo sem fim
    # é usado para pegar e disparar o que ocorrem durante o ciclo de vida
    # da aplicação

if __name__ == '__main__':
    main()

# http://zetcode.com/wxpython/firststeps/
