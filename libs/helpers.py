# coding=utf-8
#!/usr/bin/env python3

from time import strftime
from colorama import init, Fore, Back, Style
from os import system, name

def print_logo():
    logo = """{0}
    ──▄█████████████████████████▄──
    ▄█▀░█░█░█░░░░░░░░░░░░░░░░░░░▀█▄
    █░░░█░█░█░░░░░░░░░░░░░░█████░░█
    █░░░█░█░█░░░░░░░░░░░░░░█████░░█
    █░░░█░█░█░░░░░░░░░░░░░░█████░░█
    █░░░░░░░░░▄▄▄█████▄▄▄░░░░░░░░░█
    ███████████▀▀░░░░░▀▀███████████
    █░░░░░░░██░░▄█████▄░░██░░░░░░░█
    █░░░░░░░██░██▀░░░▀██░██░░░░░░░█
    █░░░░░░░██░██░░░░░██░██░░░░░░░█
    █░░░░░░░██░██▄░░░▄██░██░░░░░░░█
    █░░░░░░░██▄░▀█████▀░▄██░░░░░░░█
    █░░░░░░░░▀██▄▄░░░▄▄██▀░░░░░░░░█
    █░░░░░░░░░░▀▀█████▀▀░░░░░░░░░░█
    █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
    █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
    █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
    ▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀
    ──▀█████████████████████████▀──{1}

        {2}PocketGram | Hichigo THT
       {3}==========================
      {4}Taşınabilir phishing servisi.
            {5}GitHub:tarik0

{6}""".format(Style.BRIGHT + Fore.RED,
Style.RESET_ALL,
Style.BRIGHT + Fore.MAGENTA,
Style.BRIGHT + Fore.YELLOW,
Style.BRIGHT + Fore.WHITE,
Style.BRIGHT + Fore.WHITE,
Style.RESET_ALL
)
    print(logo)


def clear_screen():
    system('cls' if name=='nt' else 'clear')

def ask(message):
    print("{0}[{1}]{2} [ ?? ] {3}{4}{5}: ".format(
        Style.BRIGHT + Fore.YELLOW,
        strftime("%d.%m.%y %X"),
        Fore.MAGENTA,
        Fore.WHITE,
        message,
        Style.RESET_ALL
    ), end="")
    tmp = input()
    return tmp

def success(message):
    print("{0}[{1}]{2} [ OK ] {3}{4}{5}".format(
        Style.BRIGHT + Fore.YELLOW,
        strftime("%d.%m.%y %X"),
        Fore.GREEN,
        Fore.WHITE + Style.BRIGHT,
        message,
        Style.RESET_ALL
    ))

def error(message):
    print("{0}[{1}]{2} [ ER ] {3}{4}{5}".format(
        Style.BRIGHT + Fore.YELLOW,
        strftime("%d.%m.%y %X"),
        Fore.RED,
        Fore.WHITE,
        message,
        Style.RESET_ALL
    ))

def info(message):
    print("{0}[{1}]{2} [INFO] {3}{4}{5}".format(
        Style.BRIGHT + Fore.YELLOW,
        strftime("%d.%m.%y %X"),
        Fore.CYAN,
        Fore.WHITE,
        message,
        Style.RESET_ALL
    ))

def report_account(username, password, ip, user_agent, account_tried):
    tmp = None
    if (account_tried): tmp = "Evet!"
    else: tmp = "Hayır!"

    date = "\n{0}[{1}]{2}".format(Style.BRIGHT + Fore.YELLOW, strftime("%d.%m.%y %X"), Style.BRIGHT + Fore.GREEN)
    print("{0}\n > Giriş Yapıldı!!".format(date))
    print("{0} > Kullanıcı Adı: {1}".format((" " * 0), username))
    print("{0} > Şifre: {1}".format((" " * 0), password))
    print("{0} > IP: {1}".format((" " * 0), ip))
    print("{0} > Platform: {1}".format((" " * 0), user_agent.platform))
    print("{0} > Tarayıcı: {1}".format((" " * 0), user_agent.browser))
    print("{0} > User-Agent: {1}".format((" " * 0), user_agent.string))
    print("{0} > Hesap Denendi Mi?: {1}".format((" " * 0), tmp) + Style.RESET_ALL)
    print("")
