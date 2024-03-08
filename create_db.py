import sqlite3
 
DB_PATH = "quiz_bowl_db.sql"

def create_tables():
    categories = [
        "ConsumerBehavior",
        "Entrepreneurship",
        "BusinessAnalytics",
        "AmericanLiterature",
        "Coding"
    ]

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for category in categories:
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {category} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT,
                answer TEXT
            )
        ''')

    conn.commit()
    conn.close()

def add_data():
    data = {
        "ConsumerBehavior": [
            ("What is consumer behavior?", "The study of individuals and groups and the processes they use to select, purchase, use, and dispose of products."),
            ("Define the concept of brand loyalty.", "A consumer's preference for a particular brand that results in repeat purchases."),
            ("How do reference groups influence consumer behavior?", "Groups that individuals use as a reference point in forming their attitudes, beliefs, and behaviors."),
            ("What factors influence consumer decision-making?", "Cultural, social, personal, and psychological factors."),
            ("Explain the concept of consumer satisfaction.", "The extent to which a product meets or exceeds customer expectations."),
            ("What is the role of perception in consumer behavior?", "The process by which people select, organize, and interpret information from their surroundings."),
            ("How does motivation affect consumer behavior?", "The driving force that encourages individuals to take action."),
            ("Define the concept of market segmentation.", "Dividing a market into distinct groups with similar needs, characteristics, or behaviors."),
            ("What is the importance of branding in consumer behavior?", "It helps create a unique identity for a product or service."),
            ("How do cultural factors impact consumer behavior?", "They include values, beliefs, customs, and lifestyles that shape individuals' purchasing decisions."),
        ],
        "Entrepreneurship": [
            ("What is entrepreneurship?", "The process of starting and running a business, typically with the aim of making a profit."),
            ("Define bootstrapping in entrepreneurship.", "Building and growing a startup with little or no external capital."),
            ("What is the Lean Startup methodology?", "A method for developing businesses and products that emphasizes flexibility and iterative development."),
            ("Explain the concept of MVP (Minimum Viable Product).", "The simplest version of a product that allows a team to collect the maximum amount of validated learning about customers with the least effort."),
            ("What is a pivot in the context of entrepreneurship?", "A fundamental change to a product or business model in response to feedback."),
            ("How does market research contribute to entrepreneurship?", "It helps entrepreneurs understand their target audience and market demand."),
            ("What are the key characteristics of successful entrepreneurs?", "Adaptability, resilience, creativity, and a willingness to take calculated risks."),
            ("What is the importance of networking in entrepreneurship?", "Building connections can provide valuable resources, advice, and opportunities."),
            ("Define the term 'business model'", "A plan that outlines how a company will create, deliver, and capture value."),
            ("How can entrepreneurs manage risk in their ventures?", "By conducting thorough risk assessments and implementing risk mitigation strategies."),
        ],
        "BusinessAnalytics": [
            ("What is predictive analytics?", "The use of data, statistical algorithms, and machine learning techniques to identify the likelihood of future outcomes."),
            ("Define data mining.", "The process of discovering patterns in large datasets."),
            ("Explain the difference between descriptive and prescriptive analytics.", "Descriptive analytics focuses on what has happened, while prescriptive analytics recommends actions to optimize outcomes."),
            ("What is A/B testing?", "A method of comparing two versions of a webpage or app against each other to determine which one performs better."),
            ("How does data visualization aid in business analytics?", "It helps communicate insights and findings effectively."),
            ("Define key performance indicators (KPIs).", "Quantifiable measures used to evaluate the success of an organization or a specific activity."),
            ("What is the role of a data analyst in business analytics?", "Analyzing data to help organizations make informed business decisions."),
            ("Explain the concept of data-driven decision-making.", "Using data to inform and guide the decision-making process."),
            ("How can businesses use analytics for customer segmentation?", "Identifying and targeting specific groups of customers based on their behavior and characteristics."),
            ("What is the importance of data quality in analytics?", "High-quality data is essential for accurate and reliable analysis."),
        ],
        "AmericanLiterature": [
            ("Who wrote 'Moby-Dick'?", "Herman Melville"),
            ("What is the setting of 'To Kill a Mockingbird'?", "Maycomb, Alabama, during the Great Depression."),
            ("Who is the protagonist in 'The Catcher in the Rye'?", "Holden Caulfield"),
            ("What is the theme of 'The Great Gatsby'?", "The American Dream and its corruption."),
            ("Who wrote 'The Scarlet Letter'?", "Nathaniel Hawthorne"),
            ("What is the significance of the 'American Renaissance' in literature?", "A period in the mid-19th century marked by a surge in American literature with a focus on individualism and transcendentalism."),
            ("What is the plot of 'The Adventures of Huckleberry Finn'?", "The journey of a young boy and a runaway slave down the Mississippi River."),
            ("Who is the author of 'The Grapes of Wrath'?", "John Steinbeck"),
            ("What is the genre of 'The Tell-Tale Heart' by Edgar Allan Poe?", "Gothic fiction"),
            ("Explain the concept of the 'American Dream' in literature.", "The ideal that every citizen has an equal opportunity to achieve success and prosperity through hard work, determination, and initiative."),
        ],
        "Coding": [
            ("What is the purpose of a function in programming?", "To perform a specific task and return a value."),
            ("Explain the difference between '==' and '===' in JavaScript.", "'==' checks for equality, while '===' checks for both equality and type."),
            ("What is the significance of indentation in Python?", "It defines the structure and scope of code blocks."),
            ("Define recursion in programming.", "A function that calls itself in its own definition."),
            ("What is the role of a constructor in object-oriented programming?", "It initializes the object's attributes when an instance is created."),
            ("What is version control in software development?", "A system that records changes to a file or set of files over time, allowing you to recall specific versions later."),
            ("Explain the concept of 'agile' in project management.", "A project management approach that emphasizes flexibility, collaboration, and customer satisfaction."),
            ("What is the purpose of the 'return' statement in a function?", "To specify the value that a function should return."),
            ("Define the term 'algorithm'.", "A step-by-step procedure or formula for solving a problem."),
            ("How does object-oriented programming promote code reusability?", "By organizing code into reusable objects with defined properties and behaviors."),
        ],
    }

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for category, questions in data.items():
        cursor.executemany(f"INSERT INTO {category} (question, answer) VALUES (?, ?)"), questions
