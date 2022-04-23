from Models.Group import Group
def fitness_function(groups,list):
    fitness=0

 # to compute efficient of cromosome
    #fitness function
    for i in  range(0,len(groups)) :
        if int(list[i]) == int(groups[i].choicetwo):
            fitness+=1

        if int(list[i]) == int(groups[i].choiceone):
            fitness+=1

        if int(list[i]) == int(groups[i].choicethree):
            fitness+=1

    return fitness


