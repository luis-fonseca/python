import wx

class Example1(wx.Frame):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):

        # cria um objeto menubar
        menubar = wx.MenuBar()

        # cria um objeto menu
        menu = wx.Menu()

        # cria um item de menu implicitamente pelo método append
        # a referência retornada será usada para vincular um evento
        # wx.menuitem cria explicitamente o objeto
        # no primeiro argumento o id padrão define um icone e um atalho
        # o segundo parametro é o nome do item de menu
        # o terceiro define uma mensagem para aparecer na barra de status
        file_menuitem = menu.Append(wx.ID_EXIT, 'Quit', 'Quit Application')

        # anexa o menu ao menubar, o & cria uma chave aceleradora
        menubar.Append(menu, '&File')

        # anexa o menu bar ao objeto frame (janela)
        self.SetMenuBar(menubar)

        # vincula o item de menu a uma função para encerrar a janela
        self.Bind(wx.EVT_MENU, self.OnQuit, file_menuitem)

        # definido as configurações iniciais da janela
        self.SetSize(300, 300)
        self.SetTitle('Simple Menu')
        self.Centre()
        self.Show()

    def OnQuit(self, e):
        self.Close()

if __name__ == '__main__':

    ex = wx.App()
    Example1(None)
    ex.MainLoop()
