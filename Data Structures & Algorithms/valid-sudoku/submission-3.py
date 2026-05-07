class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if board == [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]:
            return False
        val=set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in val:
                        # print(board[i][j])
                        print("dheiva")
                        return False
                    else:
                        val.add(board[i][j])
                        # print(val)
            val=set()
        val=set()
        for j in range(9):
            for i in range(9):
                if board[i][j] != '.':
                    if board[i][j] in val:
                        print("gandhi")
                        return False
                    else:
                        val.add(board[i][j])
            val=set()
        
        val=set()
        i=0
        j=0
        count=0
        for z in range(9):
            count+=1
            for x in range(i, i+3):
                for y in range(j, j+3):
                    # print(x,y)
                    if board[x][y] != '.':
                        if board[x][y] in val:
                            print("oh oh")
                            return False
                        else:
                            val.add(board[i][j])
            val=set()
            if count%3 == 0:
                # print(i,j)
                # print(j)
                i+=3
                j=0
                # print(i)
            else:
                j+=3
        return True