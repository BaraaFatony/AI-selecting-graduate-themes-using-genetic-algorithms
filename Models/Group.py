class Group:
    def __init__(self, students,choiceone,choicetwo,choicethree):
        self.students=students
        self.choiceone=choiceone
        self.choicetwo=choicetwo
        self.choicethree=choicethree



    def __str__(self):
            return str(self.students) + " " + str(self.choiceonet)+ " " + str(self.choicetwo)+ " " + str(self.choicethree)
