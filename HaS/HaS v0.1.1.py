# -*- coding: utf-8 -*-
# This is HaS (hash as speech) v0.1.0. This program is currently in development.
import os
from os import system, name
import sys
import pyperclip
import random
print("HaS v1.1.0")
print("""
888    888           .d8888b.  
888    888          d88P  Y88b 
888    888          Y88b.      
8888888888  8888b.   "Y888b.   
888    888     "88b     "Y88b. 
888    888 .d888888       "888 
888    888 888  888 Y88b  d88P 
888    888 "Y888888  "Y8888P" 
        Hash and Speech
""")
print("Type HELP for a list of commands.")
# Read the data...
DATA = open("HaS_DATA.txt", "r+")
DATA_read_lines = DATA.readlines()
DATA.multi_lined_encrypting = DATA_read_lines[0]  # "multi encryption off"
DATA.audio_copy_hash = DATA_read_lines[1]  # "audio copy text off"
DATA.audio_copy_text = DATA_read_lines[2]  # "audio copy hash off"
try:
    DATA.pin1 = int(DATA_read_lines[3])  # 1
    DATA.pin2 = int(DATA_read_lines[4])  # 1
except ValueError:
    DATA.pin1 = float(DATA_read_lines[3])  # 1
    DATA.pin2 = float(DATA_read_lines[4])  # 1
DATA.use_keys = DATA_read_lines[5]  # "keys off"
DATA.use_salt = DATA_read_lines[6]  # "salt off"
DATA.mode_ = DATA_read_lines[7]
DATA.close()  # ...Save the data!

if DATA.pin1 == "1" or DATA.pin2 == "1":
    print("""    A personal identification number (PIN) is a security code for HaS. Similar to a password, your PINs 
should be kept secret because it allows access for decrypting hashes made with this program. Only those who have both
PINs will be able to decrypt your hashes, and create ones to be decrypted vice versa. Use 1 for default (no PIN).
Before continuing, both PINs must be entered.""")

RUN = True
LIST = []  # extend
INPUT_LIST = []
INPUT_ADD = ""
π = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998
key_number = 1
encrypted_keys_dic = {
    "1": [],
    "2": [],
    "3": [],
    "4": [],
    "5": []
}

keys = {
    "key1": "g1Hl5xw",
    "key2": "S9ivP4q",
    "key3": "y6XfESa",
    "key4": "C9Vlp2F",
    "key5": "oi6evbS"
}

keys_list = {
    "key1": [],
    "key2": [],
    "key3": [],
    "key4": [],
    "key5": []
}

salt = {
    "salt1": "2sMfzA",
    "salt2": "Yx1Lfj",
    "salt3": "O4SwHv",
    "salt4": "Qvqd7u",
    "salt5": "fi8Vswq",
    "salt6": "ds9Ucxs",
    "salt7": "B2cfGNW",
    "salt8": "GyH7HIyi",
    "salt9": "b4dIhwGs"
}

salt_list = {
    "salt1": [],
    "salt2": [],
    "salt3": [],
    "salt4": [],
    "salt5": [],
    "salt6": [],
    "salt7": [],
    "salt8": [],
    "salt9": []
}


def create_pin1():
    while type(DATA.pin1) != float:
        try:
            DATA.pin1 = float(input("_______________ Enter PIN 1. If greater than 999999999999999 an error may "
                                    "occur... \n"))
        except ValueError:
            print("Invalid value. PIN must be numbers only.")


create_pin1()


def create_pin2():
    while type(DATA.pin2) != float:
        try:
            DATA.pin2 = float(input("_______________ Enter PIN 2. If greater than 999999999999999 an error may "
                                    "occur... \n"))
        except ValueError:
            print("Invalid value. PIN must be numbers only.")


create_pin2()
print("Setting encryption...")
PIN = int(DATA.pin2/π + DATA.pin1/π + (π*π*2))  # After this, we don't use "pin1" or "pin2."
void_item = "|"
value = {}


def load():
    no_more = False
    with open("HaS_BASE.txt", "r", encoding="utf-8") as r:
        for line in r:
            try:
                x_ = str(line[:1])
                y_ = int(line[2:])
                if no_more is False:
                    value.update({x_: y_})
                if DATA.mode_ == "mode 0" + "\n" and x_ == " ":
                    no_more = True
            except ValueError:
                pass


