class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # rows
        for row in range(len(board)):
            nums = []
            for num in board[row]:
                if num == ".":
                    continue
                nums.append(int(num))
            if len(set(nums)) != len(nums):
                return False
            

        # cols
        for i in range(len(board)):
            nums = []
            for j in range(len(board)):
                num = board[i][j]
                if num == ".":
                    continue
                nums.append(int(num))
            if len(set(nums)) != len(nums):
                return False

        # sqs



        return True