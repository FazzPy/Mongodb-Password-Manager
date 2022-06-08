from pymongo import MongoClient
from colorama import Fore, init
from random import *
import string
import rsa

init(autoreset=True)

print(Fore.MAGENTA+"""
 _______    ___      ________   ________  
|   ____|  /   \    |       /  |       /  
|  |__    /  ^  \   `---/  /   `---/  /   
|   __|  /  /_\  \     /  /       /  /    
|  |    /  _____  \   /  /----.  /  /----.
|__|   /__/     \__\ /________| /________|
""")
print(" ")

app_pw = "123456"   
login = input("$ Password : ")

def ekle():
    hesap = input("$ Başlık : ")
    mail = input("$ Mail : ")
    username = input("$ Kullanıcı adı : ")
    password = input("$ Şifre : ")
    extra = input("$ Extra eklenicek (Eğer yok ise [0] Bırakın) : ")
    data = {
        "Hesap":hesap,
        "Mail":mail,
        "Username":username,
        "Password":password,
        "Extra":extra
    }

    accounts.insert_one(data)
    print("Ekleme başarılı!")
    start()

def görüntüle():
    baslik = input("$ Görüntülemek istediğiniz hesabın başlığını giriniz : ")
    sorgu = {"Hesap":baslik}
    for i in accounts.find(sorgu, {}):
        hesap1 = i["Hesap"]
        mail1 = i["Mail"]
        username1 = i["Username"]
        password1 = i["Password"]
        extra = i["Extra"]
        print(f"""
        Hesap : {hesap1}
        Mail : {mail1}
        Username : {username1}
        Password : {password1}
        Extra : {extra}
        """)
        print(" ")
        print(Fore.GREEN+"Görüntüleme başarılı!")
        start()

def güncelle():
    baslik = input("$ Güncellemek istediğiniz hesabın başlığı : ")
    sorgu = {"Hesap":baslik}

    hesap = input("$ Yeni Başlık : ")
    mail = input("$ Mail : ")
    username = input("$ Kullanıcı adı : ")
    password = input("$ Şifre : ")
    extra = input("$ Extra eklenicek (Eğer yok ise [0] Bırakın) : ")
    data = {
        "Hesap":hesap,
        "Mail":mail,
        "Username":username,
        "Password":password,
        "Extra":extra
    }

    accounts.delete_one(sorgu)
    accounts.insert_one(data)
    print("Güncelleme başarılı!")
    start()

def sil():
    baslik = input("$ Silmek istediğiniz hesabın başlığı : ")
    sorgu = {"Hesap":baslik}

    accounts.delete_one(sorgu)
    print(Fore.GREEN+"Silme başarılı!")
    start()

def passwordg():
    characters = string.ascii_letters + string.punctuation  + string.digits
    password =  "".join(choice(characters) for x in range(randint(16, 32)))
    print(Fore.LIGHTYELLOW_EX+f"Şifre : {password}")
    start()

def start():
    global accounts
    print(Fore.GREEN+"Succesful!")
    client = MongoClient("<mongodb-connect-link>")
    database = client["Database"]
    accounts = database["Accounts"]
    print(" ")
    print(Fore.GREEN+"Connect database!")
    print(" ")
    print(Fore.LIGHTMAGENTA_EX+"İşlemi seçiniz : ")
    print(Fore.LIGHTYELLOW_EX+"1) Hesap Ekle")
    print(Fore.LIGHTRED_EX+"2) Hesapları gör")
    print(Fore.LIGHTBLUE_EX+"3) Hesap Güncelle")
    print(Fore.RED+"4) Hesap sil")
    print(Fore.CYAN+"5) Password Generator")
    print(" ")
    process = input("$ Process : ")
    
    if process == "1":
        ekle()
    elif process == "2":
        görüntüle()
    elif process == "3":
        güncelle()
    elif process == "4":
        sil()
    elif process == "5":
        passwordg()
        


if login == app_pw:
    start()
else:
    while True:
        v = input(Fore.RED+"Yanlış giriş!!!")
