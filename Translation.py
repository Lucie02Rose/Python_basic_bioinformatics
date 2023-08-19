# "Protein translation, 09/08/22, Lucie Ruzickova"
# "what we would like this to do:
# DONE list and check total query length
# DONE find start codons and their numbers
# DONE find stop codons and their numbers
# DONE translate the 3 ORFs and not having problems with sequence length
# DONE within each ORF find the starts and stops (plus calculate them)
# DONE remove the need to copy ORFs from the console - importing functions to a working file
# DONE same length sequence checker that also checks for divisibility by 3
# DONE-ish check in which ORFs which starts and stops are - longest one the most useful
# figure out how to get rid of the "none"
# input a BLAST there that can do same-length sequences
# figure out how to shorten using functions such as combine into one
# read and write to FASTA files (strip the 1st line if necessary)"

import re

# "dictionary of codons"

codons = {'ata': 'I', 'atc': 'I', 'att': 'I', 'atg': 'M',
          'aca': 'T', 'acc': 'T', 'acg': 'T', 'act': 'T',
          'aac': 'N', 'aat': 'N', 'aaa': 'K', 'aag': 'K',
          'agc': 'S', 'agt': 'S', 'aga': 'R', 'agg': 'R',
          'cta': 'L', 'ctc': 'L', 'ctg': 'L', 'ctt': 'L',
          'cca': 'P', 'ccc': 'P', 'ccg': 'P', 'cct': 'P',
          'cac': 'H', 'cat': 'H', 'caa': 'Q', 'cag': 'Q',
          'cga': 'R', 'cgc': 'R', 'cgg': 'R', 'cgt': 'R',
          'gta': 'V', 'gtc': 'V', 'gtg': 'V', 'gtt': 'V',
          'gca': 'A', 'gcc': 'A', 'gcg': 'A', 'gct': 'A',
          'gac': 'D', 'gat': 'D', 'gaa': 'E', 'gag': 'E',
          'gga': 'G', 'ggc': 'G', 'ggg': 'G', 'ggt': 'G',
          'tca': 'S', 'tcc': 'S', 'tcg': 'S', 'tct': 'S',
          'ttc': 'F', 'ttt': 'F', 'tta': 'L', 'ttg': 'L',
          'tac': 'Y', 'tat': 'Y', 'taa': '_', 'tag': '_',
          'tgc': 'C', 'tgt': 'C', 'tga': '_', 'tgg': 'W'}

# "total query length"

print("Length Check")
length = input("Input sequence:").lower()
print("Sequence is\n" + str(len(length)) + "\nbases long")

# "transcription"


def transcription(rna):
    transcript = str()
    for nucleotide in rna:
        if nucleotide == 'a':
            transcript += 'T'
        elif nucleotide == 't':
            transcript += 'A'
        elif nucleotide == 'c':
            transcript += 'G'
        elif nucleotide == 'g':
            transcript += 'C'
    return transcript


transcribed = input("Input sequence:").lower()
print("Sequence of DNA is:\n" + str(transcription(transcribed)))

# "check if length of sequence is divisible by 3"

print("Division Check")


def division_check(rna_seq):
    if len(rna_seq) % 3 == 0:
        return "ok, proceed"
    elif len(rna_seq) % 3 == 1:
        return "not ok, 1 base extra"
    else:
        return "not ok, 2 bases extra"


divisible = input("Input sequence:").lower()
print("Sequence state is:\n" + str(division_check(divisible)))

# "check where start codons are located"

print("Start codon location in sequence")


def start_count(sequence_start_count):
    index = 0
    while index < len(sequence_start_count):
        index = sequence_start_count.find('atg', index)
        if index == -1:
            break
        print('atg found at', index)
        index += 3  # +3 because len('atg') == 3


start_codon = input("Input sequence:").lower()
print("The start codons in the sequence are:\n" + str(start_count(start_codon)))


# "doing the same for stop codons"
print("TAG codons in sequence")


def tag_count(sequence_tag_count):
    index = 0
    while index < len(sequence_tag_count):
        index = sequence_tag_count.find('tag', index)
        if index == -1:
            break
        print('tag found at', index)
        index += 3  # +2 because len('tag') == 2


tag_codon = input("Input sequence:").lower()
print("The total number of TAG codons in sequence is\n:" + str(tag_count(tag_codon)))

print("TAA codons in sequence")


def taa_count(sequence_taa_count):
    index = 0
    while index < len(sequence_taa_count):
        index = sequence_taa_count.find('taa', index)
        if index == -1:
            break
        print('taa found at', index)
        index += 3  # +3 because len('taa') == 3


taa_codon = input("Input sequence:").lower()
print("The total number of TAA codons in sequence is" + str(taa_count(taa_codon)))

print("TGA codons in sequence")


