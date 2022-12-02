from typing import List, Union 


'''
Processes the input text file for day 1 into a list containing either integers or None elements.

Example:
input.txt:
1
2
3

4
5

output:
[1, 2, 3, None, 4, 5]
'''
def process_input() -> List[Union[int, None]]:
    calorie_input = []
    with open('input.txt') as f:
        for line in f:
            if line == '\n':
                calorie_input.append(None)
            else:
                calorie_input.append(int(line))
    return calorie_input


'''
Takes a list of integer and None elements, and sums all the values between every None element.

Example:
input:
[1, 2, 3, None, 4, 5]

output:
[6, 9]

Note this does not output the actual solution, so that it may be resued for part 2.
'''
def part1(calorie_input: List[Union[int, None]]) -> int:
    sums, calorie_sum = [], 0
    for calories in calorie_input:
        if calories is None:
            sums.append(calorie_sum)
            calorie_sum = 0
            continue
        else:
            calorie_sum += calories
    return sums


'''
Takes a list of integer and None elements, sums all the values between every None element, sorts these summations,
and returns the largest three of these resulting values.

Example:
input:
[1, 2, 3, None, 4, 5, None, 1, None, 2]

output:
[2, 6, 9]

Note this does not output the actual solution, because this makes it look nicer in the main function. :)
'''
def part2(cal_input: List[Union[int, None]]) -> int:
    sums = sorted(part1(cal_input))
    return sums[-3:]


if __name__ == '__main__':
    cal_input = process_input()
    print(f'Part 1 solution: {max(part1(cal_input))}')
    print(f'Part 2 solution: {sum(part2(cal_input))}')
