# 17/2/2023
# Lucie Ruzickova
# Python recap from 1st year
# Source of code: Educational Material Provided by Imperial College, 
# below are my solutions to coding problems based on the appropriate session as part of the BSc Biochemistry course
#############################################
# importing necessary packages
import copy
import numpy as np
import pandas as pd
import math
# using the enumerate function that tracks indices
# enumerate captures more than 1 variable (for for loop)

seq_list = ['GGTAG', 'GGTAC', 'GATAG', 'GGTCC']
for index, seq in enumerate(seq_list):
    print(index, seq)
# building a PSM
# first store sequences in a list
seq_list = ['GGTAG', 'GGTAC', 'GATAG', 'GGTCC']


# In the first for loop work through the list to retrieve each each sequence
for sequence in seq_list:

    # In the inner for loop print each nucleotide in the sequence and its position e.g.:
    # 0 G
    # 1 G
    # 2 T
    # etc

    for nucleotide, index in enumerate(sequence):
        print(nucleotide, index)

# then, scoring the matrix
# matrix is a list of lists, inner list needs to be the same length as the sequences
# all positions set to 0 - not all nucleotides might be present at each
# increment the numbers as nucleotides are counted
# create a list of set length as list = [value]*length
# ex. nums = [1] * 4 is [1, 1, 1, 1]

seq_list = ['GGTAG', 'GGTAC', 'GATAG', 'GGTCC']

# The PWM requires 4 lists, one for each nucleotide count. These lists need
# to be the same length as the MSA sequences so this value can obtained
# from the first sequence in the list. seq_list[0] is the first sequence
# and len returns the length

n = len(seq_list[0])  # This has the value 5

# Next the 4 lists are initialised at the required length

A = [0] * n  # The same as A = [0,0,0,0,0]
C = [0] * n  # The same as C = [0,0,0,0,0]
G = [0] * n  # The same as G = [0,0,0,0,0]
T = [0] * n  # The same as T = [0,0,0,0,0]

# The scoring matrix is then created from these lists

score_mat = [A, C, G, T]

# completing the code so that it iterates through

seq_list = ['GGTAG', 'GGTAC', 'GATAG', 'GGTCC']

n = len(seq_list[0])  # This has the value 5

# Next the 4 lists are initialised at the required length

A = [0] * n  # The same as A = [0,0,0,0,0]
T = [0] * n  # The same as C = [0,0,0,0,0]
G = [0] * n  # The same as G = [0,0,0,0,0]
C = [0] * n  # The same as T = [0,0,0,0,0]

# The scoring matrix is then created from these lists

score_mat = [A, T, G, C]  # This is a list of lists [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# Iterate through each sequence

for seq in seq_list:

    # In the inner for loop obtain each nucleotide in the sequence and its position

    for i, nuc in enumerate(seq):

        if i == 0 and nuc == "A":
            score_mat[0][0] += 1
        if i == 1 and nuc == "A":
            score_mat[0][1] += 1
        if i == 2 and nuc == "A":
            score_mat[0][2] += 1
        if i == 3 and nuc == "A":
            score_mat[0][3] += 1
        if i == 4 and nuc == "A":
            score_mat[0][4] += 1
        if i == 0 and nuc == "T":
            score_mat[1][0] += 1
        if i == 1 and nuc == "T":
            score_mat[1][1] += 1
        if i == 2 and nuc == "T":
            score_mat[1][2] += 1
        if i == 3 and nuc == "T":
            score_mat[1][3] += 1
        if i == 4 and nuc == "T":
            score_mat[1][4] += 1
        if i == 0 and nuc == "G":
            score_mat[2][0] += 1
        if i == 1 and nuc == "G":
            score_mat[2][1] += 1
        if i == 2 and nuc == "G":
            score_mat[2][2] += 1
        if i == 3 and nuc == "G":
            score_mat[2][3] += 1
        if i == 4 and nuc == "G":
            score_mat[2][4] += 1
        if i == 0 and nuc == "C":
            score_mat[3][0] += 1
        if i == 1 and nuc == "C":
            score_mat[3][1] += 1
        if i == 2 and nuc == "C":
            score_mat[3][2] += 1
        if i == 3 and nuc == "C":
            score_mat[3][3] += 1
        if i == 4 and nuc == "C":
            score_mat[3][4] += 1
        # Increment the appropriate value in the score_mat list
        # To access an index in an inner list use score_mat[1][2]
        # The first number is the list in score_mat at index position 1
        # The second number is the index position within the that list

        # ... YOUR CODE GOES HERE

