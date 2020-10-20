
# mengimpor modul yang penting /importing important modules
import random 
import numpy

class Account:
    depositFrequency = 4
    transactionMax = 40000
   # Buat objek Akun. Mode untuk /Construct an Account object. Mode to
    def __init__(self, id, balance = 0, withdrawalDailyMax = 50000,
    withdrawalFrequency=3,withdrwalTransactionMax=20000, depoDailyMax = 150000, 
    depositFrequency = 4, depoTransactionMax = 40000):

# fungsi untuk Penarikan /a function to withdraw
    def withdraw(self, amount):
    # di sini jika Anda menarik perubahan saldo baru Anda /here if you withdraw your new balance changes
        self.balance -= amount
#  a function to depoit
    def deposit(self, amount):
    # setoran sama dengan jumlah yang disimpan + saldo yang ada  /deposit equals amount being deposited+existing balance
        self.balance += amount 

# fungsi untuk berhenti datang nanti /a function to quit coming later

def main():
    # buat akun /Creating accounts 
    accounts = []
    for i in range(1000, 9999): 
        account = Account(i, 0)
        accounts.append(account)    
    # proses di atm /ATM Processes
    while True:
       # Membaca id dari pengguna yang mewakili pin rahasia untuk keamanan /Reading id from user which represents a secret pin for security
        id = int(input("\n Please Enter Your account pin: "))
       # Ulangi sampai id berlaku antara 1000 dan 9999 secara acak (di mana modul Acak masuk) /Loop till id is valid between 1000 and 9999 in a randomised manner(where the Random module come in)
        while id < 1000 or id > 9999:
            id = int(input("\nInvalid Pin.. Re-enter your Pin please: "))

        # sementara pinnya benar (Id adalah pin di sini) /while the pin is right(Id is pin here)
        while True:
            # Menu pencetakan /Printing menu
            print("\n1 - Balance/saldo \t 2 - Withdraw/penarikan \t 3 - Deposit/setoran \t 4 - Quit ")

            # Pilihan bacaan /Reading selection
            selection = int(input("\nEnter your selection: "))
            # Mendapatkan objek akun /Getting account object
            for acc in accounts:
                # Comparing account id
                if acc.getId() == id:
                    accountObj = acc
                    break
                   # Lihat Saldo /View Balance

            if selection == 1:
               # Mencetak saldo /Printing balance
                print("Your Balance is:" +  str(accountObj.getBalance())+ " ")
             # Withdraw
            elif selection == 2:
                print("Your Balance is:" + str(accountObj.getBalance()))
               # Jumlah bacaan /Reading amount
                amt = float(input("\nPlease Enter amount to withdraw: "))
                ver_withdraw = input("Is this the correct amount, Yes or No ? " + str(amt) + " ")
    
                if ver_withdraw == "Yes":
                    print("Verify withdraw")
                else:
                    break

                if amt < accountObj.getBalance():
                    print("Your Balance is:" +  str(accountObj.getBalance())+ " ")
                    # Metode penarikan panggilan /Calling withdraw method
                    accountObj.withdraw(amt)
                    # Mencetak saldo diperbarui /Printing updated balance
                    print("\nUpdated Balance: " + str(accountObj.getBalance()) + " \n")
                    print("you have only 2 withdrawal times remaining")
                else:
                    print("\nYou're balance is less than withdrawl amount: " + str(accountObj.getBalance()) + " \n")
                    print("\nPlease make a deposit.")
             # Deposit
            elif selection == 3:
                
                print("Your Balance is:" +  str(accountObj.getBalance())+ " ")
                # Jumlah bacaan /Reading amount
                amt = float(input("\nEnter amount to deposit: "))
                ver_deposit = input("Is this the correct amount, Yes, or No ? " + str(amt) + " ")
                if ver_deposit == "Yes":
                    # Memanggil metode setoran /Calling deposit method
                    accountObj.deposit(amt)
                    # Mencetak saldo diperbarui /Printing updated balance
                    print("\nUpdated Balance: " + str(accountObj.getBalance()) + " \n")
                    print("you have only 3 deposit times remaining")
                else:
                    break
            # keluar /QUIT
            elif selection == 4:
                check = input("Are you sure you want to quit?, Yes, or No:")
                if check == "Yes":
                    print("\nYour Transaction is complete")
                    print("Transaction number: ", random.randint
                            (10000, 1000000))
                    print("Thanks for choosing us as your bank")
                else:
                    break
              
 
           # pilihan lainnya /Any other choice
            else:
                print("\nItu pilihan yang tidak valid.")
                
                # isirahat /break
# memanggil main /call main
main()
