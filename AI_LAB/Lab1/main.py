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


class AIPlayer2:
    """
    AI 玩家
    """

    def __init__(self, color):
        """
        玩家初始化
        :param color: 下棋方，'X' - 黑棋，'O' - 白棋
        """

        self.color = color
        self.minimax_step = 3
        self.ab_step = 4
        self.search = 'alpha-beta'

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

        action = None
        if self.search == 'minimax':
            action, val = self.minimax(board, self.color, self.minimax_step)
        else:
            import math
            action, val = self.alpha_beta_prunig(board, self.color, self.ab_step, -math.inf, math.inf)
        # ------------------------------------------------------------------------

        return action

    def get_score(self, board):
        win, val = board.get_winner()
        if not match_color(self.color, win):
            val = -val
        return val

    def minimax(self, board, color, step):
        action, val = None, None
        if step > 0:
            is_max_node = color == self.color
            legal_actions = list(board.get_legal_actions(color))
            if len(legal_actions):
                for action_t in legal_actions:
                    flipped = board._move(action_t, color)
                    _, val_t = self.minimax(board, reverse_color(color), step - 1)
                    board.backpropagation(action_t, flipped, color)

                    if val is None:
                        val = val_t
                        action = action_t
                    else:
                        if (is_max_node and (val_t > val)) or (not is_max_node and (val_t < val)):
                            val = val_t
                            action = action_t
            else:
                _, val = self.minimax(board, reverse_color(color), step - 1)
        else:
            val = self.get_score(board)
        return action, val

    def alpha_beta_prunig(self, board, color, step, alpha, beta):
        action, val = None, None
        if step > 0:
            is_max_node = color == self.color
            legal_actions = list(board.get_legal_actions(color))
            if len(legal_actions):
                for action_t in legal_actions:
                    flipped = board._move(action_t, color)
                    _, val_t = self.alpha_beta_prunig(board, reverse_color(color), step - 1, alpha, beta)
                    board.backpropagation(action_t, flipped, color)

                    if is_max_node and val_t > alpha:
                        alpha = val_t
                        action = action_t
                    if not is_max_node and val_t < beta:
                        beta = val_t
                        action = action_t
                    if alpha >= beta:
                        break
                if is_max_node:
                    val = alpha
                else:
                    val = beta
            else:
                _, val = self.alpha_beta_prunig(board, reverse_color(color), step - 1, alpha, beta)
        else:
            val = self.get_score(board)
        return action, val


from copy import deepcopy
from treelib import Tree, Node
import math


class AIPlayer3:
    """
    AI 玩家
    """

    def __init__(self, color):
        """
        玩家初始化
        :param color: 下棋方，'X' - 黑棋，'O' - 白棋
        """

        self.color = color
        self.Cp = 0.2
        self.root = 'root'
        self.tree = Tree()
        self.times = 100
        self.max_deep = 15

    def cal_color(self, color):
        if color == 'X':
            return 'O'
        else:
            return 'X'

    def game_over(self, board):
        b_list = list(board.get_legal_actions('X'))
        w_list = list(board.get_legal_actions('O'))
        is_over = len(b_list) == 0 and len(w_list) == 0
        return is_over

    def uct_search(self, board):

        new_board = deepcopy(board)
        self.tree.create_node(identifier=self.root, data=(0, 0, new_board, self.color))

        # explore and exploit
        cnt = 0
        while cnt < self.times:
            temp_node_id = self.tree_policy(self.root)
            winner = self.defautl_policy(temp_node_id)
            self.backup(temp_node_id, winner)
            cnt += 1

        # modify tree
        # without memory version

        # new_root, best_action = best_child(v0, 0)
        best_child_id = self.best_child(self.root, 0)
        best_action = self.tree.get_node(best_child_id).tag
        self.tree = Tree()

        return best_action

    def tree_policy(self, node_id):

        # initialize
        node = self.tree.get_node(node_id)
        Q, N, board, color = node.data
        action_list = list(board.get_legal_actions(color))
        child_list = self.tree.children(node_id)

        while self.game_over(board) != True:

            if len(action_list) > len(child_list) or (len(action_list) == 0 and len(child_list) == 0):
                return self.expand(node_id)
            else:
                node_id = self.best_child(node_id, self.Cp)

                node = self.tree.get_node(node_id)
                Q, N, board, color = node.data
                action_list = list(board.get_legal_actions(color))
                child_list = self.tree.children(node_id)

        return node_id

    def expand(self, node_id):

        # initialize
        node = self.tree.get_node(node_id)
        Q, N, board, color = node.data
        action_list = list(board.get_legal_actions(color))
        child_list = self.tree.children(node_id)
        tried_list = []

        for child in child_list:
            tried_list.append(child.tag)

        action = None
        while len(action_list) > 0:
            action = random.choice(action_list)
            if action not in tried_list: break

        new_board = deepcopy(board)
        if action != None:
            new_board._move(action, color)

        new_node = self.tree.create_node(parent=node_id, tag=action, data=(0, 0, new_board, self.cal_color(color)))

        return new_node.identifier

    def best_child(self, node_id, c):

        best_value = -float('inf')
        best_child = None

        _, N_all, _, _ = self.tree.get_node(node_id).data
        child_list = self.tree.children(node_id)

        for child in child_list:

            Q, N, board, color = child.data
            temp_value = Q / N + c * math.sqrt(2 * math.log(N_all) / N)
            if temp_value > best_value:
                best_value = temp_value
                best_child = child

        return best_child.identifier

    def defautl_policy(self, node_id):

        node = self.tree.get_node(node_id)
        _, _, board, color = node.data

        temp_board = deepcopy(board)

        cnt = 0
        while self.game_over(temp_board) != True and cnt < self.max_deep:
            cnt += 1
            action_list = list(temp_board.get_legal_actions(color))
            if len(action_list) != 0:
                action = random.choice(action_list)
                temp_board = deepcopy(temp_board)
                temp_board._move(action, color)
                color = self.cal_color(color)
            else:
                color = self.cal_color(color)

        winner, _ = temp_board.get_winner()
        return winner

    def backup(self, node_id, winner):

        temp_node_id = node_id
        while True:
            temp_node = self.tree.get_node(temp_node_id)
            Q, N, board, color = temp_node.data

            if (winner == 0 and color == 'O') or (winner == 1 and color == 'X'):
                Q += 1

            temp_node.data = (Q, N + 1, board, color)
            if temp_node_id == self.root:
                break
            temp_node_id = self.tree.parent(temp_node_id).identifier

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
        action = self.uct_search(board)
        # ------------------------------------------------------------------------

        return action
# 导入黑白棋文件
from game import Game

# 人类玩家黑棋初始化
black_player = AIPlayer2("X")
# AI 玩家 白棋初始化
white_player = AIPlayer("O")

# 游戏初始化，第一个玩家是黑棋，第二个玩家是白棋
game = Game(black_player, white_player)

# 开始下棋
game.run()