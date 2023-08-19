from matplotlib.pyplot import *
import random

x_data = [0, 1, 2,  3, 4, 5, 6]
y_data = [0, 1, 0, -1, 0, 1, 0]  # lists of coordinates

plot(x_data, y_data)  # learn syntax or pyplot.plot

xlabel("This is the x label")
ylabel("This is the y label")
title("Here is the title")  # adding labels

grid(True)  # shows grid on graph

show()  # displays plot on the screen

savefig('plot1.png', dpi=80)  # save it, dots per inch

y_data = [1.8, -3.5, 4.5, -0.7, -0.4, -4.5, -1.6, -3.5, -0.9, 4.5, -0.9, 3.8, 1.8, 3.8, 0.4, -0.7, 1.8, 3.8, 1.9, -0.4]

x_data = range(1, len(y_data)+1)

plot(x_data, y_data)

residue_count = len(y_data)
axis(xmin=1, xmax=residue_count)

xlabel("Residue number")
ylabel("Hydrophobicity")
title("Kyte & Doolittle Hydrophobicity")
show()

# Read the 5HT1A_HUMAN.fasta file and store the amino acid sequence and description in separate variables.
# Reads the hydrophobicity_values.txt file and stores the values in a dictionary.
# Test the dictionary by printing to screen the Kyte and Doolitle hydrophbicity values for each amino acid in
# #the 5HT1A_HUMAN sequence, separated by commas.
# Produce a hydrophobicity plot for the 5HT1A_HUMAN sequence.

# 5HT1A_HUMAN.fasta protein sequence and hydrophobicity_values.txt has AA letter and hydrophobicity


def read_file(file_name):
    with open(file_name) as file_in:
        # Skip the first line (the header)
        file_in.readline()

        # Create a variable to store the result
        result = str()
        # Loop through each line and extract the absorbance
        for line in file_in:
            seq = line.strip('\n')
            result += seq

            # Return the absorbance list
    return result


HT1A = read_file("exercises/5HT1A_HUMAN.fasta")

print(HT1A)


with open("exercises/hydrophobicity_values.txt") as file_in:
    KD_values = {}
    values = []
# Loop through each line and extract the absorbance
    for line in file_in:
        values = line.split()
        KD_values[values[0]] = (values[1])  # for k, v in KD_values.items():
    # KD_values[k] = float(v)
print(KD_values)


for aa in range(0, len(HT1A)):
    acid = HT1A[aa]
    print(KD_values[acid], ",", end=" ")


y_data = []

for aa in range(0, len(HT1A)):
    acid = HT1A[aa]
    y_data.append(float(KD_values[acid]))

x_data = range(1, len(y_data) + 1)

plot(x_data, y_data)

xlabel("Residue number")
ylabel("Hydrophobicity")
title("Kyte & Doolittle Hydrophobicity for 5HT1A_HUMAN")

grid(True)

show()

y_data = []

for aa in range(1, len(HT1A) - 1):
    middle_aa = HT1A[aa]
    left_aa = HT1A[aa - 1]
    right_aa = HT1A[aa + 1]
    average = (float(KD_values[left_aa]) + float(KD_values[middle_aa]) + float(KD_values[right_aa])) / 3
    y_data.append(average)

x_data = range(1, len(y_data) + 1)

plot(x_data, y_data)

xlabel("Residue number")
ylabel("Hydrophobicityl")
title("Kyte & Doolittle Hydrophobicity for 5HT1A_HUMAN")

grid(True)

show()


y_data = []

for aa in range(7, len(HT1A) - 7):
    total = 0
    for count in range(-7, 8):
        total += float(KD_values[HT1A[aa + count]])
        aver = total / 15
    y_data.append(aver)

x_data = range(1, len(y_data) + 1)

plot(x_data, y_data)

xlabel("Residue number")
ylabel("Hydrophobicityl")
title("Kyte & Doolittle Hydrophobicity for 5HT1A_HUMAN")

grid(True)

show()

amoeba = read_file("exercises/Entamoeba_Sequence.fasta")
print(amoeba)

y_data = []
y_data2 = []
x_data = []

for aa in range(0, len(amoeba), 100):
    subseq = amoeba[aa:aa + 100]
    ATcontent = subseq.count("A")
    ATcontent += subseq.count("T")
    GCcontent = subseq.count("G")
    GCcontent += subseq.count("C")

    y_data.append(GCcontent)
    y_data2.append(ATcontent)
    x_data.append(aa)

