text = [ch for ch in input() if ch != " "]
occurrences = {}

for ch in text:
    if ch not in occurrences:    # if ch not in occurrences.keys():
        occurrences[ch] = 0
    occurrences[ch] += 1

for key, value in occurrences.items():
    print(key, "->", value)
