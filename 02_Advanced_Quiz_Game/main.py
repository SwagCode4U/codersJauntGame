"""
=====================================================
🎮 CODERSJAUNT – ADVANCED PYTHON WAR GAME
Topics: OOPS | REGEX | EXCEPTIONS | FILE HANDLING
=====================================================
"""

from toon import Enemy, Weapon
from questions import QUESTIONS
import sys

# ---------------------------
# SAFE INPUT HANDLER
# ---------------------------

def safe_input(prompt):
    try:
        value = input(prompt)
        if value == "9":
            print("\n🚪 Exiting game safely. Respect for clean exit.")
            sys.exit()
        return value
    except KeyboardInterrupt:
        print("\n⛔ Interrupted. Exiting with honor.")
        sys.exit()
    except Exception as e:
        print("⚠️ Unexpected error:", e)
        return ""

# ---------------------------
# UI ART
# ---------------------------

def banner():
    print("""
╔════════════════════════════════════════════╗
║   🧠 CODERSJAUNT ADVANCED PYTHON WAR GAME  ║
║  OOPS • REGEX • FILES • EXCEPTIONS         ║
╠════════════════════════════════════════════╣
║  👉 Press 9 at ANY TIME to EXIT the game   ║
╚════════════════════════════════════════════╝
""")


# ---------------------------
# PLAYER SETUP
# ---------------------------

banner()

player_name = safe_input("Enter Player Name (9 to Exit): ")

if not player_name:
    print("❌ Invalid player name. Exiting.")
    sys.exit()

enemy_choice = safe_input("Choose Enemy (Zombie/Robot): ").upper()
weapon_choice = safe_input("Choose Weapon (Sword/Gun): ").upper()

try:
    enemy = Enemy[enemy_choice]
    weapon = Weapon[weapon_choice]
except KeyError:
    print("❌ Invalid choice. Default assigned.")
    enemy = Enemy.ZOMBIE
    weapon = Weapon.SWORD

player_level = 1
wrong_answers = 0
question_index = 0

# ---------------------------
# GAME LOOP
# ---------------------------

while question_index < len(QUESTIONS):

    print("\n" + "=" * 40)
    print(f"⚔️ LEVEL {player_level} | {QUESTIONS[question_index].topic.name}")
    print("=" * 40)
    print(f"Enemy: {enemy.name} | Weapon: {weapon.name}")
    print("🧠 Answer carefully | Press 9 to exit anytime")
    correct = 0

    for _ in range(3):
        if question_index >= len(QUESTIONS):
            break

        q = QUESTIONS[question_index]

        print(f"\n📌 {q.text}")
        ans = safe_input("Your Answer: ")

        try:
            if ans == q.answer:
                print("✅ Correct")
                correct += 1
            else:
                print("❌ Wrong")
                wrong_answers += 1
        except Exception:
            print("⚠️ Comparison failed")

        question_index += 1

    if correct == 3:
        player_level += 1
        print("\n🏆 ZONE CLEARED! LEVEL UP!")
    else:
        print("\n💀 ZONE FAILED. Knowledge incomplete.")

# ---------------------------
# FINAL RESULT
# ---------------------------

print("\n" + "=" * 45)
print("🎮 GAME COMPLETED")
print("Player:", player_name)
print("Final Level:", player_level)

if wrong_answers == 0:
    print("🏆 PYTHON ADVANCED MASTER ACHIEVED 🐍🔥")
else:
    print("📘 Advanced learner. Mastery needs precision.")

print("=" * 45)
