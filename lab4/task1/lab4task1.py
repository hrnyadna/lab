##5 вариант
from Bio import SeqIO
files = ["sequence(falco).gb", "sequence(malus).gb"]
result = "sequences.gb"
with open(result, "w") as f:
    for file in files:
        for record in SeqIO.parse(file, "genbank"):
            SeqIO.write(record, f, "genbank")


