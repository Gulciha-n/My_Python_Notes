#exp1

def main():
    str1 = 'one two three four'      
    str2 = '10:20:30:40:50'
    str3 = 'a/b/c/d/e/f'

    display_tokens(str1, ' ')
    print()
    display_tokens(str2, ':')
    print()
    display_tokens(str3, '/')
def display_tokens(data, delimiter):
    tokens = data.split(delimiter)
    for item in tokens:
        print(f'Token: {item}')
if __name__ == '__main__':
    main()





#exp2

class BankAccount:                   
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print('Error: Insufficient funds')

    def get_balance(self):
        return self._balance
BankAccount()








'''his_age = 20
his_height = 1.76
his_hair_color = "brunette"
his_hometown = "Iran"
where_he_lives = "Turkey"

print("I am", his_age,"years old,",his_height,"tall",his_hair_color,"guy from",his_hometown,"but I currently live in",where_he_lives)

print("What about you? Tell me about yourself.")'''


