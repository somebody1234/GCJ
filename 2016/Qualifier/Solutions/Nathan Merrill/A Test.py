file_name = "A-small-attempt1"


def read_file():
    with open(file_name+".in", "r") as f:
        return f.readlines(int(f.readline()))


def write(lines):
    with open(file_name+".out", "w") as out:
        for index, answer in enumerate(lines):
            out.write("Case #"+str(index+1)+": "+str(answer)+"\n")


def find_solution(adder):
    if adder is 0:
        return "INSOMNIA"
    digit_set = set()
    current_number = adder
    while True:
        digit_set.update(str(current_number))
        if len(digit_set) == 10:
            return current_number
        current_number += adder


write(map(find_solution,map(int, read_file())))