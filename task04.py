import smtplib
# help(smtplib)

with smtplib.SMTP('smtp.gmail.com', 587) as smtp_object:
    # smtp_object= smtplib.SMTP('localhost')

    smtp_object.starttls()
    pas = input("Пароль? ")
    smtp_object.login('go.noone2@gmail.com', pas)

    # help(smtp_object.sendmail)
    smtp_object.sendmail(from_addr="go.noone2@gmail.com", to_addrs="el.piankova@gmail.com", msg="It's works!")

    # smtp_object.sendmail(from_addr="your_test_login@gmail.com",to_addrs=["el.piankova@gmail.com", "smilly86@gmail.com"],msg="It's works!")
    # smtp_object.quit()
