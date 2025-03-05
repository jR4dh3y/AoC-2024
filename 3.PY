import re 
def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
def extract_and_multiply(data):
    pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    matches = pattern.findall(data)
    results = [int(x) * int(y) for x, y in matches]
    TOTAL = sum(results)
    return TOTAL

def main():
    input_data = read_input('INPUT3.txt')
    results = extract_and_multiply(input_data)
    print(results)
if __name__ == "__main__":
    main()

    def extract_and_multiply_with_control(data):
        pattern = re.compile(r'(do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\))')
        matches = pattern.findall(data)
        enabled = True
        results = []

        for match in matches:
            if match[0] == 'do()':
                enabled = True
            elif match[0] == "don't()":
                enabled = False
            elif match[1] and match[2] and enabled:
                results.append(int(match[1]) * int(match[2]))

        TOTAL = sum(results)
        return TOTAL

    def main():
        input_data = read_input('INPUT3.txt')
        results = extract_and_multiply_with_control(input_data)
        print(results)

    if __name__ == "__main__":
        main()