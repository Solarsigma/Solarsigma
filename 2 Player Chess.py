from __future__ import print_function

wKing = bKing = kwRook = qwRook = kbRook = qbRook = True

def printBoard(board, Instructions = True):
    if (Instructions == True):
        print('Enter your move as a string in official notations.')
        print('White: P, K, Q, R, N, B\t\tBlack: p, k, q, r, n, b')
        
    print('       a     b     c     d     e     f     g     h')
    for i in xrange(0, 8):
        print('     -----------------------------------------------')
        if i%2 == 0:
            print('    |#   #|     |#   #|     |#   #|     |#   #|     |')
            print('  {} '.format(int(i + 1)), end = '|# ')
        else:
            print('    |     |#   #|     |#   #|     |#   #|     |#   #|')
            print('  {} '.format(int(i + 1)), end = '|  ')
        for j in xrange(0, 8):
            if (i+j)%2 == 0:
                print(board[i][j], end = ' #|  ')
            elif j < 7:
                print(board[i][j], end = '  |# ')
            else:
                print(board[i][j], end = '  |  ')
        print('{}'.format(int(i + 1)))
        if i%2 == 0:
            print('    |#   #|     |#   #|     |#   #|     |#   #|     |')
        else:
            print('    |     |#   #|     |#   #|     |#   #|     |#   #|')
    print('     -----------------------------------------------')
    print('       a     b     c     d     e     f     g     h')
 
 
def isEmpty(board, movex, movey):
    return board[movex][movey] == ' '
    

def moveParser(board, turn, move):
    piece = origMove = differ = ''
    
    if move[0] in ['K', 'Q', 'B', 'N', 'R']:
        if turn == 'Black':
            piece = chr(ord(move[0]) + 32)
        else:
            piece = move[0]
        if move[1] == 'x':
            origMove = move[2:4]
        elif move[2] == 'x':
            origMove = move[3:5]
            differ = move[1]
        elif move[2] in ['a', 'b', 'c', 'd', 'e',  'f', 'g', 'h']:
            origMove = move[2:4]
            differ = move[1]
        else:
            origMove = move[1:3]
            
    elif move[0] == '0':
        if turn == 'White':
            piece = 'K'
            origMove = move
        else:
            piece = 'k'
            origMove = move
        differ = ''
    
    else:
        if turn == 'White':
            piece = 'P'
        else:
            piece = 'p'
        if move[1] == 'x':
            origMove = move[2:4]
            differ = move[0]
        elif move[1] in 'a b c d e f g h'.split():
            origMove = move[1:3]
            differ = move[0]
        else:
            origMove = move[0:2]
    return piece, origMove, differ


def determinePos(position):
    posr = int(position[1]) - 1
    posc = ord(position[0]) - 97
    return [posr, posc]
    

def isCheck(board, turn, posr = 8, posc = 8):
    if turn == 'White':
        enemies = ['p', 'k', 'q', 'r', 'n', 'b']
        allies = ['P', 'K', 'Q', 'R', 'N', 'B']
        oppTurn = 'Black'
        King = 'K'
    elif turn == 'Black':
        allies = ['p', 'k', 'q', 'r', 'n', 'b']
        enemies = ['P', 'K', 'Q', 'R', 'N', 'B']
        oppTurn = 'White'
        King = 'k'
    if [posr, posc] != [8, 8]:
        for i in range(0, 8):
            for j in range(0, 8):
                if board[i][j] == King:
                    posKr = i
                    posKc = j
                    break
        board[posKr][posKc], board[posr][posc] = board[posr][posc], board[posKr][posKc]
        returnbool = isCheck(board, turn)
        board[posKr][posKc], board[posr][posc] = board[posr][posc], board[posKr][posKc]
        return returnbool
    elif posr == 8 and posc == 8:
        for i in range(0, 8):
            for j in range(0, 8):
                if board[i][j] == King:
                    posr = i
                    posc = j
                    break
    for i in range(0, 8):
        for j in range(0, 8):
            if board[i][j] in enemies:
                if [posr, posc] in possibleMoves(board, i, j):
                    return True
    return False
    

