import mariadb

# connection parameters
conn_params= {
    "user" : "example_user",
    "password" : "GHbe_Su3B8",
    "host" : "localhost",
    "database" : "test"
}

# Establish a connection
connection= mariadb.connect(**conn_params)

cursor= connection.cursor()

# Populate countries table  with some data
cursor.execute("INSERT INTO countries(name, country_code, capital) VALUES (?,?,?)",
               ("Germany", "GER", "Berlin"))

# retrieve data
cursor.execute("SELECT name, country_code, capital FROM countries")

# print content
row= cursor.fetchone()
print(*row, sep=' ')

# free resources
cursor.close()
connection.close()