def tga_count(sequence_tga_count):
    index = 0
    while index < len(sequence_tga_count):
        index = sequence_tga_count.find('tga', index)
        if index == -1:
            break
        print('tga found at', index)
        index += 3  # +3 because len('tga') == 3


tga_codon = input("Input sequence:").lower()
print("The total number of TGA codons in sequence is" + str(tga_count(tga_codon)))

# "combine functions for Stop codons into one"

# "ORF1 function"
print("Open reading frame 1 translated protein")


def orf1(sequence_rf1):
    codons = {'ata': 'I', 'atc': 'I', 'att': 'I', 'atg': 'M',
              'aca': 'T', 'acc': 'T', 'acg': 'T', 'act': 'T',
              'aac': 'N', 'aat': 'N', 'aaa': 'K', 'aag': 'K',
              'agc': 'S', 'agt': 'S', 'aga': 'R', 'agg': 'R',
              'cta': 'L', 'ctc': 'L', 'ctg': 'L', 'ctt': 'L',
              'cca': 'P', 'ccc': 'P', 'ccg': 'P', 'cct': 'P',
              'cac': 'H', 'cat': 'H', 'caa': 'Q', 'cag': 'Q',
              'cga': 'R', 'cgc': 'R', 'cgg': 'R', 'cgt': 'R',
              'gta': 'V', 'gtc': 'V', 'gtg': 'V', 'gtt': 'V',
              'gca': 'A', 'gcc': 'A', 'gcg': 'A', 'gct': 'A',
              'gac': 'D', 'gat': 'D', 'gaa': 'E', 'gag': 'E',
              'gga': 'G', 'ggc': 'G', 'ggg': 'G', 'ggt': 'G',
              'tca': 'S', 'tcc': 'S', 'tcg': 'S', 'tct': 'S',
              'ttc': 'F', 'ttt': 'F', 'tta': 'L', 'ttg': 'L',
              'tac': 'Y', 'tat': 'Y', 'taa': '_', 'tag': '_',
              'tgc': 'C', 'tgt': 'C', 'tga': '_', 'tgg': 'W'}
    size = len(sequence_rf1)
    translated1 = str()
    if len(sequence_rf1) % 3 == 0:
        for j in range(0, len(sequence_rf1), 3):
            translated1 += codons[sequence_rf1[j:j + 3]]
        print(sequence_rf1)
        print(translated1)
        print("OK")
    elif len(sequence_rf1) % 3 == 1:
        sequence_1 = sequence_rf1[:size - 1]
        for j in range(0, len(sequence_1), 3):
            translated1 += codons[sequence_1[j:j + 3]]
        print(sequence_1)
        print(translated1)
    else:
        sequence_2 = sequence_rf1[:size - 2]
        for j in range(0, len(sequence_2), 3):
            translated1 += codons[sequence_2[j:j + 3]]
        print(sequence_2)
        print(translated1)


protein_orf1 = input("Input sequence:").lower()
print(orf1(protein_orf1))
# some issue with printing sequence first and then none

# "ORF2 function"
print("Open reading frame 2 translated protein")


def orf2(sequence_rf2):
    codons = {'ata': 'I', 'atc': 'I', 'att': 'I', 'atg': 'M',
              'aca': 'T', 'acc': 'T', 'acg': 'T', 'act': 'T',
              'aac': 'N', 'aat': 'N', 'aaa': 'K', 'aag': 'K',
              'agc': 'S', 'agt': 'S', 'aga': 'R', 'agg': 'R',
              'cta': 'L', 'ctc': 'L', 'ctg': 'L', 'ctt': 'L',
              'cca': 'P', 'ccc': 'P', 'ccg': 'P', 'cct': 'P',
              'cac': 'H', 'cat': 'H', 'caa': 'Q', 'cag': 'Q',
              'cga': 'R', 'cgc': 'R', 'cgg': 'R', 'cgt': 'R',
              'gta': 'V', 'gtc': 'V', 'gtg': 'V', 'gtt': 'V',
              'gca': 'A', 'gcc': 'A', 'gcg': 'A', 'gct': 'A',
              'gac': 'D', 'gat': 'D', 'gaa': 'E', 'gag': 'E',
              'gga': 'G', 'ggc': 'G', 'ggg': 'G', 'ggt': 'G',
              'tca': 'S', 'tcc': 'S', 'tcg': 'S', 'tct': 'S',
              'ttc': 'F', 'ttt': 'F', 'tta': 'L', 'ttg': 'L',
              'tac': 'Y', 'tat': 'Y', 'taa': '_', 'tag': '_',
              'tgc': 'C', 'tgt': 'C', 'tga': '_', 'tgg': 'W'}
    size = len(sequence_rf2)
    translated2 = str()
    if len(sequence_rf2) % 3 == 0:
        sequence_2 = sequence_rf2[:size - 2]
        for k in range(1, len(sequence_2), 3):
            translated2 += codons[sequence_2[k:k + 3]]
        print(sequence_2)
        print(translated2)
    elif len(sequence_rf2) % 3 == 1:
        for k in range(1, len(sequence_rf2), 3):
            translated2 += codons[sequence_rf2[k:k + 3]]
        print(sequence_rf2)
        print(translated2)
        print("OK")
    else:
        sequence_1 = sequence_rf2[:size - 1]
        for k in range(1, len(sequence_1), 3):
            translated2 += codons[sequence_1[k:k + 3]]
        print(sequence_1)
        print(translated2)


