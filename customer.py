import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="#yr username",
        password="#yr password",
        database="#dbname",
        port=3306
    )

def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            emp_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            salary FLOAT,
            designation VARCHAR(100)
        )
    """)
    print(" Table 'employee' is ready (created if it didn't exist).\n")
    

def insert_employee(cursor, conn):
    name = input("Enter employee name: ")
    salary = input("Enter employee salary: ")
    designation = input("Enter employee designation: ")
    sql = "INSERT INTO employee (name, salary, designation) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, salary, designation))
    conn.commit()
    print(f" Employee '{name}' inserted successfully with ID {cursor.lastrowid}.\n")

def view_employees(cursor):
    cursor.execute("SELECT * FROM employee")
    rows = cursor.fetchall()
    if rows:
        print("\nEmployee Records:")
        print("ID | Name          | Salary   | Designation")
        print("---|---------------|----------|----------------")
        for row in rows:
            print(f"{row[0]:<2} | {row[1]:<13} | {row[2]:<8} | {row[3]}")
    else:
        print("  No employee records found.\n")

def main():
    conn = connect_db()
    cursor = conn.cursor()
    create_table(cursor)

    while True:
        print("\nChoose an option:")
        print("1. Insert new employee")
        print("2. List all employees")
        choice = input("Enter your choice: ")

        if choice == "1":
            insert_employee(cursor, conn)
        elif choice == "2":
            view_employees(cursor)
            break
        else:
            print(" Invalid choice. Please enter 1, 2, or 0.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
