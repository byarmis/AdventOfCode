test_input = [
    "A Y", 
    "B X", 
    "C Z",
]

def get_score(line: str) -> int:
    if not line.strip():
        return 0

    them, you = line.split()
    
    return get_score_shape(you) + get_score_outcome(them, you)

def get_score_shape(you: str) -> int:
    return {'X': 1, 'Y':2, 'Z':3}[you]

def get_score_outcome(them: str, you: str) -> int:
    if them == "A":
        return {"X": 3, "Y": 6, "Z": 0}[you]
    elif them == "B":
        return {"X": 0, "Y": 3, "Z": 6}[you]
    elif them == "C":
        return {"X": 6, "Y": 0, "Z": 3}[you]

def get_move_to_play(them:str, res:str) -> str:
    if them == "A":
        return {"X": "Z", "Y":"X", "Z": "Y"}[res]
    elif them == "B":
        return {"X": "X", "Y":"Y", "Z": "Z"}[res]
    elif them == "C":
        return {"X": "Y", "Y":"Z", "Z": "X"}[res]

def get_score_p2(line:str) -> int:
    if not line.strip():
        return 0

    them, res = line.split()
    you = get_move_to_play(them, res)

    return get_score_shape(you) + get_score_outcome(them, you)

if __name__ == "__main__":
    assert sum(get_score(line) for line in test_input) == 15

    with open('input.txt') as f:
        lines = f.readlines()

    print("Part 1: ", sum(get_score(line) for line in lines))

    assert sum(get_score_p2(line) for line in test_input) == 12

    print("Part 2: ", sum(get_score_p2(line) for line in lines))