def possibleMoves(board, posr, posc):
    #posx, posy = determinePos(position) #To determine the integeral coordinates from the string position (which has something like 1A or something)
    piece = board[posr][posc]
    possibleMoves = [[]]
    if piece in ['P', 'K', 'Q', 'R', 'N', 'B']:
        enemies = ['p', 'k', 'q', 'r', 'n', 'b']
        allies = ['P', 'K', 'Q', 'R', 'N', 'B']
    else:
        enemies = ['P', 'K', 'Q', 'R', 'N', 'B']
        allies = ['p', 'k', 'q', 'r', 'n', 'b']
    
    if piece == 'P':
        if posr < 7:
            if(isEmpty(board, posr+1, posc)):
                possibleMoves.append([posr+1, posc])
        if(posr == 1):
            if isEmpty(board, posr+2, posc):
                possibleMoves.append([posr+2, posc])
        if posc<7 and posr<7:
            if board[posr+1][posc+1] in enemies:
                possibleMoves.append([posr+1, posc+1])
        if posr < 7 and posc>0:
            if board[posr+1][posc-1] in enemies:
                possibleMoves.append([posr+1, posc-1])
                
    elif piece == 'p':
        if posr > 0:
            if(isEmpty(board, posr-1, posc)):
                possibleMoves.append([posr-1, posc])
        if(posr == 6):
            if isEmpty(board, posr-2, posc):
                possibleMoves.append([posr-2, posc])
        if posc<7 and posr<7:
            if board[posr-1][posc+1] in enemies:
                possibleMoves.append([posr-1, posc+1])
        if posr < 7 and posc>0:
            if board[posr-1][posc-1] in enemies:
                possibleMoves.append([posr-1, posc-1])
      
    elif piece == 'R' or piece == 'r':
        for i in range(posr, 7):
            if board[i+1][posc] in allies:
                break
            possibleMoves.append([i+1, posc])
            if board[i+1][posc] in enemies:
                break
        for i in range(0, posr):
            if board[posr-i-1][posc] in allies:
                break
            possibleMoves.append([posr-i-1, posc])
            if board[posr-i-1][posc] in enemies:
                break
        for j in range(posc, 7):
            if board[posr][j+1] in allies:
                break
            possibleMoves.append([posr, j+1])
            if board[posr][j+1] in enemies:
                break
        for j in range(0, posc):
            if board[posr][posc-j-1] in allies:
                break
            possibleMoves.append([posr, posc-j-1])
            if board[posr][posc-j-1] in enemies:
                break
     
    elif piece == 'N' or piece == 'n':
        if posr + 2 < 8 and posc + 1 < 8:
            if board[posr+2][posc+1] not in allies:
                possibleMoves.append([posr+2, posc+1])
        if posr+2 < 8 and posc - 1 >= 0:
            if board[posr+2][posc-1] not in allies:
                possibleMoves.append([posr+2, posc-1])
        if posr+1 < 8 and posc + 2 < 8:
            if board[posr+1][posc+2] not in allies:
                possibleMoves.append([posr+1, posc+2])
        if posr-1 >= 0 and posc+2 < 8:
            if board[posr-1][posc+2] not in allies:
                possibleMoves.append([posr-1, posc+2])
        if posr-2>=0 and posc + 1 < 8:
            if board[posr-2][posc+1] not in allies:
                possibleMoves.append([posr-2, posc+1])
        if posr - 2 >= 0 and posc - 1 >= 0:
            if board[posr-2][posc-1] not in allies:
                possibleMoves.append([posr-2, posc-1])
        if posr - 1 >= 0 and posc - 2 >= 0:
            if board[posr-1][posc-2] not in allies:
                possibleMoves.append([posr-1, posc-2])
        if posr + 1 < 8 and posc - 2 >= 0:
            if board[posr+1][posc-2] not in allies:
                possibleMoves.append([posr+1, posc-2])
     
    elif piece == 'B' or piece == 'b':
        i = posr+1
        j = posc+1
        while i < 8 and j < 8:
            if board[i][j] in allies:
                break
            possibleMoves.append([i, j])
            if board[i][j] in enemies:
                break
            i+=1
            j+=1
        i = posr-1
        j = posc-1
        while i >= 0 and j >= 0:
            if board[i][j] in allies:
                break
            possibleMoves.append([i, j])
            if board[i][j] in enemies:
                break
            i -= 1
            j -= 1
        i = posr+1
        j = posc-1
        while i < 8 and j >= 0:
            if board[i][j] in allies:
                break
            possibleMoves.append([i, j])
            if board[i][j] in enemies:
                break
            i += 1
            j -= 1
        i = posr - 1
        j = posc + 1
        while i >= 0 and j < 8:
            if board[i][j] in allies:
                break
            possibleMoves.append([i, j])
            if board[i][j] in enemies:
                break
            i -= 1
            j += 1
     
    elif piece == 'Q' or piece == 'q':
        #Horizontals and Verticals
        for i in range(posr, 7):
            if board[i+1][posc] in allies:
                break
            possibleMoves.append([i+1, posc])
            if board[i+1][posc] in enemies:
                break
        for i in range(0, posr):
            if board[posr-i-1][posc] in allies:
                break
            possibleMoves.append([posr-i-1, posc])
            if board[posr-i-1][posc] in enemies:
                break
        for j in range(posc, 7):
            if board[posr][j+1] in allies:
                break
            possibleMoves.append([posr, j+1])
            if board[posr][j+1] in enemies:
                break
        for j in range(0, posc):
            if board[posr][posc-j-1] in allies:
                break
            possibleMoves.append([posr, posc-j-1])
            if board[posr][posc-j-1] in enemies:
                break
        #Diagonals
        i = posr+1
        j = posc+1
        while i < 8 and j < 8:
            if board[i][j] in allies:
                break
            possibleMoves.append([i, j])
            if board[i][j] in enemies:
                break
            i+=1
            j+=1
        i = posr-1
        j = posc-1
        while i >= 0 and j >= 0:
            if board[i][j] in allies:
                break
            possibleMoves.append([i, j])
            if board[i][j] in enemies:
                break
            i -= 1
            j -= 1
        i = posr+1
        j = posc-1
        while i < 8 and j >= 0:
            if board[i][j] in allies:
                break
            possibleMoves.append([i, j])
            if board[i][j] in enemies:
                break
            i += 1
            j -= 1
        i = posr - 1
        j = posc + 1
        while i >= 0 and j < 8:
            if board[i][j] in allies:
                break
            possibleMoves.append([i, j])
            if board[i][j] in enemies:
                break
            i -= 1
            j += 1
            
    elif piece == 'K' or piece == 'k':
        if posr+1 < 8:
            possibleMoves.append([posr+1, posc])
            if posc+1 < 8:
                possibleMoves.append([posr+1, posc+1])
        if posc+1 < 8:
            possibleMoves.append([posr, posc+1])
            if posr - 1 >= 0:
                possibleMoves.append([posr-1, posc+1])
        if posr - 1 >= 0:
            possibleMoves.append([posr-1, posc])
            if posc-1 >= 0:
                possibleMoves.append([posr-1, posc-1])
        if posc-1 >= 0:
            possibleMoves.append([posr, posc-1])
            if posr + 1 < 8:
                possibleMoves.append([posr+1, posc-1])
    
    possibleMoves.pop(0)
    return possibleMoves