load()


alternative_value = {}


D = 0
D2 = 0
HASH_VALUE = 0
HASH = ""
hash_item = 0
HASHED_LIST = []
NUMBER_LIST = []
HASH_LIST = []
MAIN_HASH_LIST = []
NUMBER_ITEM = 0
number_of_hashable = 94


def use_pin(n):
    use_ = int(PIN/π * n/π / PIN + n + 13 * π)
    return use_


list_x = []  # We actually do use this.
numbers_list = []
encrypted_duplicates_count = 0  #
extra_number = 1


def create_hashes(text):
    global HASH
    global extra_number
    HASH = ""
    HASH_LIST.clear()
    MAIN_HASH_LIST.clear()
    numbers_list.clear()
    ha = ""
    # Get the input and save it as words; ("hello world") . Put each item in a list ["h","e","l'... and so on... ???!!!
    # Find the value of each letter. value.__getitem__(h) = 25; value.__getitem__(e) = 12... and so on...
    # (remember, each item needs it's own hash. a = (a,f,r,e,s,2,f))
    for item in text:  # LIST = {"h","e","l"... and so on...
        ha = value.get(item)
        if ha is not None:
            rounds = int(1 + ha / 5)
            if rounds > 50:
                rounds = 50
            for item2 in range(rounds + 9):
                ha += PIN
                ha += extra_number
                ha = use_pin(ha)
                ha *= π
                ha %= number_of_hashable
                ha = int(ha)
                numbers_list.append(int(ha))
                extra_number += 1
        elif ha is None:
            pass

    if ha is not None:
        for i in numbers_list:
            n = i
            if n < 33:
                n += 33
            ha = (list(value.keys())[list(value.values()).index(n)])  # number turns into letter. 78 --> 'a' ("a": 78)
            HASH_LIST.append(ha)
        item = "".join(HASH_LIST)
        MAIN_HASH_LIST.append(item)
        HASH = "".join(MAIN_HASH_LIST)
        v = str(value.get(text)).__add__(".")
        HASH = v.__add__(HASH)
    elif ha is None or ha == "\n":
        HASH_LIST.append("|")
    return HASH


encrypted_values = []
found_encrypted_values = []
PRINT_HASH = []
PRINT_HASH_ADDED = ""
finding_new_hash = False


def remove_hash_number(hash_):
    dot = hash_.find(".")
    hash_without_the_number = hash_[dot + 1:]
    return hash_without_the_number


def find_encrypted_duplicates():
    hold_list = []
    one_or_five = 0
    if DATA.use_keys == "keys off"+"\n":
        one_or_five += 1
    else:
        one_or_five = 5
    for one_to_five in range(one_or_five):
        print("Loading encryption...", str(int(one_to_five*100 / 5)).__add__("%"))
        for i2 in value:
            a = create_hashes(i2)
            for h in hold_list:
                while hold_list.__contains__(a) or a.__contains__(h):
                    a = list(a)
                    a = a.__reversed__()
                    a = "".join(a)
                    a.replace(i2, "")
            hold_list.append(a)

        for h2 in hold_list:
            b = remove_hash_number(h2)
            for h3 in hold_list:
                c = remove_hash_number(h3)
                if c.__contains__(b) and c != b:
                    b = h2.__add__(" ")
                    h2 = b
            encrypted_keys_dic.get(str(one_to_five + 1)).append(h2)
    print("Loading encryption... 100%")


find_encrypted_duplicates()


def add_new_character_to_file(new_character):
    new_number = ""
    ascii_character = (ascii(new_character))
    ascii_character = list(ascii(ascii_character))
    characters_to_filter_out = "\\'\n".__add__('"')
    for i in ascii_character:
        if characters_to_filter_out.__contains__(i) is False:
            v = str(value.get(i))
            new_number = new_number.__add__(v)
    with open("HaS_BASE.txt", "a", encoding="utf-8") as af:
        value[new_character] = new_number
        to_append = "\n" + new_character + "=" + new_number
        af.write(to_append)


