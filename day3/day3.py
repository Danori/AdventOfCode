from string import ascii_lowercase, ascii_uppercase 


def process_input() -> list[str]:
    with open('input.txt') as f:
        return [line.strip() for line in f]


def split_rucksacks(rucksacks: list[str]) -> list[list[str]]:
    rucksack_pairs = []
    for rucksack in rucksacks:
        end = len(rucksack)
        mid = len(rucksack) // 2
        rucksack_pairs.append([rucksack[0 : mid], rucksack[mid : end]])
    return rucksack_pairs


def group_rucksacks(rucksacks: list[str]) -> list[list[str]]:
    return [rucksacks[i:i + 3] for i in range(0, len(rucksacks), 3)]


def find_common_char(rucksack_group: list[str]) -> str:
    sets = [set(rucksack) for rucksack in rucksack_group]
    return ''.join(set.intersection(*sets))


def solution(rucksack_groups: list[list[str]], priority_map: dict[str, int]) -> int:
    total_priority = 0
    for rucksack_group in rucksack_groups:
        total_priority += priority_map[find_common_char(rucksack_group)]
    return total_priority


if __name__ == '__main__':
    rucksacks = process_input()
    rucksack_pairs  = split_rucksacks(rucksacks)
    rucksack_groups = group_rucksacks(rucksacks)

    chars = ascii_lowercase + ascii_uppercase
    priority_map = {chars[i]: i + 1 for i in range(len(chars))}

    print(f'Part 1 solution: {solution(rucksack_pairs,  priority_map)}')
    print(f'Part 2 solution: {solution(rucksack_groups, priority_map)}')
