
if __name__ == '__main__':
    '''
    Если сложить по вертикали, то матрица будет состоять из одинаковых строк. 
    Если же сложить по горизонтали, то колонки будут совпадать
    '''

    rows, cols = map(int, input().split())
    row, col = list(range(1, cols)), list(range(1, rows, cols))

    horizontal = False
    vertical = False

    if rows >= cols:
        curr = [rows * cols - (cols - col) + col for col in range(1, cols)]
        rows //= 2
        horizontal = True
    else:
        curr = [cols * row + (row - 1) * cols + 1 for row in range(1, cols)]
        cols //= 2
        vertical = True

    s = 0
    set_ = {1}

    # складываем по горизонтали
    if rows >= cols:
        if horizontal:
            curr = [c * 2 for c in curr]
        elif vertical:
            curr = [curr[0] + curr[-1]]
        rows //= 2
        horizontal = True

    # складываем по вертикали
    else:
        if vertical:
            curr = [c * 2 for c in curr]
        elif horizontal:
            curr = [curr[0] + curr[-1]]
        cols //= 2
        vertical = True

    set_.update(curr)
