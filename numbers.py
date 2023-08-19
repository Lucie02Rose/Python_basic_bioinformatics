def star_count(sequence_star_count):
    index = 0
    while index < len(sequence_star_count):
        index = sequence_star_count.find('*', index)
        if index == -1:
            break
        print('* found at', index)
        index += 1  # +2 because len('*') == 1


star = input("Input sequence:")
print("The total number of TAG codons in sequence is\n:" + str(star_count(star)))


def colon_count(sequence_colon_count):
    index = 0
    while index < len(sequence_colon_count):
        index = sequence_colon_count.find(':', index)
        if index == -1:
            break
        print(': found at', index)
        index += 1  # +2 because len(':') == 1


colon = input("Input sequence:")
print("The total number of TAG codons in sequence is\n:" + str(colon_count(colon)))


def dot_count(sequence_dot_count):
    index = 0
    while index < len(sequence_dot_count):
        index = sequence_dot_count.find('.', index)
        if index == -1:
            break
        print('. found at', index)
        index += 1  # +2 because len('.') == 1


dot = input("Input sequence:")
print("The total number of TAG codons in sequence is\n:" + str(dot_count(dot)))


def no_count(sequence_no_count):
    index = 0
    while index < len(sequence_no_count):
        index = sequence_no_count.find('_', index)
        if index == -1:
            break
        print('_ found at', index)
        index += 1  # +2 because len('_') == 1


no = input("Input sequence:")
print("The total number of TAG codons in sequence is\n:" + str(no_count(no)))