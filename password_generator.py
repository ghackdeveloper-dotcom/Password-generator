import random
import string
import math

def password():
    banner = r"""
    ---------------------------------------------------------------------------------------------------------------
    |  ________          _____         _________   _________         _________      __________     ____    _       |
    | |   ___  |        /  __ \        |   ____|   |   ____|        |  _______|    |   _______|   |  _ \  | |      |
    | |  |___| |       /  /  \ \       |  |____    |  |____         |  |           |  |_______    | | \ \ | |      |
    | |  _____ |      /  /____\ \      |_____  |   |_____  |        |  | ______    |   _______|   | |  \ \| |      |
    | | |            /  _______\ \           | |         | |        |  | |____ |   |  |           | |   \   |      |
    | | |           /  /        \ \    ______| |   ______| |   __   |  |_____| |   |  |_______    | |    \  |  __  |
    | | |          /  /          \ \   |_______|   |_______|  |__|  |__________|   |__________|   | |     \ | |__| |
    --------------------------------------------------------------------------------------------------------------- VERSIONE 1.0   \   CREATO DA: G.HACK
    """

    print(banner)

    print("QUANTO DEVE ESSERE LUNGA LA PASSWORD?")
    try:
        lungezza = int(input("LUNGEZZA PASSWORD:"))
        items = string.ascii_letters + string.digits + "!@#$%£&*?'éç°òì^|;-_à[]{,}"
        password = "".join(random.choices(items, k=lungezza))
        print("PASSWORD:", password)
        SIMBOLI = "!@#$%£&*?'éç°òì^|;-_à[]{,}"
        set_caratteri = 0
        if any(c in string.ascii_lowercase for c in password): set_caratteri += 26
        if any(c in string.ascii_uppercase for c in password): set_caratteri += 26
        if any(c in string.digits for c in password): set_caratteri += 10
        if any(c in SIMBOLI for c in password): set_caratteri += len(SIMBOLI)
        L = len(password)
        entropia = L * math.log2(set_caratteri) if set_caratteri > 0 else 0
        SOGLIA_100_PERCENTO = 80
        percentuale = min(100, (entropia / SOGLIA_100_PERCENTO) * 100)
        print("SICUREZZA PASSWORD:", percentuale,"%")
        if percentuale <= 25:
            print("SICUREZZA PASSWORD: MOLTO DEBOLE")
        elif percentuale <= 45:
            print("SICUREZZA PASSWORD: DEBOLE")
        elif percentuale <= 65:
            print("SICUREZZA PASSWORD: SICURA")
        elif percentuale <= 85:
            print("SICUREZZA PASSWORD: FORTE")
        elif percentuale <= 100:
            print("SICUREZZA PASSWORD: MOLTO FORTE")
    except:
        print("LUNGEZZA ERRATA")
password()


