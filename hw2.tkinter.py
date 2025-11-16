import tkinter as tk
from tkinter import messagebox
from datetime import date

# Function to calculate age
def calculate_age():
    try:
        # Get user input and validate
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        # Validate date
        dob = date(year, month, day)  # Will raise ValueError if invalid date
        today = date.today()

        # Calculate age
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        if age < 0:
            messagebox.showerror("Error", "Date of birth cannot be in the future.")
        else:
            messagebox.showinfo("Age Result", f"Your current age is: {age} years")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid date (DD MM YYYY).")

# Create main window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x250")
root.resizable(False, False)

# Labels and Entry fields
tk.Label(root, text="Enter Date of Birth", font=("Arial", 14, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="Day:").grid(row=0, column=0, padx=5, pady=5)
day_entry = tk.Entry(frame, width=5)
day_entry.grid(row=0, column=1)

tk.Label(frame, text="Month:").grid(row=1, column=0, padx=5, pady=5)
month_entry = tk.Entry(frame, width=5)
month_entry.grid(row=1, column=1)

tk.Label(frame, text="Year:").grid(row=2, column=0, padx=5, pady=5)
year_entry = tk.Entry(frame, width=5)
year_entry.grid(row=2, column=1)

# Calculate Button
tk.Button(root, text="Calculate Age", command=calculate_age, bg="blue", fg="white").pack(pady=15)

# Run the application
root.mainloop()