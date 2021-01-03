import sqlite3 as sq

# Подключение к БД
with sq.connect('db.sqlite3') as con:
    cur = con.cursor()

    # CREATE, DELETE TABLE
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute('''CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL DEFAULT 1,
    score INTEGER
    )''')

    # SELECT and INSERT
    cur.execute("INSERT INTO users VALUES (43, 'Alex', 1, 10)")
    cur.execute("INSERT INTO users (name, age, score) VALUES ('Alex', 1, 10)")
    cur.execute("SELECT name, age, score FROM users")
    cur.execute("SELECT * FROM users")
    cur.execute("SELECT * FROM users LIMIT 2 OFFSET 2")
    cur.execute("SELECT * FROM users ORDER BY age")
    cur.execute("SELECT * FROM users ORDER BY age DESC")
    cur.execute("SELECT * FROM users WHERE score < 1000 OR age IN (19,20,21) OR name == 'Alex'")
    cur.execute("SELECT * FROM users WHERE score BETWEEN 100 AND 1000")
    results = cur.fetchall()  # bad way
    print(results)
    for result in cur:  # good way
        print(result)
    results = cur.fetchmany(2)  # takes first <size> results
    result = cur.fetchone()  # takes first result

    # UPDATE and DELETE
    cur.execute("UPDATE users SET score=score+500, age=20 WHERE name LIKE 'Alex' OR score <= 1000")
    cur.execute("UPDATE users SET score=score+500 WHERE name LIKE 'A%'")  # any line continuation
    cur.execute("UPDATE users SET score=score+500 WHERE name LIKE 'A_ex'")  # any letter
    cur.execute("DELETE FROM users WHERE score < 1000")

    # aggregation and grouping GROUP BY
    cur.execute("SELECT sum(user_id) as count FROM users WHERE user_id=1")
    # count()
    # sum()
    # avr() - the arithmetic mean
    # min()
    # max()
    cur.execute("SELECT count(DISTINCT user_id) as count FROM users ")  # DISTINCT = unique
    cur.execute("SELECT user_id, sun(score) as sum FROM users GROUP BY user_id")

    # JOIN
    cur.execute("SELECT name, age, games.score FROM games JOIN users ON games.user_id=users.rawid")  # summary report
    cur.execute("SELECT name, age, games.score FROM users, games")  # a set of data, not a summary report

    # UNION
    cur.execute('''SELECT score, 'from' FROM tab1
    UNION SELECT val, type FROM tab2
    )''')

    # nested queries
    cur.execute('''INSERT INTO adults
    SELECT NULL, name, age FROM users WHERE age > 25
    )''')

    # con.commit()
    # con.close()
