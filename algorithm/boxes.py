from copy import copy

k = int(input())
colors = list(map(int, input().split()))
bs = list(map(int, input().split()))

box_count = min(colors)
ball_count = sum(colors) // box_count


print(box_count, ball_count)

box_index = 0

while box_index < box_count:
    box = []
    for color_index in range(k):
        min_color_count = bs[color_index]
        box += [color_index + 1] * min_color_count
        colors[color_index] -= min_color_count
        color_index += 1

    color_index = 0
    while len(box) < ball_count:
        if colors[color_index] > box_index:
            surplus = min(colors[color_index] - box_index, len(box) - ball_count)

            box += [color_index + 1] * surplus
            colors[color_index] -= surplus
        color_index += 1

    box_index += 1
    print(*box)
