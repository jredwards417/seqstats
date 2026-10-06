from pathlib import Path

from seqstats.fasta import read_fasta
from seqstats.stats import gc_content, reverse_complement

DATA = Path(__file__).parent.parent / "data" / "samples.fasta"


def test_gc_content_basic() -> None:
    assert gc_content("GGCC") == 1.0
    assert gc_content("ATAT") == 0.0
    assert gc_content("ATGC") == 0.5


def test_gc_content_lowercase() -> None:
    assert gc_content("atgc") == 0.5


def test_reverse_complement() -> None:
    assert reverse_complement("ATGC") == "GCAT"


def test_read_fasta_reads_every_record() -> None:
    records = read_fasta(DATA)
    assert list(records) == ["sample_01", "sample_02", "sample_03"]
