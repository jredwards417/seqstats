from pathlib import Path


def read_fasta(path: str | Path) -> dict[str, str]:
    """Read a FASTA file and return a dict of {sequence name: sequence}."""
    records: dict[str, str] = {}
    name: str | None = None
    chunks: list[str] = []

    for line in Path(path).read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            if name is not None:
                records[name] = "".join(chunks)
            name = line[1:].split()[0]
            chunks = []
        else:
            chunks.append(line)

    return records
