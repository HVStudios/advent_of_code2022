def calories():
    file = open("input.txt", "r")
    current_elf = 0
    all_elves = []
    i = 0
    for line in file:
        stripped_line = line.strip()
        if stripped_line not in "['\n', '\r\n']":
            current_elf += int(stripped_line)
        else:
            all_elves.append(current_elf)
            i += 1
            current_elf = 0

    all_elves.sort()
    total = all_elves[i-1] + all_elves[i-2] + all_elves[i-3]
    return total


calories()