# import requests
# from bs4 import BeautifulSoup as bs

# git_user = input('Enter the github username: ')
# url = 'https://github.com/' + git_user
# r = requests.get(url)
# soup = bs(r.content, 'html.parser')
# profile_image = soup.find('img', {'class': 'avatar'})['src']
# print(profile_image)

import psycopg2

conn_params = {
    'dbname': 'company',
    'user': 'postgres',
    'password': 'Bara3gahata#',
    'host': 'localhost',
    'port': 5432
}

try:

    conn = psycopg2.connect(**conn_params)
    print("connection successful using psycopg2")

    cursor = conn.cursor()

    cursor.executive("SELECT version();")
    print(cursor.fetchcone())

    cursor.close()
    conn.close()

except Exception as e:
    print(f"error connecting to postgreSQL using psycopg2: {e}")