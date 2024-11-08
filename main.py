import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Define your categories and respective tables
category_tables = {
    "Business Application Development": "business_app_dev_questions",
    "Management Info Systems": "mis_questions",
    "Principles of Marketing": "marketing_questions",
    "Business Database Management": "db_management_questions",
    "Business Data Communication": "data_communications_questions",
}

# Try connecting to the SQLite database
try:
    conn = sqlite3.connect('quiz_bowl.db')
    cursor = conn.cursor()
except sqlite3.Error as e:
    messagebox.showerror("Database Error", f"Failed to connect to the database: {e}")

# Define Question class
class Question:
    def __init__(self, question_text, options, correct_answer):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer

# Main application class
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Bowl")
        self.selected_category = tk.StringVar()
        self.questions = []
        self.current_question_index = 0
        self.score = 0
        self.user_answer = tk.StringVar()

        # Load first window for category selection
        self.create_category_selection_window()

    def create_category_selection_window(self):
        tk.Label(self.root, text="Select a Category").pack(pady=10)
        category_menu = ttk.Combobox(self.root, textvariable=self.selected_category, values=list(category_tables.keys()))
        category_menu.pack(pady=5)
        tk.Button(self.root, text="Start Quiz Now", command=self.start_quiz).pack(pady=20)

    def start_quiz(self):
        category = self.selected_category.get()
        if not category:
            messagebox.showwarning("Select Category", "Please select a category to start the quiz.")
            return
        self.fetch_questions(category)
        if not self.questions:
            messagebox.showerror("No Questions", "No questions available in this category.")
            return
        # Clear the window and display the first question
        for widget in self.root.winfo_children():
            widget.destroy()
        self.display_question()

    def fetch_questions(self, category):
        table_name = category_tables.get(category)
        if not table_name:
            messagebox.showerror("Invalid Category", "This category does not exist.")
            return
        print(f"Fetching questions from table: {table_name}")
        try:
            cursor.execute(f"SELECT question_text, option_a, option_b, option_c, option_d, correct_answer FROM {table_name}")
            questions_data = cursor.fetchall()
            print(f"Fetched {len(questions_data)} questions.")
            self.questions = [
                Question(question_text=row[0], options=row[1:5], correct_answer=row[5]) for row in questions_data
            ]
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")
            print(f"Database error: {e}")

    def display_question(self):
        if self.current_question_index >= len(self.questions):
            self.show_score()
            return

        question = self.questions[self.current_question_index]
        self.user_answer.set(None)
        tk.Label(self.root, text=question.question_text, font=("Arial", 14)).pack(pady=10)
        for i, option_text in enumerate(question.options):
            tk.Radiobutton(self.root, text=option_text, variable=self.user_answer, value=chr(65 + i)).pack(anchor='w')
        tk.Button(self.root, text="Submit Answer", command=self.submit_answer).pack(pady=20)

    def submit_answer(self):
        question = self.questions[self.current_question_index]
        user_answer = self.user_answer.get()
        if not user_answer:
            messagebox.showwarning("No Answer", "Please select an answer.")
            return
        if question.check_answer(user_answer):
            self.score += 1
            messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            messagebox.showinfo("Incorrect", f"The correct answer was: {question.correct_answer}")
        self.current_question_index += 1
        for widget in self.root.winfo_children():
            widget.destroy()
        self.display_question()

    def show_score(self):
        messagebox.showinfo("Quiz Completed", f"Your score: {self.score} out of {len(self.questions)}")
        if messagebox.askyesno("Play Again?", "Do you want to restart the quiz?"):
            self.reset_quiz()
        else:
            self.root.quit()

    def reset_quiz(self):
        self.questions = []
        self.current_question_index = 0
        self.score = 0
        self.user_answer.set(None)
        for widget in self.root.winfo_children():
            widget.destroy()
        self.create_category_selection_window()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