plot(x_data, y_data, "r", label="GC")
plot(x_data, y_data2, "b", label="AT")

xlabel("Position (nuc)")
ylabel("Percentage GC")
legend(loc="upper right")
title("GC/AT Content of entamoeba sequence")

grid(True)

show()

pop_array = []

for i in range(0, 50):
    pop_array.append('A')

for i in range(50, 100):
    pop_array.append('B')

popa = []
popb = []
prevpop = pop_array
while count <= 1000:
    count += 1
    new_pop = []
    # create the new population list outside of the individuals selection while loop
    # do the selection of individuals from population 1000 times
    i = 1
    # start with one number of individuals to select
    while i <= 100:
        # while loop for selecting 100 individuals randomly from a generation
        select = random.randint(0, 99)
        # random number to select a random individual from current population
        newallele = prevpop[select]
        # select the random individual (new allele selected from prev population)
        new_pop.append(newallele)
        # append to new population list
        i = i + 1
        # increment until 100 times
    popa.append(new_pop.count("A"))
    popb.append(new_pop.count("B"))
    # we are appending to the lists that are sitting outside of both while loops
    # since both popa and popb are outside of the smaller while loop
    # they will show only the end point selection of each generation of the 1000
    # popa and popb therefore contain the numbers of A and B at each generation
    if new_pop.count("A") == 0 or new_pop.count("B") == 0:
        break
    # in case either A or B runs out, we stop the generations, so we only have 400 ish
    prevpop = new_pop
    # this has to be there to update previous population to the current one after each itteration

# Plot the final results
plot(popa, '-r', label='Allele A')
plot(popb, '-b', label='Allele B')
title('Genetic Drift of Population Size 100')
xlabel("Generation")
ylabel("Population size")
legend = plot.legend(loc='upper left')

show()

pop_array = []

for i in range(0, 25):
    pop_array.append('AA')
for i in range(0, 25):
    pop_array.append("Aa")
for i in range(0, 50):
    pop_array.append('aa')

popAa = []
popAA = []
popaa = []
prevpop = pop_array
while count <= 500:
    count += 1
    new_pop = []
    # create the new population list outside of the individuals selection while loop
    # do the selection of individuals from population 1000 times
    i = 1
    # strt with one number of individuals to select
    while i <= 100:
        # while loop for selecting 100 individuals randomly from a generation
        pos1 = random.randint(0, 99)
        # random number to select a random individual from current popoulation
        newalleles1 = prevpop[pos1]
        # select the random individual (new allele selected from prev popultion)
        ranallele = random.randint(0, 1)
        allele1 = newalleles1[ranallele:ranallele + 1]

        pos2 = random.randint(0, 99)
        newalleles2 = prevpop[pos2]
        ranallele = random.randint(0, 1)
        allele2 = newalleles2[ranallele:ranallele + 1]

        rannum = random.randint(1, 5)
        if allele1 == 'a' and allele2 == 'a':  # Only let 80% breed
            # If the random number is not 1, keep the individual
            # Otherwise do nothing so 20% are ignored
            if rannum > 1:
                new_pop.append('aa')
                i = i + 1
        else:
            new_pop.append(allele1 + allele2)
            # append to new population list
            i = i + 1
        # increment until 100 times
    popAA.append(new_pop.count("AA"))
    popAa.append(new_pop.count("Aa") + new_pop.count("aA"))
    popaa.append(new_pop.count("aa"))
    # we are appending to the lists that are sitting outside of both while loops
    # since both popa and popb are outside of the smaller while loop
    # they will show only the end point selection of each generation of the 1000
    # popa and popb therefore contain the numbers of A and B at each generation
    if new_pop.count("Aa") == 0 or new_pop.count("aa") == 0 or new_pop.count("AA") == 0:
        break
    # in case either A or B runs out, we stop the generations, so we only have 400 ish
    prevpop = new_pop
    # this has to be there to update previous population to the current one after each itteration

plot(popAA, '-r', label='Allele AA')
plot(popAa, '-b', label='Allele Aa')
plot(popaa, '-g', label='Allele aa')
title('Genetic Drift of Population Size 100')
xlabel("Generation")
ylabel("Population size")
legend = plot.legend(loc='upper left')

plot.show()
