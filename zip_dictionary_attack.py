import subprocess as sp
import sys

def main():
    zip_file_name = sys.argv[1]
    word_list_file_name = sys.argv[2]

    passwords = []
    passwords = get_password_list(word_list_file_name)
    password_index = try_passwords(passwords, zip_file_name)

    if password_index == -1:
        print("The password was not in the word_list")
    else:
        print("Passwords is", passwords[password_index])
    

def get_password_list(word_list_file_name):
    passwords = []
    with open(word_list_file_name, "r") as word_list:
        for word in word_list:
            passwords.append(word)

    return passwords


def try_passwords(passwords, zip_file_name):
    password_index = -1

    for i in range(len(passwords)):
        if extract_zip(passwords[i], zip_file_name):
            password_index = i
            break

    return password_index


def extract_zip(password, zip_file_name):
    
    correct = False

    password = password.rstrip()
    p = sp.run(['unzip','-o', '-P', password, zip_file_name], capture_output=True)

    if p.returncode == 0:
        correct = True

    return correct


main()
