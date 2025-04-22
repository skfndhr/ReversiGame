import math
import random
import time
from copy import deepcopy

# 棋盘类
#class ReversiBoard(object):
#     def __init__(self):
#         self.board_init()

#     def board_init(self):
#         self.empty = '.'
#         self._board = [[self.empty for _ in range(8)] for _ in range(8)]
#         self._board[3][4], self._board[4][3] = 'X', 'X'
#         self._board[3][3], self._board[4][4] = 'O', 'O'

#     # 显示棋盘
#     def display(self, step_time=None, total_time=None):
#         board = self._board
#         print(' ', ' '.join(list('ABCDEFGH')))
#         for i in range(8):
#             print(str(i + 1), ' '.join(board[i]))
#         if not step_time or not total_time:
#             step_time = {"X": 0, "O": 0}
#             total_time = {"X": 0, "O": 0}
#             print("统计棋局: 棋子总数 / 每一步耗时 / 总时间 ")
#             print(f"黑   棋: {self.count('X')} / {step_time['X']} / {total_time['X']}")
#             print(f"白   棋: {self.count('O')} / {step_time['O']} / {total_time['O']}\n")
#         else:
#             print("统计棋局: 棋子总数 / 每一步耗时 / 总时间 ")
#             print(f"黑   棋: {self.count('X')} / {step_time['X']} / {total_time['X']}")
#             print(f"白   棋: {self.count('O')} / {step_time['O']} / {total_time['O']}\n")

#     # 统计棋子数量
#     def count(self, color):
#         count = 0
#         for y in range(8):
#             for x in range(8):
#                 if self._board[x][y] == color:
#                     count += 1
#         return count

#     # 获取游戏结果
#     def get_winner(self):
#         black_count, white_count = 0, 0
#         for i in range(8):
#             for j in range(8):
#                 if self._board[i][j] == 'X':
#                     black_count += 1
#                 if self._board[i][j] == 'O':
#                     white_count += 1
#         if black_count > white_count:
#             return 0, black_count - white_count
#         elif black_count < white_count:
#             return 1, white_count - black_count
#         else:
#             return 2, 0

#     # 移动棋子
#     def _move(self, action, color):
#         if isinstance(action, str):
#             action = self.board_num(action)
#         fliped = self._can_fliped(action, color)
#         if fliped:
#             for flip in fliped:
#                 x, y = self.board_num(flip)
#                 self._board[x][y] = color
#             x, y = action
#             self._board[x][y] = color
#             return fliped
#         else:
#             return False

#     # 撤回移动
#     def backpropagation(self, action, flipped_pos, color):
#         if isinstance(action, str):
#             action = self.board_num(action)
#         self._board[action[0]][action[1]] = self.empty
#         op_color = "O" if color == "X" else "X"
#         for p in flipped_pos:
#             if isinstance(p, str):
#                 p = self.board_num(p)
#             self._board[p[0]][p[1]] = op_color

#     # 判断是否在棋盘内
#     def is_on_board(self, x, y):
#         return x >= 0 and x <= 7 and y >= 0 and y <= 7

#     # 判断是否可以翻转棋子
#     def _can_fliped(self, action, color):
#         if isinstance(action, str):
#             action = self.board_num(action)
#         xstart, ystart = action
#         if not self.is_on_board(xstart, ystart) or self._board[xstart][ystart] != self.empty:
#             return False
#         self._board[xstart][ystart] = color
#         op_color = "O" if color == "X" else "X"
#         flipped_pos = []
#         flipped_pos_board = []
#         for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
#             x, y = xstart, ystart
#             x += xdirection
#             y += ydirection
#             if self.is_on_board(x, y) and self._board[x][y] == op_color:
#                 x += xdirection
#                 y += ydirection
#                 if not self.is_on_board(x, y):
#                     continue
#                 while self._board[x][y] == op_color:
#                     x += xdirection
#                     y += ydirection
#                 if not self.is_on_board(x, y):
#                     break
#                 if not self.is_on_board(x, y):
#                     continue
#                 if self._board[x][y] == color:
#                     while True:
#                         x -= xdirection
#                         y -= ydirection
#                         if x == xstart and y == ystart:
#                             break
#                         flipped_pos.append((x, y))
#         self._board[xstart][ystart] = self.empty
#         if len(flipped_pos) == 0:
#             return False
#         for fp in flipped_pos:
#             flipped_pos_board.append(self.num_board(fp))
#         return flipped_pos_board

