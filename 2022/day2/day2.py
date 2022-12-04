

def process_input() -> list[tuple[str, str]]:
    with open('input.txt') as f:
        return [tuple(line.split()) for line in f]


def solution(games: list[tuple[str, str]], score_map: dict[tuple[str, str], int]) -> int:
    return sum([score_map[game] for game in games])


if __name__ == '__main__':
    games = process_input()
    part1_score_map = {
        ('A', 'X'): 1 + 3, ('A', 'Y'): 2 + 6, ('A', 'Z'): 3 + 0,
        ('B', 'X'): 1 + 0, ('B', 'Y'): 2 + 3, ('B', 'Z'): 3 + 6, 
        ('C', 'X'): 1 + 6, ('C', 'Y'): 2 + 0, ('C', 'Z'): 3 + 3, 
    }
    part2_score_map = {
        ('A', 'X'): 3 + 0, ('A', 'Y'): 1 + 3, ('A', 'Z'): 2 + 6,
        ('B', 'X'): 1 + 0, ('B', 'Y'): 2 + 3, ('B', 'Z'): 3 + 6, 
        ('C', 'X'): 2 + 0, ('C', 'Y'): 3 + 3, ('C', 'Z'): 1 + 6,
    }

    print(f'Part 1 solution: {solution(games, part1_score_map)}')
    print(f'Part 2 solution: {solution(games, part2_score_map)}')
