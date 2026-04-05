''''import platform
import os
import argparse
import subprocess

def getOsInfo():
    try:
        return {
            "system" : platform.system(),
            "version" : platform.version(),
            "release": platform.release(),
            "machine": platform.machine(),
            "processor" :platform.processor(),
            "user": os.getlogin
        }
    except Exception as e:
        print(f"[-]Error: {type}(e)")


class Logger:
    def __init__(self, name):
      self.name = name
      self.ips = []
    
    def add_ip(self, ip):
        self.ips.append(ip)

    def show(self):
        print(f"[*] Logger: {self.name}")
        for i, ip in enumerate(self.ips, 1):
            print(f"[{i}] {ip}")
      


def main():
    subprocess.run(['clear'])
    log = Logger("my_logger")
    log.add_ip("192.168.1.1")
    log.add_ip("8.8.8.8")
    log.add_ip("45.33.32.156")
    log.show()



if __name__ == '__main__':
    main()

    '''