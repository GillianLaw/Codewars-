import itertools

def choose_best_sum(t, k, ls):

    all_combinations = []
    for r in range(len(ls) + 1):

        combinations_object = itertools.combinations(ls, r)
        combinations_list = list(combinations_object)
        all_combinations += combinations_list
        threes = []
        for group in all_combinations:
            if len(group) == k:
                threes.append(group)


    final = []
    for route in threes:

        choice = sum(route)
        if choice <= t:
            final.append(choice)
    if max(final) == 0:
        return None
    else:
        print(max(final))

choose_best_sum(430, 3, [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89])
