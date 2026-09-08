# -------- USER INPUT --------

print("\nEnter your own values to predict sales")

store = int(input("Enter Store number: "))
dept = int(input("Enter Department number: "))

user_prediction = model.predict([[store, dept]])

print(f"Predicted Weekly Sales: {user_prediction[0]}")