#sequences = ["ACTCGG", "GTAGTCGTTG", "GGTTATGCA", ["CCGTAAAC", "TAACTCGA"]]

# Complete this code to print the sequences in the list with the length of each sequence
#print("Sequence 1:", sequences[0],"Length of sequence 1:", len(sequences[0]))
#print("Sequence 2:",sequences[1],"Length of sequence 2:",len(sequences[1]))
#print("Sequence 3:",sequences[2],"Length of sequence 3:",len(sequences[2]))
#print("Sequence 4:",sequences[3][0],"Length of sequence 4:",len(sequences[3][0]))
#print("Sequence 5:",sequences[3][1],"Length of sequence 5:",len(sequences[3][1]))

#sequences = ["ACTCGG", 89192, "GTAGTCGTTG", "This shouldn't be here", 1.2, "GGTTATGCA", "CCGTAAAC", False]

# Remove non-sequences from the list (with code) using the above functions
#del sequences[1]
#del sequences[2]
#del sequences[2]
#del sequences[4]
#sequence = input("Please, enter a sequence:")
#sequences.append(sequence)
#print(sequences)

#number_list = ["4", "28", "71", "91", "2", "5"]
#result = 0

# Your code here
#for number in number_list:
 #   result = result + int(number)
#print(result)

#for i in range(0, 11):
   # print(i)
#my_list = ["Element 1", "Element 2", "Element 3", "Element 4", "Element 5"]

#for i in range(0, 5):
  #  print(my_list[i])
#for i in range(0, len(my_list), 2):
   # print(my_list[i])

#list = [1,3,5,7,9,11,13,15,17,19]
#for number in range(0,len(list)):
   # print(list[number])

#boolean_list = [False, False, False, False, False, False, False, False, False, False, False, False]

# Your code here
#for i in range(0,len(boolean_list),3):
   # boolean_list[i] = True
#print(boolean_list)

#sequence = "GTCTAAGATATCACTCAAGATATATACTCA"
#i = sequence[0]
#codon = sequence[0:3]
# Loop through and print each codon
#for i in range(0,len(sequence),3):
   # codon = sequence[i+3:i+6]
    #print(codon)

# Defining a variable called sequence
#sequence = "ATGCAGCTACGCGTTCAGGA"

# Complete the loop to check for the presence of each nucleotide
#for nucleotide in sequence:
   # if nucleotide == 'A':
     #   print("A")
    #elif nucleotide == "C":
      #  print("C")
    #elif nucleotide == "T":
     #   print("T")
    #else:
      #  print("G")

#sequence = input("Please insert a DNA sequence")
#sequence_length = len(sequence)
#total_GCs = 0
#for nucleotide in sequence:
 #   if nucleotide == "G":
  ## elif nucleotide == "C":
    #    total_GCs += 1
#result = (total_GCs/sequence_length)*100
#print("Your input DNA sequence is:\n" + str(len(sequence)))
#print("This is the percentage of GC in input sequence:\n" + str(result))
    # Modify and complete the code:
with open("codons.txt") as file_in:
    for line in file_in:
        line.split(":")
        print(line)









