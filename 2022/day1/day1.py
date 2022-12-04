

def process_input() -> list[int | None]:
    with open('input.txt') as f:
        return [None if line == '\n' else int(line) for line in f]


def sum_and_sort_input(calorie_input: list[int | None]) -> list[int]:
    sums, calorie_sum = [], 0
    for calories in calorie_input:
        if calories is None:
            sums.append(calorie_sum)
            calorie_sum = 0
        else:
            calorie_sum += calories
    return sorted(sums, reverse=True)


def solution(sorted_sums: list[int], sum_amt: int) -> int:
    return sum(sorted_sums[:sum_amt])


if __name__ == '__main__':
    calorie_input = process_input()
    sorted_sums = sum_and_sort_input(calorie_input)
    print(f'Part 1 solution: {solution(sorted_sums, 1)}')
    print(f'Part 2 solution: {solution(sorted_sums, 3)}')
