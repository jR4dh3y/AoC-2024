def read_grid(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def find_word(grid, word):
    directions = [
        (0, 1), (1, 0), (1, 1), (1, -1), 
        (0, -1), (-1, 0), (-1, -1), (-1, 1)
    ]
    word_len = len(word)
    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for direction in directions:
                if check_word(grid, word, i, j, direction, word_len):
                    count += 1
    return count

def check_word(grid, word, x, y, direction, word_len):
    dx, dy = direction
    for k in range(word_len):
        nx = x + k * dx
        ny = y + k * dy
        if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx][ny] != word[k]:
            return False
    return True

if __name__ == "__main__":
    grid = read_grid('input.txt')
    word = "XMAS"
    count = find_word(grid, word)
    print(f"Total instances of '{word}': {count}")




