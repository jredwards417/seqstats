COMPLEMENT = {"A": "T", "T": "A", "G": "C", "C": "G", "N": "N"}


def gc_content(seq: str) -> float:
    """Fraction of bases that are G or C."""
    if not seq:
        return 0.0
    return (seq.count("G") + seq.count("C")) / len(seq)


def reverse_complement(seq: str) -> str:
    """Reverse complement of a DNA sequence."""
    return "".join(COMPLEMENT[base] for base in reversed(seq.upper()))
