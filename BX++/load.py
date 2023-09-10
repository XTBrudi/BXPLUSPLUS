from colorama import Fore, init; init()
import time
from datetime import datetime

def load():
    print(f"{Fore.YELLOW}┏{Fore.MAGENTA}({Fore.GREEN}SYSTEM{Fore.MAGENTA}){Fore.CYAN}-{Fore.MAGENTA}[{Fore.GREEN}OUTPUT{Fore.MAGENTA}]\n{Fore.YELLOW}┗{Fore.CYAN}>> {Fore.YELLOW}LOADING BX-Recon [{datetime.now()}]")
    time.sleep(0.2)
    print(f"{Fore.YELLOW}┏{Fore.MAGENTA}({Fore.GREEN}SYSTEM{Fore.MAGENTA}){Fore.CYAN}-{Fore.MAGENTA}[{Fore.GREEN}OUTPUT{Fore.MAGENTA}]\n{Fore.YELLOW}┗{Fore.CYAN}>> {Fore.YELLOW}LOADING Librarys. . . [{datetime.now()}]")
    time.sleep(0.1)
    print(f"{Fore.YELLOW}┏{Fore.MAGENTA}({Fore.GREEN}SYSTEM{Fore.MAGENTA}){Fore.CYAN}-{Fore.MAGENTA}[{Fore.GREEN}OUTPUT{Fore.MAGENTA}]\n{Fore.YELLOW}┗{Fore.CYAN}>> {Fore.YELLOW}Libs up to date, py up to date. LOADING PY-Libs [{datetime.now()}]")
    time.sleep(0.1)
    print(f"{Fore.YELLOW}┏{Fore.MAGENTA}({Fore.GREEN}SYSTEM{Fore.MAGENTA}){Fore.CYAN}-{Fore.MAGENTA}[{Fore.GREEN}OUTPUT{Fore.MAGENTA}]\n{Fore.YELLOW}┗{Fore.CYAN}>> {Fore.YELLOW}LOADED : time, colorama, requests, datetime, Load, sys, os, more. . . [{datetime.now()}]")
    time.sleep(0.3)
    print(f"{Fore.YELLOW}┏{Fore.MAGENTA}({Fore.GREEN}SYSTEM{Fore.MAGENTA}){Fore.CYAN}-{Fore.MAGENTA}[{Fore.GREEN}OUTPUT{Fore.MAGENTA}]\n{Fore.YELLOW}┗{Fore.CYAN}>> {Fore.GREEN}Finished. You may continue now.\n")