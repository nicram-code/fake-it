from faker import Faker
import time 
import os
import sys
from colorama import Fore, init, Back, Style
import webbrowser
init()

SITE_LINK_1 = "https://nicram-code.github.io/"
SITE_LINK_2 = "https://doxbean.cc/@nicram"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def open_bio_sites():
    webbrowser.open(SITE_LINK_1)
    webbrowser.open(SITE_LINK_2)

#Python Typing Text Effect - www.101computing.net/python-typing-text-effect/
def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.005)

def logo_typing_effect():
    reset = "\033[0m"
    typingPrint(
        "\033[38;2;255;255;0m" + "                    ______      __           ______" + "\n" +
        "\033[38;2;255;235;0m" + "                   / ____/___ _/ /_____     /  _/ /_" + "\n" +
        "\033[38;2;255;210;0m" + "                  / /_  / __ `/ //_/ _ \    / // __/" + "\n" +
        "\033[38;2;255;180;0m" + "                 / __/ / /_/ / ,< /  __/  _/ // /_" + "\n" +
        "\033[38;2;255;155;0m" + "                /_/    \__,_/_/|_|\___/  /___/\__/" + "\n" +
        "\033[38;2;255;130;0m" + "       ────────────────────────────────────────────────────" +
        reset + "\n"
    )

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
    print(Fore.YELLOW + "            [1] UK" + "  " + "          [2] PL" + "        [3] IT" + Style.RESET_ALL)
    print(" ")
    print(Fore.YELLOW + "            [4] RU" + "  " + "          [5] UA" + "        [6] DE" + Style.RESET_ALL)
    print(" ")
    print(Fore.YELLOW + "            [exit] Exit" + "       [S] Site" + Style.RESET_ALL)

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

def it_fake_data_gen():
    clear()
    fake = Faker('it_IT')
    profil = fake.profile()
    print(f"Nome (Name):                {profil['name']}")
    print(f"Email (Email):              {profil['mail']}")
    print(f"Data di nascita (DOB):      {profil['birthdate']}")
    print(f"Sesso (Sex):                {profil['sex']}")
    print(f"Professione (Job):          {profil['job']}")
    print(f"Azienda (Company):          {profil['company']}")
    print(f"Indirizzo (Address):        {profil['address']}")
    print(f"Sito web (Website):         {profil['website'][0]}")
    print(f"Telefono (Phone):           {fake.phone_number()}")
    print(f"Città (City):               {fake.city()}")
    print(f"CAP (Postcode):             {fake.postcode()}")
    print(f"Paese (Country):            Italia")
    print(f"IP (v4):                    {fake.ipv4()}")
    print(f"IP (v6):                    {fake.ipv6()}")
    print(f"MAC:                        {fake.mac_address()}")
    print(f"User Agent:                 {fake.user_agent()}")
    print(f"Nome utente (Username):     {fake.user_name()}")
    print(f"Password (Password):        {fake.password()}")
    print(f"URL:                        {fake.url()}")
    print(f"IBAN:                       {fake.iban()}")
    print(f"Carta (Card):               {fake.credit_card_number()}")
    print(f"Scadenza (Expires):         {fake.credit_card_expire()}")
    print(f"Tipo carta (Card type):     {fake.credit_card_provider()}")
    print(f"Codice Fiscale (Tax ID):    {fake.ssn()}")
    print(f"UUID:                       {fake.uuid4()}")
    print(f"Fuso orario (Timezone):     {fake.timezone()}")


def ru_fake_data_gen():
    clear()
    fake = Faker('ru_RU')
    profil = fake.profile()
    print(f"Имя (Name):                 {profil['name']}")
    print(f"Эл. почта (Email):          {profil['mail']}")
    print(f"Дата рождения (DOB):        {profil['birthdate']}")
    print(f"Пол (Sex):                  {profil['sex']}")
    print(f"Должность (Job):            {profil['job']}")
    print(f"Компания (Company):         {profil['company']}")
    print(f"Адрес (Address):            {profil['address']}")
    print(f"Сайт (Website):             {profil['website'][0]}")
    print(f"Телефон (Phone):            {fake.phone_number()}")
    print(f"Город (City):               {fake.city()}")
    print(f"Индекс (Postcode):          {fake.postcode()}")
    print(f"Страна (Country):           Россия")
    print(f"IP (v4):                    {fake.ipv4()}")
    print(f"IP (v6):                    {fake.ipv6()}")
    print(f"MAC:                        {fake.mac_address()}")
    print(f"User Agent:                 {fake.user_agent()}")
    print(f"Имя пользователя (Username):{fake.user_name()}")
    print(f"Пароль (Password):          {fake.password()}")
    print(f"URL:                        {fake.url()}")
    print(f"IBAN:                       {fake.iban()}")
    print(f"Карта (Card):               {fake.credit_card_number()}")
    print(f"Срок действия (Expires):    {fake.credit_card_expire()}")
    print(f"Тип карты (Card type):      {fake.credit_card_provider()}")
    print(f"ИНН (Tax ID):               {fake.businesses_inn()}")
    print(f"UUID:                       {fake.uuid4()}")
    print(f"Часовой пояс (Timezone):    {fake.timezone()}")