def findThreats(board, turn, posr, posc):
    threatArr = [[]]
    if turn == 'White':
        enemies = ['p', 'r', 'n', 'b', 'k', 'q']
    else:
        enemies = ['P', 'R', 'N', 'B', 'K', 'Q']
    for i in range(8):
        for j in range(8):
            if board[i][j] in enemies:
                if [posr, posc] in possibleMoves(board, i, j):
                    threatArr.append([posr, posc])
    threatArr.pop(0)
    return threatArr


def checkWin(board, turn):
    if turn == 'White':
        oppTurn = 'Black'
        oppKing = 'k'
    else:
        oppTurn = 'White'
        oppKing = 'K'
    for i in range(0, 8):
        for j in range(0, 8):
            if board[i][j] == oppKing:
                posr = i
                posc = j
                break
    checkbool = isCheck(board, oppTurn)
    threats = findThreats(board, turn, posr, posc)
    if len(threats) == 1:
        killers = findThreats(board, oppTurn, threats[0][0], threats[0][1])
        if len(killers) >= 1:
            return False
    if posr+1 < 8:
        checkbool = checkbool and (isCheck(board, oppTurn, posr+1, posc) or not isEmpty(board, posr+1, posc))
        if posc+1 < 8:
            checkbool = checkbool and (isCheck(board, oppTurn, posr+1, posc+1) or not isEmpty(board, posr+1, posc+1))
    if posc+1 < 8:
        checkbool = checkbool and (isCheck(board, oppTurn, posr, posc+1) or not isEmpty(board, posr, posc+1))
        if posr - 1 >= 0:
            checkbool = checkbool and (isCheck(board, oppTurn, posr-1, posc+1) or not isEmpty(board, posr-1, posc+1))
    if posr - 1 >= 0:
        checkbool = checkbool and (isCheck(board, oppTurn, posr-1, posc) or not isEmpty(board, posr-1, posc))
        if posc-1 >= 0:
            checkbool = checkbool and (isCheck(board, oppTurn, posr-1, posc-1) or not isEmpty(board, posr-1, posc-1))
    if posc-1 >= 0:
        checkbool = checkbool and (isCheck(board, oppTurn, posr, posc-1) or not isEmpty(board, posr, posc-1))
        if posr + 1 < 8:
            checkbool = checkbool and (isCheck(board, oppTurn, posr+1, posc-1) or not isEmpty(board, posr+1, posc-1))
    return checkbool


