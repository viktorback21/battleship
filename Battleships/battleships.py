import random
from pynput import keyboard
import os

player_board = []
computer_board = []
x = 0
y = 0
ship_list = []
ship_list_comp = []
nr = 0


class Ship:
    def __int__(self, cords):
        self.cords = cords
        self.destroyed = False
    def destroy_cords(self, cords): # Tar bort kordinaterna som är förstörda och kollar om hela skeppet är förstört
        self.cords = ()

def check_list(x_ship, y_ship, ships):
    for ship in ships:
        if ship.cords == (x_ship, y_ship):
            print("INVALID MOVE")
            return False
    return True


def create_computer_board():
    for i in range(10):
        computer_board.append(['*'] * 10)
    valid_moves = get_empty_squares(computer_board, ship_list_comp)
    for i in range(5):
        cords = random.choice(valid_moves)
        valid_moves.remove(cords)
        x = cords[0]
        y = cords[1]
        create_ship(ship_list_comp, i, x, y)
        print(cords)
    print_board()


def create_player_board():
    for i in range(10):
        player_board.append([0] * 10)
    return player_board


def create_ship(lists, number, x, y):
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
    os.system('clear' if os.name == 'posix' else 'cls')
    y1 = y
    x1 = x
    if key == keyboard.Key.up and y1 != 0:
        y1 -= 1
    elif key == keyboard.Key.down and y1 != 9:
        y1 += 1
    elif key == keyboard.Key.left and x1 != 0:
        x1 -= 1
    elif key == keyboard.Key.right and x1 != 9:
        x1 += 1
    print(y1, x1)
    player_board[y1][x1] = 'x'
    y = y1
    x = x1
    print_board()
    if key == keyboard.Key.enter:
        nr = create_ship(ship_list, nr, x, y)
        print(nr)
    else:
        player_board[y1][x1] = 0


def print_board():
    print("        Your board                                                       Enemy board")
    for i in range(10):
        print(*player_board[i], sep="  ", end='                                    ')
        print(*computer_board[i], sep="  ")


def make_move(x, y, board, ship_list):
    cords = (x, y)
    if cords in get_valid_moves(board, ship_list):
        for ship in ship_list:
            if cords == ship.cords:
                ship.destroy_cords(cords)
        print()
    for ship in ship_list_comp:
        print(ship.cords)

def rand_computer_move():
    cords = random.choice(get_valid_moves(player_board, ship_list))
    make_move(cords[0], cords[1], player_board, ship_list)


def is_win():
    pass

def get_valid_moves(board, ship_list):
    valid_moves = get_empty_squares(board, ship_list)
    for ship in ship_list:
        valid_moves.append(ship.cords)
    return valid_moves

def get_empty_squares(board, ship_list):
    empty_squares = []
    for y, list in enumerate(board):
        for x, spot in enumerate(list):
            if (x, y) not in ship_list:
                empty_squares.append((x, y))
    return empty_squares


listener = keyboard.Listener(on_press=on_press)


def start():
    create_player_board()
    create_computer_board()
    on_press(keyboard.Key.alt)
    listener.start()
    listener.join()

if __name__ == '__main__':
    start()
