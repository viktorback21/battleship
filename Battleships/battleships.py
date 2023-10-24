from pynput import keyboard

player_board = []
computer_board = []
x = 0
y = 0
ship_list = []
nr = 0


class Ship:
    def __int__(self, cords):
        self.cords = cords
        self.destroyed = False


def check_list(x_ship, y_ship, ships):
    for ship in ships:
        if ship.cords == (x_ship, y_ship):
            print("NON VALID MOVE")
            return False
    return True


def create_list():
    for i in range(10):
        player_board.append([0] * 10)
    return player_board


def create_ship(lists, number):
    if number < 5:
        if check_list(x, y, lists):
            ship = Ship()
            ship.cords = (x, y)
            lists.append(ship)
            number += 1
        if number == 5:
            for s in ship_list:
                print(s.cords)
            listener.stop()
        return number


# https://pypi.org/project/pynput/
def on_press(key):
    global nr
    global ship_list
    global y
    global x
    if key == keyboard.Key.up and y != 0:
        y -= 1
    elif key == keyboard.Key.down and y != 9:
        y += 1
    elif key == keyboard.Key.left and x != 0:
        x -= 1
    elif key == keyboard.Key.right and x != 9:
        x += 1
    print("\n" * 3)
    print(y, x)
    player_board[y][x] = 'x'
    print_board()
    if key == keyboard.Key.enter:
        nr = create_ship(ship_list, nr)
        print(nr)
    else:
        player_board[y][x] = 0


def print_board():
    print("        Your board                                                       Enemy board")
    for i in range(10):
        print(*player_board[i], sep="  ", end='                                    ')
        print(*computer_board[i], sep="  ")


def init_player_board():
    pass


def init_computer_board():
    for i in range(10):
        computer_board.append(['*'] * 10)


def make_move(x, y, board):
    if (x, y) in valid_moves(board):
        if board[y][x] == '0':
            board[y][x] = 'E'
        elif board[y][x] == 'x':
            board[y][x] = '#'
    return board


def computer_make_move():
    pass


def is_win():
    pass


def valid_moves(board):
    valid_moves1 = []
    for y, list in enumerate(board):
        for x, spot in enumerate(list):
            if str(spot) == '0':
                valid_moves1.append((x, y))
    return valid_moves1


listener = keyboard.Listener(on_press=on_press)


def start():
    create_list()
    init_computer_board()
    on_press(keyboard.Key.alt)
    listener.start()
    listener.join()


if __name__ == '__main__':
    start()
