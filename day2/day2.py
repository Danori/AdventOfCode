from typing import List, Tuple, Dict


def process_input() -> List[Tuple[str, str]]:
    games = []
    with open('input.txt') as f:
        for line in f:
            games.append(tuple(line.split()))
    return games


def solution(games: List[Tuple[str, str]], score_map: Dict[Tuple[str, str], int]) -> int:
    total_score = 0
    for game in games:
        total_score += score_map[game]
    return total_score


if __name__ == '__main__':
    games = process_input()
    part1_score_map = {
        ('A', 'X'): 1 + 3,
        ('A', 'Y'): 2 + 6,
        ('A', 'Z'): 3 + 0,
        ('B', 'X'): 1 + 0,
        ('B', 'Y'): 2 + 3,
        ('B', 'Z'): 3 + 6, 
        ('C', 'X'): 1 + 6,
        ('C', 'Y'): 2 + 0,
        ('C', 'Z'): 3 + 3, 
    }
    part2_score_map = {
        ('A', 'X'): 3 + 0,
        ('A', 'Y'): 1 + 3,
        ('A', 'Z'): 2 + 6,
        ('B', 'X'): 1 + 0,
        ('B', 'Y'): 2 + 3,
        ('B', 'Z'): 3 + 6, 
        ('C', 'X'): 2 + 0,
        ('C', 'Y'): 3 + 3,
        ('C', 'Z'): 1 + 6,
    }

    print(f'Part 1 solution: {solution(games, part1_score_map)}')
    print(f'Part 2 solution: {solution(games, part2_score_map)}')
