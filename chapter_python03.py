# 함수, 클래스

person_a_numbers = [ 70, 85, 90, 60 ]
person_b_numbers = [ 30, 75, 30, 90 ]
person_c_numbers = [ 20, 55, 70, 60 ]

# total = 0
# for n in numbers:
#     total += n

# avg = total / len(numbers)

# avg = sum(person_a_numbers) / len(person_a_numbers)
# print(f"avg: {avg}")

# avg = sum(person_b_numbers) / len(person_b_numbers)
# print(f"avg: {avg}")

# avg = sum(person_c_numbers) / len(person_c_numbers)
# print(f"avg: {avg}")

# def calc_avg(numbers):
#     avg = sum(numbers) /len(numbers)
#     print(f"avg: {avg}")
#     return avg

# person_numbers_list = [person_a_numbers, person_b_numbers, person_c_numbers]

# for numbers in person_numbers_list:
#     calc_avg(numbers)

# Class

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount}를 입금했습니다. 현재 잔액: {self.balance}원")


    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount}를 출금했습니다. 현재 잔액: {self.balance}원")
        
        else:
            print(f"잔액이 부족합니다. 현재 잔액: {self.balance}원")

person_a_account = BankAccount("123-456-789", 10000)
print(f"account_number: {person_a_account.account_number}")

person_a_account.deposit(5000)
person_a_account.withdraw(12000)
person_a_account.withdraw(5000)

print(f"account_number: {person_a_account.account_number}")
print(f"balance: {person_a_account.account_number}")

print("*"*30)

person_b_account = BankAccount("789-123-456", 5000)

print(f"account_number: {person_b_account.account_number}")
print(f"balance: {person_b_account.account_number}")

person_b_account.deposit(5000)
person_b_account.withdraw(12000)
person_b_account.withdraw(5000)