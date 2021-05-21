import sys, copy
import random
import datetime

goal = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', ' ']]




def main():
    t0 = datetime.datetime.now()
    inputt = puzzleInput() 
    algoChoice = algorithm() 
    puzzleSearch(inputt, algoChoice) 
    t1 = datetime.datetime.now()
    time = t1-t0
    print("Time taken is :",time.microseconds)

def puzzleInput():

    # the default puzzle to use
    # default = [['1', '2', '3'], ['4', ' ', '6'], ['7', '5', '8']]
    # default = [[' ', '1', '3'], ['4', '2', '5'], ['7', '8', '6']]
    default = [['1', '2', '3'], [' ', '4', '6'], ['7', '5', '8']]
    # default = [['1', '2', ' '], ['4', '6', '3'], ['7', '5', '8']]
    # set our main puzzle
    puzzle = []

   
    
    while 1:
        
        startinput = input("Type 1 to bigin puzzle,or -1 to quit.\n")

        # 1: default puzzle
        if (startinput == "1"):
           
            puzzle = default
            return puzzle
        # -1: exit
        elif (startinput == "-1"):
            sys.exit(0)


def algorithm():
    
    print ("Choice of algorithms to use for A*:")
    print ("1. The misplaced tile heuristic")
    print ("2: The Manhattan distance heuristic")
    print ("3. The max of the misplaced tile heuristic and the Manhattan distance heurist\n")
   
    while 1:
        pick = input("Enter: ")
        if(pick == '1'):
           return "misplacedTile"
           
        elif(pick == '2'):
            return "manhattan_distance"
            
        elif(pick == '3'):
            return "max_misplaced"

    return pick


def expand(puzzle):

    expandList = []

    puzzleLeft = copy.deepcopy(puzzle)
  
    for x in puzzleLeft:
        # check where the blank tile is
        if (x.count(' ') == 1):
            # make sure it's not on the left side
            # so we can actually move it legally
            if (x.index(' ') != 0):
                spaceindex = x.index(' ')
                # set space to equal left tile
                x[spaceindex] = x[spaceindex - 1]
                x[spaceindex - 1] = ' '

                expandList.append(puzzleLeft)

    puzzleRight = copy.deepcopy(puzzle)
    # move the tile right
    for x in puzzleRight:
        # check where the blank tile is    print puzzle

        if (x.count(' ') == 1):
            # make sure it's not on the right side
            # so we can actually move it legally
            if (x.index(' ') != 2):
                spaceindex = x.index(' ')
                # set space to equal right tile
                x[spaceindex] = x[spaceindex + 1]
                x[spaceindex + 1] = ' '

                expandList.append(puzzleRight)

    puzzleUp = copy.deepcopy(puzzle)
    # move the tile up
    for x in puzzle:
        # check where the blank tile is
        if (x.count(' ') == 1):
            # make sure it's not on the top (first row)
            # so we can actually move it legally
            if (x != puzzleUp[0]):
                spaceindex = x.index(' ')
                # on second row?
                if(x == puzzle[1]):
                    puzzleUp[1][spaceindex] = puzzleUp[0][spaceindex]
                    puzzleUp[0][spaceindex] = ' '
                    expandList.append(puzzleUp)
                # or third
                else:
                    puzzleUp[2][spaceindex] = puzzleUp[1][spaceindex]
                    puzzleUp[1][spaceindex] = ' '
                    expandList.append(puzzleUp)


    puzzleDown = copy.deepcopy(puzzle)
    # move the tile down
    for x in puzzle:
        # check where the blank tile is
        if (x.count(' ') == 1):
      
            if (x != puzzle[2]):
                spaceindex = x.index(' ')
                # on first row?
                if(x == puzzle[0]):
                    puzzleDown[0][spaceindex] = puzzleDown[1][spaceindex]
                    puzzleDown[1][spaceindex] = ' '
                    expandList.append(puzzleDown)
                # or second
                else:
                    puzzleDown[1][spaceindex] = puzzleDown[2][spaceindex]
                    puzzleDown[2][spaceindex] = ' '
                    expandList.append(puzzleDown)

    return expandList


