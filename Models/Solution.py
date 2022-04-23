
class Solution:
    def __init__(self, list  ):
        self.list = list
        self.fitness = -1 #not assigned yet

    def __str__(self):
        return str(self.list) + " " + str(self.fitness)

