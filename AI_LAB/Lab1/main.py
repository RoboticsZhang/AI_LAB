###############################################################################
# 重要: 请务必把任务(jobs)中需要保存的文件存放在 results 文件夹内
# Important : Please make sure your files are saved to the 'results' folder
# in your jobs
###############################################################################
# 导入棋盘文件
from board import Board

"""
# 初始化棋盘
board = Board()

# 打印初始化棋盘
board.display()
# 查看坐标 (4,3) 在棋盘上的位置 
position = (4, 3)
print(board.num_board(position))

# 查看棋盘位置 'G2' 的坐标
position = 'G2'
print(board.board_num(position))
# 棋盘初始化后，黑方可以落子的位置
print(list(board.get_legal_actions('X')))
# 打印初始化后的棋盘
board.display()

# 假设现在黑棋下棋，可以落子的位置有：['D3', 'C4', 'F5', 'E6']，
# 黑棋落子 D3 , 则白棋被翻转的棋子是 D4。 

# 表示黑棋
color = 'X' 

# 落子坐标
action = 'D3' 

# 打印白方被翻转的棋子位置
print(board._move(action,color))

# 打印棋盘
board.display() 
"""


# 导入随机包
import random

class RandomPlayer:
    """
    随机玩家, 随机返回一个合法落子位置
    """

    def __init__(self, color):
        """
        玩家初始化
        :param color: 下棋方，'X' - 黑棋，'O' - 白棋
        """
        self.color = color
        

    def random_choice(self, board):
        """
        从合法落子位置中随机选一个落子位置
        :param board: 棋盘
        :return: 随机合法落子位置, e.g. 'A1' 
        """
        # 用 list() 方法获取所有合法落子位置坐标列表
        action_list = list(board.get_legal_actions(self.color))

        # 如果 action_list 为空，则返回 None,否则从中选取一个随机元素，即合法的落子坐标
        if len(action_list) == 0:
            return None
        else:
            return random.choice(action_list)

    def get_move(self, board):
        """
        根据当前棋盘状态获取最佳落子位置
        :param board: 棋盘
        :return: action 最佳落子位置, e.g. 'A1'
        """
        if self.color == 'X':
            player_name = '黑棋'
        else:
            player_name = '白棋'
        print("请等一会，对方 {}-{} 正在思考中...".format(player_name, self.color))
        action = self.random_choice(board)
        return action
"""
# 导入棋盘文件
from board import Board

# 棋盘初始化
board = Board() 

# 打印初始化棋盘
board.display() 

# 玩家初始化，输入黑棋玩家
black_player = RandomPlayer("X") 

# 黑棋玩家的随机落子位置
black_action = black_player.get_move(board)  


print("黑棋玩家落子位置: %s"%(black_action))

# 打印白方被翻转的棋子位置
print("黑棋落子后反转白棋的棋子坐标：",board._move(black_action,black_player.color))

# 打印黑棋随机落子后的棋盘
board.display() 

# 玩家初始化，输入白棋玩家
white_player = RandomPlayer("O") 

# 白棋玩家的随机落子位置
white_action = white_player.get_move(board) 

print("白棋玩家落子位置:%s"%(white_action))

# 打印黑棋方被翻转的棋子位置
print("白棋落子后反转黑棋的棋子坐标：",board._move(white_action,white_player.color))

# 打印白棋随机落子后的棋盘
board.display() 
"""


class HumanPlayer:
    """
    人类玩家
    """

    def __init__(self, color):
        """
        玩家初始化
        :param color: 下棋方，'X' - 黑棋，'O' - 白棋
        """
        self.color = color
    

    def get_move(self, board):
        """
        根据当前棋盘输入人类合法落子位置
        :param board: 棋盘
        :return: 人类下棋落子位置
        """
        # 如果 self.color 是黑棋 "X",则 player 是 "黑棋"，否则是 "白棋"
        if self.color == "X":
            player = "黑棋"
        else:
            player = "白棋"

        # 人类玩家输入落子位置，如果输入 'Q', 则返回 'Q'并结束比赛。
        # 如果人类玩家输入棋盘位置，e.g. 'A1'，
        # 首先判断输入是否正确，然后再判断是否符合黑白棋规则的落子位置
        while True:
            action = input(
                    "请'{}-{}'方输入一个合法的坐标(e.g. 'D3'，若不想进行，请务必输入'Q'结束游戏。): ".format(player,
                                                                                 self.color))

            # 如果人类玩家输入 Q 则表示想结束比赛
            if action == "Q" or action == 'q':
                return "Q"
            else:
                row, col = action[1].upper(), action[0].upper()

                # 检查人类输入是否正确
                if row in '12345678' and col in 'ABCDEFGH':
                    # 检查人类输入是否为符合规则的可落子位置
                    if action in board.get_legal_actions(self.color):
                        return action
                else:
                    print("你的输入不合法，请重新输入!")
