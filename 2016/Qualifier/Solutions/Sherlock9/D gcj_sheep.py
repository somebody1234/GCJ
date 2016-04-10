import os

def sheep():

    cases = []

    # place in same-level directory
    with open("A-small-attempt2.in") as file:
        lines = file.readlines()

    for index, test in enumerate(lines[1:]):

        test = test.strip()        
        current_sheep = int(test)
        digits = set("0123456789")
        last_three_sheep = [test*i for i in range(3)]
        sheep_seen = test

        while len(set(last_three_sheep)) > 1 and set(sheep_seen) < digits:            
            current_sheep += int(test)
            sheep_seen += str(current_sheep)
            last_three_sheep = [*last_three_sheep[1:], current_sheep]

        if len(set(last_three_sheep)) < 2:
            cases.append("Case #{}: INSOMNIA\n".format(index+1))
        else:
            cases.append("Case #{}: {}\n".format(index+1, current_sheep))

    with open("A-small-attempt2.out", 'w') as file:
        for string in cases:
            file.write(string)

sheep()
