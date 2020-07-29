import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

GMAIL_SMTP = 'smtp.gmail.com'
GMAIL_IMAP = 'imap.gmail.com'


class Mail:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def send_message(
        self,
        subject,
        recipients,
        message,
        ):

        # send message

        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP(GMAIL_SMTP, 587)

        # identify ourselves to smtp gmail client

        ms.ehlo()

        # secure our email with tls encryption

        ms.starttls()

        # re-identify ourselves as an encrypted connection

        ms.ehlo()

        ms.login(self.login, self.password)
        ms.sendmail(self.login, ms, msg.as_string())

        ms.quit()

        # send end

    def receive_message(self, header):

        # receive

        mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select('inbox')
        criterion = ('(HEADER Subject "%s")'
                     % header if header else 'ALL')
        (result, data) = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        (result, data) = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()

        # end receive


if __name__ == '__main__':
    mail = Mail('login@gmail.com', 'qwerty')

    mail.send_message('Subject', ['vasya@email.com', 'petya@email.com'],
                      'Message')

    mail.receive_message(header=None)