def add_key(print_hash):
    global key_number
    extend_keys = []
    extend_keys.extend(print_hash)
    key_to_add = "".join(keys_list.get("key"+str(key_number)))
    try:
        extend_keys.insert(random.randint(1, extend_keys.__len__()), key_to_add)
    except ValueError:
        pass
    extend_keys = "".join(extend_keys)
    return extend_keys


lower_salt_amount = 7
higher_salt_amount = 14


def add_salt(print_hash):
    global lower_salt_amount
    global higher_salt_amount
    extend_salt = []
    extend_salt.extend(print_hash)
    salt_number = salt_list.__len__()
    for _ in range(int(print_hash.__len__() / (random.randint(lower_salt_amount, higher_salt_amount)) + 1)):  # This...
        # is how manny "salts" to insert.
        salt_to_add = "".join(salt_list.get("salt"+str(random.randint(1, salt_number))))  # Which "salt" to add.
        try:
            extend_salt.insert(random.randint(1, extend_salt.__len__()), salt_to_add)  # This is were to add the "salt."
        except ValueError:
            pass
    extend_salt = "".join(extend_salt)
    return extend_salt


def salt_amount():
    global lower_salt_amount
    global higher_salt_amount
    amount = int(input(">>> \n ENTER A NUMBER >"))
    lower_salt_amount = amount - 3
    higher_salt_amount = amount + 4
    print("Salt amount is now", amount)


def turn_character_to_hash(character):
    global key_number
    one_hash = ""
    number = str(value.get(character))  # Get the number of the character we want to encrypt, so we can find it's hash.
    number = number.__add__(".")
    if DATA.use_keys == "keys on" + "\n":  # Ger the dictionary we want to search in...
        per_hash = encrypted_keys_dic.get(str(key_number))
    else:
        per_hash = encrypted_keys_dic.get("1")
    for i in per_hash:
        if i.__contains__(number):
            one_hash = i.replace(number, "")
    return one_hash


def encrypt(text):
    global PRINT_HASH
    global key_number
    PRINT_HASH = ""
    found_encrypted_values.clear()
    for letter in text:
        if value.__contains__(letter) is False and letter != "\n" and DATA.mode_ == "mode 0"+"\n":
            print("WARNING: Non ascii character detected. Current mode 0 is not optimized for Non ascii characters. "
                  "Type /c MODE 1 for proper optimization.")
        if value.__contains__(letter) is False and letter != "\n" and DATA.mode_ == "mode 1"+"\n":
            print("WARNING:", letter, "does not currently have a hash, so it will return blank. "
                                      "Reset is required to fix this. /c RELOAD")
            add_new_character_to_file(letter)
        else:
            PRINT_HASH = PRINT_HASH.__add__((turn_character_to_hash(letter)))
    return PRINT_HASH


def encrypt_keys():
    k_n = 1
    for k in keys:
        k4 = ""
        k2 = encrypt(keys.get(k))
        for number in range(7):
            k3 = k2.__getitem__(number + 13)
            k4 = k4.__add__(k3)
        k4 = list(k4)
        k4.extend("")
        k4.reverse()
        k4 = "".join(k4)
        keys_list.get("key"+str(k_n)).append(k4)
        k_n += 1


encrypt_keys()


def encrypt_salt():
    s_n = 1
    s_n2 = 7
    for s in salt:
        s4 = ""
        s2 = encrypt(salt.get(s))
        for number in range(int(s_n2)):
            s3 = s2.__getitem__(number + 11)
            s4 = s4.__add__(s3)
        s4 = list(s4)
        s4.extend("")
        s4.reverse()
        s4 = "".join(s4)
        salt_list.get("salt"+str(s_n)).append(s4)
        s_n += 1
        s_n2 += 0.25


encrypt_salt()


hashed_items_list = []
per_hashed_value_list = []
decrypted_list = []


