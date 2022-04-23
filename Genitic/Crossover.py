import random
def breed_by_crossover(parent_1, parent_2):
    # Get length of chromosome
    chromosome_length = len(parent_1)
    # Pick crossover point, avoding ends of chromsome
    crossover_points = random.sample(range(0, chromosome_length), 2)  # generate 2 random start and end points
    # performing ordered X1 crossover
    endpoint = 0
    start = 0
    if crossover_points[0] > crossover_points[1]:
        start = crossover_points[1]
        endpoint = crossover_points[0]
    else:
        start = crossover_points[0]
        endpoint = crossover_points[1]
    child = parent_1[start : endpoint]
    # initializing the new lists
    for i in range(len(parent_2)):
       if not (parent_2[i] in child):
           child.append(parent_2[i])
    return child
# function used to mutate a chromosome
def mutate(solution):
    newsolution=[]

    index = random.sample(range(0, len(solution.list)), 2)  # generate 2 random indexes to swap
    temp = solution.list[index[0]]
    solution.list[index[0]] = solution.list[index[1]]
    solution.list[index[1]] = temp
    return solution
