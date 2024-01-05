def viewWorkoutFile(username,workout):
    file_path = f"{username}{workout}.txt"

    try:
        with open(file_path, "r") as user_file:
            # Read all lines and display them
            lines = user_file.readlines()
            for line in lines:
                print(line.strip())  # Strip to remove newline characters

    except FileNotFoundError:
        print(f"User '{username}' not found. Please register or enter a valid username.")


def editWorkoutFile(username, workout):
    file_path = f"{username}{workout}.txt"

    try:
        with open(file_path, "r") as user_file:
            # Read all lines and display them
            lines = user_file.readlines()
            for i, line in enumerate(lines):
                print(f"{i + 1}. {line.strip()}")  # Display line numbers for user to choose

            # Allow user to make edits
            while True:
                try:
                    #User chooses which set to edit
                    choice = int(input("Enter the line number to edit (or type '0' to finish): "))
                    if choice == 0:
                        break
                    #check that number is in bounds
                    elif 1 <= choice <= len(lines):
                        #change the data on the line
                        #edit_line = lines[choice - 1].strip()
                        new_weight = input("Enter the new weight: ")
                        new_reps = input("Enter the new reps: ")
                        new_data = f"{new_weight} x {new_reps} reps\n"
                        lines[choice - 1] = new_data
                    else:
                        print("Invalid line number. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        # Write the updated data back to the file
        with open(file_path, "w") as user_file:
            user_file.writelines(lines)

        print(f"Workout data successfully updated in {file_path}")

    except FileNotFoundError:
        print(f"User '{username}' or workout '{workout}' not found. Please register or enter valid information.")


def log_new_workout(username,workout):
    #get from User how many exercises they did
    while True:
        try:
            exerciseCount = int(input("Enter the amount of exercises you did: "))
            break
        except ValueError: 
            print("Enter a number")
    #loop through each exercise
    while exerciseCount > 0:
        #first take in the exercise type and write it to the file
        exercise_type = input("Enter the exercise type: ")
        file_path = f"{username}{workout}.txt"
        try:
            #write the exercise type to the file
            with open(file_path, "a") as user_file: 
                user_file.write(f"{exercise_type}: " + "\n")  
            print(f"Data successfully written to {file_path}")
        except FileNotFoundError:
            print(f"User '{username}' not found. Please register or enter a valid username.")
        #then write workout data to the file on a line for each set 
        try:
            sets = int(input("Enter the amount of sets: "))
        except ValueError: 
            print("Enter a number")
        for _ in range(sets):
            weight = input("Enter the weight: ")
            reps = input("Enter the amount of reps: ")
            workout_data = f"{weight} x {reps} reps"#send the data to be written to the file
            write_user_file(username, workout, workout_data)
        exerciseCount = exerciseCount - 1

def write_user_file(username, workout,workoutdata):
    file_path = f"{username}{workout}.txt"

    try:
        #write the workout data to the file - one line per exercise done
        with open(file_path, "a") as user_file: 
            user_file.write(workoutdata + "\n")  
        print(f"Data successfully written to {file_path}")

    except FileNotFoundError:
        print(f"User '{username}' not found. Please register or enter a valid username.")


# Check user file for the provided username
# Return False if the user is found in the file
def verify_user(username):
    file_path = "users.txt"
    try:
        with open(file_path, "r") as user_file:
            for line in user_file:
                if line.strip() == username:
                    return False
    except FileNotFoundError:
        return True
    
    return True  # Username not found, available

# Add user or log the user in if they are not new
def register_user(username):
    # Check if the user is not in the user file (i.e., the username is available)
    if verify_user(username):
        with open("users.txt", "a") as user_file:
            user_file.write(f"{username}\n")
        print(f"User '{username}' successfully registered.")
    else:
        print(f"User '{username}' already exists. Logging in...")


def main():
    print("Welcome to the Command-Line Workout Tracker!\n")

    username = input("Type your username or create one if you are new: ")
    register_user(username)  # You can choose to register a new user or log in an existing one.

    while True:
        print("\nChoose an option:\n")
        print("A - View Workout History\n")
        print("B - Log New Workout\n")
        print("C - Edit Existing Workout\n")
        print("D - Exit\n")

        choice = input("Enter your choice (A / B / C / D): ")

        if choice == "A":
            workout = input("\nEnter the workout you want to view:\n")
            viewWorkoutFile(username, workout)
        elif choice == "B":
            workout = input("\nEnter the workout you are doing today:\n")
            log_new_workout(username, workout)
        elif choice == "C":
            workout = input("\nEnter the workout you want to edit:\n")
            editWorkoutFile(username, workout)
        elif choice == "D":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
