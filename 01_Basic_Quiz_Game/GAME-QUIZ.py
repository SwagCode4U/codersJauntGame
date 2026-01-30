"""
=====================================================
🎮 CODERSJAUNT - PYTHON BASICS WAR GAME
Author: CodersJaunt - @mit
Purpose: Learn Python Basics through fun battles
Level: Beginner after learning - Variables, Conditions,
       Input, Data Structures, Functions
=====================================================
"""

# -----------------------------
# QUESTIONS & ANSWERS DATABASE
# -----------------------------

landingWar = [

    # VARIABLES & DATA TYPES
    "What is the type of 5?",
    "What is the type of 5.0?",
    "What keyword takes input from user?",
    "What converts string to integer?",
    "Is Python case-sensitive? (yes/no)",

    # CONDITIONS
    "What keyword checks condition?",
    "What keyword runs if condition false?",
    "What is output of: 5 > 3?",
    "Which operator means AND?",
    "What value represents nothing?",

    # DATA STRUCTURES
    "Which DS stores key-value?",
    "Which DS stores unique values?",
    "What method adds item to list?",
    "What method removes last item?",
    "What method empties list?",

    # FUNCTIONS
    "Which keyword defines function?",
    "Which keyword sends value back?",
    "Can function call function? (yes/no)",
    "What happens after return?",
    "Reusable code block is called?"
]

war_answers = [
    "int","float","input","int","yes",
    "if","else","True","and","None",
    "dict","set","append","pop","clear",
    "def","return","yes","stop","function"
]

# -----------------------------
# GAME ART & WELCOME
# -----------------------------

print("""
╔══════════════════════════════════════╗
║      🐍 CODERSJAUNT WAR GAME 🐍      ║
║  Learn Python. Fight Bugs. Level Up. ║
╚══════════════════════════════════════╝
""")

print("📌 RULES:")
print("- Answer correctly to win wars")
print("- 3 correct answers = Level Up")
print("- Any wrong answer → No MASTER title")
print("- Press 9 anytime to exit\n")

# -----------------------------
# PLAYER SETUP
# -----------------------------

player_name = input("Enter Player Name: ")
player_level = 1
wrong_answers = 0

player_enemy = input("Choose Enemy (Zombie/Robot): ")
player_weapon = input("Choose Weapon (Sword/Gun): ")

# -----------------------------
# AREAS SETUP
# -----------------------------

areaNames = ["Kuala Island", "Gola Yard", "Motipura", "Mahavir Nagar", "Bus Stand"]
visited_areas = []

question_index = 0

# -----------------------------
# GAME LOOP
# -----------------------------

while question_index < len(landingWar) and len(visited_areas) < len(areaNames):

    print("\n==============================")
    print(f"🔥 LEVEL {player_level} | Player: {player_name}")
    print("==============================")

    print("\nAvailable Areas:")
    for area in areaNames:
        if area not in visited_areas:
            print("-", area)

    choice = input("\nChoose area (or press 9 to exit): ")

    if choice == "9":
        print("\n🚪 You exited the battlefield. Come back stronger!")
        break

    if choice in visited_areas or choice not in areaNames:
        print("⚠️ Invalid or already cleared area.")
        continue

    visited_areas.append(choice)
    print(f"\n🛬 Landing in {choice}")
    print("⚔️ WAR STARTED ⚔️")

    correct = 0

    # -----------------------------
    # ASK 3 QUESTIONS PER AREA
    # -----------------------------

    for _ in range(3):

        if question_index >= len(landingWar):
            break

        print("\nQuestion:", landingWar[question_index])
        answer = input("Your Answer (or 9 to exit): ")

        if answer == "9":
            print("\n🚪 Exiting game safely...")
            exit()

        if answer == war_answers[question_index]:
            print("✅ Correct!")
            correct += 1
        else:
            print("❌ Wrong!")
            wrong_answers += 1

        question_index += 1

    # -----------------------------
    # RESULT OF WAR
    # -----------------------------

    if correct == 3:
        player_level += 1
        print("\n🏆 WAR WON! LEVEL UP!")
    else:
        print("\n💀 WAR LOST! Train harder.")

# -----------------------------
# FINAL RESULT
# -----------------------------

print("\n===================================")
print("🎮 GAME OVER")
print("Player:", player_name)
print("Final Level:", player_level)

if wrong_answers == 0 and question_index == len(landingWar):
    print("🏆 YOU ARE THE PYTHON BASIC MASTER 🐍🔥")
else:
    print("📘 Good effort! Mastery needs perfection.")

print("===================================")
