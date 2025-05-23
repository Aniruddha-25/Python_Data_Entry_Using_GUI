import psycopg2
from tkinter import *
from tkinter import ttk
from datetime import datetime

PAGE_SIZE = 20

def fetch_data():
    conn = psycopg2.connect(
        database="person_data",
        user="postgres",
        password="jaihind",
        host="127.0.0.1",
        port="5432",
    )
    cur = conn.cursor()
    cur.execute("SELECT id, first_name, last_name, d_o_b, age, phone_no FROM employees")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def show_employee_table(parent=None):
    if parent is None:
        window = Tk()
    else:
        window = Toplevel(parent)
    window.title("Employee Data")
    window.configure(bg="white")

    columns = ("ID", "First Name", "Last Name", "DOB", "Age", "Phone No")
    style = ttk.Style()
    style.theme_use("default")
    style.configure(
        "Treeview.Heading",
        background="#00b386",
        foreground="white",
        font=("Roboto", 15, "bold"),
    )
    style.configure(
        "Treeview",
        font=("Roboto", 15, "bold"),
        rowheight=44,
        background="white",
        fieldbackground="white",
        borderwidth=0,
        relief="flat",
    )
    style.map(
        "Treeview",
        background=[("selected", "#b3ffd9")],
        foreground=[("selected", "black")]
    )

    tree = ttk.Treeview(window, columns=columns, show="headings", selectmode="browse")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=180, minwidth=120, stretch=True)
    tree.pack(fill=BOTH, expand=True, padx=20, pady=(20, 0))

    nav_frame = Frame(window, bg="white")
    nav_frame.pack(fill=X, pady=(0, 20))
    page_var = StringVar()
    page_label = Label(nav_frame, text="", font=("Arial", 14, "bold"), bg="white", fg="#00b386")
    page_label.pack(side=LEFT, padx=10)
    def goto_page(event=None):
        try:
            page = int(page_var.get())
            total_pages = max(1, (len(all_rows) + PAGE_SIZE - 1) // PAGE_SIZE)
            if 1 <= page <= total_pages:
                update_table(page)
        except ValueError:
            pass
    page_entry = Entry(nav_frame, textvariable=page_var, width=3, font=("Arial", 14, "bold"), justify="center")
    page_entry.pack(side=LEFT)
    page_entry.bind("<Return>", goto_page)
    def first_page(): update_table(1)
    def last_page(): update_table((len(all_rows) + PAGE_SIZE - 1) // PAGE_SIZE)
    def prev_page():
        p = int(page_var.get())
        if p > 1: update_table(p - 1)
    def next_page():
        p = int(page_var.get())
        total_pages = max(1, (len(all_rows) + PAGE_SIZE - 1) // PAGE_SIZE)
        if p < total_pages: update_table(p + 1)
    Button(nav_frame, text="<<", command=first_page, font=("Arial", 14, "bold"), width=3, bg="#e0e0e0", fg="#00b386", relief="flat").pack(side=LEFT, padx=2)
    Button(nav_frame, text="<", command=prev_page, font=("Arial", 14, "bold"), width=3, bg="#e0e0e0", fg="#00b386", relief="flat").pack(side=LEFT, padx=2)
    Button(nav_frame, text=">", command=next_page, font=("Arial", 14, "bold"), width=3, bg="#e0e0e0", fg="#00b386", relief="flat").pack(side=LEFT, padx=2)
    Button(nav_frame, text=">>", command=last_page, font=("Arial", 14, "bold"), width=3, bg="#e0e0e0", fg="#00b386", relief="flat").pack(side=LEFT, padx=2)

    all_rows = fetch_data()

    def update_table(page):
        tree.delete(*tree.get_children())
        start = (page - 1) * PAGE_SIZE
        end = start + PAGE_SIZE
        for row in all_rows[start:end]:
           
            try:
                dob_obj = datetime.strptime(row[3], "%Y-%m-%d")
                dob_str = dob_obj.strftime("%d %B %Y")
            except Exception:
                dob_str = row[3]
            display_row = list(row)
            display_row[3] = dob_str
            tree.insert("", END, values=display_row)
        total_pages = max(1, (len(all_rows) + PAGE_SIZE - 1) // PAGE_SIZE)
        page_label.config(text=f"Page {page} of {total_pages}")
        page_var.set(str(page))

    page_var.set("1")
    update_table(1)
    window.mainloop()


if __name__ == "__main__":
    show_employee_table()
