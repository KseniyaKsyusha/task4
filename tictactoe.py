TheBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def PrintBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

    if board['top-L'] == board['top-M'] == board['top-R'] != ' ':
        print('Победили ' + board['top-L'] + '!!!!')
        return True
    elif board['mid-L'] == board['mid-M'] == board['mid-R'] != ' ':
        print('Победили ' + board['mid-L'] + '!!!!')
        return True
    elif board['low-L'] == board['low-M'] == board['low-R'] != ' ':
        print('Победили ' + board['low-L'] + '!!!!')
        return True
    elif board['top-L'] == board['mid-L'] == board['low-L'] != ' ':
        print('Победили ' + board['top-L'] + '!!!!')
        return True
    elif board['top-L'] == board['mid-L'] == board['low-L'] != ' ':
        print('Победили ' + board['top-L'] + '!!!!')
        return True
    elif board['top-M'] == board['mid-M'] == board['low-M'] != ' ':
        print('Победили ' + board['top-M'] + '!!!!')
        return True
    elif board['top-R'] == board['mid-R'] == board['low-R'] != ' ':
        print('Победили ' + board['top-R'] + '!!!!')
        return True
    elif board['top-L'] == board['mid-M'] == board['low-R'] != ' ':
        print('Победили ' + board['top-L'] + '!!!!')
        return True
    elif board['top-R'] == board['mid-M'] == board['low-L'] != ' ':
        print('Победили ' + board['top-R'] + '!!!!')
        return True
    return False


turn = 'X'

for i in range(9):
    if PrintBoard(TheBoard) == True:
        break

    print('Turn for ' + turn + ' Move on which space?')
    move = input()
    TheBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
PrintBoard(TheBoard)
