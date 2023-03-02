def polyrhythm():
    count_left = count_right = 1

    # prompt the user for a (poly)rhythmic combination:
    while True:
        try:
            count_left = int(input('Left hand: '))
            count_right = int(input('Right hand: '))
        except ValueError:
            print('Only integers are accepted')
            continue
        if count_left > 20 or count_right > 20 or count_left <= 0 or count_right <= 0:
            print('This combination doesn\'t seem realistic. Please try again!')
            continue
        break

    left_pattern = ['*' if x == 0 else '-' for x in range(count_left)]
    right_pattern = ['*' if y == 0 else '-' for y in range(count_right)]

    left = (' '.join(left_pattern) + ' ') * count_right
    right = (' '.join(right_pattern) + ' ') * count_left

    return f'L: {left}||\nR: {right}||\n'


print(polyrhythm())
