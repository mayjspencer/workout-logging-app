import os

def getWorkoutFile(username):
    file_path = f"{username}.txt"

    try:
        with open(file_path, "r") as user_file:
            # Read all lines and display them
            lines = user_file.readlines()
            for line in lines:
                print(line.strip())  # Strip to remove newline characters

    except FileNotFoundError:
        print(f"User '{username}' not found. Please register or enter a valid username.")

def log_new_workout(username):
    #get from User how many exercises they did
    exerciseCount = int(input("Enter the amount of exercises you did: "))
    #create a line for each exercise in the file
    while exerciseCount > 0:
        exercise_type = input("Enter the exercise type: ")
        sets = input("Enter the number of sets: ")
        reps = input("Enter the number of reps per set: ")
        workout_data = f"{exercise_type}, {sets} sets x {reps} reps"
        #send the data to be written to the file
        write_user_file(username, workout_data)
        exerciseCount = exerciseCount - 1

def write_user_file(username, workoutdata):
    file_path = f"{username}.txt"

    try:
        #write the workout data to the file - one line per exercise done
        with open(file_path, "a") as user_file: 
            user_file.write(workoutdata + "\n")  
        print(f"Data successfully written to {file_path}")

    except FileNotFoundError:
        print(f"User '{username}' not found. Please register or enter a valid username.")

def register_user(username):
    # Check if the user already exists
    if os.path.isfile(f"{username}.txt"):
        print(f"User '{username}' already exists. Logging in...")
    else:
        # Create a new user and associated text file
        with open(f"{username}.txt", "w") as user_file:
            user_file.write(f"User: {username}\n\nWorkout History:\n")

        print(f"User '{username}' successfully registered.")

def main():
    print("Welcome to the Command-Line Workout Tracker!\n")

    username = input("Type your username or create one if you are new: ")
    register_user(username)  # You can choose to register a new user or log in an existing one.

    while True:
        print("\nChoose an option:\n")
        print("A- View Workout History\n")
        print("B - Log New Workout\n")
        print("C - Exit\n")

        choice = input("Enter your choice (A / B / C): ")

        if choice == "A":
            getWorkoutFile(username)
        elif choice == "B":
            log_new_workout(username)
        elif choice == "C":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
