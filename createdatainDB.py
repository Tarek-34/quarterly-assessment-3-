import sqlite3

# Define each category and the corresponding SQL command for creating tables
category_tables = {
    "Business Application Development": '''CREATE TABLE IF NOT EXISTS business_app_dev_questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_text TEXT,
        option_a TEXT,
        option_b TEXT,
        option_c TEXT,
        option_d TEXT,
        correct_answer TEXT 
    )''',
    "Management Information Systems": '''CREATE TABLE IF NOT EXISTS mis_questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_text TEXT,
        option_a TEXT,
        option_b TEXT,
        option_c TEXT,
        option_d TEXT,
        correct_answer TEXT
    )''',
    "Principles of Marketing": '''CREATE TABLE IF NOT EXISTS marketing_questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_text TEXT,
        option_a TEXT,
        option_b TEXT,
        option_c TEXT,
        option_d TEXT,
        correct_answer TEXT
    )''',
    "Business Database Management": '''CREATE TABLE IF NOT EXISTS db_management_questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_text TEXT,
        option_a TEXT,
        option_b TEXT,
        option_c TEXT,
        option_d TEXT,
        correct_answer TEXT
    )''',
    "Business Data Communication": '''CREATE TABLE IF NOT EXISTS data_communications_questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_text TEXT,
        option_a TEXT,
        option_b TEXT,
        option_c TEXT,
        option_d TEXT,
        correct_answer TEXT
    )'''
}

# Use a with statement for the database connection
with sqlite3.connect('quiz_bowl.db') as conn:
    cursor = conn.cursor()
    # Create tables in the database
    for category, query in category_tables.items():
        cursor.execute(query)
        print(f"Table for '{category}' created or already exists.")  # Optional: Log table creation
    conn.commit()

# No need to explicitly close the connection, as 'with' handles it
