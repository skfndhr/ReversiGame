from utils.AiPlayer import AIPlayer as AiPlayer
from utils.ReversiGame import ReversiGame
import tkinter as tk
from utils.Menu import aiMenu
from utils.Menu import mainMenu


def ai_callback(mode):
    if tk._default_root is None:
        root = tk.Tk()
    else:
        root = tk._default_root
    Game = ReversiGame(root,mode)
    # root.mainloop()


def main_callback(mode):
    if mode == 0:
        if tk._default_root is None:
            root = tk.Tk()
        else:
            root = tk._default_root
        Game = ReversiGame(root,mode)
        # root.mainloop()
    else:
        if tk._default_root is None:
            root = tk.Tk()
        else:
            root = tk._default_root
        AiMenu = aiMenu(root, ai_callback)
        # root.mainloop() 



root = tk.Tk()
menu = mainMenu(root, main_callback)
root.mainloop()    

    