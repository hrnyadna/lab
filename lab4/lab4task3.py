from Bio import SeqIO

def protein(gb_file):
    for record in SeqIO.parse(gb_file, "genbank"):
        print(f"{record.id}: {record.description}")
        print()

        for feature in record.features:
            if feature.type == "CDS":
                start = int(feature.location.start) + 1
                end = int(feature.location.end)
                strand = "+" if feature.location.strand > 0 else "-"

                if "translation" in feature.qualifiers:
                    protein_seq = feature.qualifiers["translation"][0]
                else:
                    cds_seq = feature.location.extract(record.seq)
                    protein_seq = str(cds_seq.translate(table=1, cds=True))

                print(f"Coding sequence location = [{start}:{end}]({strand})")
                print("Translation =")

                for i in range(0, len(protein_seq), 60):
                    print(protein_seq[i:i + 60])

                print("\n" + "=" * 80 + "\n")


gb_file = "sequences.gb"
protein(gb_file)