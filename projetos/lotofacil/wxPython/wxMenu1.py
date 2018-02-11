import wx, os

APP_EXIT = 1

script = __file__
basedir = os.path.dirname(script)
exit_bitmap_path = os.path.join(basedir, 'exit.png')

class Menu1(wx.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.initUI()


    def initUI(self):
        menubar = wx.MenuBar()
        fmenu = wx.Menu()

        fmenuitem = wx.MenuItem(fmenu, APP_EXIT, '&Quit\tCtrl+Q')
        fmenuitem.SetBitmap(wx.Bitmap(exit_bitmap_path))

        fmenu.Append(fmenuitem)
        menubar.Append(fmenu, '&File')

        self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)
        self.SetMenuBar(menubar)

        self.SetSize(300, 300)
        self.Centre()
        self.Show()

    def OnQuit(self, e):
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    Menu1(None)
    app.MainLoop()