# create our node class for enqueuing puzzle states
class node:

    def __init__(self):
        self.heuristic = 0
        self.depth = 0
        
    def printPuzzle(self):
        print ('')
        print (self.puzzleState[0][0], self.puzzleState[0][1], self.puzzleState[0][2])
        print (self.puzzleState[1][0], self.puzzleState[1][1], self.puzzleState[1][2])
        print (self.puzzleState[2][0], self.puzzleState[2][1], self.puzzleState[2][2])

    def setPuzzle(self, puzzle):
        self.puzzleState = puzzle


def checkGoal(puzzle):
    # check if puzzle has been solved (equals goal state)
    return goal == puzzle


def misplacedTiles(puzzle):
    
    misplace = 0
    for x in range(3):
        for y in range(3):
            # make sure we don't check blank
            if (puzzle[x][y] != ' '):
                # if it's not at it's proper place, it's misplaced
                if (puzzle[x][y] != goal[x][y]):
                    misplace += 1

    return misplace


def manhattan_distance(puzzle):

    mDistance = 0
    puzzleContents = ['1', '2', '3', '4', '5', '6', '7', '8']
   
    for x in puzzleContents:
        for i in range(3):
            for j in range(3):
                # get where the number should be
                if (x == goal[i][j]):
                    goalRow = i
                    goalCol = j
                # get where the number is now
                if (x == puzzle[i][j]):
                    puzzleRow = i
                    puzzleCol = j
      
        mDistance += ( abs(goalRow - puzzleRow) + abs(goalCol - puzzleCol) )

    return mDistance



def bubblesort(que):

    for passesLeft in range(len(que)-1, 0, -1):
        for index in range(passesLeft):
            if (que[index].heuristic + que[index].depth) > \
                   (que[index + 1].heuristic + que[index + 1].depth):
                que[index], que[index + 1] = que[index + 1], que[index]

    return que


def puzzleSearch(puzzle, algorithm):

    nodesExpanded = 0
    maxQueueSize = 0
    queue = []

    # make the new node (set to intial puzzle)
    puzzleNode = node()
    puzzleNode.setPuzzle(puzzle)
    # the initial depth
    puzzleNode.depth = 0
    # pick our heuristics algorithm
    if (algorithm == "max_misplaced"):
        puzzleNode.heuristic = 1
    if (algorithm == "misplacedTile"):
        puzzleNode.heuristic = misplacedTiles(puzzleNode.puzzleState)
    if (algorithm == "manhattan"):
        puzzleNode.heuristic = manhattan_distance(puzzleNode.puzzleState)

  
    queue.append(puzzleNode)

  
    while 1:

        if (len(queue) == 0):
            print ("Puzzle search exhausted")
            sys.exit(0)

        
        checkNode = node()
        checkNode.puzzleState = queue[0].puzzleState
        checkNode.heuristic = queue[0].heuristic
        checkNode.depth = queue[0].depth

        print ('')
        print ("The best node to expand with g(n) =", checkNode.depth, \
              "and h(n) =", checkNode.heuristic, "is...")
        checkNode.printPuzzle()
        print ("Expanding this node...")
        
        
        queue.pop(0)

       
        if (checkGoal(checkNode.puzzleState)):
            
            print ('')
            print ("Solution found!!")
            checkNode.printPuzzle()
            print ('')
            print ("Expanded a total of", nodesExpanded, "nodes")
            print ("Maximum number of nodes in the queue was", maxQueueSize)
            print ("The depth of the goal node was", checkNode.depth)
            return

      
        expandedPuzzle = expand(checkNode.puzzleState)

        for x in expandedPuzzle:
            
            tempNode = node()
            tempNode.setPuzzle(x)
            
            if (algorithm == "max_misplaced"):
                tempNode.heuristic = 1
            if (algorithm == "misplacedTile"):
                tempNode.heuristic = misplacedTiles(tempNode.puzzleState)
            if (algorithm == "manhattan_distance"):
                tempNode.heuristic = manhattan_distance(tempNode.puzzleState)
           
            tempNode.depth = checkNode.depth + 1
            
            queue.append(tempNode)
            nodesExpanded += 1

            if(len(queue) > maxQueueSize):
                maxQueueSize = len(queue)

        queue = bubblesort(queue)

    
if __name__ == "__main__":
    main()