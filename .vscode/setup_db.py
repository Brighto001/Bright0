import psycopg2

conn = psycopg2.connect(
    dbname="library_db",  # replace with your DB name
    user="your_username",
    password="your_password",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    gender VARCHAR(10),
    age INT,
    phone_number VARCHAR(20),
    home_address TEXT,
    username VARCHAR(50) UNIQUE,
    password TEXT,
    profile_picture TEXT,
    is_librarian BOOLEAN DEFAULT FALSE,
    employment_id VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    book_name VARCHAR(255),
    author_name VARCHAR(255),
    year_of_publication INT,
    isbn VARCHAR(30),
    age_bracket VARCHAR(30),
    available BOOLEAN DEFAULT TRUE
);
""")

conn.commit()
print("✅ Tables created.")
cur.close()
conn.close()
