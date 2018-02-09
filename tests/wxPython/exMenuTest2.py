import wx

class Menu1(wx.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initializeUI()


    def initializeUI(self):

        # cria o menubar, menu e menuitem
        menubar = wx.MenuBar()
        file_menu = wx.Menu()

        # define o nome do menu e subitens
        menubar.Append(file_menu, '&File')
        file_menuitem = wx.MenuItem(file_menu, wx.ID_EXIT, 'Quit', 'Quit Application')

        # define os eventos
        menubar.Bind(wx.EVT_MENU, self.OnQuit, file_menuitem)

        # vincula menubar e menu
        file_menu.Append(file_menuitem)
        self.SetMenuBar(menubar)

        # configurações iniciais da janela
        self.SetSize(300, 300)
        self.Centre()
        self.Show()

    def OnQuit(self, e):
        self.Close()

if __name__ == '__main__':
     app = wx.App()
     Menu1(None)
     app.MainLoop()
