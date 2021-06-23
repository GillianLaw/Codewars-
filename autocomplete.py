def autocomplete(input_, dictionary):
    input_ = ''.join([c for c in input_.lower() if c.isalpha()])
    ret = []
    i = 0
    for key in dictionary:
        if key.lower().startswith(input_):
            ret.append(key)
            i += 1
            if i == 5:
                return ret
    return ret


    # weebit = input_
    # longbit = dictionary
    # for word in longbit:
    #     if weebit == word[:len(weebit) + 1]:
    #         return word

print(autocomplete('ai', ['airplane','airport', 'apple', 'airy']))
