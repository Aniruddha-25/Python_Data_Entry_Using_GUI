from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import date
from PIL import Image, ImageTk
from Program_Display import show_employee_table

Phone_Number = [
    "+91", "+93", "+355", "+213", "+376", "+244", "+54", "+374", "+61", "+43", "+994", "+973", "+880", "+375", "+32", "+501", "+229", "+975", "+591", "+387", "+267", "+55", "+673", "+359", "+226", "+257", "+855", "+237", "+1", "+238", "+236", "+235", "+56", "+86", "+57", "+269", "+242", "+243", "+506", "+385", "+53", "+357", "+420", "+45", "+253", "+1", "+593", "+20", "+503", "+240", "+291", "+372", "+268", "+251", "+679", "+358", "+33", "+241", "+220", "+995", "+49", "+233", "+30", "+1", "+502", "+224", "+245", "+592", "+509", "+504", "+36", "+354", "+62", "+98", "+964", "+353", "+972", "+39", "+225", "+1", "+81", "+962", "+7", "+254", "+686", "+850", "+82", "+965", "+996", "+856", "+371", "+961", "+266", "+231", "+218", "+423", "+370", "+352", "+261", "+265", "+60", "+960", "+223", "+356", "+692", "+222", "+230", "+52", "+691", "+373", "+377", "+976", "+382", "+212", "+258", "+95", "+264", "+674", "+977", "+31", "+64", "+505", "+227", "+234", "+47", "+968", "+92", "+680", "+507", "+675", "+595", "+51", "+63", "+48", "+351", "+974", "+40", "+7", "+250", "+1", "+1", "+1", "+685", "+378", "+239", "+966", "+221", "+381", "+248", "+232", "+65", "+421", "+386", "+677", "+252", "+27", "+211", "+34", "+94", "+249", "+597", "+46", "+41", "+963", "+886", "+992", "+255", "+66", "+228", "+676", "+1", "+216", "+90", "+993", "+688", "+256", "+380", "+971", "+44", "+1", "+598", "+998", "+678", "+58", "+84", "+967", "+260", "+263"
]

window = Tk()
window.title("Data Entry Page")
window.configure(bg="white")

bg_color = "white"
label_color = "#00b386"
entry_bg = "white"
entry_fg = "black"
entry_bd = 2

roboto_font = ("Roboto", 15, "bold")

def open_display():
    show_employee_table(window)


top_frame = Frame(window, bg="white")
top_frame.pack(fill=X, pady=(10, 0), padx=10)

display_button = Button(
    top_frame,
    text="Display",
    command=open_display,
    font=roboto_font,
    fg="white",
    bg="#00b386",
    activebackground="#00a373",
    activeforeground="white",
    width=12,
    relief="flat",
    bd=0,
    highlightthickness=0,
)
display_button.pack(side=RIGHT)


form_frame = Frame(window, bg=bg_color)
form_frame.pack(expand=True, pady=30, padx=30)

#   First Name
first_name_row = Frame(form_frame, bg=bg_color)
first_name_row.pack(anchor="w", pady=5, fill="x")
first_name_label = Label(
    first_name_row,
    text="First Name:",
    font=roboto_font,
    fg=label_color,
    bg=bg_color,
    width=14,
    anchor="w",
)
first_name_label.pack(side=LEFT, padx=(0, 10))
first_name_entry = Entry(
    first_name_row,
    font=roboto_font,
    bg=entry_bg,
    fg=entry_fg,
    insertbackground=entry_fg,
    width=20,
    bd=entry_bd,
    highlightthickness=2,
    highlightbackground=label_color,
    highlightcolor=label_color,
    relief="flat",
)
first_name_entry.pack(side=LEFT)

#   Last Name
last_name_row = Frame(form_frame, bg=bg_color)
last_name_row.pack(anchor="w", pady=5, fill="x")
last_name_label = Label(
    last_name_row,
    text="Last Name:",
    font=roboto_font,
    fg=label_color,
    bg=bg_color,
    width=14,
    anchor="w",
)
last_name_label.pack(side=LEFT, padx=(0, 10))
last_name_entry = Entry(
    last_name_row,
    font=roboto_font,
    bg=entry_bg,
    fg=entry_fg,
    insertbackground=entry_fg,
    width=20,
    bd=entry_bd,
    highlightthickness=2,
    highlightbackground=label_color,
    highlightcolor=label_color,
    relief="flat",
)
last_name_entry.pack(side=LEFT)

#   Date of Birth
dob_row = Frame(form_frame, bg=bg_color)
dob_row.pack(anchor="w", pady=5, fill="x")
dob_label = Label(
    dob_row,
    text="Date of Birth:",
    font=roboto_font,
    fg=label_color,
    bg=bg_color,
    width=14,
    anchor="w",
)
dob_label.pack(side=LEFT, padx=(0, 10))
today = date.today()
cal = DateEntry(
    dob_row,
    font=roboto_font,
    selectmode="day",
    year=today.year,
    month=today.month,
    day=today.day,
    date_pattern="yyyy-mm-dd",
    width=18,
    background=entry_bg,
    foreground=entry_fg,
    borderwidth=entry_bd,
)
cal.pack(side=LEFT)

#   Age
age_row = Frame(form_frame, bg=bg_color)
age_row.pack(anchor="w", pady=5, fill="x")
age_label = Label(
    age_row,
    text="Age:",
    font=roboto_font,
    fg=label_color,
    bg=bg_color,
    width=14,
    anchor="w",
)
age_label.pack(side=LEFT, padx=(0, 10))
age_var = StringVar()
age_entry = Entry(
    age_row,
    font=roboto_font,
    bg=entry_bg,
    fg=entry_fg,
    insertbackground=entry_fg,
    width=20,
    textvariable=age_var,
    state="readonly",
    bd=entry_bd,
    highlightthickness=2,
    highlightbackground=label_color,
    highlightcolor=label_color,
    relief="flat",
)
age_entry.pack(side=LEFT)

