import random
import string
import tkinter as tk

def generate_password(length):
    # Define a string containing all the possible characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Use the random.choices() function to randomly select characters from the characters string
    password = "".join(random.choices(characters, k=length))
    # Return the generated password
    return password

def generate_password_gui():
    # Create a new window
    window = tk.Tk()
    window.title("Password Generator by Noel Blancs")
    
    # Create a label and an entry box for the password length
    length_label = tk.Label(window, text="Password Length:")
    length_label.pack()
    length_entry = tk.Entry(window)
    length_entry.pack()
    
    # Create a label to display the generated password
    password_label = tk.Label(window, text="", font=("Arial",15))
    password_label.pack()
    
    # Create a button to generate the password
    def generate_password_action():
        length = int(length_entry.get())
        password = generate_password(length)
        password_label.config(text="Generated Password: " + password)
    
    generate_button = tk.Button(window, text="Generate Password", command=generate_password_action)
    generate_button.pack()
    
    # Start the GUI main loop
    window.mainloop()

generate_password_gui()