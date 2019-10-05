import sqlite3
from sqlite3 import Error
from tkinter import *
from PIL import Image, ImageTk
import card_utils
import card_type
import card_issuer
# connect to sql database

#card_num = '4813720000219479'
card_num = '5379151000436090'

card_utils.format_card(card_num)
chk = card_utils.validate_card(card_num)

if not chk:
    import sys
    sys.exit("Invalid Card number")

card_type = card_type.identify_card_type(card_num)
issuer_details = card_issuer.identify_card_issuer(card_num)


def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

# create a new table
def create_table(conn, create_table_sql):

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = r"database.db"

    sql_create_myCC_table = """CREATE TABLE IF NOT EXISTS card_metadata (
                                            CCID integer PRIMARY KEY,
                                            Card_Name text,
                                            Card_Type text,
                                            utility text,
                                            Offer text,
                                            discount float
                                        );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create myCC table
        conn.execute("""DROP TABLE card_metadata""")
        create_table(conn, sql_create_myCC_table)
        
        #Hardcoding the values for the prototype. Would love to fully automate this portion.
        #This will involve web scrolling for all the offers for the banks..
        conn.execute("""INSERT INTO card_metadata VALUES(1, 'Bank of the West', 'Credit Card', 'Medicine', '5% off', 0.05)""")
        conn.execute("""INSERT INTO card_metadata VALUES(2, 'Bank of the West', 'Credit Card', 'Clothes', '10% off', 0.10)""")
        conn.execute("""INSERT INTO card_metadata VALUES(3, 'Bank of the West', 'Credit Card', 'Grocery', '15% off', 0.15)""")
        conn.execute("""INSERT INTO card_metadata VALUES(4, 'Bank of the West', 'Credit Card', 'Electronics', '30% off', 0.30)""")
        
        conn.execute("""INSERT INTO card_metadata VALUES(5, 'Bank of America', 'Credit Card', 'Medicine', '3% off', 0.03)""")
        conn.execute("""INSERT INTO card_metadata VALUES(6, 'Chase Bank', 'Credit Card', 'Clothes', '5% off', 0.05)""")
        conn.execute("""INSERT INTO card_metadata VALUES(7, 'Bank of America', 'Credit Card', 'Grocery', '10% off', 0.10)""")
        conn.execute("""INSERT INTO card_metadata VALUES(8, 'Chase Bank', 'Credit Card', 'Electronics', '20% off', 0.20)""")
    else:
        print("Error! cannot create the database connection.")

    rows = conn.execute("""SELECT distinct utility FROM card_metadata""")
    data = [i[0] for i in rows.fetchall()]
    return data, conn


OPTIONS, conn = main()

def fetch_data():
  print ("value is:" + variable.get())
  r = conn.execute("""SELECT Card_Name, Card_Type, Offer FROM card_metadata WHERE utility = '{}' order by discount desc""".format(variable.get()))
  data = []
  data.append(list(map(lambda x: x[0], r.description)))
  for row in r.fetchall():
    data.append(row) 

  print_data(data)

master = Tk()
variable = StringVar(master)
variable.set(OPTIONS[0]) # default value
master.geometry("300x300")

master.configure(background = 'light blue')

space = Label(text="   ", pady=5, background = 'light blue')
space.pack()
image = Image.open("bank_of_the_west.png")
photo = ImageTk.PhotoImage(image)
label = Label(image=photo, pady=5)
label.image = photo # keep a reference!
label.pack()
instruction = Label(text="What kind of purchase are you making today?",pady = 10, background = 'light blue')
instruction.pack()

w = OptionMenu(master, variable, *OPTIONS)
w.pack()
sub = Frame(master, pady=20, background = 'light blue')
button = Button(master, text="search", command=fetch_data)
button.pack()
sub.pack()


def print_data(data):
  master.geometry("500x500")
  #height = 5
  #width = 5
  try:
      for widget in sub.winfo_children():
         widget.destroy()
  except:
      pass
  frame = Frame(sub,background = 'grey', highlightthickness = 4, width = 300)
  frame.pack()
  for i ,row in enumerate(data): #Rows
      for j,d in enumerate(row): #Columns
          b = Label(frame, text="{}".format(d), relief=RIDGE, borderwidth=4, background = 'white')
          b.grid(row=i, column=j, padx = 10, pady = 3)
mainloop()

#if __name__ == "__main__":
#    main()
