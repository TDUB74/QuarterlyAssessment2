import sqlite3
import random

DB_PATH = "quiz_bowl_db.sql"

# ANSI escape codes for text colors
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

def select_category():
    print("Select a category:")
    print("1. Consumer Behavior")
    print("2. Entrepreneurship")
    print("3. Business Analytics")
    print("4. American Literature")
    print("5. Coding")

    choice = input("Enter the number of your chosen category: ")

    categories = {
        "1": "ConsumerBehavior",
        "2": "Entrepreneurship",
        "3": "BusinessAnalytics",
        "4": "AmericanLiterature",
        "5": "Coding",
    }

    return categories.get(choice)

def get_random_question(category):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(f"SELECT id, question, answer FROM {category} ORDER BY RANDOM() LIMIT 1")
        question_data = cursor.fetchone()
        conn.close()

        return question_data
    except sqlite3.OperationalError as e:
        print(f"Error accessing the '{category}' table: {e}")
        return None

def display_colored_message(message, color):
    print(f"{color}{message}{RESET}")

def main():
    print("Welcome to Quiz Bowl!\n")

    while True:
        selected_category = select_category()

        if not selected_category:
            print("Invalid category selection. Please try again.\n")
            continue

        question_data = get_random_question(selected_category)

        if not question_data:
            print("Error retrieving a question. Please try again.\n")
            continue

        question_id, question, correct_answer = question_data

        print("\nQuestion:")
        print(question)

        user_answer = input("Your Answer: ").strip()

        if user_answer.lower() == correct_answer.lower():
            display_colored_message("Correct!", GREEN)
        else:
            display_colored_message(f"Incorrect. The correct answer is: {correct_answer}", RED)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()
