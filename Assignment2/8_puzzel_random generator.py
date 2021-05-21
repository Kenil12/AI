import random

class Randompuzzle:

    def __init__(self, number):
        
        self.CreatePuzzle(number)

    def CreatePuzzle(self,number):
        MAX = 8
        MIN = 0 
        USABLENUMBERS   = list(range(0, 9))
        USEDNUMBERS = []
        board = [-1] * 9
        while(self.checksolvable(board)):
            i = 0
            USEDNUMBERS = []
            board = [-1] * 9
            while(len(USEDNUMBERS) < len(USABLENUMBERS)):
                rand = random.randint(MIN,MAX)
                if(rand not in USEDNUMBERS):
                    USEDNUMBERS.append(rand)
                    board[i] = rand
                    i = i + 1
        self.printboard(board)
        
    
    def checksolvable (self, board):
        inversion = 0
        for i in (range(0, 9)):
            for j in range(i+1, 9):
                # make sure not to count 0 tile
                if (board [i] != 0 and board[j] != 0 and board[i] >= board[j]):
                    inversion = inversion+1
                   
        return inversion%2 == 0
    
    
    def printboard (self, board):
        for i in range(9):
            print(board[i], end=' ')
            if (i+1)%3==0:
                print()

test1= Randompuzzle(0)