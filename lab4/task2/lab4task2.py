from Bio import SeqIO

def gc_procent(sequence):
    g = sequence.count('G')
    c = sequence.count('C')
    total = len(sequence)
    if total == 0:
        return 0
    return (g + c) / total * 100

def main(input_file):
    records_gc = []
    for record in SeqIO.parse(input_file, "genbank"):
        gc_content = gc_procent(str(record.seq))
        records_gc.append((record, gc_content))

    records_gc.sort(key=lambda x: x[1])

    for record, gc_content in records_gc:
        print(f"ID: {record.id}, GC Content: {gc_content:.2f}%")


input_file = "sequences.gb"
main(input_file)