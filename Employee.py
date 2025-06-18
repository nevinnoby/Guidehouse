employees = {}

for _ in range(5):
    while True:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employees:
            print("Error: Employee ID already exists. Please enter a different ID.")
            continue
        break
   
    name = input("Enter Employee Name: ")
    salary = float(input("Enter Salary: "))
    designation = input("Enter Designation: ")  
    employees[emp_id] = {
        "name": name,
        "salary": salary,
        "designation": designation
    }
def get_salary(item):
    return item[1]["salary"]
sorted_items = sorted(employees.items(), key=get_salary)
sorted_employees = dict(sorted_items)
last_key = list(sorted_employees.keys())[-1]
sorted_employees.pop(last_key)
print("Employee Details (Sorted by Salary):\n")
for emp_id, info in sorted_employees.items():
    print(f"ID: {emp_id}, Name: {info['name']}, Salary: {info['salary']}, Designation: {info['designation']}")