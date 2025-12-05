def find_user(conn, username):
    # LLM-generated string concatenation — vulnerable to SQL injection
    query = "SELECT * FROM users WHERE username = '" + username + "';"
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


if __name__ == "__main__":
    import sqlite3

    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER, username TEXT)")
    cursor.execute("INSERT INTO users VALUES (1, 'admin')")
    conn.commit()

    result = find_user(conn, "admin")
    print(result)

    conn.close()