import imprev

def build(points, size=3):
    nearest = {}
    for point in points:
        closest = {}
        m = float('inf')
        for other in points:
            if other != point:
                d = round(imprev.dist(point, other), 5)

                if d < m and len(closest) < size:
                    closest[d] = other
                elif d < max(closest.keys()):
                    closest.pop(max(closest.keys()))
                    closest[d] = other

        nearest[point] = closest

    return nearest


points = [key[0] for key in imprev.color_definitions.values()]
nearest = build(points)
pairs = [
    ("}, (", "},\n("),
    ("), ", "), \n\t"),
    ("): {", "): {\n\t"),
    (")},", ")\n},"),
]

out = str(nearest)
for a, b in pairs:
    out = out.replace(a, b)

print(out)


# graph results
