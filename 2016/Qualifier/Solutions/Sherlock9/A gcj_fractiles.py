import math
import itertools

def fractiles():

    with open("D-small-attempt5.in") as file:
        lines = file.readlines()

    cases = []

    for index, test in enumerate(lines[1:]):
        orig_len, comp, limit = map(int, test.split())

        num_poss_seq = 2 ** orig_len

        len_comp_seq = orig_len ** comp

        the_solution = []

        matrix = list(range(orig_len))
        indices = 0

        if math.ceil(orig_len / comp) <= limit:
            while indices < orig_len:
                array = matrix[indices+1:indices+comp]
                num = indices
                indices += 1

                if len(array) != comp - 1:
                    array += [0]*(comp - 1 - len(array))
                for item in range(len(array)):
                    if num * orig_len > len_comp_seq:
                        break
                    else:
                        num *= orig_len
                        num += array[item]
                        indices += 1
                    
                the_solution.append(str(num + 1))

        if the_solution:
            cases.append("Case #{}: {}\n".format(index+1,
                                                 ' '.join(the_solution)))
        else:
            cases.append("Case #{}: IMPOSSIBLE\n".format(index+1))
        print(orig_len, comp, limit, cases[-1])

    with open("D-small-attempt5.out", 'w') as file:
        for string in cases:
            file.write(string)

fractiles()
