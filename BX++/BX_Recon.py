from colorama import Style, Fore, init; init()
import requests; import time; import os; import subprocess; import sys
from datetime import datetime
from load import load;
from cmd_usfetch import fetch, Print_lines
from cmd_servernuker import Get_Info
from joiner import B

B()

def cmds_help():
    helpText = f"""
{Fore.MAGENTA}<sys> HELP / -h {Fore.CYAN}: Displays this help text.{Style.RESET_ALL}
{Fore.MAGENTA}<sys> CLEAR / -cls {Fore.CYAN}: Clears the console.{Style.RESET_ALL}
{Fore.MAGENTA}<sys> EXIT / -l / Alt + F4 {Fore.CYAN}: Exits the program. The command is safer{Style.RESET_ALL}
{Fore.MAGENTA}-fetch_usernames / -f {Fore.CYAN}: Fetches the same username for many Websites (Social Media).{Style.RESET_ALL}
{Fore.MAGENTA}-ServerNuker / -SN {Fore.CYAN}: Can nuke an discord server. By using a bot.{Style.RESET_ALL}
                """
    print(helpText)
    return main()
Intro = """
                                                            ___        
                                             ________.-----''          
                                    ___.--'""___.----''                
                                 .-'    _.-'"                          
                      _ .-.__.--'    .-'                               
                    .' `  / ' __ _.-'                                  
                    ) '  '   )   /`-._.                                
                   (.'\          )/))-)\                               
                 .'    >.________.--'                                  
              .-'   .-'                                                
            .'    .'             ______   __
         .-'   .-'              |  _ \ \ / /_     _   
       .'    .'                 | |_) \ V /| |_ _| |_ 
      /    .'                   |  _ < > <_   _|_   _|
    .'   .'                     | |_) / . \|_|   |_|  
   /  ,,/                       |____/_/ \_\ 
  /'''/         ╔════════════════════════════════════════════════════╗
 / ,''          ║   [!]  Author: .brudi (discord)                    ║
/''             ║   [!]  Type 'HELP' or '-h' to see all commands     ║   
                ╚════════════════════════════════════════════════════╝
                ╔════════════════════════════════════════════════════╗
                ║   [TM]              [SETTINGS]            [HELP]   ║
                ╚════════════════════════════════════════════════════╝
"""

value = "╗ ╚ ═ ║ ╔ ╝"
print(Fore.GREEN + Style.BRIGHT + Intro + Style.RESET_ALL)

def clear_text():
    subprocess.call("clear" if os.name == "posix" else "cls", shell=True)
    print(Fore.GREEN + Style.BRIGHT + Intro + Style.RESET_ALL)
    return main()

def program_exit():
    print(f"{Fore.RED}Leaving. . .")
    time.sleep(0.2)
    sys.exit()


def main():
    prompt = input(f"{Fore.YELLOW}┏{Fore.MAGENTA}({Fore.GREEN}BX|PLUS-PLUS{Fore.MAGENTA}){Fore.CYAN}-{Fore.MAGENTA}[{Fore.GREEN}Version.v5.1&cons.py{Fore.MAGENTA}]\n{Fore.YELLOW}┗{Fore.CYAN}# {Fore.LIGHTMAGENTA_EX}")
    if prompt in ["HELP", "-h"]:
        cmds_help()

    elif prompt in ["CLEAR", "-cls"]:
        clear_text()
    
    elif prompt == "TM":
        print(f"{Fore.YELLOW}┏{Fore.MAGENTA}({Fore.GREEN}SYSTEM{Fore.MAGENTA}){Fore.CYAN}-{Fore.MAGENTA}[{Fore.GREEN}TM{Fore.MAGENTA}]\n{Fore.YELLOW}┗{Fore.CYAN}>> {Fore.GREEN}Loader by brudi, many scripts from Xvirus, cracked ChatGPT. I made this if someone doesn't believe Xvirus to be real.\n")
        main()
    elif prompt == "SETTINGS":
        print(f"{Fore.YELLOW}┏{Fore.MAGENTA}({Fore.GREEN}SYSTEM{Fore.MAGENTA}){Fore.CYAN}-{Fore.MAGENTA}[{Fore.GREEN}TM{Fore.MAGENTA}]\n{Fore.YELLOW}┗{Fore.CYAN}>> {Fore.GREEN}\n")
        main()
    elif prompt in ["EXIT", "-l"]:
        program_exit()

    elif prompt in ["-fetch_usernames", "-f"]:
        fetch()
        main()

    elif prompt in ["-fetch_library", "-fl"]:
        Print_lines()
        main()
        
    elif prompt in ["ServerNuker", "-SN"]:
        Get_Info()
        main()

    else:
        print(f"{Fore.YELLOW}┏{Fore.MAGENTA}({Fore.GREEN}SYSTEM{Fore.MAGENTA}){Fore.CYAN}-{Fore.MAGENTA}[{Fore.GREEN}OUTPUT{Fore.MAGENTA}]\n{Fore.YELLOW}┗{Fore.CYAN}>> {Fore.RED}No command named like this ):")
        main()

# Not existing function
def fetch_usernames():
    print(f"{Fore.RED}[!] Function name doesn't exist anymore. (fetch_usernames), moved to 'cmd_usfetch'")

if __name__ == "__main__":
    main()