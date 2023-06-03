# def queue_time(customers, n):
#     pass
    # multiprocessing? Interesting - kind of hpc?
def queue_time(customers, n):
    tills = [0]*n
    for i in customers:
      tills[0] += i
      tills.sort()
    return max(tills)

print(queue_time([10,2,3,3], 2))