"""
# 导入棋盘文件
from board import Board

 # 棋盘初始化
board = Board() 

# 打印初始化后棋盘
board.display() 

# 人类玩家黑棋初始化
black_player = HumanPlayer("X") 

# 人类玩家黑棋落子位置
action = black_player.get_move(board)


# 如果人类玩家输入 'Q',则表示想结束比赛，
# 现在只展示人类玩家的输入结果。
if action == "Q":
    print("结束游戏：",action)
else:
    # 打印白方被翻转的棋子位置
    print("黑棋落子后反转白棋的棋子坐标：", board._move(action,black_player.color))

# 打印人类玩家黑棋落子后的棋盘
board.display() 
# 导入黑白棋文件
from game import Game  

# 人类玩家黑棋初始化
black_player = HumanPlayer("X")

# 随机玩家白棋初始化
white_player = RandomPlayer("O")

# 游戏初始化，第一个玩家是黑棋，第二个玩家是白棋
game = Game(black_player, white_player)

# 开始下棋
game.run()
# 导入黑白棋文件
from game import Game  

# 随机玩家黑棋初始化
black_player = RandomPlayer("X")

# 随机玩家白棋初始化
white_player = RandomPlayer("O")

# 游戏初始化，第一个玩家是黑棋，第二个玩家是白棋
game = Game(black_player, white_player)

# 开始下棋
game.run()
"""


class AIPlayer:
    """
    AI 玩家
    """

    def __init__(self, color):
        """
        玩家初始化
        :param color: 下棋方，'X' - 黑棋，'O' - 白棋
        """

        self.color = color

        self.INFINITY = 100

        self.max_depth = 6

    def get_move(self, board):
        """
        根据当前棋盘状态获取最佳落子位置
        :param board: 棋盘
        :return: action 最佳落子位置, e.g. 'A1'
        """
        if self.color == 'X':
            player_name = '黑棋'
        else:
            player_name = '白棋'
        print("请等一会，对方 {}-{} 正在思考中...".format(player_name, self.color))

        # -----------------请实现你的算法代码--------------------------------------

        action, _ = self.alpha_beta_pruning(self.color, board, alpha=-self.INFINITY, beta=self.INFINITY, depth=0)
        # ------------------------------------------------------------------------
        return action

    def alpha_beta_pruning(self, color, board, alpha, beta, depth):
        # initialization
        final_action = None
        action_list = list(board.get_legal_actions(color))
        rival_color = "O" if color == "X" else "X"
        max_node = (color == self.color)

        if not depth == self.max_depth:
            # alpha_beta search by recursion
            # cases that there are legal actions
            if len(action_list):
                for action in action_list:
                    rival_color = "O" if color == "X" else "X"
                    flipped_pos = board._move(action, color)
                    _, temp_value = self.alpha_beta_pruning(rival_color, board, alpha, beta, depth=depth+1)
                    board.backpropagation(action, flipped_pos, color)
                    # max_node
                    if max_node and temp_value > alpha:
                        final_action = action
                        alpha = temp_value
                    # min_node
                    if max_node == 0 and temp_value < beta:
                        final_action = action
                        beta = temp_value
                    # pruning
                    if alpha >= beta:
                        break
            # cases that there aren't legal actions
            else:
                rival_color = "O" if color == "X" else "X"
                _, temp_value = self.alpha_beta_pruning(rival_color, board, alpha, beta, depth=depth+1)
                if max_node:
                    alpha = temp_value
                else:
                    beta = temp_value

            # return alpha(beta) value and action
            if max_node:
                return final_action, alpha
            else:
                return final_action, beta

        # recursive termination condition (return the value of utility function to the parent node)
        else:

            winner, utility = board.get_winner()
            # AI wins (black or white)
            if (winner == 0 and self.color == 'X') or (winner == 1 and self.color == 'O'):
                return None, utility
            # AI loses (black or white)
            else:
                return None, -utility

from board import *


def reverse_color(color):
    if color == 'X':
        return 'O'
    return 'X'


def match_color(color, win):
    if color == 'X':
        return win == 0
    else:
        return win == 1


# 导入黑白棋文件
from game import Game

# 人类玩家黑棋初始化
black_player = HumanPlayer("X")
# AI 玩家 白棋初始化
white_player = AIPlayer("O")

# 游戏初始化，第一个玩家是黑棋，第二个玩家是白棋
game = Game(black_player, white_player)

# 开始下棋
game.run()
