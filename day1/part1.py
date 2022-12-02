def calories():
    file = open("input.txt", "r")
    current_elf = 0
    max_elf = 0
    for line in file:
        stripped_line = line.strip()
        if stripped_line not in "['\n', '\r\n']":
            current_elf += int(stripped_line)
        else:
            if current_elf > max_elf:
                max_elf = current_elf
            current_elf = 0

    return max_elf


calories()