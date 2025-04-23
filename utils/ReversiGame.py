import tkinter as tk
import time
import tkinter.messagebox as messagebox
import random
from utils.AiPlayer import AIPlayer
# 棋盘大小
BOARD_SIZE = 8
# 每个格子的大小
CELL_SIZE = 80

class ReversiGame:
    def has_valid_move(self, player):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.is_valid_move(i, j, player):
                    return True
        return False
    def __init__(self, root,mode):
        self.root = root
        self.mode=mode
        self.col=None
        self.row=None
        self.ai_player=AIPlayer(self.mode)
        self.root.title('黑白棋')
        self.canvas = tk.Canvas(root, width=BOARD_SIZE * CELL_SIZE, height=BOARD_SIZE * CELL_SIZE, bg='#3CB371')
        # self.canvas.resizable(False, False)
        self.canvas.pack()
        self.board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.hints = []
        self.current_player = 1
        self.score_label = tk.Label(root, text='白棋: 2 黑棋: 2')
        self.score_label.pack()
        self.initialize_board()
        self.draw_board()
    


        if self.mode==1:
            self.make_move(3, 5)  # 机器先手
            self.draw_board()  # 绘制初始状态
            self.update_score()  # 更新分数
        
        self.canvas.bind('<Button-1>', self.on_click)
        self.reset_button = tk.Button(root, text='重新开始', command=self.reset_game)
        self.reset_button.pack()

    def copy(self):
        import copy
        new_game = ReversiGame(self.root, self.mode)
        new_game.board = copy.deepcopy(self.board)
        new_game.current_player = self.current_player
        new_game.hints = []
        return new_game

    def initialize_board(self):
        self.board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.board[3][3] = 1
        self.board[3][4] = 2
        self.board[4][3] = 2
        self.board[4][4] = 1

    def reset_game(self):
        if self.mode==0:
            self.initialize_board()
            self.current_player = 1
            self.draw_board()
            self.update_score()
            # 清空提示
            for hint in self.hints:
                self.canvas.delete(hint)
            self.hints = []
        else:
            self.initialize_board()
            self.current_player = 1
            self.draw_board()
            self.update_score()
            # 清空提示
            for hint in self.hints:
                self.canvas.delete(hint)
            self.hints = []
            if self.mode==1:
                self.make_move(3, 5)  # 机器先手


    def update_score(self):
        white_score = sum(row.count(1) for row in self.board)
        black_score = sum(row.count(2) for row in self.board)
        self.score_label.config(text=f'白棋: {white_score} 黑棋: {black_score}')

    def make_move(self, row, col):
        self.board[row][col] = self.current_player
        opponent = 3 - self.current_player
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dr, dc in directions:
            to_flip = []
            r, c = row + dr, col + dc

            while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and self.board[r][c] == opponent:
                to_flip.append((r, c))
                r += dr
                c += dc

            if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and self.board[r][c] == self.current_player:
                for r_flip, c_flip in to_flip:
                    self.board[r_flip][c_flip] = self.current_player

        # 切换玩家
        opponent = 3 - self.current_player
        if self.has_valid_move(opponent):
            self.current_player = opponent
        elif self.has_valid_move(self.current_player):
            # 对手无合法移动，当前玩家继续
            pass
        else:
            # 双方都无合法移动，游戏结束
            pass
        self.update_score()
        try:
            if not self.has_valid_move(1) and not self.has_valid_move(2):
                white_score = sum(row.count(1) for row in self.board)
                black_score = sum(row.count(2) for row in self.board)
                if white_score > black_score:
                    messagebox.showinfo('游戏结束', '白棋获胜！')
                elif white_score < black_score:
                    messagebox.showinfo('游戏结束', '黑棋获胜！')
                else:
                    messagebox.showinfo('游戏结束', '平局！')
        except Exception as e:
            print(f'游戏结束判断时出错: {e}')

    def make_move_test(self, row, col):
        self.board[row][col] = self.current_player
        opponent = 3 - self.current_player
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dr, dc in directions:
            to_flip = []
            r, c = row + dr, col + dc

            while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and self.board[r][c] == opponent:
                to_flip.append((r, c))
                r += dr
                c += dc

            if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and self.board[r][c] == self.current_player:
                for r_flip, c_flip in to_flip:
                    self.board[r_flip][c_flip] = self.current_player

        # 切换玩家
        opponent = 3 - self.current_player
        if self.has_valid_move(opponent):
            self.current_player = opponent
        elif self.has_valid_move(self.current_player):
            # 对手无合法移动，当前玩家继续
            pass
        else:
            # 双方都无合法移动，游戏结束
            pass
        self.update_score()
        


    def draw_board(self):
        self.canvas.delete('all')
        # 绘制棋盘网格
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                x1 = j * CELL_SIZE
                y1 = i * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                self.canvas.create_rectangle(x1, y1, x2, y2, fill='#228B22', outline='#006400', width=2)
        # 绘制棋子
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.board[i][j] == 1:
                    x = j * CELL_SIZE + CELL_SIZE // 2
                    y = i * CELL_SIZE + CELL_SIZE // 2
                    self.canvas.create_oval(x - 35, y - 35, x + 35, y + 35, fill='white', outline='gray', width=2)
                elif self.board[i][j] == 2:
                    x = j * CELL_SIZE + CELL_SIZE // 2
                    y = i * CELL_SIZE + CELL_SIZE // 2
                    self.canvas.create_oval(x - 35, y - 35, x + 35, y + 35, fill='black', outline='gray', width=2)
        # 绘制上一次落子的位置
        if self.col is not None and self.row is not None:
            x = self.col * CELL_SIZE + CELL_SIZE // 2
            y = self.row * CELL_SIZE + CELL_SIZE // 2
            self.canvas.create_oval(x - 8, y - 8, x + 8, y + 8, fill='red', outline='gray', width=2)
        # 显示当前玩家的合法落子位置
        self.show_hints()
        
    def show_hints(self):
        for hint in self.hints:
            self.canvas.delete(hint)
        self.hints = []
        # 显示当前玩家的合法落子位置
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.is_valid_move(i, j, self.current_player):
                    x1 = j * CELL_SIZE + 10
                    y1 = i * CELL_SIZE + 10
                    x2 = x1 + CELL_SIZE - 20
                    y2 = y1 + CELL_SIZE - 20
                    hint = self.canvas.create_rectangle(x1, y1, x2, y2, fill='yellow', stipple='gray50')
                    self.hints.append(hint)


    def on_click(self, event):
        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE
        self.col=col
        self.row=row
        # 检查当前玩家的合法移动        
        if self.is_valid_move(row, col, self.current_player):
            self.make_move(row, col)
            self.draw_board()
            # 检查是否轮到 AI 下棋
            if self.mode == self.current_player:
                self.root.after(100, self.ai_move_wrapper)

    def ai_move_wrapper(self):
        if self.mode == self.current_player:
            self.ai_move()
            self.draw_board()
            # 递归调用，直到 AI 下完或者轮到玩家
            if self.mode == self.current_player:
                self.root.after(100, self.ai_move_wrapper)





    def game_over(self):
        return not self.has_valid_move(1) and not self.has_valid_move(2)

    def is_valid_move(self, row, col, player):
        # 检查落子位置是否在棋盘内且为空
        if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE) or self.board[row][col] != 0:
            return False

        # 定义八个方向
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        # 确定对手玩家
        opponent = 3 - player

        # 遍历所有方向
        for dr, dc in directions:
            r, c = row + dr, col + dc
            seen_opponent = False

            # 沿着当前方向检查是否能翻转棋子
            while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE:
                if self.board[r][c] == opponent:
                    seen_opponent = True
                    r += dr
                    c += dc
                elif self.board[r][c] == player and seen_opponent:
                    return True
                else:
                    break

        return False


    def ai_move(self):
        valid_moves = self.get_legal_moves(self.current_player)
        if valid_moves:
            move = self.ai_player.get_move(self)
            if move is not None:
                row, col = move
                self.col=col
                self.row=row
                self.make_move(row, col)
            else:
                row, col = random.choice(valid_moves)
                self.col=col
                self.row=row
                self.make_move(row, col)
                print("AI 未找到合适的走法")
        else:
            opponent = 3 - self.current_player
            if not self.has_valid_move(opponent):
                white_score = sum(row.count(1) for row in self.board)
                black_score = sum(row.count(2) for row in self.board)
                if white_score > black_score:
                    messagebox.showinfo('游戏结束', '白棋获胜！')
                elif white_score < black_score:
                    messagebox.showinfo('游戏结束', '黑棋获胜！')
                else:
                    messagebox.showinfo('游戏结束', '平局！')
            else:
                self.current_player = opponent
            self.update_score()




                
    def get_legal_moves(self, player):
        valid_moves = []
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.is_valid_move(i, j, player):
                    valid_moves.append((i, j))
        return valid_moves



# if __name__ == '__main__':
#     root = tk.Tk()
#     game = ReversiGame(root)
#     root.mainloop()