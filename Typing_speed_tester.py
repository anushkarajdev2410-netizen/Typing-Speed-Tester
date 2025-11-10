import time
import random
import os

# ==========================================================
#              🧠  TYPING SPEED TESTER PROJECT 🧠
# ==========================================================
# This program tests your typing speed and accuracy.
# It measures how fast and accurately you can type given sentences.
# ==========================================================

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an interpreted and high-level programming language.",
    "Typing fast requires regular practice and concentration.",
    "Never stop learning because life never stops teaching.",
    "Artificial intelligence is shaping the world of tomorrow.",
    "Consistency is the key to mastering any skill."
]

# Function to clear screen (works for Windows, Mac, Linux)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to calculate accuracy
def calculate_accuracy(original, typed):
    correct_chars = 0
    for i in range(min(len(original), len(typed))):
        if original[i] == typed[i]:
            correct_chars += 1
    accuracy = (correct_chars / len(original)) * 100
    return round(accuracy, 2)

# Function for each round
def typing_round(round_number):
    clear_screen()
    print("\n------------------------------------------")
    print(f"🕹  Round {round_number}")
    print("------------------------------------------")

    # Random sentence
    sentence = random.choice(sentences)
    print("\nType this sentence:\n")
    print(sentence)

    print("\nGet ready...")
    for i in range(3, 0, -1):
        print(f"Starting in {i}...")
        time.sleep(1)

    print("\nStart typing now!\n")

    # Start timer
    start_time = time.time()
    typed = input("👉 Type here: ")
    end_time = time.time()

    # Calculate results
    total_time = round(end_time - start_time, 2)
    words = len(typed.split())
    if total_time > 0:
        speed = round((words / total_time) * 60, 2)
    else:
        speed = 0
    accuracy = calculate_accuracy(sentence, typed)

    print("\n========== ROUND RESULTS ==========")
    print(f"Time taken : {total_time} seconds")
    print(f"Speed      : {speed} words per minute (WPM)")
    print(f"Accuracy   : {accuracy}%")
    print("===================================\n")

    return speed, accuracy

# Function to show summary
def show_summary(results):
    clear_screen()
    print("\n===================================")
    print("        🧾 TYPING TEST SUMMARY")
    print("===================================")

    total_rounds = len(results)
    total_speed = sum(r[0] for r in results)
    total_accuracy = sum(r[1] for r in results)
    best_speed = max(r[0] for r in results)
    avg_speed = round(total_speed / total_rounds, 2)
    avg_accuracy = round(total_accuracy / total_rounds, 2)

    print(f"Total Rounds Played : {total_rounds}")
    print(f"Average Speed        : {avg_speed} WPM")
    print(f"Average Accuracy     : {avg_accuracy}%")
    print(f"Best Speed           : {best_speed} WPM")
    print("===================================")
    print("Thank you for using Typing Speed Tester!")
    print("Keep practicing and improve your typing skills 🧑‍💻\n")

# Main program
def main():
    clear_screen()
    print("=" * 60)
    print("               🧠 TYPING SPEED TESTER 🧠")
    print("=" * 60)
    print("Test your typing speed and accuracy.")
    print("You can play multiple rounds and see your best score.\n")

    results = []
    round_number = 1

    while True:
        speed, accuracy = typing_round(round_number)
        results.append((speed, accuracy))
        round_number += 1

        again = input("Do you want to play another round? (y/n): ").lower()
        if again != 'y':
            break

    show_summary(results)

# Run the program
if __name__ == "__main__":
    main()
