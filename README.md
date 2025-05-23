# 📊 Python Data Entry Using GUI
#### A simple Data Entry and Display application built with Python, Tkinter, and PostgreSQL. This tool enables users to enter employee data through a graphical interface, store it securely in a PostgreSQL database, and view all records in a paginated table.


 ## Features
 
- User-friendly data entry form with field validation

- Automatic age calculation based on Date of Birth

- Gender selection with icons

- Country code dropdown for phone numbers

- Data stored securely in a PostgreSQL database

- Paginated display of employee records

- Clean and modern Tkinter interface

- Easy setup and local execution

## How to Use
1. Clone the Repository
2.  Install Libraries
  ````
   pip install -r Requirement.txt
  ````
4.  Setup PostgreSQL
     - Open your PostgreSQL client and run:


  ````     
    CREATE DATABASE person_data;
  ````
     
   - Ensure your database connection details are updated in the script (e.g., host, port, username, password).
6. Run the Application
   
````
 python Program.py
 ````
     
   ### Usage
-  Open the GUI window.

-  Fill out the employee form with Name, Date of Birth, Gender, and Phone Number.

-  Click Submit to save the data to the database.

-  Click Display to view stored records in a paginated format.

