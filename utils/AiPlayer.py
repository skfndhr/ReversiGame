import copy
import math
import random
import time
from copy import deepcopy


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
            node, current_board, path = self.select(root, board.copy())
            # 扩张
            if node.is_leaf():
                legal_actions = board.get_legal_moves(node.color)  # 假设board有get_legal_moves方法
                if legal_actions:
                    move = random.choice(legal_actions)
                    node.expand(move)
                    child_node = node.get_child(move)
                    path.append((child_node, current_board.copy(), move))
                    current_board.make_move_test(move[0], move[1])
                    node = child_node
            # 模拟
            winner, _ = self.simulate(current_board.copy(), node.color)
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
            i,j=best_move
            current_board.make_move_test(i,j)
            path.append((node, current_board, best_move))

    # 模拟游戏
        # 模拟游戏
    def simulate(self, board, color):
        current_color = color
        while True:
            legal_actions = board.get_legal_moves(current_color)
            if not legal_actions:
                opponent_actions = board.get_legal_moves(3 - current_color)
                if not opponent_actions:
                    # 双方都无合法移动，游戏结束
                    black_count = sum(row.count(1) for row in board.board)
                    white_count = sum(row.count(2) for row in board.board)
                    if black_count > white_count:
                        return 0, black_count - white_count
                    elif white_count > black_count:
                        return 1, white_count - black_count
                    else:
                        return 2, 0
                else:
                    # 切换到对手玩家
                    current_color = 3 - current_color
                    continue
            move = random.choice(legal_actions)
            board.make_move_test(move[0], move[1])
            # 切换玩家
            current_color = 3 - current_color
             

    # 反向传播
    def back_propagate(self, path, winner):
        for node, _, move in path:
            node.visit_count += 1
            if self.color == 1:  # 假设 1 是黑棋
                if winner == 1:
                    node.win_score += 1
                elif winner == 2:
                    node.win_score += 0
                else:
                    node.win_score += 0.5
            else:  # 假设 2 是白棋
                if winner == 1:
                    node.win_score += 0
                elif winner == 2:
                    node.win_score += 1
                else:
                    node.win_score += 0.5

    # 获取走法
    def get_move(self, board):
        action = self.mcts(board.copy())
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
        child_color = 3-self.color
        self.children[move] = TreeNode(self, child_color)

    # 获取子节点
    def get_child(self, move):
        return self.children.get(move, None)

    # 获取合法走法
    def get_legal_actions(self):
        return list(self.children.keys())

# # 主函数，用于测试
# if __name__ == "__main__":
#     # 创建玩家
#     human_player = HumanPlayer("X")
#     ai_player = AIPlayer("O")

#     # 创建游戏
#     game = Game(human_player, ai_player)

#     # 开始游戏
#     game.run()