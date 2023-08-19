# "Molecular biology file as refined by bf, 11/08/22, Lucie Ruzickova"

from functools import reduce


def transcript(rna):
    transcriptase = {"a": "T", "t": "A", "c": "G", "g": "C"}
    return reduce(lambda acc, char: acc + transcriptase[char] if char in transcriptase else acc, rna, "")
