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


def solution(stacks, instructions, operation_mode):
    if operation_mode not in ['one', 'many']:
        return 'ERROR: invalid operation_mode'

    if operation_mode == 'one':
        for instruction in instructions:
            for _ in range(instruction[0]):
                crate = stacks[instruction[1]].pop()
                stacks[instruction[2]].append(crate)
                
    elif operation_mode == 'many':
        for instruction in instructions:
            crates = stacks[instruction[1]][-instruction[0]:]
            del stacks[instruction[1]][-instruction[0]:]
            stacks[instruction[2]] = stacks[instruction[2]] + crates

    stack_tops = ''
    for stack in stacks.values():
        stack_tops += stack[-1]

    return stack_tops
        

if __name__ == '__main__':
    stacks, instructions = process_input()

    print(f'Part 1 solution: {solution(deepcopy(stacks), instructions, "one")}')
    print(f'Part 2 solution: {solution(deepcopy(stacks), instructions, "many")}')