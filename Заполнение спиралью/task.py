def print_matrix():
    for i in range(lines):
        for j in range(columns):
            print(str(matrix[i][j]).ljust(3), end='')
        print()


def fill_square():
    for j in range(start_columns, end_columns):
        matrix[start_lines][j] = next(counter)

    for i in range(start_lines + 1, end_lines - 1):
        matrix[i][end_columns - 1] = next(counter)

    for j in range(end_columns - 1, start_columns - 1, -1):
        matrix[end_lines - 1][j] = next(counter)

    for i in range(end_lines - 2, start_lines, -1):
        matrix[i][start_columns] = next(counter)


lines, columns = map(int, input().split())
counter = iter(range(1, lines * columns + 1))
matrix = [[0] * columns for _ in range(lines)]

start_lines = 0
end_lines = lines
start_columns = 0
end_columns = columns

while start_lines < end_lines or start_columns < end_columns:
    try:
        fill_square()
    except StopIteration:
        break

    start_lines += 1
    end_lines -= 1
    start_columns += 1
    end_columns -= 1

print_matrix()
