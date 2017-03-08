#!/usr/bin/env python

import csv
import send_email
import smtplib
import sys
import config
import time

recruiter_company = []
recruiter_names = []
recruiter_emails = []

SUBJECT = "Summer Internship Opportunity at %s - Software Development Domain"
SENDER = "%s <%s>" % (config.FROM_NAME, config.FROM_EMAIL)

def get_body_content():
    try:
        return open(config.BODY_FILENAME,"r").read()
    except Exception, e:
        print e
        sys.exit(0)
	

def read_csv_file():
    first_line = True
    reader = csv.reader(open(config.CSV_FILENAME, 'r'), delimiter=',')
    for row in reader:
        if first_line:
            first_line = False
            continue
    recruiter_company.append(row[config.COMPANY_NAME_COLUMN_INDEX])
    recruiter_names.append(row[config.RECRUITER_NAME_COLUMN_INDEX])
    recruiter_emails.append(row[config.EMAIL_COLUMN_INDEX])

def login_smtp_server():
    try:
        smtp = smtplib.SMTP(config.SMTP_HOST + ":"+ config.SMTP_PORT)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(config.FROM_EMAIL, config.EMAIL_PASSWORD)
        return smtp
    except Exception, e:
        print e
        sys.exit(0)
    


def send_emails():
    current_row = 0
    body_content = get_body_content()
    smtp = login_smtp_server()
    read_csv_file()
    for email in recruiter_emails:
        new_body_content = body_content % (recruiter_names[current_row],recruiter_company[current_row] )
        new_subject =  SUBJECT  % (recruiter_company[current_row])
        send_email.send_mail(SENDER,email,new_subject,new_body_content,smtp)
        current_row += 1
        time.sleep(0.5)

send_emails()