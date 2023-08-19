sequence_1 = input("Please, enter first sequence:\n")
sequence_2 = input("Please, enter second sequence:\n")
for i in range(0, len(sequence_1)):
    if len(sequence_1) <= 10:
        print("First sequence is too short.")
    if len(sequence_2) <= 10:
        print("Second sequence is too short.\n Try again:\n")
    else:
        print("sum of sequences is \n" + sequence_1 + sequence_2)