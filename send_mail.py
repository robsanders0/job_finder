import smtplib

sent_from = 'robertosanders03@gmail.com'
to = ['morganmcopeland@gmail.com','mahopaccrazy@yahoo.com']
subject = 'Testing Testing 123'
body = 'Testing my ability to send an email thru Python'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

gmail_user = 'robertosanders03@gmail.com'
gmail_password = 'Doustraat1963'

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()
    print('Sent!')
except:
    print('error')