def findOrigPosition(board, turn, piece, position, differ):
    if position[0] == '0':
        return [True]
    if turn == 'White':
        enemies = ['p', 'k', 'q', 'r', 'n', 'b']
        allies = ['P', 'K', 'Q', 'R', 'N', 'B']
    elif turn == 'Black':
        allies = ['p', 'k', 'q', 'r', 'n', 'b']
        enemies = ['P', 'K', 'Q', 'R', 'N', 'B']
    posArr = determinePos(position)
    if piece in allies:
        for i in range(0, 8):
            for j in range(0, 8):
                if board[i][j] == piece:
                    possMovesArr = possibleMoves(board, i, j)
                    if posArr in possMovesArr and ((differ == str(i+1) or differ == chr(j + 97) or differ == '')):
                        return [True, i, j]
    return [False]


def faceConsequences(board, turn, piece, origPos, finalPos):
    if finalPos[0] == '0':
        return False
    origPosr, origPosc = origPos
    finalPosr, finalPosc = determinePos(finalPos)
    board[origPosr][origPosc] = ' '
    endPiece = board[finalPosr][finalPosc]
    board[finalPosr][finalPosc] = piece
    if isCheck(board, turn):
        board[finalPosr][finalPosc] = endPiece
        board[origPosr][origPosc] = piece
        return False
    return True


def takePlayerInput(turn):
    move = raw_input('What is {}\'s next move?: '.format(turn))
    return move


def checkCorrectInput(board, turn, move, bval = False):
    if not bval:
        move = raw_input('Incorrect Move. Try again: ')
    piece, finalPos, differ = moveParser(board, turn, move)
    origPos = findOrigPosition(board, turn, piece, finalPos, differ)
    while not origPos[0]:
        move = raw_input('Incorrect Move. Try again: ')
        if move == 'not':
            break
        piece, finalPos, differ = moveParser(board, turn, move)
        origPos = findOrigPosition(board, turn, piece, finalPos, differ)
    origPos.pop(0)
    while not (doCastling(board, turn, move) or faceConsequences(board, turn, piece, origPos, finalPos)):
        move, piece, origPos, finalPos = checkCorrectInput(board, turn, move)
    return move, piece, origPos, finalPos