print(score_mat)

# copying lists
a = [1, 2, 3]
b = a[:]
print("b: ", b)  # b is now the same as a

# If we now do
b[1] = 10

print("a: ", a)
print("b: ", b)  # When we change b list a is unaffected so they are independent lists
# slice [:] creates a new copy of a list

# deepcopy

a = [[1, 2, 3], [4, 5, 6]]
print("List a was: ", a)
b = a[:]
c = copy.deepcopy(a)

b[0][1] = 10  # Will change a too
c[1][1] = 12  # Will not change a

print("List a now: ", a)
print("List b now: ", b)
print("List c now: ", c)

# numpy

arr = np.array([10, 3, 23, 8, 16])

print(arr.mean())
print(arr.sum())
print(arr.std())

pwm = copy.deepcopy(score_mat)

print("Initial scoring matrix:", pwm)

final_pwm = []

for base in pwm:

    # In the inner for loop obtain each nucleotide in the sequence and its position
    for j, i in enumerate(base):
        score = math.log2((i + 0.25) / (4 + 1) / 0.25)
        value = round(score, 3)
        final_pwm.append(value)
print(final_pwm)

F_pwm = []
for i in range(0, len(final_pwm), 5):
    F_pwm.append(final_pwm[i:i + 5])

print(F_pwm)

pwm = copy.deepcopy(score_mat)

np_list = np.array(pwm)

np_list = (np_list + 0.25)/5
np_list = np_list/0.25
pwm = np.log2(np_list)

# To round numbers use the numpy round function
pwm = np.round(pwm, 3)

print("Final PWM:", pwm)

# scoring another sequence

seq = 'TGCTAGAAGGCGTATAAGTTGGTAGA'

# PWM is ATGC
pwm = [[-2.322, 0.0, -2.322, 1.379, -2.322], [-2.322, -2.322, -2.322, 0.0, 0.848],
       [1.766, 1.379, -2.322, -2.322, 0.848], [-2.322, -2.322, 1.766, -2.322, -2.322]]

for index, nuc in enumerate(seq):
    score = 0
    if nuc == 'A':
        score += pwm[0][0]
    elif nuc == 'T':
        score += pwm[1][0]
    elif nuc == 'G':
        score += pwm[2][0]
    elif nuc == 'C':
        score += pwm[3][0]
    if score > 0:
        print("Position ", index, ":", score)

    seq = 'TGCTAGAAGGCGTATAAGTTGGTAGA'

    # PWM is ATGC
    pwm = [[-2.322, 0.0, -2.322, 1.379, -2.322], [-2.322, -2.322, -2.322, 0.0, 0.848],
           [1.766, 1.379, -2.322, -2.322, 0.848], [-2.322, -2.322, 1.766, -2.322, -2.322]]


    def calcpwmpositionscore(nuc, pos):
        # nuc is the nucleotide in the sequence to chek
        # pos is the position in the PWM
        # Complete the function to return the score for the
        # nucleotide nuc at position pos in the PWM

        if nuc == 'A':
            score = pwm[0][pos]
        elif nuc == 'T':
            score = pwm[1][pos]
        elif nuc == 'G':
            score = pwm[2][pos]
        elif nuc == 'C':
            score = pwm[3][pos]

        return score


    # The for loop needs to stop at the last 4 nucleotides
    # as that will be the last possible PWM match. If it proceeds
    # further is will cause an index out of range error
    # To enable this the enumeration is on a slice of the sequence
    # that finishes 4 nucleotides from the end, the length of the PWM

    for index, nucl in enumerate(seq[0:len(seq) - 4]):
        score = 0
        # Call the calcPWMPositionScore function
        # to calculate the PWM score at this position.
        # nuc is the first nucleotide to check in the
        # PWM with the calcPWMPositionScore but you can
        # use the index value to specify the next 4
        # nucleotides to check

        score += calcpwmpositionscore(nuc, 0)  # This is the same as score += calcPWMPositionScore(seq[index], 0)
        score += calcpwmpositionscore(seq[index + 1], 1)
        score += calcpwmpositionscore(seq[index + 2], 2)
        score += calcpwmpositionscore(seq[index + 3], 3)
        score += calcpwmpositionscore(seq[index + 4], 4)

        # The above method is verbose for clarity but this could be achieved with greater efficiency
        # by using a for loop

        # for i in range(5):
        #    score += calcPWMPositionScore(seq[index+i], i)

        if score > 0:
            score = round(score, 3)
            print("Position ", index, ":", score)

