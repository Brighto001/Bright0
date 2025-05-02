conn = psycopg2.connect(
    host="localhost",
    database="your_database_name",  # e.g., "library_db"
    user="your_username",           # e.g., "postgres"
    password="your_password"        # e.g., "admin"
)
