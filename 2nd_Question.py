import mysql.connector


conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='sqlconnect'
)


if conn.is_connected():

    cursor = conn.cursor()


    query = """ SELECT location_id, street_address, city, state_province, 'Canada' AS country_name FROM locations WHERE country_id = 'CA'  """


    cursor.execute(query)

 
    result = cursor.fetchall()
    for row in result:
        print(row)

 
    cursor.close()
    conn.close()
    print('Connection closed.')
else:
    print('Failed to connect to MySQL database')