def decrypt(h, no_print=False):
    global key_number
    h_2 = []
    hash_ = "".join(h)
    h_2.append(hash_)
    hash_ = "".join(h_2)
    if DATA.use_keys == "keys on"+"\n":
        for k in keys_list:
            k2 = keys_list.get(k)
            k2 = "".join(k2)
            if hash_.__contains__(k2):
                key_number = k.replace("key", "")  # "key1" --> "1"
                key_number = int(key_number)  # "1" --> 1
                hash_ = hash_.replace(k2, "")
    if DATA.use_salt == "salt on"+"\n":
        for s in salt_list:
            s2 = salt_list.get(s)
            s2 = "".join(s2)
            if hash_.__contains__(s2):
                hash_ = hash_.replace(s2, "")
    if hash_.__contains__("|"):
        hash_ = hash_.replace("|", "\n")
    for i in value:
        per_value = encrypt(i)
        if hash_.__contains__(per_value):
            hash_ = hash_.replace(per_value, i)
    if DATA.audio_copy_text == "audio copy text on"+"\n":
        pyperclip.copy(hash_)
        if no_print is False:
            print("Decrypted text copied to clipboard.")
    if no_print is False:
        print(" DECRYPTED HASH. ")
        print(hash_.__add__("\n"))
    return hash_  # It's text...


def encrypt_file(file_name, same_file, warm_up=False):
    print_list = []
    _list = []
    input_file_name = ""
    void = ""
    try:
        with open(file_name, "r", encoding="utf-8") as rf:
            if same_file is False:
                print("""Enter a file name to be created and writen to. (Recommended file type: .txt)
Remember to include the file type at the end. (Example: FILE NAME.txt)
Or leave it blank to avoid encrypting to a file, and just print into terminal.
Warning: If you use the same name as an existing file, it will be overwritten.""")
                input_file_name = str(input(">>> \n FILE NAME >"))
            elif same_file is True:
                input_file_name = "HaS_HASH.txt"
            if input_file_name == "" or input_file_name == " ":
                print("No file selected to be encrypted to.")
                for line_ in rf:
                    rf_ = encrypt(line_)
                    try:
                        if DATA.use_salt == "salt on" + "\n":
                            rf_ = add_salt(rf_)
                        if DATA.use_keys == "keys on" + "\n":
                            rf_ = add_key(rf_)
                    except ValueError:
                        pass
                    print_list.append(rf_)
            else:
                with open(input_file_name, "w", encoding="utf-8") as wf:
                    if warm_up is False:
                        print("Encrypting to", input_file_name)
                    for line in rf:
                        wf_ = encrypt(line)
                        try:
                            if DATA.use_salt == "salt on"+"\n":
                                wf_ = add_salt(wf_)
                            if DATA.use_keys == "keys on"+"\n":
                                wf_ = add_key(wf_)
                        except ValueError:
                            pass
                        wf.write(void)
                        wf.write(wf_)
                        print_list.append(wf_.__add__("|"))
                        void = "|"

            if input_file_name == "HaS_HASH.txt":
                with open(input_file_name, "r", encoding="utf-8") as rf2:
                    with open(file_name, "w", encoding="utf-8") as wf2:
                        for line2 in rf2:
                            wf2.write(line2)

    except FileNotFoundError:
        print(file_name, """can not be found.
Be sure your input is exactly the same name as the existing file's name and be sure it's in the same directory.
Also be sure you specify the file type. (Example: FILE NAME.txt)
Note: Only the first file must be existing. The second one can be created on command.""")
    if warm_up is False:
        join = "".join(print_list)
        _list.append(join)
        join = "".join(_list)
        if input_file_name != "":
            print(" FILE ENCRYPTED. ")
        print(join)


def decrypt_file(has_file_name, same_file, warm_up=False):
    try:
        with open(has_file_name, "r", encoding="utf-8") as rf:
            if same_file is False:
                print("""Enter a file name to be created and writen to. (Recommended file type: .txt).
Remember to include the file type at the end. (Example: FILE NAME.txt)
Warning: If you use the same name as an existing file, it will be overwritten.
Or leave it blank to avoid decrypting to a file, and just print into terminal.""")
                input_file_name = str(input(">>> \n FILE NAME >"))
            elif same_file is True:
                input_file_name = "HaS_TEXT.txt"
            if input_file_name == "" or input_file_name == " ":
                print("No file selected to be decrypted to.")
                for line_ in rf:
                    decrypt(line_)  # No need for a 'print'. It will be done all the same.
            else:
                with open(input_file_name, "w", encoding="utf-8") as wf:
                    if warm_up is False:
                        print("Decrypting to", input_file_name)
                    for line in rf:
                        wf.write(str(decrypt(line, warm_up)))
            if input_file_name == "HaS_TEXT.txt":
                with open("HaS_TEXT.txt", "r", encoding="utf-8") as rf2:
                    with open(has_file_name, "w", encoding="utf-8") as wf2:
                        for line in rf2:
                            wf2.write(line)
    except FileNotFoundError:
        print(has_file_name, """can not be found.
Be sure your input is exactly the same name as the existing file's name and be sure it's in the same directory.
Also be sure you specify the file type. (Example: FILE NAME.txt)
Note: Only the first file must be existing. The second one can be created on command.""")


