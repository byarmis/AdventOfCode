test_input = [
    "30373",
    "25512",
    "65332",
    "33549",
    "35390",
]

def part_1(lines):
    trees = [[int(i) for i in line.strip()] for line in lines]

    top = set((0, i) for i in range(len(trees[0])))
    bottom = set((len(trees)-1, i) for i in range(len(trees[0])))
    left = set((i, 0) for i in range(len(trees)))
    right = set((i, len(trees[0])-1) for i in range(len(trees)))       
    
    visible_trees = top | bottom | left | right

    for row_idx, row in enumerate(trees):
        for col_idx, tree in enumerate(row):
            visible_count = 0
            for other_tree in row[:col_idx]:
                # Checking to the left
                if other_tree >= tree:
                    break
            else:
                visible_count += 1
            # Search coming in from the right
            for other_tree in row[col_idx+1:]:
                if other_tree >= tree:
                    break

            else:
                visible_count += 1

            # Search coming down from the top
            for other_row in trees[:row_idx]:
                other_tree = other_row[col_idx]

                if other_tree >= tree:
                    break

            else:
                visible_count += 1

            # Lastly we need to check if visible from the bottom
            for other_row in trees[row_idx+1:]:
                other_tree = other_row[col_idx]

                if other_tree >= tree:
                    break
            else:
                visible_count += 1

            if visible_count:
                visible_trees.add((row_idx, col_idx))

    return len(visible_trees)

def part_2(lines):
    trees = [[int(i) for i in line.strip()] for line in lines]
    scenic_scores = []

    for row_idx, row in enumerate(trees[:-1]):
        for col_idx, tree in enumerate(row[:-1]):
            if col_idx == 0:
                continue
            if row_idx == 0:
                continue

            visible_trees_left = 0
            for other_tree in row[col_idx-1::-1]:
                visible_trees_left += 1
                if other_tree >= tree:
                    break

            visible_trees_right = 0
            for other_tree in row[col_idx+1:]:
                visible_trees_right += 1
                if other_tree >= tree:
                    break

            visible_trees_top = 0
            for other_row in trees[row_idx-1::-1]:
                other_tree = other_row[col_idx]
                visible_trees_top += 1
                if other_tree >= tree:
                    break

            visible_trees_bottom = 0
            for other_row in trees[row_idx+1:]:
                other_tree = other_row[col_idx]
                visible_trees_bottom += 1
                if other_tree >= tree:
                    break

            scenic_scores.append(visible_trees_left * visible_trees_right * visible_trees_top * visible_trees_bottom)

    return max(scenic_scores)


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    assert part_1(test_input) == 21
    print('Part 1: ', part_1(lines))

    assert part_2(test_input) == 8
    print('Part 2: ', part_2(lines))

