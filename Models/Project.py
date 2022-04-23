import  random

class Project:

    def __init__(self,number, doctorname, Title):
        self.number = number
        self.doctorname = doctorname
        self.Title=Title

    def __str__(self):
        return "number: " + self.number + ", doctor name=" + str(self.doctorname) + "Title: " + str(
            self.Title)

