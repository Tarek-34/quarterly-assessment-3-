import sqlite3

# Sample data to insert into the database
sample_data = {
    "business_app_dev_questions": [
        ("What is the main purpose of business application development?", "Data analysis", 
         "Software creation for business processes", "Customer service", "Marketing", "B"),

        ("Which language is commonly used for business web applications?", "JavaScript", "Python", 
         "COBOL", "Fortran", "A"),

        ("What is front-end development focused on?", "Database management", 
         "User interface and experience", "Server maintenance", "Networking", "B"),

        ("What is a common tool for back-end development?", "HTML", "CSS", "Node.js", "XML", "C"),

        ("What does SDLC stand for?", "System Development Life Cycle", 
         "Software Development Life Cycle", "System Design Logic Code", "Software Data Link Control", "B"),

        ("What is a common software development methodology used in business application development?", "Waterfall",
         "Spiral", "Agile", "V-Model", "C"),

        ("Which phase in the software development life cycle focuses on understanding the user's needs?", "Design",
            "Testing", "Requirements gathering", "Deployment", "C"),

        ("What does the term version control refer to in business application development?", "Tracking software bugs"
         ,"Managing changes to the source code", "controlling software access permissions", "Designing user interfaces","B"),

        ("Which of the following is a tool commonly used for Agile project management?","Microsoft Word", "Jira", "Photoshop", 
          "GitHub","B"), 

        ("Which of the following is typically a key benefit of using Agile methodology in business application development?",
         "Clear, fixed project deadlines", "Ability to quickly respond to changing requirements", "Focus on comprehensive documentation",
            "Linear and sequential development process", "B")



    ],
    "mis_questions": [
        ("What is MIS primarily concerned with?", "Manufacturing", 
         "Information management and decision-making", "Programming", "Legal compliance", "B"),

        ("Which component is a part of an information system?", "People", "Products", 
         "Raw materials", "Vehicles", "A"),

        ("What is ERP?", "Efficient Resource Planning", "Enterprise Resource Planning", 
         "Extended Resource Platform", "Enhanced Research Program", "B"),

        ("Which of these is a core MIS function?", "Building websites", "Managing data", 
         "Customer feedback analysis", "Physical security", "B"),

        ("What does CRM stand for in business?", "Customer Retention Methodology", 
         "Customer Relationship Management", "Critical Response Model", "Customer Resource Manual", "B"),

        ("Which of the following is a key benefit of using an MIS in an organization?",
         "Reduces the need for strategic planning", "Enhances communication and collaboration within departments", 
         "Increases manual paperwork", "Eliminates the need for data storage","B"),

         ("What role does data analytics play in an MIS?","It is only used for marketing purposes", "It helps managers analyze trends and make data-driven decisions",
            "It automates payroll processing", "It designs user interfaces","B"),

        ("Which of the following describes a Decision Support System (DSS) in the context of MIS?", "A system that handles routine data processing tasks",
            "A system designed to assist managers in making non-routine decisions", "A tool for developing computer games","A platform for social media marketing","B"),
        
        ("How does an MIS typically handle large amounts of data?","By using spreadsheets only","By manually organizing paper files",
         "By outsourcing all data storage", "By employing databases and data management systems", "D"),

        ("Which of the following describes the relationship between MIS and business processes?",
          "MIS supports and improves business processes by automating information flow","MIS is unrelated to business operations",
          "MIS replaces all manual business processes", "MIS slows down business processes by introducing complexity","A"),
        


    ],
    "marketing_questions": [
        ("What is the primary goal of marketing?", "Creating advertisements", 
         "Meeting customer needs profitably", "Developing products", "Managing supply chains", "B"),
        ("Which of these is one of the 4Ps of Marketing?", "Profit", "Price", 
         "People", "Productivity", "B"),
        ("What is market segmentation?", "Setting product prices", 
         "Dividing a market into groups", "Creating promotional materials", "Analyzing customer feedback", "B"),
        ("What is a target market?", "Any potential customer", "Specific group a company aims to reach", 
         "International customers", "Local customers only", "B"),
        ("What is the purpose of branding?", "Product design", "Differentiating a product", 
         "Cost reduction", "Increasing sales tax", "B"),

        ("What is the purpose of a sales funnel?", "To track financial performance", 
            "To visualize the customer journey from awareness to purchase", "To store product information", 
            "To manage supplier relationships", "B"),

        ("What is influencer marketing?", "Marketing that uses celebrities or online personalities to promote products", 
            "Hiring new employees for a marketing team", "Conducting public relations events", 
                "Creating a product prototype", "A"),

        ("What is customer relationship management (CRM)?", "A system to manage financial transactions", 
            "A strategy for managing a company's interactions with current and future customers", 
            "A marketing campaign for new products", "A process for designing websites", "B"),

        ("Which metric is commonly used to measure the success of a marketing campaign?", "Employee retention rate", 
            "Click-through rate (CTR)", "Number of meetings held", "Office supply costs", "B"),

        ("What does B2B stand for in marketing?", "Back to Back", 
        "Business to Business", "Build to Break", "Buy to Borrow", "B"),

    ],
    "db_management_questions": [
        ("What is a database?", "A software for designing websites", 
         "A collection of organized data", "A programming language", "A network protocol", "B"),
        ("What is SQL?", "Standard Query Language", 
         "Structured Query Language", "Simple Query Layout", "Standard Queue Link", "B"),
        ("What is a primary key in a database?", "A field that uniquely identifies a record", 
         "A type of software", "An encryption method", "A programming function", "A"),
        ("What is the purpose of a relational database?", "Organize data in tables", 
         "Analyze network traffic", "Optimize web content", "Design application interfaces", "A"),
        ("Which command is used to retrieve data in SQL?", "UPDATE", 
         "DELETE", "SELECT", "INSERT", "C"),

        ("What is the purpose of a 'marketing mix'?", "To define a company’s hiring practices", 
            "To guide a company’s approach to pricing, product, promotion, and place", "To reduce operational costs", 
            "To manage employee relationships", "B"),

        ("What does 'customer loyalty' refer to?", "The number of products a customer buys", 
            "The likelihood that customers will return and continue to buy from a company", 
            "The speed at which products are sold", "The cost of acquiring new customers", "B"),

        ("Which of the following is an example of 'direct marketing'?", "Television commercials", 
            "Email campaigns targeted to specific customers", "Billboard advertising", "Magazine features", "B"),

        ("What is the main purpose of 'content marketing'?", "Selling products door-to-door", 
            "Creating valuable and relevant content to attract and engage an audience", 
            "Developing software tools", "Handling logistics and supply chain management", "B"),

        ("What does the term 'USP' stand for in marketing?", "Universal Selling Point", 
            "Unique Selling Proposition", "Uniting Sales Practices", "Ultimate Sales Process", "B")

    ],
    "data_communications_questions": [
        ("What is data communication?", "The process of printing data", 
         "Exchange of data between devices", "A programming language", "A type of database", "B"),
        ("What is bandwidth?", "The speed of a car", 
         "Amount of data transmitted over a network", "Strength of an internet signal", "Number of computers in a network", "B"),
        ("Which device is essential for networking?", "Keyboard", "Router", 
         "Mouse", "Scanner", "B"),
        ("What is Wi-Fi?", "A data management system", 
         "Wireless communication technology", "An internet service provider", "A programming language", "B"),
        ("What is the purpose of an IP address?", "To store user data", 
         "To identify devices on a network", "To provide internet speed", "To analyze data", "B"),

        ("What is the function of a firewall in a network?", "To speed up data transfer", 
            "To prevent unauthorized access to or from a private network", "To store backup data", 
            "To compress files", "B"),

        ("Which of the following is a common data transmission medium?", "Copper cable", 
        "Plastic tubing", "Wooden plank", "Stone wall", "A"),

        ("What does the term packet refer to in data communications?", "A physical mail package", 
            "A formatted unit of data carried by a network", "A type of storage device", 
            "A software update", "B"),

        ("What is latency in a network?", "The total number of devices connected", 
            "The time delay in data transmission", "The width of the network cables", 
            "The storage capacity of a server", "B"),

        ("What is an example of a wireless communication technology?", "Fiber optic cable", 
            "Bluetooth", "Copper wire", "Ethernet", "B")

    ]
}

# Use a with statement for the database connection
try:
    with sqlite3.connect('quiz_bowl.db') as conn:
        cursor = conn.cursor()
        # Insert sample data into each category table if empty
        for table_name, questions in sample_data.items():
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            if cursor.fetchone()[0] == 0:
                for question in questions:
                    cursor.execute(f'''
                    INSERT INTO {table_name} (question_text, option_a, option_b, option_c, option_d, correct_answer)
                    VALUES (?, ?, ?, ?, ?, ?)
                    ''', question)
                print(f"Inserted data into {table_name}")  # Confirmation message
        conn.commit()
except sqlite3.Error as e:
    print(f"An error occurred: {e}")
