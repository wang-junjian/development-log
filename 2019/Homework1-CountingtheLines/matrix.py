# o o o o o o o o
# x x o o o o x o
# o x x o o x x x
# o o o o x x x x
# o o o o o o o o
# x x x x x x x x
# o o o x x x o o
# x x o o x o o o


ANSWER_CHAR = 'x'


def read_matrix(filename):
    lines = None
    with open('matrix.txt') as f:
        lines = f.read().splitlines()

    for i, line in enumerate(lines):
        lines[i] = lines[i].replace(' ', '')

    if lines and len(lines):
        row = len(lines)
        col = len(lines[0])

    matrix = [['']*col for _ in range(0, row)]

    for r in range(0, row):
        for c in range(0, col):
            matrix[r][c] = lines[r][c]

    return matrix


def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print(col, end='')
        print()


def get_answer(matrix):
    x = get_horizonta_lines(matrix)
    y = get_vertical_lines(matrix)
    z = get_diagonal(matrix)
    k = get_anti_diagonal(matrix)

    return (x, y, z, k)


def get_horizonta_lines(matrix):
    lines = []
    for row in matrix:
        lines.append(''.join([col for col in row]))

    print('\nHorizonta Lines')
    [print(line) for line in lines]

    return analysis(lines)


def analysis(lines):
    count = 0
    for line in lines:
        pos = 0
        answer_char_queue = []
        for char in line:
            if char != ANSWER_CHAR and len(answer_char_queue) > 0:
                if len(answer_char_queue) >= 2:
                    count += 1
                
                answer_char_queue.clear()
            else:
                answer_char_queue.append(ANSWER_CHAR)

    return count


def get_vertical_lines(matrix):
    lines = []
    for row in range(len(matrix)):
        line = ''
        for col in range(len(matrix[0])):
            line += matrix[col][row]
        lines.append(line)
    
    print('\nVertical Lines')
    [print(line) for line in lines]

    return analysis(lines)


def get_diagonal(matrix):
    lines = []
    # 自己实现取线
    
    return analysis(lines)


def get_anti_diagonal(matrix):
    lines = []
    # 自己实现取线
    
    return analysis(lines)


def main():
    matrix = read_matrix('matrix.txt')
    print_matrix(matrix)
    answer = get_answer(matrix)
    print(answer)

if __name__ == '__main__':
    main()

