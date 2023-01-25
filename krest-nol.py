
X = "X"
O = "O"
Empty = " "
Comp = "comp"
Num_field = 9

def game_instruct():    #Выводит на экран инструкцию для игрока
    print(
        """
        Добро пожаловать на игру "Крестики-нолики".
        Чтобы сделать ход, введи число от 0 до 8. Числа однозначно соотвествуют полям
        доски - так, как показано ниже:
    
                            0 | 1 | 2
                            ---------
                            3 | 4 | 5
                            ---------
                            6 | 7 | 8
    
        """
    )

def ask_yes_or_no(question):    #Задаёт вопрос с ответом 'Да' или 'Нет'
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number_game(question, low, high):   #Просит ввести число из диапазона
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def first_move():   #Определяет принадлежность перового хода
    go_first = ask_yes_or_no("Хочешь оставить за собой первый ход? (y, n): ")
    if go_first == "y":
        print("\nВы ходите первым, крестиками.")
        human = X
        computer = O
    else:
        print("\nПервый ходит компьютер.")
        computer = X
        human = O
    return computer, human


def position():    #Создаем новую игровую доску
    board = []
    for square in range(Num_field):
        board.append(Empty)
    return board


def display_board(board):   #Отображает игровую доску на экране
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "----------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "----------")
    print("\t", board[6], "|", board[7], "|", board[8])


def winner(board):      #Определяет победителя в игре
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != Empty:
            winner = board[row[0]]
            return winner
        if Empty not in board:
            return Comp
    return None


def legal_moves(board):        #Создаёт список доступных ходов
    moves = []
    for square in range(Num_field):
        if board[square] == Empty:
            moves.append(square)
    return moves


def human_move(board, human):   #Ходит человек
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number_game("Ваш ход. Выберите одно из полей (0 - 8):", 0, Num_field)
        if move not in legal:
            print("\nЭто поле уже занято. Выберите другое.\n")
    print("Хорошо")
    return move


def computer_move(board, computer, human):      #Ход компьютера
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)    #Ходы компьютера по порядку

    print("Я выберу поле номер", end=" ")
    for move in legal_moves(board):             #Если сдедующим ходом может победить компьютер, выберем этот ход
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = Empty

    for moves in legal_moves(board):            #Если следующим ходом может победить чегловек, блокируем этот ход
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = Empty

    for move in BEST_MOVES:                      #Выберем лучший ход из доступных полей
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):                             #Переход хода
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human): #Поздравляет победителя игры
    if the_winner != Comp:
        print("Три", the_winner, "в ряд!\n")
    else:
        print("Ничья!\n")
    if the_winner == computer:
        print("Компьютер побеждает!")
    elif the_winner == human:
        print("Поздравляю Вы выйграли!")
    elif the_winner == Comp:
        print("У Вас ничья!")


def main():
    game_instruct()
    computer, human = first_move()
    turn = X
    board = position()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


# запуск программы
main()
