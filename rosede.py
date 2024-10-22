from pystyle import Colors, Colorate, Write, Center
import requests
import time
import os

from FaceAnimator import FaceAnimator

animator = FaceAnimator()

# Очистка экрана
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
clear_screen()


# Заголовок программы
def print_banner():
    banner = r"""
██████╗  ██████╗ ███████╗███████╗██████╗ ███████╗
██╔══██╗██╔═══██╗██╔════╝██╔════╝██╔══██╗██╔════╝
██████╔╝██║   ██║███████╗█████╗  ██║  ██║█████╗ 
██╔══██╗██║   ██║╚════██║██╔══╝  ██║  ██║██╔══╝ 
██║  ██║╚██████╔╝███████║███████╗██████╔╝███████╗
╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚═════╝ ╚══════╝
    """
    # Яркий градиент для заголовка
    print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter(banner)))

info = """
╔═════════════════════════════════╗
│         ROSEDE - V1.1.1         │
│     AUTORS: Corede, DarkRose    │
│     CONTACTS: @coredepffical    │
│         and  @darkrosec         │
│                                 │
│             GITHUB:             │
│    github.com/TheCoree/RoseDe   │
╚═════════════════════════════════╝
"""

def print_info():
    info = r"""
♥ Maked by @coredeoffical and @darkrosec | v1.1.1 ♥"""
    print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter(info)))

# Главное меню программы
def main_menu():
    # Меню с функциями, разбитое на два столбца
    menu = """
╔═════════════════════════════════╗     ╔═════════════════════════════════╗
║ [1]  Check Phone Number         ║     ║ [11] Get Proxy                  ║
║ [2]  Check IP                   ║     ║ [12] Gmail Osint                ║
║ [3]  Validate Email             ║     ║ [13] Temp Mail                  ║
║ [4]  About the Software         ║     ║ [14] Database Search            ║
║ [5]  AHC Decrypt                ║     ║ [15] Check Website              ║
║ [6]  Info Website               ║     ║ [16] DOS Attack                 ║
║ [7]  Password Generator         ║     ║ [17] IP Attack                  ║
║ [8]  XSS Scan                   ║     ║ [18] Check URL                  ║
║ [9]  Port Scanner               ║     ║ [19] MAC Address Lookup         ║
║ [10] Exit                       ║     ║ [20] XSS Vulnerability Scan     ║
╚═════════════════════════════════╝     ╚═════════════════════════════════╝
    """
    # Яркий градиент для меню
    print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter(menu)))

def wrap_text(text, width):
    """Разбивает текст на строки фиксированной длины."""
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 <= width:
            current_line += (word + " ")
        else:
            lines.append(current_line.strip())
            current_line = word + " "

    if current_line:
        lines.append(current_line.strip())

    return lines

def print_with_frame_multiline(status, text, max_width=80):
    """Печатает текст в рамке с поддержкой переноса строк."""
    # Разбиваем текст на строки с заданной шириной
    wrapped_lines = []
    for line in text.split("\n"):
        wrapped_lines.extend(wrap_text(line, max_width))

    # Определяем ширину самой длинной строки
    frame_width = max(len(line) for line in wrapped_lines)

    # Создаём верхнюю и нижнюю границы рамки
    top_border = "╔" + "═╧" + "═" * (frame_width) + "╗"
    bottom_border = "╚" + "═" * (frame_width + 2) + "╝"

    # Формируем строки с текстом внутри рамки, с выравниванием по ширине
    framed_lines = [f"│ {line.ljust(frame_width)} │" for line in wrapped_lines]

    # Выводим рамку с текстом
    if status == "success":
        print(Colorate.Horizontal(Colors.green_to_white, f'  ┌─ Status: {status}'))
        print(Colorate.Horizontal(Colors.green_to_white, top_border))
        for framed_line in framed_lines:
            print(Colorate.Horizontal(Colors.green_to_white, framed_line))
        print(Colorate.Horizontal(Colors.green_to_white, bottom_border))
    elif status == "fail":
        print(Colorate.Horizontal(Colors.red_to_purple, f'  ┌─ Status: {status}'))
        print(Colorate.Horizontal(Colors.red_to_purple, top_border))
        for framed_line in framed_lines:
            print(Colorate.Horizontal(Colors.red_to_purple, framed_line))
        print(Colorate.Horizontal(Colors.red_to_purple, bottom_border))


