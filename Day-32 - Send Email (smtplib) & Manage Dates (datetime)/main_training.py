# import smtplib
#
# my_email = "@gmail.com"
# password = ""
#
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )

# ------------------------------------------------------------------------ #

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# print(year)
#
# date_of_birth = dt.datetime(year=1990, month=6, day=5)
# print(date_of_birth)

# ------------------------------------------------------------------------ #

# import smtplib
# import datetime as dt
# import random
#
# now = dt.datetime.now()
# MY_EMAIL = "@gmail.com"
# MY_PASSWORD = ""
#
# with open("quotes.txt") as data_file:
#     all_quotes = data_file.readlines()
#     quote = random.choice(all_quotes)
#
# if now.weekday() == 3:
#     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#         connection.starttls()
#         connection.login(user=MY_EMAIL, password=MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs="@gmail.com",
#             msg=f"Subject:Your weekly motivational quote!\n\n{quote}"
#         )

