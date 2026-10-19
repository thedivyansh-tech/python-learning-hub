def habit_tracker():
    print("==========================================")
    print("      WELCOME TO YOUR HABIT TRACKER       ")
    print("==========================================")
    
    # A dictionary to store habits and their streaks
    # Format: {"Habit Name": streak_count}
    habits = {
        "Drink Water": 3,
        "Read 15 mins": 5,
        "Exercise": 1
    }
    
    while True:
        print("\n--- Habit Menu ---")
        print("1. View Habits & Streaks")
        print("2. Add a New Habit")
        print("3. Complete a Habit (Increase Streak)")
        print("4. Delete a Habit")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        # Using the match-case statement we learned!
        match choice:
            case "1":
                if not habits:
                    print("\nNo habits found. Add one to get started!")
                else:
                    print("\nYour Current Habits:")
                    for habit, streak in habits.items():
                        print(f"  🔥 {habit}: {streak} day streak!")
            
            case "2":
                new_habit = input("\nEnter the name of the new habit: ").strip()
                if new_habit in habits:
                    print(f"\n'{new_habit}' is already in your tracker!")
                elif new_habit == "":
                    print("\nHabit name cannot be empty.")
                else:
                    habits[new_habit] = 0 # Starts with a 0-day streak
                    print(f"\nSuccess! Added '{new_habit}' to your tracker.")
            
            case "3":
                if not habits:
                    print("\nNo habits to complete yet.")
                    continue
                
                print("\nWhich habit did you complete today?")
                # Convert dictionary keys into a list so we can number them
                habit_list = list(habits.keys())
                for i, habit in enumerate(habit_list, 1):
                    print(f"  {i}. {habit} (Current streak: {habits[habit]})")
                
                try:
                    habit_choice = int(input("Enter the number of the habit: "))
                    if 1 <= habit_choice <= len(habit_list):
                        selected_habit = habit_list[habit_choice - 1]
                        habits[selected_habit] += 1 # Add 1 to the streak
                        print(f"\nAwesome job! Streak for '{selected_habit}' is now {habits[selected_habit]} days! 🎉")
                    else:
                        print("\nInvalid number selection.")
                except ValueError:
                    print("\nError: Please enter a valid number.")
            
            case "4":
                if not habits:
                    print("\nNo habits to delete.")
                    continue
                
                print("\nWhich habit would you like to delete?")
                habit_list = list(habits.keys())
                for i, habit in enumerate(habit_list, 1):
                    print(f"  {i}. {habit}")
                
                try:
                    habit_choice = int(input("Enter the number of the habit to delete: "))
                    if 1 <= habit_choice <= len(habit_list):
                        deleted_habit = habit_list[habit_choice - 1]
                        del habits[deleted_habit] # Removes it from the dictionary
                        print(f"\nDeleted '{deleted_habit}' from your tracker.")
                    else:
                        print("\nInvalid number selection.")
                except ValueError:
                    print("\nError: Please enter a valid number.")
            
            case "5":
                print("\nKeep up the great work! Goodbye!")
                break
                
            case _:
                print("\nInvalid choice! Please pick a number between 1 and 5.")

# Run the habit tracker program
if __name__ == "__main__":
    habit_tracker()