import smtplib
from tkinter import messagebox
import pandas
import random
import datetime as dt
import os

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("PASSWORD")

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
current_data = {
    "name": ["Aletta", "Mbali"],
    "email": ["bxaba@hotmail.com","bxaba@hotmail.com"],
    "year": [1962, 2026],
    "month": [4, 10],
    "day": [4, 16]
}
data = pandas.read_csv("birthdays.csv")
new_data = pandas.DataFrame(current_data)
data.update(new_data)
data.to_csv("birthdays.csv", index=False)

# 2. Check if today matches a birthday in the birthdays.csv
today_date = dt.datetime.now()
today = (today_date.month, today_date.day)
birthday_dict = {(value.month, value.day): value for key, value in data.iterrows()}

if today in birthday_dict:
    rand = random.randint(1, 3)
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    with open(f"letter_templates/letter_{rand}.txt") as file:
        letter = file.read()
        new_letter = letter.replace("[NAME]", birthday_dict.get(today).get("name"))

    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as server:
        server.starttls()
        server.login(user=my_email, password=password)
        server.sendmail(to_addrs=birthday_dict.get(today).get("email"), from_addr=my_email, msg=f"Subject:HAPPY BIRTHDAY\n\n{new_letter}")
        # print("Email sent!")
        # messagebox.showinfo("HAPPY BIRTHDAY", "Email sent!")




