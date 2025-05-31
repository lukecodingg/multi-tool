import os
import sys
import smtplib
import getpass

G = '\033[92m'
RESET = '\033[0m'

os.system('cls' if os.name == 'nt' else 'clear')

menu = f"""{G}
                                                                           
 _    _   _ _  _______   __  __ _   _ _   _____ ___ _____ ___   ___  _     
| |  | | | | |/ | ____| |  \/  | | | | | |_   _|_ _|_   _/ _ \ / _ \| |    
| |  | | | | ' /|  _|   | |\/| | | | | |   | |  | |  | || | | | | | | |    
| |__| |_| | . \| |___  | |  | | |_| | |___| |  | |  | || |_| | |_| | |___ 
|_____\___/|_|\_|_____| |_|  |_|\___/|_____|_| |___| |_| \___/ \___/|_____|
---------------------------------------------------------------------------
By lukecodingg for ebola 😻
{RESET}
"""

print(menu)

server_input = input(G + 'Mail Server (Gmail/Yahoo): ' + RESET).strip().lower()

if server_input == 'gmail':
    smtp_server = 'smtp.gmail.com'
    port = 587
elif server_input == 'yahoo':
    smtp_server = 'smtp.mail.yahoo.com'
    port = 587
else:
    print(G + 'Error - This script only works on Gmail or Yahoo.' + RESET)
    sys.exit()

email_user = input(G + 'Email: ' + RESET)
passwd = getpass.getpass(G + 'Password: ' + RESET)
email_to = input(G + '\nTo: ' + RESET)
subject = input(G + 'Subject: ' + RESET)
body = input(G + 'Message: ' + RESET)

try:
    total = int(input(G + 'Amount of Sendings: ' + RESET))
except ValueError:
    print(G + 'Error - Please enter a valid number.' + RESET)
    sys.exit()

try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()

    if port == 587:
        server.starttls()

    server.login(email_user, passwd)

    print(G + f'\n\n\n - Target : {email_to} -\n' + RESET)

    for i in range(1, total + 1):
        msg = f"From: {email_user}\nTo: {email_to}\nSubject: {subject}\n\n{body}"

        server.sendmail(email_user, email_to, msg)

        print(G + f'\rEmail Sent - {i}/{total}' + RESET, end='')
        sys.stdout.flush()

    server.quit()

    print(G + '\n\n- Process Terminated -' + RESET)

except KeyboardInterrupt:
    print(G + '\nError - Keyboard Interrupt' + RESET)
    sys.exit()

except smtplib.SMTPAuthenticationError:
    print(G + '\nError - Authentication failed. Check your email/password or allow less secure apps.' + RESET)
    sys.exit()

except Exception as e:
    print(G + f'\nUnexpected Error: {e}' + RESET)
    sys.exit()
