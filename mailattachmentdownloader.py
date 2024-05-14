import email
import imaplib
import os

# Directory where attachments will be saved
detach_dir = '/home/bager/Desktop/'

# Gmail account credentials
user = "birkullanicix@gmail.com"
pwd = "wrrt pxqr pyib nzcs"

# Connecting to the Gmail IMAP server
m = imaplib.IMAP4_SSL("imap.gmail.com", 993)

# Login to the Gmail account
m.login(user, pwd)

# Select the INBOX mailbox
m.select("INBOX")

# Search for unread emails with attachments
resp, items = m.search(None, 'UNSEEN', 'X-GM-RAW', 'has:attachment')

# Getting the mail IDs
items = items[0].split()

# Loop through the emails
for email_id in items:
    # Fetching the email
    resp, data = m.fetch(email_id, "(RFC822)")
    email_body = data[0][1]

    # Parsing the email content to get a mail object
    mail = email.message_from_bytes(email_body)

    # Check if any attachments exist
    if mail.get_content_maintype() != 'multipart':
        continue

    # Loop through the parts of the email
    for part in mail.walk():
        # Check if the part is an attachment
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue

        # Check if the attachment is an Excel file
        if part.get_filename().endswith('.xls') or part.get_filename().endswith('.xlsx'):
            filename = part.get_filename()

            # Construct the file path to save the attachment
            att_path = os.path.join(detach_dir, filename)

            # Check if the file already exists
            if not os.path.isfile(att_path):
                # Write the attachment to the file
                with open(att_path, 'wb') as fp:
                    fp.write(part.get_payload(decode=True))

# Close the mailbox
m.close()

# Logout from the Gmail account
m.logout()
