import re

def parse_struct(struct):
    record = re.sub(r'\s+', ' ', struct.strip())
    pattern = re.compile(
        r'^(\w+):([A-Z]{3})\s+(\d+)\s*\[\s*([A-Za-z0-9]+)\s*\]\s*$'
    )

    m = pattern.match(record)
    if not m:
        raise ValueError(f"Format inattendu : {record!r}")

    chain, aa, position, atome = m.groups()
    return chain, position, aa, atome