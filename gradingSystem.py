def show_history() -> None:
    print("\n=== Brief History of Python ===")
    print("- Created in the year 1991")
    print("- Python 3 released in the year 2008")
    print("\n*** Program that Computes the Average Score and Grade of Students ***\n")


def get_names_score() -> tuple[list[str], list[float]]:
    while True:
        try:
            num_students = int(input("Number of students: "))
            if num_students <= 0:
                print("Please enter a number greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    names_of_students = []
    scores = []

    print("\nEnter student names and their scores:\n")

    for i in range(num_students):
        name = input(f'Student {i + 1} name: ').strip()
        if not name:
            name = f'Student {i + 1}'
        names_of_students.append(name)

        while True:
            try:
                score = float(input(f"Enter the score of {name}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    return names_of_students, scores


def compute_average(scores: list[float]) -> float:
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def grade_student(score: float) -> str:
    if score >= 70:
        return 'A'
    elif score >= 60:
        return 'B'
    elif score >= 50:
        return 'C'
    elif score >= 40:
        return 'D'
    else:
        return 'F'


def show_results(names: list[str], scores: list[float]) -> None:
    print("\n=== Student Results ===")
    for name, score in zip(names, scores):
        grade = grade_student(score)
        print(f"{name}: Score = {score:.2f}, Grade = {grade}")

    avg = compute_average(scores)
    print(f"\nAverage Score: {avg:.2f}")
    print(f"Average Grade: {grade_student(avg)}")


# === Main Program ===
if __name__ == "__main__":
    show_history()
    names, scores = get_names_score()
    show_results(names, scores)