# which position and match are present
seq = 'TGCTAGAAGGCGTATAAGTTGGTAGA'

# The dictionary is created with the nucleotides as the keys and the associated
# list in the original PWM as the value
pwm_dict = {'A': pwm[0], 'T': pwm[1], 'G': pwm[2], 'C': pwm[3]}

for index in range(len(seq) - 4):
    score = 0
    # Using the nucleotide lookup the score in the dictionary at
    # at the appropriate position in the list. In this case it is
    # the first value
    for i in range(5):
        # score += calcPWMPositionScore(seq[index+i], i)
        score += pwm_dict[seq[index + i]][i]

    if score > 0:
        score = round(score, 3)
        print("Position ", index, ":", score, "Match:",
              seq[index] + seq[index + 1] + seq[index + 2] + seq[index + 3] + seq[index + 4])


# applying this to a file
# Your code here
# To read a single line from the file use:
# file_in.readline()

with open("exercises/sequence.fsa") as file_in:
    file_in.readline()
    seq = file_in.readline()

# seq = seq.rstrip()

pwm_dict = {'A': pwm[0], 'T': pwm[1], 'G': pwm[2], 'C': pwm[3]}

for index in range(len(seq) - 4):
    score = 0
    # Using the nucleotide lookup the score in the dictionary at
    # at the appropriate position in the list. In this case it is
    # the first value
    for i in range(5):
        score += calcpwmpositionscore(seq[index + i], i)

    if score > 0:
        score = round(score, 3)
        print("Position:", index, "Score:", score, "Match:",
              seq[index] + seq[index + 1] + seq[index + 2] + seq[index + 3] + seq[index + 4])

# using Pandas

ls = [5, 8, 12, 16, 22, 45]

ser = pd.Series(ls)

print(ser)

ls = [5, 8, 12, 16, 22, 45]

dat = pd.Series(ls, index=['first', 'second', 'third', 'fourth', 'fifth', 'sixth'])

print(dat)

print('Using index to access value:', dat['second'])

dicti = {'first': '5', 'second': '8', 'third': '12', 'fourth': '16', 'fifth': '22', 'sixth': '45'}

dat = pd.Series(dicti)

print(dat)

print('Using slice:')
print(dat['second': 'fifth'])

map_dict = {'ENST': 'RNA', 'ENSG': 'gene', 'ENSP': 'protein'}
count_dict = {'ENST': 3300, 'ENSG': 18435, 'ENSP': 12034}

df = pd.DataFrame({'mapping': map_dict, 'counts': count_dict})

print(df)

file_path = "exercises/DESeq2.xlsx"
df = pd.read_excel(file_path)

print(df['external_gene_name'])

# Or try:
# print(df.external_gene_name)
print(df['external_gene_name'][5]) # or df.external_gene_name[5]
df = pd.read_excel(file_path, index_col=0)
print(df['description']['JCAD'])
print(df.loc['JCAD':'TNNT1'])
print(df['external_gene_name'])     # The dictionary method
print(df.external_gene_name)       # The Pandas method

# Get only genes that are up regulated and significant pvalue
up_df = df[(df.log2FoldChange > 0) & (df.padj <= 0.05)]

print(up_df)

pwm = [[-2.322, 0.0, -2.322, 1.379, -2.322], [-2.322, -2.322, -2.322, 0.0, 0.848], [1.766, 1.379, -2.322, -2.322, 0.848], [-2.322, -2.322, 1.766, -2.322, -2.322]]

# Create a Pandas dataframe from the Python pwm list
df = pd.DataFrame(pwm)
print(df)
# Transpose the dataframe
df_pwm = df.transpose()
print(df_pwm)
# Define column headings for the dataframe
df_pwm.columns = ['A', 'T', 'G', 'C']