protein_orf2 = input("Input sequence:").lower()
print(orf2(protein_orf2))


# "ORF3 function"
print("Open reading frame 3 translated protein")


def orf3(sequence_rf3):
    codons = {'ata': 'I', 'atc': 'I', 'att': 'I', 'atg': 'M',
              'aca': 'T', 'acc': 'T', 'acg': 'T', 'act': 'T',
              'aac': 'N', 'aat': 'N', 'aaa': 'K', 'aag': 'K',
              'agc': 'S', 'agt': 'S', 'aga': 'R', 'agg': 'R',
              'cta': 'L', 'ctc': 'L', 'ctg': 'L', 'ctt': 'L',
              'cca': 'P', 'ccc': 'P', 'ccg': 'P', 'cct': 'P',
              'cac': 'H', 'cat': 'H', 'caa': 'Q', 'cag': 'Q',
              'cga': 'R', 'cgc': 'R', 'cgg': 'R', 'cgt': 'R',
              'gta': 'V', 'gtc': 'V', 'gtg': 'V', 'gtt': 'V',
              'gca': 'A', 'gcc': 'A', 'gcg': 'A', 'gct': 'A',
              'gac': 'D', 'gat': 'D', 'gaa': 'E', 'gag': 'E',
              'gga': 'G', 'ggc': 'G', 'ggg': 'G', 'ggt': 'G',
              'tca': 'S', 'tcc': 'S', 'tcg': 'S', 'tct': 'S',
              'ttc': 'F', 'ttt': 'F', 'tta': 'L', 'ttg': 'L',
              'tac': 'Y', 'tat': 'Y', 'taa': '_', 'tag': '_',
              'tgc': 'C', 'tgt': 'C', 'tga': '_', 'tgg': 'W'}
    size = len(sequence_rf3)
    translated3 = str()
    if len(sequence_rf3) % 3 == 0:
        sequence_1 = sequence_rf3[:size - 1]
        for m in range(2, len(sequence_1), 3):
            translated3 += codons[sequence_1[m:m + 3]]
        print(sequence_1)
        print(translated3)
    elif len(sequence_rf3) % 3 == 1:
        sequence_2 = sequence_rf3[:size - 2]
        for m in range(2, len(sequence_2), 3):
            translated3 += codons[sequence_2[m:m + 3]]
        print(sequence_2)
        print(translated3)
    else:
        for m in range(2, len(sequence_rf3), 3):
            translated3 += codons[sequence_rf3[m:m + 3]]
        print(sequence_rf3)
        print(translated3)
        print("OK")


protein_orf3 = input("Input sequence:").lower()
print((orf3(protein_orf3)))

# "for each of the ORF, define how many STOPS

print("How many stop codons are in each ORF transcript?")


def stop_cdn(protein):
    index = 0
    while index < len(protein):
        index = protein.find('_', index)
        if index == -1:
            break
        print('_ found at', index)
        index += 1  # +3 because len('atg') == 3


protein_orf1 = input("Input ORF1 translated sequence:")
protein_orf2 = input("Input ORF2 translated sequence:")
protein_orf3 = input("Input ORF3 translated sequence:")
print("The number of STOP codons in protein ORF1 is" + str(stop_cdn(protein_orf1)))
print("The number of STOP codons in protein ORF2 is" + str(stop_cdn(protein_orf2)))
print("The number of STOP codons in protein ORF3 is" + str(stop_cdn(protein_orf3)))

# "for each of the ORF, define how many STARTS

print("How many start (Met) codons are there in each ORF transcript?")


def start_cdn(protein):
    index = 0
    while index < len(protein):
        index = protein.find('M', index)
        if index == -1:
            break
        print('M found at', index)
        index += 1  # +3 because len('atg') == 3


protein_orf1 = input("Input ORF1 translated sequence:")
protein_orf2 = input("Input ORF2 translated sequence:")
protein_orf3 = input("Input ORF3 translated sequence:")
print("The number of start codons in protein ORF1 is" + str(start_cdn(protein_orf1)))
print("The number of start codons in protein ORF2 is" + str(start_cdn(protein_orf2)))
print("The number of start codons in protein ORF3 is" + str(start_cdn(protein_orf3)))

