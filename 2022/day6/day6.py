

def process_input():
    with open('input.txt') as f:
        return f.readline().strip()


def all_unique(signal):
    return len(set(signal)) == len(signal)


def solution(signal, packet_len):
    for i in range(len(signal) - packet_len):
        if all_unique(signal[i:i + packet_len]):
            return i + packet_len
    return -1


if __name__ == '__main__':
    signal = process_input()

    print(f'Part 1 solution: {solution(signal, 4)}' )
    print(f'Part 2 solution: {solution(signal, 14)}')
