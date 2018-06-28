import getpass


user_credentials = ['begueradj', 'password']

def get_user_credentials():
   username = input('Username: ')
   password = getpass.getpass('Password: ')   
   return username, password

def check_user_credentials(user_credentials):
   username, password = get_user_credentials()
   return user_credentials[0] == username and user_credentials[1] == password


if __name__ == "__main__":
    login_attempts = 1
    correct_credentials = check_user_credentials(user_credentials)
    while not correct_credentials and login_attempts < 3:  
       print('\nWrong credentials, try again:')  
       correct_credentials = check_user_credentials(user_credentials)
       login_attempts += 1
    if correct_credentials:
       print('Welcome! Do whatever work you need here ...')
    else:
       print('Game over!')
