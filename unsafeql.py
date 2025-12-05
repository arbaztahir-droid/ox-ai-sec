import json
import urllib.request

def find_user(conn, username):
    # LLM-generated string concatenation — vulnerable to SQL injection
    query = "SELECT * FROM users WHERE username = '" + username + "';"
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

DB_PASS = "SuperSecret123!"

def fetch_data(client_base_url, id):
    url = f"{client_base_url}/data/{id}?token={DB_PASS}"
    with urllib.request.urlopen(url) as response:
        data = response.read()
        return json.loads(data)