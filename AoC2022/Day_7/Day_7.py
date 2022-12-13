class Directory:
    def __init__(self, name, parent=None, children=None, files=None):
        self.name = name
        self.parent = parent
        self.children = children or []
        self.files = files or []

    @property
    def size(self):
        return sum(child.size for child in self.children) + self.self_size
    
    @property
    def self_size(self)->int:
        return sum(file.size for file in self.files)


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

test_input = [
    "$ cd /", 
    "$ ls", 
    "dir a", 
    "14848514 b.txt", 
    "8504156 c.dat", 
    "dir d", 
    "$ cd a", 
    "$ ls", 
    "dir e", 
    "29116 f", 
    "2557 g", 
    "62596 h.lst", 
    "$ cd e", 
    "$ ls", 
    "584 i", 
    "$ cd ..", 
    "$ cd ..", 
    "$ cd d", 
    "$ ls", 
    "4060174 j", 
    "8033020 d.log", 
    "5626152 d.ext", 
    "7214296 k", 
]

def build_dir(lines):
    root = Directory('/')
    node = root

    L = 1
    directories = [root]

    while L < len(lines):
        line = lines[L]

        if not line.strip():
            continue

        if line.startswith('$'):
            _, *command = line.split()

            if command == ['ls']:
                output = []

                L += 1

                while L < len(lines) and not lines[L].startswith('$'):
                    output.append(lines[L])
                    L += 1

                for out in output:
                    first, second = out.split()

                    if first == 'dir':
                        d = Directory(name=second, parent=node)
                        directories.append(d)

                        node.children.append(d)

                    elif first.isdigit():
                        node.files.append(File(name=second, size=int(first)))


            elif command[0] == 'cd':
                directory = command[1].strip()

                if directory == '..':
                    node = node.parent

                elif directory != '/':
                    node_search = [child for child in node.children if child.name == directory]
                    assert len(node_search) == 1

                    node = node_search[0]

                elif directory == '/':
                    node = root

                L += 1

    return root, directories

def part_1(lines):
    _, directories = build_dir(lines)

    out = 0
    for d in directories:
        if d.size <= 100000:
            out += d.size

    return out

def part_2(lines):
    total_size = 70000000
    space_needed = 30000000

    root, directories = build_dir(lines)

    consumed_space = root.size
    unused_space = total_size - consumed_space
    need_to_delete = space_needed - unused_space

    candidates = [d for d in directories if d.size >= need_to_delete]

    return sorted(candidates, key=lambda x: x.size)[0].size

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    assert part_1(test_input) == 95437
    print('Part 1: ', part_1(lines))

    assert part_2(test_input) == 24933642
    print('Part 2: ', part_2(lines))