#     # 获取合法走法
#     def get_legal_actions(self, color):
#         direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
#         op_color = "O" if color == "X" else "X"
#         op_color_near_points = []
#         board = self._board
#         for i in range(8):
#             for j in range(8):
#                 if board[i][j] == op_color:
#                     for dx, dy in direction:
#                         x, y = i + dx, j + dy
#                         if 0 <= x <= 7 and 0 <= y <= 7 and board[x][y] == self.empty and (x, y) not in op_color_near_points:
#                             op_color_near_points.append((x, y))
#         l = [0, 1, 2, 3, 4, 5, 6, 7]
#         for p in op_color_near_points:
#             if self._can_fliped(p, color):
#                 if p[0] in l and p[1] in l:
#                     p = self.num_board(p)
#                 yield p

#     # 坐标转换
#     def board_num(self, action):
#         row, col = str(action[1]).upper(), str(action[0]).upper()
#         if row in '12345678' and col in 'ABCDEFGH':
#             x, y = '12345678'.index(row), 'ABCDEFGH'.index(col)
#             return x, y

#     def num_board(self, action):
#         row, col = action
#         l = [0, 1, 2, 3, 4, 5, 6, 7]
#         if col in l and row in l:
#             return chr(ord('A') + col) + str(row + 1)

# 游戏类
# class Game(object):
#     def __init__(self, black_player, white_player):
#         self.game_init()
#         self.black_player = black_player
#         self.white_player = white_player

#     def game_init(self):
#         self.board = ReversiBoard()
#         self.current_player = None

#     # 切换玩家
#     def switch_player(self, black_player, white_player):
#         if self.current_player is None:
#             return black_player
#         else:
#             if self.current_player == self.black_player:
#                 return white_player
#             else:
#                 return black_player

#     # 打印获胜者
#     def print_winner(self, winner):
#         print(['黑棋获胜!', '白棋获胜!', '平局'][winner])

#     # 强制输棋
#     def force_loss(self, is_timeout=False, is_board=False, is_legal=False):
#         if self.current_player == self.black_player:
#             win_color = '白棋 - O'
#             loss_color = '黑棋 - X'
#             winner = 1
#         else:
#             win_color = '黑棋 - X'
#             loss_color = '白棋 - O'
#             winner = 0
#         if is_timeout:
#             print(f'\n{loss_color} 思考超过 60s, {win_color} 胜')
#         if is_legal:
#             print(f'\n{loss_color} 落子 3 次不符合规则, 故 {win_color} 胜')
#         if is_board:
#             print(f'\n{loss_color} 擅自改动棋盘判输, 故 {win_color} 胜')
#         diff = 0
#         return winner, diff

#     # 运行游戏
#     def run(self):
#         total_time = {"X": 0, "O": 0}
#         step_time = {"X": 0, "O": 0}
#         winner = None
#         diff = -1
#         print('\n=====开始游戏!=====\n')
#         self.board.display(step_time, total_time)
#         while True:
#             self.current_player = self.switch_player(self.black_player, self.white_player)
#             start_time = time.time()
#             color = "X" if self.current_player == self.black_player else "O"
#             legal_actions = list(self.board.get_legal_actions(color))
#             if len(legal_actions) == 0:
#                 if self.game_over():
#                     winner, diff = self.board.get_winner()
#                     break
#                 else:
#                     continue
#             board = deepcopy(self.board._board)
#             try:
#                 action = self.current_player.get_move(self.board)
#                 if action == "Q":
#                     break
#                 if action not in legal_actions:
#                     print("你落子不符合规则, 请重新落子！")
#                     continue
#             except Exception as e:
#                 winner, diff = self.force_loss(is_timeout=True)
#                 break
#             end_time = time.time()
#             if board != self.board._board:
#                 winner, diff = self.force_loss(is_board=True)
#                 break
#             if action == "Q":
#                 winner, diff = self.board.get_winner()
#                 break
#             if action is None:
#                 continue
#             else:
#                 es_time = end_time - start_time
#                 if es_time > 60:
#                     print(f'\n{self.current_player} 思考超过 60s')
#                     winner, diff = self.force_loss(is_timeout=True)
#                     break
#                 self.board._move(action, color)
#                 if self.current_player == self.black_player:
#                     step_time["X"] = es_time
#                     total_time["X"] += es_time
#                 else:
#                     step_time["O"] = es_time
#                     total_time["O"] += es_time
#                 self.board.display(step_time, total_time)
#                 if self.game_over():
#                     winner, diff = self.board.get_winner()
#                     break
#         print('\n=====游戏结束!=====\n')
#         self.board.display(step_time, total_time)
#         self.print_winner(winner)
#         if winner is not None and diff > -1:
#             result = {0: 'black_win', 1: 'white_win', 2: 'draw'}[winner]

#     # 判断游戏是否结束
#     def game_over(self):
#         b_list = list(self.board.get_legal_actions('X'))
#         w_list = list(self.board.get_legal_actions('O'))
#         is_over = len(b_list) == 0 and len(w_list) == 0
#         return is_over

