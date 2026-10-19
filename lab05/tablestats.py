def read_rows(lines):
    
    rows = []
    header = None

    for line in lines:
        line = line.strip()
        if not line:
            continue

        fields = [field.strip() for field in line.split(",")]

        if header is None:
            header = fields
            continue

        if len(fields) != len(header):
            continue

        rows.append(dict(zip(header, fields)))

    return rows

def count_types(rows):
    counts = {}
    for row in rows:
        kind = row["тип"]
        counts[kind] = counts.get(kind, 0) + 1
    return counts

def total_minutes(rows, kind):
    total = 0.0
    for row in rows:
        if row["тип"] != kind:
            continue
        try:
            minutes = float(row["минуты"].replace(",", "."))
        except ValueError:
            continue
        total += minutes
    return round(total, 1)

