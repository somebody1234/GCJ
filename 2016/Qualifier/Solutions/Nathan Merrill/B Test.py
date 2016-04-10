file_name = "B-small-attempt0"


def read_file():
    with open(file_name+".in", "r") as f:
        return f.readlines(int(f.readline()))


def write(lines):
    with open(file_name+".out", "w") as out:
        for index, answer in enumerate(lines):
            out.write("Case #"+str(index+1)+": "+str(answer)+"\n")


def find_solution(stack):
    count = 0
    while "-" in stack:
        flip_index = stack.rfind("-")
        if stack.startswith("+"):
            flip_index = stack.rfind("+", 0, flip_index)
        flip_index += 1
        stack = stack[:flip_index][::-1].replace("+", "*").replace("-", "+").replace("*", "-")+stack[flip_index:]
        count += 1
    return count


write(map(find_solution, read_file()))