# 人类玩家类
# class HumanPlayer:
#     def __init__(self, color):
#         self.color = color

#     def get_move(self, game):
#         # 确保 game 是 ReversiGame 实例
#         if not isinstance(game, ReversiGame):
#             print('错误：game 不是 ReversiGame 实例')
#             return None
#         import threading
#         import queue
#         move_queue = queue.Queue()

#         def on_click(event):
#             col = event.x // game.CELL_SIZE
#             row = event.y // game.CELL_SIZE
#             action = chr(ord('A') + col) + str(row + 1)
#             if action in game.get_legal_actions(self.color):
#                 move_queue.put(action)
#                 game.canvas.unbind('<Button-1>')

#         game.canvas.bind('<Button-1>', on_click)
#         try:
#             return move_queue.get(timeout=60)
#         except queue.Empty:
#             print('思考超过 60s，自动结束当前操作。')
#             return None

# AI 玩家类
class AIPlayer:
    def __init__(self, color, time_limit=5):
        self.time_limit = time_limit
        self.color = color

    # MCTS 算法
    def mcts(self, board):
        root = TreeNode(None, self.color)
        start_time = time.time()
        while time.time() - start_time < self.time_limit:
            # 选择
            node, current_board, path = self.select(root, deepcopy(board))
            # 扩张
            if not node.is_leaf():
                move = random.choice(list(node.get_legal_actions()))
                node.expand(move)
                child_node = node.get_child(move)
                path.append((child_node, deepcopy(current_board), move))
                current_board, _ = current_board._move(move, node.color)
                node = child_node
            # 模拟
            winner, _ = self.simulate(deepcopy(current_board), node.color)
            # 反向传播
            self.back_propagate(path, winner)
        # 选择访问次数最多的子节点对应的走法
        best_move = None
        max_visit = -1
        for move, child in root.children.items():
            if child.visit_count > max_visit:
                max_visit = child.visit_count
                best_move = move
        return best_move

    # 选择节点
    def select(self, node, board):
        path = []
        current_board = board
        while True:
            path.append((node, current_board, None))
            if node.is_leaf():
                return node, current_board, path
            # 选择 UCB 值最大的子节点
            best_value = -float('inf')
            best_node = None
            best_move = None
            for move, child in node.children.items():
                ucb_value = child.win_score / child.visit_count + math.sqrt(2 * math.log(node.visit_count) / child.visit_count)
                if ucb_value > best_value:
                    best_value = ucb_value
                    best_node = child
                    best_move = move
            node = best_node
            current_board._move(best_move, node.color)
            path.append((node, current_board, best_move))

    # 模拟游戏
    def simulate(self, board, color):
        current_color = color
        while True:
            legal_actions = list(board.get_legal_actions(current_color))
            if not legal_actions:
                # 判断游戏是否结束
                black_count = board.count('X')
                white_count = board.count('O')
                if black_count > white_count:
                    return 0, black_count - white_count
                elif white_count > black_count:
                    return 1, white_count - black_count
                else:
                    return 2, 0
            move = random.choice(legal_actions)
            board._move(move, current_color)
            current_color = 'O' if current_color == 'X' else 'X'

    # 反向传播
    def back_propagate(self, path, winner):
        for node, _, move in path:
            node.visit_count += 1
            if node.color == 'X':
                if winner == 0:
                    node.win_score += 1
                elif winner == 1:
                    node.win_score += 0
                else:
                    node.win_score += 0.5
            else:
                if winner == 1:
                    node.win_score += 1
                elif winner == 0:
                    node.win_score += 0
                else:
                    node.win_score += 0.5

    # 获取走法
    def get_move(self, board):
        action = self.mcts(deepcopy(board))
        return action

# 节点类
class TreeNode:
    def __init__(self, parent, color):
        self.parent = parent
        self.color = color
        self.visit_count = 0
        self.win_score = 0.0
        self.children = {}

    # 判断是否是叶子节点
    def is_leaf(self):
        return len(self.children) == 0

    # 扩展子节点
    def expand(self, move):
        child_color = 'O' if self.color == 'X' else 'X'
        self.children[move] = TreeNode(self, child_color)

    # 获取子节点
    def get_child(self, move):
        return self.children.get(move, None)

    # 获取合法走法
    def get_legal_actions(self):
        return list(self.children.keys())

# 主函数，用于测试
if __name__ == "__main__":
    # 创建玩家
    human_player = HumanPlayer("X")
    ai_player = AIPlayer("O")

    # 创建游戏
    game = Game(human_player, ai_player)

    # 开始游戏
    game.run()