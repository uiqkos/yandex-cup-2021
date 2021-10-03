
def solve(rows, cols):
    n, m = rows, cols
    first_range = 1
    set_ = set()

    if rows != 1 or cols != 1:
        horizontal = False
        vertical = False

        # начальная инициализация
        # если строк больше, то складываем по горизонтали
        if rows >= cols:
            # если же сложить по горизонтали, то колонки будут совпадать
            # curr = [rows * cols - (cols - col) + col for col in range(1, cols + 1)]
            first_range = (rows - 1) * cols + 1 + (cols - 1) // 2
            curr = []

            for col in range(1, cols + 1):
                x = rows * cols - (cols - col) + col
                curr.append(x)
                set_.add(x)

            rows //= 2
            horizontal = True

        # если больше столбцов, то складываем по вертикали
        else:
            # если сложить по вертикали, то матрица будет состоять из одинаковых строк.
            # curr = [cols * row + (row - 1) * cols + 1 for row in range(1, rows + 1)]
            curr = []
            first_range = rows * cols - (rows // 2)

            for row in range(1, rows + 1):
                x = cols * row + (row - 1) * cols + 1
                curr.append(x)
                set_.add(x)

            cols //= 2
            vertical = True

        # print(curr)
        # print(set_)

        while rows != 1 or cols != 1:
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

            # print(curr)
            set_.update(filter(lambda r: r > n * m, curr))
            # print(set_)
        set_.update(filter(lambda r: r > n * m, curr))
        # set_.update(curr)

    # print(len(set_), first_range)
    return len(set_) + first_range


if __name__ == '__main__':
    print(solve(*map(int, input().split())))
