from pathlib import Path
import subprocess
import os
from colorama import Fore, Back, Style, init


'''myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for fileName in myFiles:
    print(Path(r'C:/Users/Al', fileName))'''

path = Path.cwd() #prints the current directory

def sum_dir():
    homeFolder = Path('home/Alejandro')
    subFolder = Path('coding_projects')
    result = homeFolder / subFolder
    print(result)
    print(type(result))
     
    print(f'\n{path}')
    print(f"{type(path)}")

def change_dir():
    try: #changes directories in this case is an unexisting 
        notExistenDir = os.chdir('/home/alejandro/coding_projects/sysinfo/doesNotExist') 
        print(f"{notExistenDir}")

    except FileNotFoundError:
        print(f"[-] Directory not found")

def create_dir():

    name_dir = input('Type the name of the new directory: ').strip() # removes any spaces from a string
    if name_dir == '':
        print(Fore.RED +'[!]'+ Fore.RESET +' you should type something')
        return
    
    new_dir = new_dir = f"{path}/{name_dir}"
    os.makedirs(new_dir, exist_ok=True)

    if os.path.exists(new_dir): 
        print(Fore.CYAN + Style.BRIGHT + "[+] Directory created succesfully" + Fore.RESET)
        for dir in os.listdir('.'):
            if dir == name_dir:
                print(Fore.YELLOW + dir)
            else: print(dir)
    else: print(Fore.RED + "[-] directory not created")

def main():
    subprocess.run(['clear'])
    #change_dir()
    create_dir()

if __name__ == '__main__':
    main()