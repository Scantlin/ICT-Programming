import tkinter as tk
from tkinter import ttk

def main():
    # Create main window
    root = tk.Tk()
    root.title("Tkinter in Codespace")
    root.geometry("400x300")
    
    # Add a label
    label = ttk.Label(root, text="Hello from Codespace!", font=('Arial', 14))
    label.pack(pady=20)
    
    # Add a button
    button = ttk.Button(
        root, 
        text="Click Me", 
        command=lambda: label.config(text="Button clicked!")
    )
    button.pack(pady=10)
    
    # Add an exit button
    exit_button = ttk.Button(
        root,
        text="Exit",
        command=root.destroy
    )
    exit_button.pack(pady=10)
    
    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()