def convert(s, num_rows):
    rows = [ []  for _ in range(num_rows) ]
    direction = -1
    for c in s:
        rows[i].append(c)
        if i==0 or i==num_rows-1:
            direction = -direction
        i += direction
    return "".join("".join(r) for r in rows)
