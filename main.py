# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

start_letter = "Input/Letters/starting_letter.txt"
names_letter = "Input/Names/invited_names.txt"
# final_letter = "Output/ReadyToSend/final_letter.txt"
example_letter = "Output/ReadyToSend/example.txt"
stripped_names = []

with open(start_letter) as start_let:
    start_content = start_let.readlines()
#     print(start_content)
#
# print(start_content)

with open(names_letter) as names_letter:
    names_to_use = names_letter.readlines()
    for n in names_to_use:
        stripped_names.append(n.strip())


for name in stripped_names:
    f = open(f"Output/ReadyToSend/final_letter_{name}.txt", "w+")
    for e in start_content:
        f.write(e)

    with open(f"Output/ReadyToSend/final_letter_{name}.txt") as open_f:
        print(f.readline())
