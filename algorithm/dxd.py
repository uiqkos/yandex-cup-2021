from dataclasses import dataclass


@dataclass
class Cell:
    color: str # W, B
    pos: tuple[int, int] # (+1, 0), (-1, 0), (0, +1), (0, -1), (0, 0)

def get_next_pos(x, y, colors: dict, board):
    for x_shift, y_shift in (
        (+1, 0),
        # (-1, 0),
        # (0, +1),
        (0, -1)
    ):
        if 0 <= x + x_shift < len(board[0]) and 0 <= y + y_shift <= len(board):
            mb = board[x + x_shift][y + y_shift]

            if board[x][y].color + mb.color in colors.keys():
                remove_color(colors, board[x][y].color + mb.color)
                yield x_shift, y_shift


def link_cells(x, y, x_shift, y_shift, board):
    board[x][y].pos = (x_shift, y_shift)
    board[x + x_shift][y + y_shift].pos = (-x_shift, -y_shift)


def break_cell(x, y, board):
    x_shift, y_shift = board[x][y].pos
    board[x + x_shift][y + y_shift].pos = (0, 0)
    board[x][y].pos = (0, 0)

def remove_color(colors, color):
    colors[color] -= 1
    colors[color[::-1]] -= 1

def append_color(colors, color):
    colors.setdefault(color, 0)
    colors[color] += 1

    colors.setdefault(color[::-1], 0)
    colors[color[::-1]] += 1

def main():
    n = int(input())
    colors = {}

    for _ in range(n):
        color = input()
        append_color(colors, color)

    print(colors)

    rows, cols = map(int, input().split())
    board = []

    for _ in range(rows):
        board.append(list(map(lambda color: Cell(color, (0, 0)), input())))

    list(map(print, board))

    x, y = 0, 0

    while input() != '0':
        cell = board[x][y]
        if cell.pos == (0, 0):
            next_horizontal, next_vertical = get_next_pos(x, y, colors, board)
            xsh, ysh = next_horizontal
            xsv, ysv = next_vertical

            if board[x + xsh][y + ysh].pos != (0, 0):
                if board[x + xsv][y + ysv].pos != (0, 0):
                    raise Exception("NONNO")

                board[x][y].pos = (xsv, ysv)
                board[x + xsv][y + ysv].pos = (-xsv, -ysv)

            else:
                board[x][y].pos = (xsh, ysh)
                board[x + xsh][y + ysh].pos = (-xsh, -ysh)
        else:
            if x + 1 < len(board[0]):
                x += 1
            elif y + 1 < len(board):
                x = 0
                y += 1
            else:
                break
        list(map(print, board))

    list(map(print, board))
    print(colors)


if __name__ == '__main__':
    main()


