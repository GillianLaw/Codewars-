def setup_gradebook(gradebook) -> object:
    """Create a new gradebook dictionary containing the same student
    names but resetting grades to zero for the new school year
    :rtype: object"""
    new_book = gradebook.copy()
    print('Original gradebook: ', gradebook)
    for key in new_book:
        new_book[key] = 0
    print('New gradebook: ', new_book)



gradebook = {'Gillian' : 10, 'Jason': 11, 'Green Bear': 7}

setup_gradebook(gradebook)
