import eel
import wx
import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass
def getPath(wildcard):
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()
    return path
@eel.expose
def saveFile():
    app = wx.App(None)
    style = wx.FD_SAVE
    dialog = wx.FileDialog(None, 'Open', wildcard='*.py', style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
        print(f'path found {path}')
        return path
    else:
        path = None
    dialog.Destroy()
@eel.expose
def getFile():
    path = getPath('*')
    if path != None:
        return open(path, "r").read()
    else:
        return 'No File Selected'
eel.init('web')
eel.start('index.html')
