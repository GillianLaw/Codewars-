def duplicate_count(text):
    count = {}
    lst = []
    for char in text.casefold():
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for key in count:
        if count[key] > 1:
            lst.append(count[key])
        else:
                continue
    print(len(lst))
