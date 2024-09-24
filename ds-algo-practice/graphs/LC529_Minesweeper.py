class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def countMines(someR, someC):
            neighbours = [[someR+1, someC], [someR-1, someC], [someR, someC+1], [someR, someC-1], \
            [someR+1, someC+1], [someR-1, someC+1], [someR-1, someC-1], [someR+1, someC-1]]
            count = 0
            for r, c in neighbours:
                if not (r < 0 or c < 0 or r >= ROWS or c >= COLS) and board[r][c] == 'M':
                    count += 1
            return count
    
        ROWS, COLS = len(board), len(board[0])
        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        elif board[r][c] == 'E':
            mines = countMines(r, c)
            if mines == 0:
                board[r][c] = 'B'
                neighbours = [[r+1, c], [r-1, c], [r, c+1], [r, c-1], \
                [r+1, c+1], [r-1, c+1], [r-1, c-1], [r+1, c-1]]
                validNeighbours = []
                for newR, newC in neighbours:
                    if not (newR < 0 or newC < 0 or newR >= ROWS or newC >= COLS):
                        validNeighbours.append([newR, newC])
                for newClick in validNeighbours:
                   self.updateBoard(board, newClick)
            else:
                board[r][c] = f"{mines}"
        return board
            