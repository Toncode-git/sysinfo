from pathlib import Path
import subprocess
import os

subprocess.run(['clear'])

'''myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for fileName in myFiles:
    print(Path(r'C:/Users/Al', fileName))'''

homeFolder = Path('home/Alejandro')
subFolder = Path('coding_projects')

result = homeFolder / subFolder

print(result)
print(type(result))

path = Path.cwd()
print(f'\n{path}')
print(f"{type(path)}")

try:
    notExistenDir = os.chdir('/home/alejandro/coding_projects/sysinfo/doesNotExist')
    print(f"{notExistenDir}")

except FileNotFoundError:
    print(f"[-] Directory not found")