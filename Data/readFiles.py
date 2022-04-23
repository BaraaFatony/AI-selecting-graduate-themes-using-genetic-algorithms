from Models.Group import Group
from Models.Project import Project

def readProjectsFile(projectsFile, projects):
    for x in projectsFile:
        if x == '\n':
            continue
        else:
            s = x.split(":")  # splitting the line for name and subjects
            number = s[0]
            doctorname = s[1]
            Title=s[2]
            project = Project(number, doctorname ,Title)
            projects.append(project)


def readGroupsFile(groupsFile, groups):
    # Reading the groups file and creating objects of them

    for x in groupsFile:
        if x == '\n':
            continue
        else:
            s = x.split(":")
            students = s[0]
            choicesofproject = s[1].split(",")
            choiceone = choicesofproject[0]
            choicetwo = choicesofproject[1]
            choicethree = choicesofproject[2]

            group = Group(students, choiceone,choicetwo,choicethree)
            groups.append(group)
