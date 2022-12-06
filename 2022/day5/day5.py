from copy import deepcopy
import re


def process_input(filename='input.txt'):
    crate = re.compile('\[[A-Z]\]')
    num = re.compile('\d+')
    instruction = re.compile(f'move {num.pattern} from {num.pattern} to {num.pattern}')

    stacks, instructions = {}, []
    with open(filename) as f:
        while crate.findall(line := f.readline()):
            crates = crate.finditer(line)
            for c in crates:
                stack_num = ((c.start() // 4) + 1)
                crate_label = c.group().strip('[]')
                
                if stack_num in stacks:
                    stacks[stack_num].append(crate_label)
                else:
                    stacks[stack_num] = [crate_label]

        for stack in stacks.values():
            stack = stack.reverse()

        while not instruction.match(line := f.readline()):
            pass

        instructions.append([int(i) for i in num.findall(line)])
        while instruction.match(line := f.readline()):
            instructions.append([int(i) for i in num.findall(line)])

    return dict(sorted(stacks.items())), instructions


def move_one(stacks, num_crates, from_stack, to_stack):
    for _ in range(num_crates):
        crate = stacks[from_stack].pop()
        stacks[to_stack].append(crate)
    return stacks


def move_many(stacks, num_crates, from_stack, to_stack):
    crates = stacks[from_stack][-num_crates:]
    del stacks[from_stack][-num_crates:]
    stacks[to_stack] = stacks[to_stack] + crates
    return stacks


def solution(stacks, instructions, move_func):
    for instruction in instructions:
        stacks = move_func(stacks, *instruction)

    return ''.join([stack[-1] for stack in stacks.values()])
        

if __name__ == '__main__':
    stacks, instructions = process_input()

    print(f'Part 1 solution: {solution(deepcopy(stacks), instructions, move_one )}')
    print(f'Part 2 solution: {solution(deepcopy(stacks), instructions, move_many)}')