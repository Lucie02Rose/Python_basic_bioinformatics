print("Give two amino acid sequences longer than 10pb")
sequence_1 = input("Please, enter first sequence:\n")
sequence_2 = input("Please, enter second sequence:\n")
if len(sequence_1) >= 10 and len(sequence_2) >= 10 and len(sequence_1) == len(sequence_2):
    print("Correct input. Sum of sequences is \n" + sequence_1 + sequence_2)
elif len(sequence_1) != len(sequence_2):
    print("Input sequences are not the same length. Please enter sequences of the same length.")
else:
    print("All wrong, try again.")