def save_settings():
    with open("HaS_DATA.txt", "w") as write_data:
        write_data.write(DATA.multi_lined_encrypting)
        write_data.write(DATA.audio_copy_hash)
        write_data.write(DATA.audio_copy_text)
        write_data.write(str(DATA.pin1)+"\n")
        write_data.write(str(DATA.pin2)+"\n")
        write_data.write(DATA.use_keys)
        write_data.write(DATA.use_salt)
        write_data.write(DATA.mode_)
    print("Current settings have been saved.")


def default_settings():
    global lower_salt_amount
    global higher_salt_amount
    DATA.multi_lined_encrypting = "multi encryption off"+"\n"
    DATA.audio_copy_hash = "audio copy hash off"+"\n"
    DATA.audio_copy_text = "audio copy text off"+"\n"
    DATA.pin1 = "1"
    DATA.pin2 = "1"
    DATA.use_keys = "keys off"+"\n"
    DATA.use_salt = "salt off"+"\n"
    lower_salt_amount = 7
    higher_salt_amount = 14
    DATA.mode_ = "mode 0"
    print("Settings have been to default.")


def reload():
    load()
    find_encrypted_duplicates()


# This all is to warm up the functions. The first time we try encrypting "\n" to a file, it will miss it.
with open("HaS_open.txt", "w", encoding="utf-8") as open_:
    open_.write("\n")
    open_.write("open")
