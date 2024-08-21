import sys
import csv
import random
# import pyttsx3

def main():
    check_commandla()
    last_name = input("Lastname: ").title().strip()
    initials = input("Initials: ").upper().strip()
    student_no = input("Student number: ")
    # engine = pyttsx3.init()
    play(last_name, initials, student_no)# engine

def check_commandla():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")

def play(last_name, initials, student_no):# engine
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            students = [row for row in reader]

        for student in students:
            if (last_name == student["Lastname"]) and (initials == student["Initials"]) and (student_no == student["Student_number"]):
                score = round((simulate_game()/6) * 100)
                print("Score: ", score)
                print(percentage(score))
                results = percentage(score)
                # engine.say(results)
                # engine.runAndWait()
                creating_reports(last_name, initials, student_no, score, results)
            else:
                pass
    except FileNotFoundError:
        sys.exit("Could,t read CSV file")

def percentage(score):
    if score >= 50:
        results = "PASS"
    else:
        results = "FAIL"
    return results


def creating_reports(last_name, initials, student_no, score, results):
    try:
        with open(sys.argv[2]) as file1:
            reader = csv.DictReader(file1)
            students = [row for row in reader]

        sn = [student["Student_number"] for student in students]
        if student_no not in sn:
            with open(sys.argv[2], "a") as file:
                writer = csv.DictWriter(file, fieldnames=["Lastname", "Initials", "Student_number", "Score", "Results"])
                writer.writerow({"Lastname": last_name, "Initials": initials, "Student_number": student_no, "Score": score, "Results": results})
    except FileNotFoundError:
        sys.exit("Could,t read CSV file")


def generate_integer():
    x = random.randint(0, 10)
    y = random.randint(1, 10)
    return x, y


def simulate_round(x, y):
    count_tries = 0
    sign = random.choice(["+","-","//","*"])
    while count_tries <= 1:
        try:
            answer = int(input(f"{x} {sign} {y} = "))
            if sign == "+":
                if answer == (x + y):
                    return True
                else:
                    count_tries += 1
                    print("Try Again!")
            elif sign == "-":
                if answer == (x - y):
                    return True
                else:
                    count_tries += 1
                    print("Try Again!")
            elif sign == "//":
                if answer == (x // y):
                    return True
                else:
                    count_tries += 1
                    print("Try Again!")
            elif sign == "*":
                if answer == (x * y):
                    return True
                else:
                    count_tries += 1
                    print("Try Again!")
        except:
            count_tries += 1
            print("Try Again!")
    correct = f"{x} {sign} {y}"
    print(f"{x} {sign} {y} = {eval(correct)}")
    return f"{x} {sign} {y} = {eval(correct)}"


def simulate_game():
    count_round = 1
    score = 0
    while count_round <= 6:
        x, y = generate_integer()
        response = simulate_round(x, y)
        if response == True:
            score += 1
        count_round += 1
    return score


if __name__ == "__main__":
    main()

