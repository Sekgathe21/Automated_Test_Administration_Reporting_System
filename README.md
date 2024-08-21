# Automated Test Administration and Reporting System for University Students
#### Video Demo:  <https://www.youtube.com/watch?v=1hGLmxbTXRc&ab_channel=KaraboMatlala>
#### Description: A final project for CS50P in Python, designed to facilitate University students in a csv file **`students.csv`** who are eligible to take a test, enabling them to do so, and upon completion, the program will automatically generate a comprehensive report **`results.csv`** detailing the results.

### Introduction:
The provided Python script is designed to simulate a quiz game for university students, involving arithmetic questions. The script utilizes command-line arguments and CSV files for input and output, allowing for flexibility and data persistence.

### Functionality Overview:
1. **Main Functionality**: The `main()` function acts as the central entry point. It orchestrates the flow of the program by ensuring correct command-line arguments, collecting student information, and initiating the quiz game.

2. **Command-line Argument Validation**: The `check_commandla()` function verifies the presence and correctness of command-line arguments. It ensures that the script is invoked with exactly two CSV file paths, one for input and one for output.

3. **Student Information Retrieval and Quiz Initialization**: The `play(last_name, initials, student_no)` function reads student details from the first CSV file provided as an argument. If the entered student information matches any entry, the function proceeds to simulate the quiz game.

4. **Score Calculation and Result Determination**: Upon completion of the quiz game, the score is calculated based on the number of correct answers. The `percentage(score)` function determines whether the score meets the passing threshold (50%) and assigns a pass/fail status accordingly.

5. **Result Recording**: The `creating_reports(last_name, initials, student_no, score, results)` function appends the student's results, including their name, initials, student number, score, and pass/fail status, to the second CSV file provided as an argument.

6. **Arithmetic Question Generation and Answer Validation**: The script generates random arithmetic questions using the `generate_integer()` function. Each question involves two random integers and a randomly selected arithmetic operation. The `simulate_round(x, y)` function prompts the user for the answer, validates it against the correct answer, and allows for a maximum of two attempts per question.

7. **Quiz Simulation**: The `simulate_game()` function orchestrates the simulation of the quiz game by repeatedly calling `simulate_round()` for six rounds (representing six questions) and accumulating the score.

### Additional Features:
- **Error Handling**: The script incorporates robust error handling mechanisms to manage potential exceptions, such as missing CSV files or invalid input.
- **Text-to-Speech Integration**: Although commented out, the script includes code snippets for integrating text-to-speech functionality using the `pyttsx3` library. This feature, if activated, could provide auditory feedback of the quiz results.

### Conclusion:
In summary, the Python script offers a comprehensive solution for conducting a simulated quiz game for university students. It employs CSV files for storing student information and results, utilizes command-line arguments for configuration, and includes error handling mechanisms for robustness. The modular design of the script facilitates easy maintenance and extensibility, making it adaptable to various educational settings and scenarios.

Additionally, the script's flexibility allows for customization, such as adjusting pass/fail thresholds or expanding the question pool. Future enhancements could include support for more question types or integration with learning management systems for automated grading and reporting.

### Test Code Explanation:
The provided test code verifies the correctness of specific functions within the project using the Pytest framework. Here's a breakdown:

1. **`test_check_commandla()`**: This test ensures that the `check_commandla()` function correctly raises a `SystemExit` exception when invoked with insufficient command-line arguments.

2. **`test_generate_integer()`**: This test validates the `percentage()` function's behavior by checking its output against expected results for both passing and failing scores.

3. **`test_simulate_round()`**: This test verifies that the `simulate_round()` function raises a `TypeError` when called without required arguments.

These tests provide a mechanism for automated validation of critical functionality within the project, ensuring reliability and correctness.
