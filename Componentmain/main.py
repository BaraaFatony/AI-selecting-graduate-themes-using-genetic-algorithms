import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

from Data import readFiles
from Genitic.Generate import generate
from Genitic.Fitness import fitness_function
from Models.Solution import Solution

ROOT_DIR = os.path.abspath(os.curdir)

import plotly.graph_objects as go
from Genitic.Crossover import *
from Models.Group import Group

import matplotlib.pyplot as plt
import numpy as np

# Initializing 2 lists for professors and groups and solutions
projects = []
groups = []
solutions = []
#
numberofiterations = 150
def openProjectDialog(root):
    root.filename = filedialog.askopenfilename(initialdir=ROOT_DIR + "/input", title="Select file",
                                               filetypes=(("Text Files", "*.txt"), ("all files", "*.*")))
    try:
        with open(root.filename, 'r') as UseFile:
            readFiles.readProjectsFile(UseFile, projects)

    except Exception as e:
        print(e)


def printProjects():
    numbers = []
    doctornames=[]
    Titles=[]
    for Project in projects:
        numbers.append(Project.number)
        doctornames.append(Project.doctorname)
        Titles.append(Project.Title)

    fig = go.Figure(data=[go.Table(columnwidth=[300, 300],
                                   header=dict(values=['<b>Project number<b>', '<b>Doctor name<b>' , '<b>Title<b>'],
                                               line_color='darkslategray',
                                               fill_color='yellow',
                                               height=70,
                                               align='center'),
                                   cells=dict(values=[numbers,  # 1st column
                                                      doctornames ,# 2nd column
                                                      Titles],  # 3nd column

                                              line_color='darkslategray',
                                              fill_color='lightyellow',
                                              height=30,
                                              align='center'))
                          ])

    fig.update_layout(width=1800, height=1800)
    fig.show()


def openGroupsDialog(root):
    root.filename = filedialog.askopenfilename(initialdir=ROOT_DIR + "/input", title="Select file",
                                               filetypes=(("Text Files", "*.txt"), ("all files", "*.*")))
    try:
        with open(root.filename, 'r') as UseFile:
            readFiles.readGroupsFile(UseFile, groups)
    except Exception as e:
        print(e)


def printGroups():
    students = []
    choiceone = []
    choicetwo = []
    choicethree = []

    for Group in groups:
        students.append(Group.students)
        choiceone.append(Group.choiceone)
        choicetwo.append(Group.choicetwo)
        choicethree.append(Group.choicethree)
    fig = go.Figure(data=[go.Table(columnwidth=[450, 450, 450, 450],
                                   header=dict(values=['<b>Students\' names<b>', '<b>Choice one<b>',
                                                       "<b>Choice two<b>", "<b>Choice three<b>"],
                                               line_color='darkslategray',
                                               fill_color='yellow',
                                               height=70,
                                               align='center'),
                                   cells=dict(values=[students,  # 1st column
                                                      choiceone, choicetwo, choicethree],  # 2nd column
                                              line_color='darkslategray',
                                              fill_color='lightyellow',
                                              height=40,
                                              align='center'))
                          ])

    fig.update_layout(width=1800, height=1800)
    fig.show()





# This is the main loop of the program
x_number_values=[]
y_number_values=[]


# ---------------------------------------------------------------------------------------------------------------------------------------------------------
def goBt(populationEntry):
    global population
    population = int(populationEntry)
    solutions = []
    # Initializing the solutions
    for i in range(0, population):
        solution = generate(groups)
        solution.fitness = fitness_function(groups,solution.list)
        solutions.append(solution)
        solutions.sort(key=lambda x: x.fitness, reverse=True)

    for i in range(0 ,numberofiterations):
        solutions2 = []
        print("iteration number " , i)

        for j in range(0 ,int(population / 2)):  # generating by crossover
            newlist = breed_by_crossover(solutions[0].list, solutions[j+1].list)
            newsolution=Solution(newlist)
            newsolution.fitness = fitness_function(groups, newsolution.list)
            solutions2.append(newsolution)

        #update fitness and resort
        solutions2.sort(key=lambda x:x.fitness, reverse=True)

        for j in range(0 ,int(population / 4)):  # generating by mutation
            tmpsolution = mutate(solutions2[0])
            tmpsolution.fitness = fitness_function(groups ,tmpsolution.list)
            solutions2.append(tmpsolution)

        for j in range(0 ,int(population/8)):
            tmpsolution=generate(groups)
            tmpsolution.fitness=fitness_function(groups , tmpsolution.list)
            solutions2.append(tmpsolution)


        solutions = solutions + solutions2
        # update fitness and resort
        for solution in solutions:
            solution.fitness=fitness_function(groups , solution.list)
        solutions.sort(key=lambda x: x.fitness, reverse=True)
        solutions = solutions[0:population]


        x_number_values.append(i)
        y_number_values.append(solutions[0].fitness)


    final_answer = solutions[0]
    print("Final answer fitness = " , final_answer.fitness)

    students=[]
    projectstitle=[]
    for Group in groups:
        students.append(Group.students)
    for Project in projects:
        projectstitle.append(Project.Title)

    fig = go.Figure(data=[go.Table(columnwidth=[300, 300],
                                       header=dict(values=['<b>group student name<b>', '<b>project number<b>', '<b>project title<b>' ],
                                                   line_color='darkslategray',
                                                   fill_color='yellow',
                                                   height=70,
                                                   align='center'),
                                       cells=dict(values=[students,  # 1st column
                                                          final_answer.list,  # 2nd column
                                                          projectstitle],  # 3nd column

                                                  line_color='darkslategray',
                                                  fill_color='lightyellow',
                                                  height=30,
                                                  align='center'))
                              ])

    fig.update_layout(width=1800, height=1800)
    fig.show()


    # Draw point based on above x, y axis values.
    plt.plot(x_number_values, y_number_values)

    # Set chart title.
    plt.title("Fitness through time ")
    axes = plt.gca()
    axes.set_xlim([0, 100])
    axes.set_ylim([0, max(y_number_values) + 10])

    # Set x, y label text.
    plt.xlabel("Iteration")
    plt.ylabel("Fitness")
    plt.show()

