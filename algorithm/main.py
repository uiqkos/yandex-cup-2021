from copy import deepcopy
from pprint import pprint


def solve(n, m):
    matrix = []
    set_ = set()
    i = 1

    for _ in range(n):
        matrix.append([])
        for _ in range(m):
            matrix[-1].append(i)
            set_.add(i)
            i += 1

    # print(len(set_))

    def sumOf(m1, m2, invert=False):
        # print(len(m1), len(m1[0]))
        # print(len(m2), len(m2[0]))
        r = deepcopy(m1)
        for row in range(len(m2)):
            for col in range(len(m2[row])):
                r[row][col] += m2[row][col]
        return r

    def vslice(mat, begcol, endcol, step=1):
        if step == -1:
            return [line[begcol:endcol - 1:step] for line in mat]
        return [line[begcol:endcol:step] for line in mat]

    while len(matrix) * len(matrix[0]) != 1:
        for line in matrix:
            set_.update(line)

        rows, columns = len(matrix), len(matrix[0])
        # for l in matrix:
        #     print(*l)
        # print()

        if rows >= columns:
            matrix = sumOf(matrix[:rows // 2], matrix[rows // 2:][::-1])
        else:
            # pprint(vslice(matrix, columns, columns // 2, -1))
            # pprint(vslice(matrix, columns // 2, columns))

            matrix = sumOf(
                vslice(matrix, columns, columns // 2, -1),
                vslice(matrix, 0, columns // 2),
            )

    for line in matrix:
        set_.update(line)

    return len(set_)


if __name__ == '__main__':
    print(solve(*map(int, input().split())))
