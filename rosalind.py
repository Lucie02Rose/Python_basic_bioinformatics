text = open("rosalind_ini5.txt", "r")
output = open('output.txt', 'w')
out = (text.readlines()[1:1000:2])
for line in out:
    output.write(str(line))