# Пробив по номеру
def check_phone():
    try:
        query = input('Enter phone number (without +): ')
        url = "http://apilayer.net/api/validate"
        params = {
            "access_key": "024f419a6d98aac7058c2199bb785121",
            "number": query
        }
        respone = requests.get(url, params=params)

        if respone.status_code == 200:
            data = respone.json()
            valid = data['valid']
            if valid == True:
                local_format = data['local_format']
                country_name = data['country_name']
                country_code = data['country_code']
                location = data['location']
                carrier = data['carrier']
                line_type = data['line_type']
                print_with_frame_multiline('success', f"""Query:        {query}
Local Format: {local_format}
Country:      {country_name}, {country_code}
Location:     {location}
Carrier:      {carrier}
Type:         {line_type}""")
            else:
                print_with_frame_multiline('fail', f'Query:   {query}\nError:   number is not correct')
    except Exception as e:
        print_with_frame_multiline('fail', f'Query:   {query}\nError:   number is not correct')

def check_ip():
    try:
        query = input('Enter IP: ')
        url = f'http://ip-api.com/json/{query}'
        respone = requests.get(url)
        if respone.status_code == 200:
            data = respone.json()
            status = data['status']
            if status == 'success':
                country = data['country']
                code = data['countryCode']
                region = data['region']
                region_name = data['regionName']
                city = data['city']
                zip = data['zip']
                lat = data['lat']
                lon = data['lon']
                timezone = data['timezone']
                isp = data['isp']
                org = data['org']
                as_ = data['as']
                print_with_frame_multiline('success', f"""Query:    {query}
Country   {country}, {code}
Region:   {region_name}, {region}
City:     {city}
Zip:      {zip}

Lat:      {lat}
Lon:      {lon}
Location: https://google.com/maps?q={lat},{lon}

Timezone: {timezone}
Isp:      {isp}
Org:      {org}
As:       {as_}""")
            else:
                print_with_frame_multiline('fail', f'Query:   {query}\nError:   Ip address is not correct')
    except Exception as e:
        print_with_frame_multiline('fail', f'Query:   {query}\nError:   unexpected error')

def validate_email():
    pass

def about_software():
    rose_art = """
    _,--._.-,
   /\_r-,\\_ )
.-.) _;='_/ (.;
 \\ \\'     \/S )
  L.'-. _.'|-'
 <_`-'\\'_.'/
   `'-._( \\
    ___   \\\,      ___
    \\ .'-. \\\   .-'_. /
     '._' '.\\\/.-'_.'
        '--``\\('--'
     rosede   \\\\
              `\\\\,
                \|"""
    
    print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter(rose_art)))
    print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter(info)))

def exit_programm():
    rose_art = """
    _,--._.-,
   /\_r-,\\_ )
.-.) _;='_/ (.;
 \\ \\'     \/S )
  L.'-. _.'|-'
 <_`-'\\'_.'/
   `'-._( \\
    ___   \\\,      ___
    \\ .'-. \\\   .-'_. /
     '._' '.\\\/.-'_.'
        '--``\\('--'
     Good Bye \\\\
              `\\\\,
                \|"""

    print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter(rose_art)))
    print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter(info)))

def decrypter(query, mixing):
    try:
        text = query[:-20]
        message = ""
        for i in text:
            decoded = str(ord(i))
            decodedminone = decoded[:-1]
            final = int(decodedminone) - int(mixing)
            message = message + chr(int(final))
        print_with_frame_multiline('success', message)
    except Exception as e:
        print_with_frame_multiline('fail', f'Query:   {query}\nError:   unexpected error')

def ahc_decrypt():
    try:
        query = input('Enter a encrypted text: ')
        key = None
        mixing = None
        for i in query[::-1]:
            if key is not None and mixing is not None:
                decrypter(query, mixing)
                break
            elif i.isdigit() and key is None:
                key = i
            elif i.isdigit() and mixing is None:
                mixing = i
        if key == None and mixing == None:
            print_with_frame_multiline('fail', f'Query:   {query}\nError:   mixing and key not found')
    except Exception as e:
        print_with_frame_multiline('fail', f'Query:   {query}\nError:   unexpected error')


def info_website():
    Write.Print("Website info gathered...\n", Colors.blue_to_cyan, interval=0.05)
    time.sleep(1)

