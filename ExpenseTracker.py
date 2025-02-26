import json
from datetime import datetime

def load_data():
    try:
        with open('expenses.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(data):
    with open('expenses.json', 'w') as file:
        json.dump(data, file)

def add_transaction(data, amount, category, transaction_type):
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    transaction = {"amount": amount, "category": category, "type": transaction_type, "date": date}
    data.append(transaction)
    save_data(data)

def generate_report(data):
    categories = {}
    for transaction in data:
        if transaction["category"] not in categories:
            categories[transaction["category"]] = 0
        if transaction["type"] == "income":
            categories[transaction["category"]] += transaction["amount"]
        elif transaction["type"] == "expense":
            categories[transaction["category"]] -= transaction["amount"]
    
    print("\nExpense Report:")
    for category, total in categories.items():
        print(f"{category}: {total:.2f}")

def main():
    data = load_data()

    while True:
        print("\nOptions:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Generate Report")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            category = input("Enter category (e.g., Salary, Freelance): ")
            add_transaction(data, amount, category, "income")
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            category = input("Enter category (e.g., Food, Rent): ")
            add_transaction(data, amount, category, "expense")
        elif choice == '3':
            generate_report(data)
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
