# renderTarget.py
# Compat layer for clients without renderTarget

import wndMgr

class RenderTarget:
    def __init__(self):
        self.width = 0
        self.height = 0

    def SetSize(self, width, height):
        self.width = width
        self.height = height

    def Create(self, *args, **kwargs):
        return True

    def Destroy(self):
        pass

    def Clear(self):
        pass

    def Update(self):
        pass