def grade_checker():
    while True:
        user_input = input("Enter your grade (0 - 100) or 'q' to quit: ").strip()

        if user_input.lower() == 'q':
            print("Goodbye!")
            break

        try:
            grade = float(user_input)

            if 90 <= grade <=100:
                print("Grade: A")
            elif 80 <= grade <=90:
                print("Grade: B")
            elif 70 <= grade <=80:
                print("Grade: C")
            elif 60 <= grade <=70:
                print("Grade: D")
            elif 0 <= grade <=60:
                print("Grade: F")
            else:
                print("INVALID GRADE! Must be between 0 and 100.")
        except ValueError:
            print("INVALID INPUT! Please enter a number or 'q' to quit.")

if __name__ == "__main__":
    grade_checker()