def password_generator():
    Write.Print("Generating a secure password...\n", Colors.blue_to_cyan, interval=0.05)
    time.sleep(1)
    Write.Print("Password generated: P@ssw0rd1234\n", Colors.green_to_black, interval=0.05)

def xss_scan():
    Write.Print("Running XSS scan...\n", Colors.blue_to_cyan, interval=0.05)
    time.sleep(1)
    Write.Print("XSS scan complete!\n", Colors.green_to_black, interval=0.05)

def port_scanner():
    Write.Print("Scanning ports...\n", Colors.blue_to_cyan, interval=0.05)
    time.sleep(1)
    Write.Print("Port scan complete!\n", Colors.green_to_black, interval=0.05)

# Новые тестовые функции
def get_proxy():
    Write.Print("Fetching proxy list...\n", Colors.blue_to_cyan, interval=0.05)
    time.sleep(1)
    Write.Print("Proxy list retrieved!\n", Colors.green_to_black, interval=0.05)

def gmail_osint():
    Write.Print("Performing Gmail OSINT...\n", Colors.blue_to_cyan, interval=0.05)
    time.sleep(1)
    Write.Print("Gmail OSINT complete!\n", Colors.green_to_black, interval=0.05)

def temp_mail():
    Write.Print("Generating temporary email...\n", Colors.blue_to_cyan, interval=0.05)
    time.sleep(1)
    Write.Print("Temporary email generated!\n", Colors.green_to_black, interval=0.05)

def database_search():
    Write.Print("Searching in database...\n", Colors.blue_to_cyan, interval=0.05)
    time.sleep(1)
    Write.Print("Database search complete!\n", Colors.green_to_black, interval=0.05)

def check_website():
    Write.Print("Checking website status...\n", Colors.blue_to_cyan, interval=0.05)
    time.sleep(1)
    Write.Print("Website check complete!\n", Colors.green_to_black, interval=0.05)

def dos_attack():
    Write.Print("Executing DOS attack...\n", Colors.blue_to_cyan, interval=0.05)
    time.sleep(1)
    Write.Print("DOS attack simulated!\n", Colors.green_to_black, interval=0.05)

def ip_attack():
    Write.Print("Executing IP attack...\n", Colors.blue_to_cyan, interval=0.05)
    time.sleep(1)
    Write.Print("IP attack simulated!\n", Colors.green_to_black, interval=0.05)

def check_url():
    Write.Print("Checking URL...\n", Colors.blue_to_cyan, interval=0.05)
    time.sleep(1)
    Write.Print("URL check complete!\n", Colors.green_to_black, interval=0.05)

def check_mac_address():
    Write.Print("Checking MAC address...\n", Colors.blue_to_cyan, interval=0.05)
    time.sleep(1)
    Write.Print("MAC address check complete!\n", Colors.green_to_black, interval=0.05)

def xss_vulnerability_scan():
    Write.Print("Running XSS vulnerability scan...\n", Colors.blue_to_cyan, interval=0.05)
    time.sleep(1)
    Write.Print("XSS vulnerability scan complete!\n", Colors.green_to_black, interval=0.05)

# Основная функция программы
def main():
    print_banner()
    print_info()
    main_menu()
    while True:
        choice = input(Colorate.Horizontal(Colors.white_to_green, "RoseDe> "))
        
        if choice == "1":
            check_phone()
        elif choice == "2":
            check_ip()
        elif choice == "3":
            validate_email()
        elif choice == "4":
            about_software()
        elif choice == "5":
            ahc_decrypt()
        elif choice == "6":
            info_website()
        elif choice == "7":
            password_generator()
        elif choice == "8":
            xss_scan()
        elif choice == "9":
            port_scanner()
        elif choice == "10":
            exit_programm()
            break
        elif choice == "11":
            get_proxy()
        elif choice == "12":
            gmail_osint()
        elif choice == "13":
            temp_mail()
        elif choice == "14":
            database_search()
        elif choice == "15":
            check_website()
        elif choice == "16":
            dos_attack()
        elif choice == "17":
            ip_attack()
        elif choice == "18":
            check_url()
        elif choice == "19":
            check_mac_address()
        elif choice == "20":
            xss_vulnerability_scan()
        else:
            print(Colorate.Horizontal(Colors.red_to_purple, (animator.say(None, "I don't now this command!"))))
            continue

# Запуск программы
if __name__ == "__main__":
    main()