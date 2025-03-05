def is_safe_report(report):
    increasing = all(1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def main():
    count = 0
    with open('in.txt', 'r') as file:
        reports = [list(map(int, line.split())) for line in file]

    safe_reports = [report for report in reports if is_safe_report(report)]

    for report in safe_reports:
        count += 1

    print(count)
if __name__ == "__main__":
    main()




def is_safe_with_dampener(report):
    if is_safe_report(report):
        return True
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe_report(modified_report):
            return True
    return False
def main():
    count = 0
    with open('in.txt', 'r') as file:
        reports = [list(map(int, line.split())) for line in file]
    safe_reports = [report for report in reports if is_safe_with_dampener(report)]
    for report in safe_reports:
        count += 1
    print(count)
if __name__ == "__main__":
    main()