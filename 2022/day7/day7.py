import re


class Node:
    def __init__(self, name='', size=0, parent=None, is_dir=False):
        self.name = name
        self.size = size
        self.parent = parent
        self.is_dir = is_dir
        self.children = {}

    def __repr__(self):
        return f'{self.name} {self.size} {self.is_dir}'


def parent(node, _):
    return node.parent


def child(node, tokens):
    return node.children[tokens[2]]


def create_child_dir(node, tokens):
    node.children[tokens[1]] = Node(name=tokens[1], parent=node, is_dir=True)
    return node
    

def create_child_file(node, tokens):
    node.children[tokens[1]] = Node(name=tokens[1], size=int(tokens[0]), parent=node)
    return node


def print_tree(node, depth=0):
    padding = '\t' * depth
    print(f'{padding}{node}')

    for child in node.children.values():
        print_tree(child, depth+1)


def calc_dir_size(node):
    for child in node.children.values():
        calc_dir_size(child)
        node.size += child.size


def process_input():
    regex_to_func = {
        re.compile('\$ cd \.\.'):     parent,
        re.compile('\$ cd [a-z]+'):   child,
        re.compile('dir [a-z]+'):     create_child_dir,
        re.compile('\d+ ([a-z]|\.)+'): create_child_file,
    }

    curr, func = Node(name='/', is_dir=True), None
    root = curr
    with open('input.txt') as f:
        for line in f:
            for regex in regex_to_func:
                if regex.match(line):
                    func = regex_to_func[regex]
                    tokens = line.split()
                    curr = func(curr, tokens)
                    break

    calc_dir_size(root)              
    
    return root


def sum_dirs_smaller_than(node, max_size):
    sum_size = 0
    
    for child in node.children.values():
        sum_size += sum_dirs_smaller_than(child, max_size)

    if node.is_dir and node.size < max_size:
        sum_size += node.size

    return sum_size


def min_dir_size_to_delete(node, needed_space, unused_space):
    dir_sizes = [node.size]

    for child in node.children.values():
        if child.is_dir and child.size + unused_space > needed_space:
            dir_sizes.append(min_dir_size_to_delete(child, needed_space, unused_space))

    return min(dir_sizes)
    

if __name__ == '__main__':
    root = process_input()

    print_tree(root)

    part1 = sum_dirs_smaller_than(root, 100000)
    print(f'Part 1 solution: {part1}')

    part2 = min_dir_size_to_delete(root, 30000000, 70000000 - root.size)
    print(f'Part 2 solution: {part2}')    