def calculate_age(event=None):
    selected_date = cal.get_date()
    str1_year = int(selected_date.strftime("%Y"))
    str1_month = int(selected_date.strftime("%m"))
    str1_date = int(selected_date.strftime("%d"))
    year_final = today.year - str1_year
    month_final = today.month - str1_month
    date_final = today.day - str1_date
    if month_final < 0 or (month_final == 0 and date_final < 0):
        year_final -= 1
    age_var.set(str(year_final if year_final > 0 else ""))

cal.bind("<<DateEntrySelected>>", calculate_age)
calculate_age()

#   Gender
gender_row = Frame(form_frame, bg=bg_color)
gender_row.pack(anchor="w", pady=5, fill="x")
gender_label = Label(
    gender_row,
    text="Gender:",
    font=roboto_font,
    fg=label_color,
    bg=bg_color,
    width=14,
    anchor="w",
)
gender_label.pack(side=LEFT, padx=(0, 10))

size = 14
ICON_SIZE = (size * 6, size * 6)
male_img = Image.open("Data/Gender/male.png").resize(ICON_SIZE, Image.LANCZOS)
female_img = Image.open("Data/Gender/female.png").resize(ICON_SIZE, Image.LANCZOS)
trans_img = Image.open("Data/Gender/transgender.png").resize(ICON_SIZE, Image.LANCZOS)
male_image = ImageTk.PhotoImage(male_img)
female_image = ImageTk.PhotoImage(female_img)
trans_image = ImageTk.PhotoImage(trans_img)

gender_var = StringVar(value="Male")
gender_radio_frame = Frame(gender_row, bg=bg_color)
gender_radio_frame.pack(side=LEFT)

radio_button1 = Radiobutton(
    gender_radio_frame,
    text="   Male",
    image=male_image,
    variable=gender_var,
    value="Male",
    compound="left",
    font=roboto_font,
    fg="#1E90FF",
    bg="white",
    selectcolor="white",
    activebackground="white",
    activeforeground="#0047AB",
    borderwidth=0,
    highlightthickness=0,
)
radio_button1.image = male_image
radio_button1.pack(side=LEFT, padx=10)

radio_button2 = Radiobutton(
    gender_radio_frame,
    text="   Female",
    image=female_image,
    variable=gender_var,
    value="Female",
    compound="left",
    font=roboto_font,
    fg="#FF4191",
    bg="white",
    selectcolor="white",
    activebackground="white",
    activeforeground="#C21E56",
    borderwidth=0,
    highlightthickness=0,
)
radio_button2.image = female_image
radio_button2.pack(side=LEFT, padx=10)

radio_button3 = Radiobutton(
    gender_radio_frame,
    text="   TransGender",
    image=trans_image,
    variable=gender_var,
    value="TransGender",
    compound="left",
    font=roboto_font,
    fg="#DA70D6",
    bg="white",
    selectcolor="white",
    activebackground="white",
    activeforeground="#FF10F0",
    borderwidth=0,
    highlightthickness=0,
)
radio_button3.image = trans_image
radio_button3.pack(side=LEFT, padx=10)

#   Phone no
phone_row = Frame(form_frame, bg=bg_color)
phone_row.pack(anchor="w", pady=5, fill="x")

phone_label = Label(
    phone_row,
    text="Mobile Number:",
    font=roboto_font,
    fg=label_color,
    bg=bg_color,
    width=14,
    anchor="w",
)
phone_label.pack(side=LEFT, padx=(0, 10))

country_var = StringVar(window)
country_choices = Phone_Number
country_var.set(country_choices[0])

country_menu = OptionMenu(phone_row, country_var, *country_choices)
country_menu.config(
    font=roboto_font, bg="white", fg="black", highlightthickness=0, width=6
)
country_menu.pack(side=LEFT, padx=(0, 10))

number_entry = Entry(
    phone_row,
    font=roboto_font,
    bg=entry_bg,
    fg=entry_fg,
    insertbackground=entry_fg,
    width=16,
    bd=entry_bd,
    highlightthickness=2,
    highlightbackground=label_color,
    highlightcolor=label_color,
    relief="flat",
)
number_entry.pack(side=LEFT)

#    Submit Button
def submit():
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    dob = cal.get_date().strftime("%Y-%m-%d")  
    age = age_var.get()
    gender = gender_var.get()
    country_code = country_var.get()
    mobile_number = number_entry.get()
    phone_no = f"{country_code}{mobile_number}"

    from Program_Database_Entry import insert_employee
    success = insert_employee(firstname, lastname, dob, age, phone_no)

    if success:
        messagebox.showinfo("Success", "Data inserted successfully!")
        first_name_entry.delete(0, END)
        last_name_entry.delete(0, END)
        cal.set_date(date.today())
        age_var.set("")
        gender_var.set("Male")
        country_var.set(Phone_Number[0])
        number_entry.delete(0, END)
    else:
        messagebox.showerror("Error", "Failed to insert data.")

submit_button = Button(
    form_frame,
    text="Submit",
    command=submit,
    font=roboto_font,
    fg="white",
    bg="#00b386",
    activebackground="#00a373",
    activeforeground="white",
    width=12,
    relief="flat",
    bd=0,
    highlightthickness=0,
)
submit_button.pack(pady=30)

window.mainloop()
