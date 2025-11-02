import pandas as pd

data_file = "employees.csv"

# Load existing data or create a new one
try:
    df = pd.read_csv(data_file)
except FileNotFoundError:
    df = pd.DataFrame(columns=["ID", "Name", "Role", "Salary"])

while True:
    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Delete Employee")
    print("4. Save & Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = input("Enter ID: ")
        name = input("Enter Name: ")
        role = input("Enter Role: ")
        salary = input("Enter Salary: ")
        new_data = pd.DataFrame([[emp_id, name, role, salary]], columns=df.columns)
        df = pd.concat([df, new_data], ignore_index=True)
        print("Employee added successfully!")

    elif choice == "2":
        print("\nEmployee List:")
        print(df if not df.empty else "No data found!")

    elif choice == "3":
        emp_id = input("Enter ID to delete: ")
        df = df[df["ID"] != emp_id]
        print("Employee deleted if ID existed.")

    elif choice == "4":
        df.to_csv(data_file, index=False)
        print("Data saved. Exiting...")
        break

    else:
        print("Invalid choice. Try again.")
