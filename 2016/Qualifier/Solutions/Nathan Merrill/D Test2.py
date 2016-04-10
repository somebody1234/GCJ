import itertools, math

file_name = "D-small-attempt3"


def read_file():
    with open(file_name+".in", "r") as f:
        return f.readlines(int(f.readline()))


def write(lines):
    with open(file_name+".out", "w") as out:
        for index, answer in enumerate(lines):
            out.write("Case #"+str(index+1)+": "+str(answer)+"\n")


def find_solution(tiles, complexity, students):
    powers = [tiles**a for a in range(complexity)]
    indicies = []
    for i in range(0, tiles, complexity):
        zipped = list(zip(powers, range(i, min(i+complexity, tiles))))
        multiplied = list(map(lambda a: a[0]*a[1], zipped))
        indicies.append(sum(multiplied)+1)
    if students < len(indicies):
        return "IMPOSSIBLE"
    return " ".join(map(str, indicies))




def read_input(string):
    return map(int, string.split())

write(itertools.starmap(find_solution, map(read_input, read_file())))