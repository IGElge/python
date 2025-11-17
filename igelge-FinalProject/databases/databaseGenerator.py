import sqlite3

def create_database():
    conn = sqlite3.connect("Database.db")
    cursor = conn.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                currentlyEnrolled BOOLEAN,
                age INTEGER,
                firstName TEXT,
                lastName TEXT,
                gender TEXT,
                email TEXT,
                phone TEXT,
                address TEXT,
                registered TEXT,
                classes TEXT
            )
        ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS classes (
                id INTEGER PRIMARY KEY,
                code TEXT,
                title TEXT,
                description TEXT
            )
        ''')

    # seed students (this took a long time, thank goodness for copy and paste)
    initial_students = [
        (0, 0, 21, 'Veronica', 'Potter', 'female', 'veronicapotter@furnigeer.com', '+1 (849) 512-2231', '771 Downing Street, Tyro, Nebraska, 6696', 'Wed Feb 19 2020 07:25:47', '0,2,14,9'),
        (1, 1, 25, 'Bray', 'Summers', 'male', 'braysummers@furnigeer.com', '+1 (833) 417-2236', '184 Dekoven Court, Driftwood, Marshall Islands, 6520', 'Mon Aug 06 2018 04:13:31', '1,9,4,14'),
        (2, 0, 38, 'Isabelle', 'Robles', 'female', 'isabellerobles@furnigeer.com', '+1 (830) 458-3893', '250 Jamaica Avenue, Elrama, District Of Columbia, 1166', 'Tue Nov 28 2017 19:13:59', '11,12,13'),
        (3, 0, 25, 'Cynthia', 'Campbell', 'female', 'cynthiacampbell@furnigeer.com', '+1 (900) 441-2849', '816 Preston Court, Coinjock, Wisconsin, 9858', 'Wed Sep 27 2017 12:42:10', '1'),
        (4, 0, 21, 'Holder', 'Livingston', 'male', 'holderlivingston@furnigeer.com', '+1 (943) 407-3952', '380 Prospect Street, Adelino, New Hampshire, 4695', 'Sat Sep 21 2019 19:58:47', '5,7,14,2,1'),
        (5, 0, 29, 'Bentley', 'Burke', 'male', 'bentleyburke@furnigeer.com', '+1 (804) 565-2529', '950 Kingston Avenue, Ribera, American Samoa, 2016', 'Tue Feb 09 2021 04:07:36', '15,12,13'),
        (6, 1, 34, 'Velazquez', 'Lucas', 'male', 'velazquezlucas@furnigeer.com', '+1 (919) 519-3148', '148 Beacon Court, Bradenville, Connecticut, 4771', 'Fri Aug 27 2021 04:49:06', '6,8,13'),
        (7, 1, 26, 'Blevins', 'Farmer', 'male', 'blevinsfarmer@furnigeer.com', '+1 (962) 490-2957', '425 Ridge Court, Dotsero, South Carolina, 3021', 'Mon Oct 12 2015 15:41:49', '1,2,3'),
        (8, 1, 37, 'Doyle', 'Camacho', 'male', 'doylecamacho@furnigeer.com', '+1 (909) 436-2106', '812 Christopher Avenue, Kiskimere, Palau, 175', 'Thu Jan 10 2019 16:19:30', '2,4,7,10,15'),
        (9, 0, 18, 'Donovan', 'Rowe', 'male', 'donovanrowe@furnigeer.com', '+1 (812) 464-3111', '490 Alice Court, Bangor, Maine, 979', 'Sat Nov 28 2020 13:59:50', '0,1,3,5,15'),
        (10, 1, 25, 'Estelle', 'Casey', 'female', 'estellecasey@furnigeer.com', '+1 (846) 424-3549', '470 Senator Street, Lindcove, Northern Mariana Islands, 927', 'Tue Dec 12 2017 01:00:47', '10,4,13'),
        (11, 1, 26, 'Sherman', 'Gay', 'male', 'shermangay@furnigeer.com', '+1 (849) 447-2805', '145 Lamont Court, Spelter, New Mexico, 7050', 'Wed Jan 20 2016 00:48:42', '9,4,3,5,1'),
        (12, 0, 26, 'Cummings', 'Hester', 'male', 'cummingshester@furnigeer.com', '+1 (935) 590-2194', '323 Division Avenue, Hobucken, Federated States Of Micronesia, 6081', 'Wed Mar 16 2022 09:44:27', '3,4,9,6,14'),
        (13, 1, 28, 'Allyson', 'Wiggins', 'female', 'allysonwiggins@furnigeer.com', '+1 (934) 514-3729', '759 Bergen Street, Fairforest, Alabama, 7393', 'Fri Apr 23 2021 09:42:15', '11,12,2'),
        (14, 1, 20, 'Powell', 'Walsh', 'male', 'powellwalsh@furnigeer.com', '+1 (922) 572-3476', '138 Glendale Court, Gratton, California, 2403', 'Thu Dec 10 2015 19:44:09', '0,10,5')
    ]

    cursor.executemany("""
           INSERT OR IGNORE INTO students (id, currentlyEnrolled, age, firstName, lastName, gender, email, phone, address, registered, classes)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
       """, initial_students)

    # seed classes (this took a long time, thank goodness for copy and paste)
    initial_classes = [
        (0, 'INFO 1003', 'Basic Programming', 'Basic programming class using Python.'),
        (1, 'INFO 1001', 'Intro to Programming', 'Visual programming class'),
        (2, 'INFO 1002', 'Intro to Web Development', 'Basics of HTML and CSS'),
        (3, 'INFO 1004', 'Programming I', 'Advanced topics of programming'),
        (4, 'INFO 1005', 'Intro to Database', 'Basics of databases design and development class.'),
        (5, 'INFO 1011', 'Intro to C#', 'Programming class using C# language.'),
        (6, 'INFO 1010', 'Intro to Java', 'Programming class using Java language.'),
        (7, 'INFO 1021', 'Advanced C#', 'Advanced Programming Class using C# language'),
        (8, 'INFO 1020', 'Advanced Java', 'Advanced Programming Class using Java language'),
        (9, 'INFO 1015', 'Intro to AWS', 'Basics of Cloud services using AWS'),
        (10, 'INFO 1014', 'Intro to Azure', 'Basics of Cloud services using Azure'),
        (11, 'INFO 1012', 'Intro to Game Development', 'Basics of Game Development using Unity3d Engine'),
        (12, 'INFO 1022', 'Advanced to Game Development', 'Advanced Game Development using Unity3d Engine'),
        (13, 'INFO 1032', 'Intro to .NET', 'Basics of .NET Framework'),
        (14, 'INFO 1101', 'Intro to Spring Boot', 'Basics of Spring Boot using Java'),
        (15, 'INFO 1102', 'Advanced Spring Boot', 'Advanced topics of Spring Boot with Java.')
    ]

    cursor.executemany("""
            INSERT OR IGNORE INTO classes (id, code, title, description)
            VALUES (?, ?, ?, ?)
        """, initial_classes)

    conn.commit()
    conn.close()
    print("Database created and seeded successfully!")

def create_tokens_table():
    conn = sqlite3.connect("Database.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tokens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            token TEXT NOT NULL UNIQUE
        )
    """)

    initial_tokens = [
        ("abc123",),
        ("xyz789",),
        ("token555",)
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO tokens (token) VALUES (?)
    """, initial_tokens)

    conn.commit()
    conn.close()
    print("Tokens table created and seeded successfully!")

if __name__ == "__main__":
    create_database()
    create_tokens_table()
