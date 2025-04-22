from utils.AiPlayer import HumanPlayer, AIPlayer as AiPlayer
from utils.ReversiGame import ReversiGame
import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    game = ReversiGame(root)
    human_player = HumanPlayer('X')
    ai_player = AiPlayer('O')
    current_player = human_player
    while not game.game_over():
        game.draw_board()
        if isinstance(current_player, HumanPlayer):
            action = current_player.get_move(game.board)
            if action == 'Q':
                break
            row = int(action[1]) - 1
        col = ord(action[0].upper()) - ord('A')
        game.make_move(row, col)
    else:
        action = ai_player.get_move(game.board)
        row = int(action[1]) - 1
        col = ord(action[0].upper()) - ord('A')
        game.make_move(row, col)
        current_player = ai_player if current_player == human_player else human_player
    game.print_board()
    winner = game.get_winner()
    print('游戏结束！')
    if winner == 0:
        print('平局！')
    elif winner == 1:
        print('黑棋获胜！')
    else:
        print('白棋获胜！')