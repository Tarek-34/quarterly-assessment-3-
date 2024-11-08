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
def connect_db():
    try:
        conn = sqlite3.connect('quiz_bowl.db')
        cursor = conn.cursor()
        return conn, cursor
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Failed to connect to the database: {e}")
        return None, None

# Main application class
class DeleteQuestionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Delete Questions from Quiz Bowl")
        self.selected_category = tk.StringVar()
        self.questions = []
        self.selected_question_id = None
        
        self.conn, self.cursor = connect_db()
        if not self.conn:
            self.root.quit()  # Exit the app if DB connection fails
        
        # Load first window for category selection
        self.create_category_selection_window()

    def create_category_selection_window(self):
        tk.Label(self.root, text="Select a Category to Delete Questions").pack(pady=10)
        category_menu = ttk.Combobox(self.root, textvariable=self.selected_category, values=list(category_tables.keys()))
        category_menu.pack(pady=5)
        tk.Button(self.root, text="Show Questions", command=self.show_questions).pack(pady=20)

    def show_questions(self):
        category = self.selected_category.get()
        if not category:
            messagebox.showwarning("Select Category", "Please select a category.")
            return
        
        # Fetch questions from the selected category
        self.fetch_questions(category)
        if not self.questions:
            messagebox.showerror("No Questions", "No questions available in this category.")
            return
        
        # Clear previous widgets and display question list
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.display_question_list()

    def fetch_questions(self, category):
        table_name = category_tables.get(category)
        if not table_name:
            messagebox.showerror("Invalid Category", "This category does not exist.")
            return
        try:
            self.cursor.execute(f"SELECT id, question_text FROM {table_name}")
            questions_data = self.cursor.fetchall()
            self.questions = [(row[0], row[1]) for row in questions_data]
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")
            print(f"Database error: {e}")

    def display_question_list(self):
        tk.Label(self.root, text="Select a Question to Delete").pack(pady=10)
        
        # Create a listbox to display questions
        question_listbox = tk.Listbox(self.root, height=10, width=50)
        question_listbox.pack(pady=5)
        
        for question_id, question_text in self.questions:
            question_listbox.insert(tk.END, question_text)
        
        # Bind selection to set the question to delete
        question_listbox.bind("<<ListboxSelect>>", lambda event: self.on_question_select(event, question_listbox))
        
        # Delete Button
        tk.Button(self.root, text="Delete Selected Question", command=self.delete_question).pack(pady=20)

    def on_question_select(self, event, listbox):
        selected_index = listbox.curselection()
        if selected_index:
            self.selected_question_id = self.questions[selected_index[0]][0]  # Store the ID of the selected question
        else:
            self.selected_question_id = None

    def delete_question(self):
        if not self.selected_question_id:
            messagebox.showwarning("No Selection", "Please select a question to delete.")
            return
        
        # Get the selected category
        category = self.selected_category.get()
        table_name = category_tables.get(category)

        # Ask for confirmation before deleting
        confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete this question?")
        if confirm:
            try:
                # Delete the selected question
                self.cursor.execute(f"DELETE FROM {table_name} WHERE id = ?", (self.selected_question_id,))
                self.conn.commit()
                messagebox.showinfo("Success", "The question was deleted successfully!")
                self.show_questions()  # Refresh the question list
            except sqlite3.Error as e:
                messagebox.showerror("Database Error", f"An error occurred: {e}")
                print(f"Database error: {e}")
    
# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = DeleteQuestionApp(root)
    root.mainloop()