def pawnPromotion(board, turn):
    if turn == 'White':
        pawn = 'P'
        allies = 'Q R N B'.split()
        finalrow = 7
    if turn == 'Black':
        pawn = 'p'
        allies = 'q r n b'.split()
        finalrow = 0
    pieces = 'Q R N B'.split()
    for i in range(0, 8):
        if board[finalrow][i] == pawn:
            change = raw_input('What would {} like to change the pawn into?'.format(turn))
            while change not in pieces:
                change = raw_input('Incorrect input. Enter again: ')
            change = allies[pieces.index(change)]
            board[finalrow][i] = change


def doCastling(board, turn, move):
    if move[0] != '0':
        return False
    kingOrigCol = 4
    if move == '0-0':
        if turn == 'White':
            retBool = kwRook and wKing
            row = 0
        else:
            retBool = kbRook and bKing
            row = 7
        rookOrigCol = 7
        rookFinalCol = 5
        kingFinalCol = 6
        kingMovesAcross = [4, 5]
        rookMovesAcross = [5, 6]
    elif move == '0-0-0':
        if turn == 'White':
            retBool = qwRook and wKing
            row = 0
        else:
            retBool = qbRook and bKing
            row = 7
        rookOrigCol = 0
        rookFinalCol = 3
        kingFinalCol = 2
        kingMovesAcross = [2, 3, 4]
        rookMovesAcross = [1, 2, 3]
    else:
        return False
    for i in kingMovesAcross:
        retBool = retBool and (not isCheck(board, turn, row, i))
    for i in rookMovesAcross:
        retBool = retBool and isEmpty(board, row, i)
    if retBool:
        board[row][kingOrigCol], board[row][kingFinalCol] = board[row][kingFinalCol], board[row][kingOrigCol]
        board[row][rookOrigCol], board[row][rookFinalCol] = board[row][rookFinalCol], board[row][rookOrigCol]
        return True
    return False


if __name__ == "__main__":
    board = [['0']*8] * 8
    board[0] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    board[1] = ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']
    board[2] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    board[3] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    board[4] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    board[5] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    board[6] = ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p']
    board[7] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
    printBoard(board)
    gameOver = False
    turn = 'White'
    oppTurn = 'Black'
    allMoves = 'White\t\tBlack\n'
    currMove = ''
    
    while(not gameOver):
        move = takePlayerInput(turn)
        move, piece, origPos, finalPos = checkCorrectInput(board, turn, move, True)
        if len(origPos) == 2:
            origPosR, origPosC = origPos
        if piece == 'K':
            wKing = False
        if piece == 'k':
            bKing = False
        if piece == 'R':
            if [origPosR, origPosC] == [0, 0]:
                qwRook = False
            if [origPosR, origPosC] == [0, 7]:
                kwRook = False
        if piece == 'r':
            if [origPosR, origPosC] == [7, 0]:
                qbRook = False
            if [origPosR, origPosC] == [7, 7]:
                kbRook = False
        pawnPromotion(board, turn)
        printBoard(board, False)
        if checkWin(board, turn):
            move += '#'
            print('CheckMate!\n{} has won the game. Congratulations!'.format(turn))
            gameOver = True
        elif isCheck(board, oppTurn):
            move += '+'
            print('Check!')
        if turn == 'White':
            allMoves += move
            turn = 'Black'
            oppTurn = 'White'
        else:
            allMoves += '\t\t' + move + '\n'
            turn = 'White'
            oppTurn = 'Black'
            
    print('The List of all Moves:')
    print(allMoves)
#Things to do:
    #Castling:
        #Current Plan: Check the whole archive of past plays. Few problems
        #New plan: Keep a bool value and you can update it and use it. Bas functions mein idhar udhar pass karna padega