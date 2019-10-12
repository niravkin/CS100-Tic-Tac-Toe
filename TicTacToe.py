import random
import string
import time
import turtle

class Game:        
    def createGame():
        ''' Creates a new tic-tac-toe game. Sets up a screen for output, a turtle, and an initial empty board state.'''
        global boardState
        boardState = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        
        global gameScreen
        global gameDraw
        global penDraw #text only
        gameScreen = turtle.Screen()
        gameScreen.setup(1000, 1000, 0, 0) #size of the screen
        gameScreen.title('Tic-Tac-Toe')
        
        gameDraw = turtle.Turtle()
        penDraw = turtle.Turtle()
        penDraw.hideturtle()
        penDraw.speed(0)
        
        gameDraw.hideturtle()
        gameDraw.speed(0)
        gameDraw.penup()
        
        Game.getName(gameScreen) #Ask for player names
        Game.drawGrid() #Draw playing grid
        Game.runGame() #Start the game
    
    def runGame():
        ''' Starts the game. Randomly selects a player to go first.'''
        global moveX
        global moveO
        random.seed() #seed with current time
        turn = random.randint(1, 100)
        if turn <= 50:
            moveX = False
            moveO = True
            Game.turtleWrite(penDraw, 0, 370, "It is " + nameO + "'s turn.")
        else:  
            moveO = False
            moveX = True
            Game.turtleWrite(penDraw, 0, 370, "It is " + nameX + "'s turn.")
            
        while True:
            state = Game.getGameState()
            if state == 1: #1 for a non draw-state
                Game.turtleWrite(penDraw, 0, 400, "The game is still in play.")
                Game.chooseBox()
                penDraw.clear()
                Game.getMove()
            elif state == 0: #0 for a draw state
                penDraw.clear()
                Game.turtleWrite(penDraw, 0, 375, "The game is a draw.")
                break
            elif state == "X":
                penDraw.clear()
                Game.turtleWrite(penDraw, 0, 375, "Game over! " + nameX + " wins!")
                break
            elif state == "O":
                penDraw.clear()
                Game.turtleWrite(penDraw, 0, 375, "Game over! " + nameO + " wins!")
                break

    def drawGrid():
        ''' Draws a 3x3 tic-tac-toe grid. Labels each cell. '''
        gameDraw.goto(-300, -300)
        gameDraw.pendown()
        for i in range(4):
            gameDraw.forward(600)
            gameDraw.left(90)
        for i in range(2):
            gameDraw.forward(200)
            gameDraw.left(90)
            gameDraw.forward(600)
            gameDraw.back(600)
            gameDraw.right(90)
        gameDraw.back(400)
        for i in range(2):
            gameDraw.left(90)
            gameDraw.forward(200)
            gameDraw.right(90)
            gameDraw.forward(600)
            gameDraw.back(600)
        gameDraw.right(90)
        gameDraw.forward(400)
        gameDraw.left(90)

        gameDraw.penup()
        gameDraw.goto(-285,270)
        gameDraw.write('1', True, 'left', ('Arial', 12, 'bold'))

        gameDraw.goto(-85,270)
        gameDraw.write('2', True, 'left', ('Arial', 12, 'bold'))

        gameDraw.goto(115,270)
        gameDraw.write('3', True, 'left', ('Arial', 12, 'bold'))
        
        gameDraw.goto(-285,70)
        gameDraw.write('4', True, 'left', ('Arial', 12, 'bold'))

        gameDraw.goto(-85,70)
        gameDraw.write('5', True, 'left', ('Arial', 12, 'bold'))

        gameDraw.goto(115,70)
        gameDraw.write('6', True, 'left', ('Arial', 12, 'bold'))

        gameDraw.goto(-285,-130)
        gameDraw.write('7', True, 'left', ('Arial', 12, 'bold'))

        gameDraw.goto(-85,-130)
        gameDraw.write('8', True, 'left', ('Arial', 12, 'bold'))

        gameDraw.goto(115,-130)
        gameDraw.write('9', True, 'left', ('Arial', 12, 'bold'))

    
    def drawX():
        ''' Draws an 'X'. Corresponds to a move made by player X. '''
        gameDraw.pendown()
        for i in range(2):
            gameDraw.right(45)
            gameDraw.forward(75)
            gameDraw.back(75)
            gameDraw.right(90)
            gameDraw.forward(75)
            gameDraw.back(75)
            gameDraw.right(45)
        gameDraw.penup()

    def drawO():
        ''' Draws an 'O'. Corresponds to a move made by player O. '''
        gameDraw.penup()
        gameDraw.right(90)
        gameDraw.forward(75)
        gameDraw.left(90)
        gameDraw.pendown()
        gameDraw.circle(75)
        gameDraw.penup()
        
    def getMove():
        global moveX
        global moveO
        global gameDraw
        
        if moveX:
            gameDraw.penup()
            gameDraw.goto(drawSpotX, drawSpotY)
            gameDraw.pendown()
            Game.drawX()
            boardState[cell] = "X"
                
            moveX = False
            moveO = True
            Game.turtleWrite(penDraw, 0, 370, "It is " + nameO + "'s turn.")
                
        elif moveO:
            gameDraw.penup()
            gameDraw.goto(drawSpotX, drawSpotY)
            gameDraw.pendown()
            Game.drawO()
            boardState[cell] = "O"
                  
            moveO = False
            moveX = True
            Game.turtleWrite(penDraw, 0, 370, "It is " + nameX + "'s turn.")
    
    def chooseBox():
        while True:
            Game.turtleWrite(penDraw, 0, 340, "Select an empty box.")
            bNum = input("Select box 1-9 (starting from the top-left): ")

            #Check for invalid input
            if not bNum.isdigit() or int(bNum) > 9 or int(bNum) < 1 or not boardState[int(bNum)-1] == "-":
                print("Please select an empty cell numbers 1-9")
            else:
                break
        
        global drawSpotX
        global drawSpotY
        global cell

        #convert to int
        boxNumber = int(bNum)

        #Move cursor to draw area based on boxNumber
        if boxNumber == 1:
            drawSpotX = -200
            drawSpotY = 200
        elif boxNumber == 2:
            drawSpotX = 0
            drawSpotY = 200
        elif boxNumber == 3:
            drawSpotX = 200
            drawSpotY = 200
        elif boxNumber ==  4:
            drawSpotX = -200
            drawSpotY = 0
        elif boxNumber == 5:
            drawSpotX = 0
            drawSpotY = 0
        elif boxNumber == 6:
            drawSpotX = 200
            drawSpotY = 0
        elif boxNumber == 7:
            drawSpotX = -200
            drawSpotY = -200
        elif boxNumber == 8:
            drawSpotX = 0
            drawSpotY = -200
        elif boxNumber == 9:
            drawSpotX = 200
            drawSpotY = -200

        cell = boxNumber - 1

        return 

    def getName(t):
        global nameX
        global nameO
        nameX = t.textinput("Player X", "What is Player X's name?")
        nameO = t.textinput("Player O", "What is Player O's name?")

        #nameX = input("What is player X's name? ")
        #nameO = input("What is player O's name? ")

    def getGameState():
        state = ""
        isDraw = True
        for i in range(3):
            #Check for vertical win conditions. 0,3,6; 1,4,7; 2,5,8
            if not boardState[i] == "-" and boardState[i] == boardState[i+3] == boardState[i+6] :
                state = boardState[i]
                return state
        for i in range(3):
            #Check for horizontal win conditions. 0,1,2; 3,4,5; 6,7,8
            if not boardState[i*3] == "-" and boardState[i*3] == boardState[i*3+1] == boardState[i*3+2]:
                state = boardState[i]
                return state
        #Check for diagonal win condition 1: 0,4,8
        if not boardState[0] == "-" and boardState[0] == boardState[4] == boardState[8]:
            state = boardState[0]
            return state
        
        #Check for diagonal win condition 2: 2,4,6
        if not boardState[2] == "-" and boardState[2] == boardState[4] == boardState[6]:
            state = boardState[2]
            return state

        #Game is not won yet:
        
        for gameState in boardState:
            #Check for a draw. Draw if no slot is empty '-' and the game is not won
            if gameState == "-":
                isDraw = False
                
        if isDraw:
            state = 0 #0 for a draw state
        else:
            state = 1 #1 for a non-draw state 

        return state

    def turtleWrite(t, positionX, positionY, message):
        t.pu()
        t.goto(positionX, positionY)
        t.write(message, False, 'center', ('Arial', 16, 'bold'))


Game.createGame()