def ua_fake_data_gen():
    clear()
    fake = Faker('uk_UA')
    profil = fake.profile()
    print(f"Ім'я (Name):                {profil['name']}")
    print(f"Ел. пошта (Email):          {profil['mail']}")
    print(f"Дата народження (DOB):      {profil['birthdate']}")
    print(f"Стать (Sex):                {profil['sex']}")
    print(f"Посада (Job):               {profil['job']}")
    print(f"Компанія (Company):         {profil['company']}")
    print(f"Адреса (Address):           {profil['address']}")
    print(f"Сайт (Website):             {profil['website'][0]}")
    print(f"Телефон (Phone):            {fake.phone_number()}")
    print(f"Місто (City):               {fake.city()}")
    print(f"Індекс (Postcode):          {fake.postcode()}")
    print(f"Країна (Country):           Україна")
    print(f"IP (v4):                    {fake.ipv4()}")
    print(f"IP (v6):                    {fake.ipv6()}")
    print(f"MAC:                        {fake.mac_address()}")
    print(f"User Agent:                 {fake.user_agent()}")
    print(f"Користувач (Username):      {fake.user_name()}")
    print(f"Пароль (Password):          {fake.password()}")
    print(f"URL:                        {fake.url()}")
    print(f"IBAN:                       {fake.iban()}")
    print(f"Картка (Card):              {fake.credit_card_number()}")
    print(f"Термін дії (Expires):       {fake.credit_card_expire()}")
    print(f"Тип картки (Card type):     {fake.credit_card_provider()}")
    print(f"РНОКПП (Tax ID):            {fake.ssn()}")
    print(f"UUID:                       {fake.uuid4()}")
    print(f"Часовий пояс (Timezone):    {fake.timezone()}")




def de_fake_data_gen():
    clear()
    fake = Faker('de_DE')
    profil = fake.profile()
    print(f"Name (Name):                {profil['name']}")
    print(f"E-Mail (Email):             {profil['mail']}")
    print(f"Geburtsdatum (DOB):         {profil['birthdate']}")
    print(f"Geschlecht (Sex):           {profil['sex']}")
    print(f"Beruf (Job):                {profil['job']}")
    print(f"Unternehmen (Company):      {profil['company']}")
    print(f"Adresse (Address):          {profil['address']}")
    print(f"Webseite (Website):         {profil['website'][0]}")
    print(f"Telefon (Phone):            {fake.phone_number()}")
    print(f"Stadt (City):               {fake.city()}")
    print(f"Postleitzahl (Postcode):    {fake.postcode()}")
    print(f"Land (Country):             Deutschland")
    print(f"IP (v4):                    {fake.ipv4()}")
    print(f"IP (v6):                    {fake.ipv6()}")
    print(f"MAC:                        {fake.mac_address()}")
    print(f"User Agent:                 {fake.user_agent()}")
    print(f"Benutzername (Username):    {fake.user_name()}")
    print(f"Passwort (Password):        {fake.password()}")
    print(f"URL:                        {fake.url()}")
    print(f"IBAN:                       {fake.iban()}")
    print(f"Karte (Card):               {fake.credit_card_number()}")
    print(f"Ablaufdatum (Expires):      {fake.credit_card_expire()}")
    print(f"Kartentyp (Card type):      {fake.credit_card_provider()}")
    print(f"Steuernummer (Tax ID):      {fake.ssn()}")
    print(f"UUID:                       {fake.uuid4()}")
    print(f"Zeitzone (Timezone):        {fake.timezone()}")


def main_loop():
    clear()
    logo_typing_effect()
    choice_country()
    while True:
        choice = input("» ")
        if choice == "1":
            uk_fake_data_gen()
            input("\n» Press Enter to return...")
            clear()
            logo()
            choice_country()
        elif choice == "2":
            poland_fake_data_gen()
            input("\n» Press Enter to return...")
            clear()
            logo()
            choice_country()

        elif choice == "3":
            it_fake_data_gen()
            input("\n» Press Enter to return...")
            clear()
            logo()
            choice_country()
        elif choice == "4":
            ru_fake_data_gen()
            input("\n» Press Enter to return...")
            clear()
            logo()
            choice_country()
        elif choice == "5":
            ua_fake_data_gen()
            input("\n» Press Enter to return...")
            clear()
            logo()
            choice_country()
        
        elif choice == "6":
            de_fake_data_gen()
            input("\n» Press Enter to return...")
            clear()
            logo()
            choice_country()
        
        elif choice == "exit":
            typingPrint("Goodbye!\n")
            break
        elif choice.lower() == 's':
            open_bio_sites()
            input("\n» Press Enter to return...")
            clear()
            logo()
            choice_country()

        else:
            print(Fore.RED + "Invalid option." + Style.RESET_ALL)

if __name__ == "__main__":
    main_loop()