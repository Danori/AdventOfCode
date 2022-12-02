from typing import List, Union 


'''
Processes the input text file for day 1 into a list containing either integers or None elements.

Example:
input.txt:
1
2
3

6
7

4
5

output:
[1, 2, 3, None, 6, 7, None, 4, 5]
'''
def process_input() -> List[Union[int, None]]:
    with open('input.txt') as f:
        return [None if line == '\n' else int(line) for line in f]


'''
Takes a list of integer and None elements, sums all the values between every None element, and sorts these sums.

Example:
input:
[1, 2, 3, None, 6, 7, None, 4, 5]

output:
[6, 9, 13]
'''
def sum_and_sort_input(calorie_input: List[Union[int, None]]) -> List[int]:
    sums, calorie_sum = [], 0
    for calories in calorie_input:
        if calories is None:
            sums.append(calorie_sum)
            calorie_sum = 0
        else:
            calorie_sum += calories
    return sorted(sums)


'''
Takes a sorted list, and return the max element of the list (the last element).
'''
def part1(sorted_sums: List[int]) -> int:
    return sorted_sums[-1]


'''
Takes a sorted list, and returns a sum of the largest 3 elements (the last 3 elements).
'''
def part2(sorted_sums: List[int]) -> int:
    return sum(sorted_sums[-3:])


if __name__ == '__main__':
    calorie_input = process_input()
    sorted_sums = sum_and_sort_input(calorie_input)
    print(f'Part 1 solution: {part1(sorted_sums)}')
    print(f'Part 2 solution: {part2(sorted_sums)}')
