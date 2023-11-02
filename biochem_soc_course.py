# -*- coding: utf-8 -*-
# The following code contains my notes and solutions to the problems of the 
# Biochemical Society R and Python studentship 2023
"""
Spyder Editor

This is a temporary script file.
"""
4 + 7 
# running scripts here with F9 key

# - subtraction
4 - 7
# / division
4 / 7
# * multiplication
4 * 7
# ** exponentiation (“to the power of”)
4 ** 7
# % modulus (remainder after division)
4 % 7
# < is less than
4 < 7
# > is greater than
4 > 7
# == is equal to
4 == 7
# != is not equal to
4 != 7

# assignment
num1 = 4
num2 = 7
type(num1)
num3 = 4.0
type(num3)

word1 = "hello"
word2 = "Lucie"
word1 + word2
word1 + " " + word2
print(word1)

pi = 3.14
radius = 5
circumference = 2 * pi * radius
area = pi * radius**2
print(area, circumference)

# list
values = [2, 5, 3, 7]
type(values)
len(values)
max(values)
min(values)
values[-1:]
values[len(values)-1]
names = ['maria', 'isaac', 'sam', 'jamie'] 
type(names)
type(names[0])
values2 = [2, 5, 'fred', 'maria']
print(values[1])
names.count('maria') # how many times it appears
names.index('maria') # what is its index
names.pop() # deletes last element
names
names.append('jamie')
names

# loops
for i in 'spam':
    print(i)
for b in range(3):
    print("hello")
# all letters in Ham twice
for a in range(2):
    for j in 'Ham':
        print(j)
# using loops
present = ['kick', 'lick', 'chuck']
past = []
for verb in present:
    past.append(verb + 'ed')
print(past)
he = []
for s in present:
    he.append(s + "s")
print(he)  

present_verbs = ['kick', 'lick', 'chuck', 'tie']
past_verbs = []
for verbs in present_verbs:
    if 'ck' in verbs:
        past_verbs.append(verbs + 'ed')
    else: 
        past_verbs.append(verbs + 'd')
print(past_verbs)
    
pres = ['kick', 'lick', 'chuck', 'tie']
pas = []
for ver in pres:
    if 'tie' in ver:
        pas.append(ver + 'd')
    else:
        pas.append(ver)
print(pas)

# breaking and continuing
for number in range(4):
    if number == 1:
        break
    print(number)
# prints the one before 1, before the break 
for number in range(4):
    if number == 1:
        continue
    print(number)
# prints everything apart from 1

# stacking things together
for number in range(5):
    if number == 0:
        print('Zero')
    elif number%2 == 1:
        print('Odd')
    else:
        print('Even')

for no in range(11):
    if no % 2 == 0:
        print(no)

# libraries - numpy (scientific computing, maths, data manipulation), 
# pandas (specialist data analysis library), 
# seaborn (graphs, data visualization)

import numpy
import numpy as np
a = np.array([1,2,3]) 
b = numpy.array([1,2,3])
# matrices
# operations
c = np.array([(1,2,3), (4,5,6)])
d = np.array([(6,5,4), (3,2,1)])
e = c + d
f = c * d
print(e)
print(f)
ee = e * 10
ee
np.log(e)
# more dimensions
z = np.array([(1,2,3), (4,5,6), (7,8,9), (10,11,12)])
z
# operations
x = np.arange(0,8,1) 
x # 0 to 8 without 8, step = 1 element
# a placeholder array (empty 3 by 3)
y = np.zeros((3,3))
print(y)

import pandas as pd
List1 = [('Maria', 98, 70, 11),('Isaac', 20, 87, 34),
         ('Sam', 93, 60, 100),('Jamie', 100, 68, 0)]
df1 = pd.DataFrame(data = List1)
print(df1)

df2 = pd.DataFrame(data = List1, 
                  columns =['student', 'maths', 'chemistry', 'biology'])
df2 = df2.set_index('student') # naming rows with students' names
print(df2)

import os # finds our working directory
os.getcwd()
os.chdir('C:\\Users\\Acer\\Desktop\\Python Course') 
os.getcwd()
os.mkdir('biochem_soc_python_work')
os.chdir('C:\\Users\\Acer\\Desktop\\Python Course\\biochem_soc_python_work')
os.getcwd()

df3 = pd.read_csv('results.csv') # import csv file
print(df3)
print(df2)
# to get rid of indices in df3 we could do
df3 = df3.set_index('student')
print (df3)
# df4 = pd.read_csv('filename.txt') # import txt to csv
# df5 = pd.read_excel('filename.xlsx', sheet_name='Sheet1')

# see dimensions (not practical for huge datasets)
pd.set_option('display.max_rows', df3.shape[0]) # [0] rows
pd.set_option('display.max_columns', df3.shape[1]) # [1] columns
print(df3)

# Instead, you can print specific rows and/or columns
# of the dataFrame using loc and iloc (location and integer-location). 
# The differences between these are very slight, but important to know. 
print(df3.loc['Maria':'Isaac','maths'])
# With loc, you need to use the names of the rows and columns, 
# but with iloc it is integer based
print(df3.iloc[0:2,0])
# How would you print the maths and biology scores for everyone, 
# using both loc and then iloc?
print(df3.iloc[:,[0,2]]) # would print the entire DataFrame.)
print(df3.loc['Maria':'Jamie', ['biology', 'maths']])
# need to make a nested list to skip the chemistry in between 
