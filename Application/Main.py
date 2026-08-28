import mysql.connector as mp 
import random as rd
import sys
def play_head_tail():
    print("\n--- Head / Tail ---")
    ch = ["head", "tail"]
    toss = rd.choice(ch)
    player = input("Type head or tail: ").strip().lower()
    
    if toss == player:
        print("Result: WIN!")
    else:
        print(f"Result: LOSE! It was {toss}.")

def play_number_guessing():
    print("\n--- Number Guessing ---")
    computer = rd.randint(1, 5)
    try:
        player = int(input("Guess the number from 1 to 5: "))
        if computer == player:
            print("Result: WIN!")
        else:
            print("Result: LOSE!")
        print("Actual number was:", computer)
    except ValueError:
        print("Please enter a valid number!")

def play_roll_game():
    print("\n--- Roll Game ---")
    options = ["apple", "mango", "banana"]
    choices = []
    
    for opt in range(3):
        choices.append(rd.choice(options))
        
    print(f"Spins: {choices}")
    
    if choices[0] == choices[1] == choices[2]:
        print("Result: WIN! All three match!")
    else:
        print("Result: LOSE! Not all match.")
def game_menu(user_name):
    while True:
        print(f"\n--- {user_name}'s Game Arcade ---")
        print("1. Head/Tail")
        print("2. Number Guessing")
        print("3. Roll Game")
        print("4. Log Out")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == "1":
            play_head_tail()
        elif choice == "2":
            play_number_guessing()
        elif choice == "3":
            play_roll_game()
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid choice! Please try again.")

def main():
    try:
        db = mp.connect(
            host="localhost",
            user="root",
            password="",
            database="royalhackerone"
        )
        cursor = db.cursor()
        
        tablecommand = """CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name TEXT,
                    email TEXT,
                    password TEXT
                )"""
        cursor.execute(tablecommand)

    except mp.Error as err:
        print(f"Error connecting to MySQL: {err}")
        sys.exit(1)

    while True:
        print("\n--- Main Menu ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            
            variable = (name, email, password)
            insertcommand = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            cursor.execute(insertcommand, variable)
            db.commit()
            print("Registration successful!")
            
        elif choice == "2":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            
            variable = (email, password)
            selectcommand = "SELECT * FROM users WHERE email=%s AND password=%s"
            cursor.execute(selectcommand, variable)
            result = cursor.fetchone()
            
            if result:
                user_name = result[1]
                print(f"\nLogin successful! Welcome, {user_name}.")
                game_menu(user_name) 
            else:
                print("Invalid credentials!")
                
        elif choice == "3":
            print("Exiting program...")
            break
            
        else:
            print("Invalid choice! Please select 1, 2, or 3.")
    if db.is_connected():
        cursor.close()
        db.close()

if __name__ == "__main__":
    main()