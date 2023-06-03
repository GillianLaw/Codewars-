def open_or_senior(data):
    responses = []
    for flamingo in data:
        print(flamingo)
        # for x in flamingo:
        #     print(x) #this works, but I need to be able to unpack

        x, y = flamingo
        if x >= 55 and y > 7:
            responses.append('Senior')
        else:
            responses.append('Open')
    print(responses)


open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)])
