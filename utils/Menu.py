import tkinter as tk
import random


class mainMenu:
    def __init__(self, root, start_game_callback):
        self.root = root
        self.start_game_callback = start_game_callback
        self.create_widgets()

    def create_widgets(self):
        # 创建标题标签
        title_label = tk.Label(self.root, text="黑白棋游戏", font=("Arial", 24))
        title_label.pack(pady=20)

        # 创建人人对弈按钮
        pvp_button = tk.Button(self.root, text="人人对弈", font=("Arial", 18), command=lambda: self.start_game(0))
        pvp_button.pack(pady=10)

        # 创建人机对弈按钮
        pvc_button = tk.Button(self.root, text="人机对弈", font=("Arial", 18), command=lambda: self.start_game(1))
        pvc_button.pack(pady=10)

    def start_game(self, mode):
        # 关闭菜单窗口
        self.root.destroy()
        # 调用回调函数开始游戏，并传入游戏模式
        self.start_game_callback(mode)

class aiMenu:
    def __init__(self, root, start_game_callback):
        self.root = root
        self.start_game_callback = start_game_callback
        self.create_widgets()

    def create_widgets(self):
        # 创建标题标签
        title_label = tk.Label(self.root, text="先手选择", font=("Arial", 24))
        title_label.pack(pady=20)

        # 创建机器先手按钮
        pvp_button = tk.Button(self.root, text="机器先手", font=("Arial", 18), command=lambda: self.start_game(1))
        pvp_button.pack(pady=10)

        # 创建自己先手按钮
        pvc_button = tk.Button(self.root, text="自己先手", font=("Arial", 18), command=lambda: self.start_game(2))
        pvc_button.pack(pady=10)

        # 创建随机按钮
        back_button = tk.Button(self.root, text="随机先手", font=("Arial", 18), command=lambda: self.start_game(random.choice([1, 2])))
        back_button.pack(pady=10)

    def start_game(self, mode):
        # 关闭菜单窗口
        self.root.destroy()
        # 调用回调函数开始游戏，并传入游戏模式
        self.start_game_callback(mode)


if __name__ == "__main__":
    def ai_callback(mode):
        if mode == 1:
            print("启动机器先手模式")
        else:
            print("启动自己先手模式")


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

