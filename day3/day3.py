from typing import List, Tuple


def process_input() -> List[Tuple[str, str]]:
    with open('input.txt') as f:
        return [line.strip() for line in f]


def split_rucksacks(rucksacks: List[str]) -> List[Tuple[str, str]]:
    rucksack_pairs = []
    for rucksack in rucksacks:
        end = len(rucksack)
        mid = len(rucksack) // 2
        rucksack_pairs.append(tuple([rucksack[0 : mid], rucksack[mid : end]]))
    return rucksack_pairs


def find_common(left_rucksack: str, right_rucksack: str) -> List[int]:
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    left_chars_to_count = {char: 0 for char in chars}
    right_chars_to_count = {char: 0 for char in chars}

    for char in left_rucksack:
        left_chars_to_count[char] += 1
    for char in right_rucksack:
        right_chars_to_count[char] += 1

    for char in chars:
        if left_chars_to_count[char] > 0 and right_chars_to_count[char] > 0:
            return char

def find_common_three(left_rucksack: str, middle_rucksack: str, right_rucksack: str) -> List[int]:
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    left_chars_to_count = {char: 0 for char in chars}
    middle_chars_to_count = {char: 0 for char in chars}
    right_chars_to_count = {char: 0 for char in chars}

    for char in left_rucksack:
        left_chars_to_count[char] += 1
    for char in middle_rucksack:
        middle_chars_to_count[char] += 1
    for char in right_rucksack:
        right_chars_to_count[char] += 1

    for char in chars:
        if left_chars_to_count[char] > 0 and middle_chars_to_count[char] > 0 and right_chars_to_count[char] > 0:
            return char

if __name__ == '__main__':
    rucksacks = process_input()
    rucksack_pairs = split_rucksacks(rucksacks)
    total1, total2 = 0, 0
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for rucksack_pair in rucksack_pairs:
        total1 += (chars.index(find_common(*rucksack_pair)) + 1)

    rucksack_groups = []
    for i in range(0, len(rucksacks), 3):
        rucksack_groups.append(rucksacks[i:i + 3])

    for rucksack_group in rucksack_groups:
        total2 += (chars.index(find_common_three(*rucksack_group)) + 1)

    print(f'Part 1 solution: {total1}')
    print(f'Part 2 solution: {total2}')
    


