

def process_input():
    with open('input.txt') as f:
        section_input = []
        for line in f:
            left, right = line.split(',')
            left  = ([int(i) for i in left.split('-') ])
            right = ([int(i) for i in right.split('-')])
            section_input.append((left, right))
        return section_input


def section_contained(left, right, func):
    left_range  = range(left[0],  left[1]  + 1)
    right_range = range(right[0], right[1] + 1)
    return func(section in left_range for section in right_range) or \
           func(section in right_range for section in left_range) 


def solution(sections_input, func):
    num_contained = 0
    for sections in sections_input:
        if section_contained(*sections, func):
            num_contained += 1
    return num_contained


if __name__ == '__main__':
    section_input = process_input()

    print(f'Part 1 solution: {solution(section_input, all)}')
    print(f'Part 2 solution: {solution(section_input, any)}')