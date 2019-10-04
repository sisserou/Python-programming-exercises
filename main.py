qbank = {}
with open("100+ Python challenging programming exercises.txt", "r") as f:
    key = None
    question = 0
    for line in f:
        if "Question:" in line:
            question += 1
            key = "q"
            qbank[question] = {}
        elif "Hints:" in line:
            key = "h"
        elif "Solution:" in line:
            key = "s"
        elif "#----------------------------------------#" in line:
            key = None
        if key is not None and line.strip() != "":
            qbank[question][key] = qbank[question].get(key, "") + line

while True:
    try:
        qnum = int(input(f"Enter a Question number between 1 and {question}: "))
    except ValueError:
        print("Must be valid integer.")
    else:
        break

for i in range(qnum, question + 1):
    print(f"Question {i}")
    print(qbank[i]["q"])
    while True:
        cmd = input(
            "Enter 'q' for question, 'h' for hints, 's' for solutions, 'n' for next question: "
        )
        if cmd == "n":
            break
        elif cmd in qbank[i].keys():
            print(qbank[i][cmd])
