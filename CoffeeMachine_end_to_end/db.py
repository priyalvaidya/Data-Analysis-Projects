import mysql.connector

def connect_to_mysql():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Prajuav@03112001"
        )
        print("Connected to MySQL successfully")
        return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def create_database(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS coffee_machine")
        print("Database 'coffee_machine' created successfully")
    except mysql.connector.Error as e:
        print(f"Error creating database 'coffee_machine': {e}")

def create_orders_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS coffee_machine.orders (
                id INT AUTO_INCREMENT PRIMARY KEY,
                order_date VARCHAR(10),
                customer_name VARCHAR(255),
                drink_choice VARCHAR(255),
                amount_$ DECIMAL(10, 2)
            )
        """)
        print("Orders table created successfully")
    except mysql.connector.Error as e:
        print(f"Error creating orders table: {e}")

def insert_data(conn, order_date, name,  drink_choice, amount):
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO coffee_machine.orders (order_date, customer_name, drink_choice, amount_$) VALUES (%s, %s, %s, %s)"
        val = (order_date, name, drink_choice, amount)
        cursor.execute(sql, val)
        conn.commit()
        print("Data inserted successfully")
    except mysql.connector.Error as e:
        print(f"Error inserting data into MySQL: {e}")

def close_connection(conn):
    conn.close()
    print("MySQL connection closed")

if __name__ == "__main__":
    conn = connect_to_mysql()
    if conn:
        create_database(conn)
        create_orders_table(conn)
        close_connection(conn)