# "check the protein length"

print("What is the protein length?")

protein_orf_len = input("Input protein sequence:")
print("The protein transcript length is:\n" + str(len(protein_orf_len)))

# same-length sequence checker
print("Same length checker")

seq1 = input("Enter the first sequence:")
seq2 = input("Enter the second sequence:")
if len(seq1) == len(seq2):
    print("Sequences are the same length of:\n" + str(len(seq1)))
else:
    print("Sequence are not the same length ")

# Checking if AA are the same

seq1 = input("Enter the first sequence:")
seq2 = input("Enter the second sequence:")
output = str()
for i in range(0, len(seq1)):
    if seq1[i] == seq2[i]:
        output += "*"
    else:
        output += "-"
print(output)

# Creating a BLAST-like tool
# actions = list["A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","Y"]

# sequence = str()
# for AA in range(0, len(sequence),1):
# if AA in seq1 == AA in seq2:
# print("*")
# elif AA in seq1 == "D" or "E" and AA in seq2 == "D" or "E":
# print("a")
# elif AA in seq1 == ["R", "H", "K"] and AA in seq2 == ["R", "H", "K"]:
# print("b")
# elif AA in seq1 == ["S", "T", "Q", "N", "C"] and AA in seq2 == ["S", "T", "Q", "N", "C"]:
# print("p")
# elif AA in seq1 == ["F", "Y", "W"] and AA in seq2 == ["F", "Y", "W"]:
# print("@")
# elif AA in seq1 == ["A", "V", "I", "L", "M", "G", "P"] and AA in seq2 == ["A", "V", "I", "L", "M", "G", "P"]:
# print("n")

# "read and write to FASTA files"

# with open("exercises/sequences.fasta") as file_in:
# for line in file_in:
# line = line.strip()
# if line.startswith('>'):
# print("Sequence name:\n", line)
# else:
# print("Sequence:\n", line)

# how it could be done using regex
# looking at the start codons

sequence = input("Input sequence:")
methionine = re.compile('M')
matches = methionine.finditer(sequence)
counter = 0
for match in matches:
    counter += 1
print("There are ", counter, " methionine bases in this sequence.")

# looking at the stop codons

sequence = input("Input sequence:")
stop_codon = re.compile('(?i:tga|tag|taa)')
matches = stop_codon.finditer(sequence)
counter = 0
for match in matches:
    counter += 1
    print(match)
print("Matches =", counter)

# reading frames using regex

sequence = input("Input sequence:")
stop_codon = re.compile('(?i:TGA|TAG|TAA)')
# This uses a list comprehension....
n = 3
rf1_codons = [sequence[i:i+n] for i in range(0, len(sequence), n)]
print(rf1_codons)

# It is equivalent to, but faster and more Python than the code...
rf1_codons = []
n = 3
for i in range(0, len(sequence), n):
    rf1_codons.append(sequence[i: i+n])
print(rf1_codons)


def search_orf(codons_3):
    start_codon_1 = re.compile('(?i:atg)')
    stop_codon_1 = re.compile('(?i:tga|tag|taa)')
    inside_orf = False
    for code in codons_3:
        if start_codon_1.search(code) and not inside_orf:
            inside_orf = True
            print("Start codon " + str(code))
        elif stop_codon_1.search(code) and inside_orf:
            inside_orf = False
            print("Stop codon " + str(code))
        elif inside_orf:
            print("\tCodon " + str(code))
        else:
            print("UTR " + str(code))


long_sequence = input("Input sequence:")

n = 3

print("Searching for ORFs in reading frame +1")
rf1_codons = [long_sequence[i:i+n] for i in range(0, len(long_sequence), n)]
search_orf(rf1_codons)

print("\nSearching for ORFs in reading frame +2")
rf2_codons = [long_sequence[i:i+n] for i in range(1, len(long_sequence), n)]
search_orf(rf2_codons)

print("\nSearching for ORFs in reading frame +3")
rf3_codons = [long_sequence[i:i+n] for i in range(2, len(long_sequence), n)]
search_orf(rf3_codons)

sequence = input("Input sequence:")
stop_codon = re.compile('(?i:tga|tag|taa)')

n = 3
rf2_codons = [sequence[i:i+n] for i in range(1, len(sequence), n)]
print(rf2_codons)

count = 0
codon_number = 1
for codon in rf2_codons:
    if stop_codon.search(codon):
        print("Stop codon " + str(codon) + " found at codon " + str(codon_number) +
              "in reading frame +2 starting at sequence position+" + str(2+3*(codon_number-1)))
        count += 1
    codon_number += 1
print("Found " + str(count) + " stop codons in +2 reading frame")
