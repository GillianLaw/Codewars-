def correctness(bobs_decisions, expert_decisions):
    # chicks = 0
    # for i in bobs_decisions:
    #     for j in expert_decisions:
    #         if i == j:
    #             chicks += 1
    #         elif i == '?' or j == '?':
    #             chicks += 0.5
    #         else:
    #             chicks += 0
    # print(chicks)


    chicks = 0
    for i, j in zip(bobs_decisions, expert_decisions):
        if i == j:
            chicks += 1
        if i!= j:
            if i == '?' or j == '?':
                chicks += 0.5

    print(chicks)



correctness(('M', 'F', '?'), ('M', 'M', 'M'))
