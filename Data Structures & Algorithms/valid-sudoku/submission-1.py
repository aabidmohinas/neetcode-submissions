from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def IsValid(l: list) -> bool:
            r = [c for c in l if c != '.']
            return len(set(r)) == len(r)

        rcheck = all([IsValid(r) for r in board])
        ccheck = all([IsValid(c) for c in zip(*board)])

        dictionary = defaultdict(list)
        for r in range(9):
            for c in range(9):
                dictionary[(r // 3, c // 3)].append(board[r][c])

        boxcheck = all([IsValid(r) for r in dictionary.values()])
        return rcheck and ccheck and boxcheck

        
      

