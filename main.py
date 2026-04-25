from faker import Faker
import time 
import os
import sys
from colorama import Fore, init, Back, Style
import webbrowser
init()

SITE_LINK = "https://nicram-code.github.io/"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#Python Typing Text Effect - www.101computing.net/python-typing-text-effect/
def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)

def logo():
    reset = "\033[0m"
    print(
        "\033[38;2;255;255;0m" + "                    ______      __           ______" + "\n" +
        "\033[38;2;255;235;0m" + "                   / ____/___ _/ /_____     /  _/ /_" + "\n" +
        "\033[38;2;255;210;0m" + "                  / /_  / __ `/ //_/ _ \    / // __/" + "\n" +
        "\033[38;2;255;180;0m" + "                 / __/ / /_/ / ,< /  __/  _/ // /_" + "\n" +
        "\033[38;2;255;155;0m" + "                /_/    \__,_/_/|_|\___/  /___/\__/" + "\n" +
        "\033[38;2;255;130;0m" + "       ────────────────────────────────────────────────────" +
        reset + "\n"
    )

def choice_country():
    print(Fore.YELLOW + "            [1] UK" + "  " + "          [2] PL" + "        [S] Site" + Style.RESET_ALL)

def poland_fake_data_gen():
    clear()
    fake = Faker('pl_PL')
    profil = fake.profile()
    print(f"Imię i nazwisko: {profil['name']}")
    print(f"Email:           {profil['mail']}")
    print(f"Data urodzenia:  {profil['birthdate']}")
    print(f"Płeć:            {profil['sex']}")
    print(f"Job:             {profil['job']}")
    print(f"Firma:           {profil['company']}")
    print(f"Adres:           {profil['address']}")
    print(f"Strona:          {profil['website'][0]}")
    print(f"Telefon:         {fake.phone_number()}")
    print(f"Miasto:          {fake.city()}")
    print(f"Kod pocztowy:    {fake.postcode()}")
    print(f"Kraj:            {fake.country()}")
    print(f"IP (v4):         {fake.ipv4()}")
    print(f"IP (v6):         {fake.ipv6()}")
    print(f"MAC:             {fake.mac_address()}")
    print(f"User Agent:      {fake.user_agent()}")
    print(f"Username:        {fake.user_name()}")
    print(f"Hasło:           {fake.password()}")
    print(f"URL:             {fake.url()}")
    print(f"IBAN:            {fake.iban()}")
    print(f"Karta:           {fake.credit_card_number()}")
    print(f"Ważna do:        {fake.credit_card_expire()}")
    print(f"Typ karty:       {fake.credit_card_provider()}")
    print(f"PESEL:           {fake.ssn()}")
    print(f"UUID:            {fake.uuid4()}")
    print(f"Kolor:           {fake.color_name()}")
    print(f"Timezone:        {fake.timezone()}")

def uk_fake_data_gen():
    clear()
    fake = Faker('en_GB')
    profil = fake.profile()
    print(f"Name:            {profil['name']}")
    print(f"Email:           {profil['mail']}")
    print(f"Date of birth:   {profil['birthdate']}")
    print(f"Sex:             {profil['sex']}")
    print(f"Job:             {profil['job']}")
    print(f"Company:         {profil['company']}")
    print(f"Address:         {profil['address']}")
    print(f"Website:         {profil['website'][0]}")
    print(f"Phone:           {fake.phone_number()}")
    print(f"City:            {fake.city()}")
    print(f"Postcode:        {fake.postcode()}")
    print(f"Country:         United Kingdom")
    print(f"IP (v4):         {fake.ipv4()}")
    print(f"IP (v6):         {fake.ipv6()}")
    print(f"MAC:             {fake.mac_address()}")
    print(f"User Agent:      {fake.user_agent()}")
    print(f"Username:        {fake.user_name()}")
    print(f"Password:        {fake.password()}")
    print(f"URL:             {fake.url()}")
    print(f"IBAN:            {fake.iban()}")
    print(f"Card:            {fake.credit_card_number()}")
    print(f"Expires:         {fake.credit_card_expire()}")
    print(f"Card type:       {fake.credit_card_provider()}")
    print(f"NIN:             {fake.ssn()}")
    print(f"UUID:            {fake.uuid4()}")
    print(f"Timezone:        {fake.timezone()}")

def main_loop():
    clear()
    logo()
    choice_country()
    while True:
        choice = input("» ")
        if choice == "1":
            uk_fake_data_gen()
            input("\n» Wciśnij Enter aby wrócić...")
            clear()
            logo()
            choice_country()
        elif choice == "2":
            poland_fake_data_gen()
            input("\n» Wciśnij Enter aby wrócić...")
            clear()
            logo()
            choice_country()
        elif choice == "exit":
            typingPrint("Do zobaczenia!\n")
            break
        elif choice == 'S':
            webbrowser.open(SITE_LINK)


        else:
            print(Fore.RED + "Nieznana opcja." + Style.RESET_ALL)

if __name__ == "__main__":
    main_loop()