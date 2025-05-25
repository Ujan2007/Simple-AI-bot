#1. Answer simple questions
#2. Play songs
#3. simple calculations
#4. Play any youtube video


import speakcommands

while True:
    user_input = input("anything you want me to do ? (yes/no): ").strip().lower()

    if user_input == "yes":
        ques = speakcommands.yes()
        speakcommands.question(ques)  # <-- Call this after yes()
    elif user_input == "no":
        speakcommands.no()
        break
    else:
        print("Invalid input! Please type 'yes' or 'no'.")