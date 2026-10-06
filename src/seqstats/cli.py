import sys

from seqstats.fasta import read_fasta
from seqstats.stats import gc_content


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: seqstats <file.fasta>")
        sys.exit(1)

    records = read_fasta(sys.argv[1])
    print("name\tlength\tgc")
    for name, seq in records.items():
        print(f"{name}\t{len(seq)}\t{gc_content(seq):.3f}")
