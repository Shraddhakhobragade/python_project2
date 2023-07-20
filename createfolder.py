import tkinter as tk
import sqlite3
from tkinter import filedialog
import os
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="shraddha@2000",
  database="filepathsave"
)



def create_abc_folder():                      # Function to create the folder and save the path in the database
    folder_path = filedialog.askdirectory()   # Open file dialog to select the folder path

                                                   
    folder_name = "abc"                         # Create the folder
    full_path = folder_path + "/" + folder_name
    try:
        os.mkdir(full_path)
        status_label.config(text="Folder created successfully!")
    except FileExistsError:
        status_label.config(text="Folder already exists!")
        os.startfile(full_path)                 # Open the existing folder in the file explorer

    
    mycursor = mydb.cursor()                        # Save the path in the database
    mycursor.execute("INSERT INTO Pathsave (path) VALUES (%s)", (folder_path,))
    mydb.commit()
    mydb.close()



# Create the GUI window

window = tk.Tk()
window.title("Folder Creator")

# Create a button to select the folder path and create the "abc" folder
create_abc_folder_btn = tk.Button(window, text="ABC Folder", command=create_abc_folder)
create_abc_folder_btn.pack(pady=10)

# Create a label to display the status
status_label = tk.Label(window, text="")
status_label.pack()

# Run the GUI application
window.mainloop()
