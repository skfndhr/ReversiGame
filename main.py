from utils.AiPlayer import AIPlayer as AiPlayer
from utils.ReversiGame import ReversiGame
import tkinter as tk
from utils.Menu import aiMenu
from utils.Menu import mainMenu


def ai_callback(mode):
    if mode == 1:
        root = tk.Tk()
        Game = ReversiGame(root,mode)
        root.mainloop()
    else:
        root = tk.Tk()
        Game = ReversiGame(root,mode)
        root.mainloop()


def main_callback(mode):
    if mode == 0:
        root = tk.Tk()
        Game = ReversiGame(root,mode)
        root.mainloop()
    else:
        root = tk.Tk()
        AiMenu = aiMenu(root, ai_callback)
        root.mainloop() 





root = tk.Tk()
menu = mainMenu(root, main_callback)
root.mainloop()    

    