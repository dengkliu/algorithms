# On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.
# A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.
# The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

# Given a puzzle board, return the least number of moves required so that the state of the board is solved. 
# If it is impossible for the state of the board to be solved, return -1.

# board will be a 2 x 3 array as described above.
# board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].

# Given board = `[[1,2,3],[4,0,5]]`, return `1`.

# Explanation: 
# Swap the 0 and the 5 in one move.

class Solution(object):
    
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        def convert_board_to_state(board):
            state_list = []
            for i in range(len(board)):
                for j in range(len(board[0])):
                    state_list.append(str(board[i][j]))

            return "".join(state_list)

        def get_next(curr_state):
            next_states = []
            zero_index = curr_state.find('0')
            zero_row = zero_index // len(board[0])
            zero_col = zero_index % len(board[0])
            for row_d, col_d in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                adj_row = zero_row + row_d
                adj_col = zero_col + col_d

                if adj_row < 0 or adj_row >= len(board):
                    continue
                if adj_col < 0 or adj_col >= len(board[0]):
                    continue

                number_index =  adj_row*len(board[0]) + adj_col
                next_state = list(curr_state)
                next_state[zero_index] = next_state[number_index]
                next_state[number_index] = '0'
                next_states.append("".join(next_state))

            return next_states

        destination = [[1,2,3],[4,5,0]]
        destination_state = convert_board_to_state(destination)
        start = convert_board_to_state(board)
        queue = collections.deque()
        queue.append(start)
        distance = {start:0}
