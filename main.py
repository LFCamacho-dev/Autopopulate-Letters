
start_letter = "Input/Letters/starting_letter.txt"
names_letter = "Input/Names/invited_names.txt"
stripped_names = []

with open(start_letter) as start_let:
    start_content = start_let.readlines()

with open(names_letter) as names_letter:
    names_to_use = names_letter.readlines()
    for n in names_to_use:
        stripped_names.append(n.strip())

for name in stripped_names:
    _name = name.lower().replace(" ", "_")

    with open(f"Output/ReadyToSend/final_letter_{_name}.txt", "w") as f:
        for line in start_content:
            if line == start_content[0]:
                f.write(line.replace("[name]", name))
            else:
                f.write(line)