encrypt_file("HaS_open.txt", True, True)
decrypt_file("HaS_open.txt", True, True)
print('Settings complete. Type "/c HELP" for context.')
input_list = []
still_encrypting = False  # This is not a setting.
D3 = ""
D4 = ""
end_of_hash = "\n"
while RUN is True:
    INPUT = input(">>>")
    INPUT_ADD = INPUT_ADD.__add__(INPUT).__add__("\n")
    INPUT_LIST = LIST
    LIST.extend(INPUT)
    try:
        if LIST.__len__() > 2:
            D = LIST.__getitem__(0)
            D2 = LIST.__getitem__(1)
            D3 = LIST.__getitem__(2)
            D4 = LIST.__getitem__(3)
            if D == "/" and D2.lower() == "e":
                print(" ENCRYPTING TEXT... ")
    except IndexError:
        D = ""
        D2 = ""
        D3 = ""
        D4 = ""

    if DATA.multi_lined_encrypting == "multi encryption on"+"\n":
        end_of_hash = "|"
        still_encrypting = True
    else:
        end_of_hash = "\n"

    if INPUT.lower() == "/print":
        if still_encrypting is True and DATA.multi_lined_encrypting == "multi encryption on"+"\n":
            still_encrypting = False
            print(PRINT_HASH_ADDED.__add__("\n"))
        else:
            print("There is nothing to print right now.")

    elif D == "/":
        if still_encrypting is True and D2.lower() == "e" and D3.lower() != "f":
            print(" ENCRYPTED TEXT. Press ENTER to move to the next line. Afterwards you can continue typing, or"
                  " use /PRINT to finish current input.")
        still_encrypting = False
        PRINT_HASH_ADDED = ""
        if D2.lower() == "e" and D3 == " ":
            LIST.pop(0)
            LIST.pop(0)
            LIST.pop(0)
            key_number += 1
            if key_number >= 6:  # There's 5 keys. After the 5th key, go back to the 1st key.
                key_number = 1
            encrypt(LIST)
            if DATA.use_salt == "salt on"+"\n":  # ALWAYS add salt BEFORE adding keys.
                PRINT_HASH = add_salt(PRINT_HASH)
            if DATA.use_keys == "keys on"+"\n":
                PRINT_HASH = add_key(PRINT_HASH)
            if DATA.multi_lined_encrypting == "multi encryption off"+"\n":
                print(PRINT_HASH, end=end_of_hash)
                if DATA.audio_copy_hash == "audio copy hash on"+"\n":
                    pyperclip.copy(PRINT_HASH)
                    print("Encrypted text copied to clipboard.")
            elif DATA.multi_lined_encrypting == "multi encryption on"+"\n":
                # This is so we get the first line. Or, we'll miss it.
                PRINT_HASH_ADDED = PRINT_HASH_ADDED.__add__(PRINT_HASH.__add__("|"))
                if DATA.audio_copy_hash == "audio copy hash on"+"\n":
                    pyperclip.copy(PRINT_HASH_ADDED.__add__("\n"))

        elif D2 == ("d" or "d") and D3 == " ":
            print(" DECRYPTING HASH... ")
            LIST.pop(0)
            LIST.pop(0)
            LIST.pop(0)
            decrypt(LIST)
        elif D2 == ("c" or "C") and D3 == " ":
            LIST.pop(0)
            LIST.pop(0)
            LIST.pop(0)
            x = "".join(input_list)
            LIST.append(x)
            x = "".join(LIST)
            x_lower = x.lower()
            if x_lower == "exit":
                print(" Exiting... ")
                sys.exit()
            elif x_lower == "keys on":
                DATA.use_keys = "keys on"
                find_encrypted_duplicates()
                print("Keys has been activated.")
            elif x_lower == "keys off":
                DATA.use_keys = "keys off"
                print("Keys has been deactivated.")
            elif x_lower == "salt on":
                DATA.use_salt = "salt on"
                print("Salt has been activated.")
            elif x_lower == "salt off":
                DATA.use_salt = "salt off"
                print("Salt has been deactivated.")
            elif x_lower == "salt number":
                salt_amount()
            elif x_lower == "pin 1":
                print(" PIN 1 was", DATA.pin1, "Enter new number.")
                DATA.pin1 = 1
                create_pin1()
                PIN = int(DATA.pin2 / π + DATA.pin1 / π + (π * π * 2))
                find_encrypted_duplicates()  # Recreate hashes.
                print(" PIN 1 was changed to", DATA.pin1)
            elif x_lower == "pin 2":
                print(" PIN 2 was", DATA.pin2, "Enter new number.")
                DATA.pin2 = 1
                create_pin2()
                PIN = int(DATA.pin2 / π + DATA.pin1 / π + (π * π * 2))
                find_encrypted_duplicates()  # Recreate hashes.
                print(" PIN 2 was changed to", DATA.pin2)
            elif x_lower == "audio copy text on":
                DATA.audio_copy_text = "audio copy text on"
                print(" Decrypted hashes will now automatically be copied to the clipboard as plan text.")
            elif x_lower == "audio copy text off":
                DATA.audio_copy_text = "audio copy text off"
                print(" Decrypted hashes will no longer be automatically copied to the clipboard.")
            elif x_lower == "audio copy hash on":
                DATA.audio_copy_hash = "audio copy hash on"+"\n"
                print(" Encrypted hashes will now be automatically copied to the clipboard as encrypted text.")
            elif x_lower == "audio copy hash off":
                DATA.audio_copy_hash = "audio copy hash off"+"\n"
                print(" Encrypted hashes will no longer be automatically copied to the clipboard.")
            elif x_lower == "multi encryption on":
                DATA.multi_lined_encrypting = "multi encryption on"+"\n"
                print('''Inputs with multiple lines can now be encrypted. However you'll need to type /PRINT in order
to finish encrypting the input. WARNING: If you are using this in a terminal, it may not work as intended if your input
is more then eight lines.''')
            elif x_lower == "multi encryption off":
                DATA.multi_lined_encrypting = "multi encryption off"+"\n"
                print("Multi encryption has been turned off.")
            elif x_lower == "help":
                print(''' All commands must begin with "/c COMMAND". General commands will use this method. 
To create a hash, use "/e TEXT".   
To decrypt a hash, use "/d HASH". Remember: In order the decrypt a hash, some of your settings will have to be the same
    as when the hash was made: PIN 1; PIN 2; Salt ON/OFF; keys ON/OFF and the HaS_BASE.txt file (Only if it's on mode 1)
    which is already the same by default. To quickly see all the required settings for decrypting interchangeably.
    type /c ISETTINGS
To encrypt a file (like a .txt file) "/ef FILE NAME.FILE-TYPE"
To decrypt a file (like a .txt file) "/df FILE NAME.FILE-TYPE"
To see a list of commands, use "/c COMMANDS".
 Remember: If you want to encrypt/decrypt very large inputs, it's recommended you put them in a text file (.txt) and
 use "/ef FILE NAME.FILE-TYPE" / "/df FILE NAME.FILE-TYPE" ''')
            elif x_lower == "commands":
                print(''' "/c HELP" (For basic help.)
"/e TEXT" (Turn text into a hash.)
"/d HASH" (Decrypt a hash and turn it into plan text.)
"/ef FILE NAME.FILE-TYPE" (Encrypt all the text in a file. The recommended file type is .txt. WARNING: if you try
    encrypting a file with non ascii character(s) that are not in HaS_BASE.txt they will be deleted. If you are not sure
    the file contains such characters, then please back up the file first!)
"/df FILE NAME.FILE-TYPE" (Decrypt all the text in a file. The recommended file type is .txt)
"/e+ FIRST FILE NAME.FILE-TYPE" (Encrypt all the text in a file, and ether create a file to put the encrypted text
    "SECOND FILE NAME.FILE-TYPE" (inside of, or write the hash inside an existing file. Or leave the second input
        empty and just print in the terminal. The recommended file type is .txt)
"/d+ FIRST FILE NAME.FILE-TYPE" (Decrypt all the text in a file, and ether create a file to put the decrypted text
    "SECOND FILE NAME.FILE-TYPE" (inside of, or write the text inside an existing file. Or leave the second input
        empty and just print in the terminal. The recommended file type is .txt)
"/c PIN 1" (Assign a new number for PIN 1.)
"/c PIN 2" (Assign a new number for PIN 2.)
"/c KEYS ON/OFF" (Enable/disable the KEYS function. Enabling keys will further security, but may slightly reduce
    encrypting/decrypting speed, and vice versa, if disabled.)
"/c SALT ON/OFF" (Enable/disable the SALT function. Enabling salt will further security, but may slightly reduce
    encrypting/decrypting speed, and vice versa, if disabled.)
"/c SALT NUMBER" (Edit the amount of salt that is added to a hash. It's recommended you chose a number between 4 to 15.
    No lower then 4, and no higher then 15. 10 it default. NOTE: The lower the number, the more salt.
    The more salt (as long as it's not too much) the more secure, but more bytes as well, as it will be a larger hash.)
"/c AUDIO COPY TEXT ON/OFF" (Enable/disable audio copping text to the clipboard when decrypting hashes.)
"/c AUDIO COPY HASH ON/OFF" (Enable/disable audio copping hashes to the clipboard when encrypting text.)
"/c MULTI ENCRYPTION ON/OFF" (Enable/disable the multi encryption ability, which allows inputs that are multiple lines
    to be automatically encrypted. For use when pasting after copying into terminal.)
"/c MODE 0/1" (0 = Default. 1 = advance encryption. Recommended only when encrypting text with non ascii characters.
    This is not required for encrypting files, just inputs. WARNING: Some non ascii characters may appear different,
    not show up, look blank or invisible in the terminal. For such characters, it's recommended you put them in a file
    (like .txt) and then encrypt/decrypt it order for an exact operation. Put the text in the file, save it, 
    and type /ef YOUR FILE NAME.FILE-TYPE)
"/c SAVE SETTINGS" (Saves the current setting.)
"/c SHOW SETTINGS" (Shows all the current settings.)
"/c ISETTINGS" (Shows all the required settings for decrypting interchangeably on another machine.)
"/c DEFAULT SETTINGS" (Automatically sets all settings to default, including PINs.)
"/c RELOAD" (Automatically reloads encryption. Always use this when adding a non ascii character.)
"/c EXIT" (Exit the terminal.)''')
            elif x_lower == "save settings":
                save_settings()
            elif x_lower == "show settings":
                print("Current settings...")
                print(DATA.multi_lined_encrypting)
                print(DATA.audio_copy_hash)
                print(DATA.audio_copy_text)
                print("PIN 1 =", DATA.pin1)
                print("PIN 2 =", DATA.pin2)
                print(DATA.use_keys)
                print(DATA.use_salt)
                print("salt number =", lower_salt_amount + 3)
                print(DATA.mode_)
            elif x_lower == "isettings":
                print("These are all the required settings for decrypting interchangeably on another machine. These "
                      "must be the same for both computers.")
                non_ascii_letters = ""
                print("PIN 1 =", DATA.pin1)
                print("PIN 2 =", DATA.pin2)
                print(DATA.use_keys)
                print(DATA.use_salt)
                print(DATA.mode_)
                if DATA.mode_ == "mode 0"+"\n":
                    print("Mode is 0. That means the HaS_BASE.txt file has to be configured, assuming all original"
                          "contend still remains.")
                else:
                    print("Mode is 1. So in order for another machine too decrypt hashes created with this programs"
                          " current configuration, copy...")
                    for ch in value:
                        if all(ord(char) < 128 for char in ch) is False:
                            non_ascii_letters = non_ascii_letters.__add__(ch)
                    print("/e", non_ascii_letters)
                    print("And paste on other machine(s), then reload. Other machine also must be using mode 1")
            elif x_lower == "default settings":
                default_settings()
            elif x_lower == "mode 0":
                DATA.mode_ = "mode 0"+"\n"
                print("The MODE has been set to 0.")
                reload()
            elif x_lower == "mode 1":
                DATA.mode_ = "mode 1"+"\n"
                print("The MODE has been set to 1.")
                reload()
            elif x_lower == "reload":
                print("Updating and Reloading encryption...")
                reload()
        elif D2.lower() == "e" and D3.lower() == "f" and D4.lower() == " ":
            LIST.pop(0)
            LIST.pop(0)
            LIST.pop(0)
            LIST.pop(0)
            x = "".join(input_list)
            LIST.append(x)
            x = "".join(LIST)
            encrypt_file(x, True)
        elif D2.lower() == "e" and D3.lower() == "+" and D4.lower() == " ":
            LIST.pop(0)
            LIST.pop(0)
            LIST.pop(0)
            LIST.pop(0)
            x = "".join(input_list)
            LIST.append(x)
            x = "".join(LIST)
            encrypt_file(x, False)  # was "w"
        elif D2.lower() == "d" and D3.lower() == "f" and D4.lower() == " ":
            LIST.pop(0)
            LIST.pop(0)
            LIST.pop(0)
            LIST.pop(0)
            x = "".join(input_list)
            LIST.append(x)
            x = "".join(LIST)
            decrypt_file(x, True)
        elif D2.lower() == "d" and D3.lower() == "+" and D4.lower() == " ":
            LIST.pop(0)
            LIST.pop(0)
            LIST.pop(0)
            LIST.pop(0)
            x = "".join(input_list)
            LIST.append(x)
            x = "".join(LIST)
            decrypt_file(x, False)
        else:
            print("Invalid command. Type HELP for a list of commands and information.")

    # This is used only when we're encrypting multi lined inputs.
    elif still_encrypting is True and DATA.multi_lined_encrypting == "multi encryption on"+"\n":
        encrypt(LIST)
        try:
            if DATA.use_salt == "salt on"+"\n" and PRINT_HASH != "|":
                PRINT_HASH = add_salt(PRINT_HASH)
            if DATA.use_keys == "keys on"+"\n":
                PRINT_HASH = add_key(PRINT_HASH)
        except ValueError:
            pass
        PRINT_HASH_ADDED = PRINT_HASH_ADDED.__add__(PRINT_HASH.__add__("|"))
        if DATA.multi_lined_encrypting == "multi encryption on"+"\n" and \
                DATA.audio_copy_hash == "audio copy hash on"+"\n":
            pyperclip.copy(PRINT_HASH_ADDED.__add__("\n"))

    INPUT = " "
    LIST = []
    numbers_list.clear()
    list_x.clear()
    HASH_LIST.clear()
    D, D2, D3 = "", "", ""
    count = 0
