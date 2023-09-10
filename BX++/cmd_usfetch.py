from colorama import Style, Fore, init
import requests; import os
from datetime import datetime
from resources.Database import links
init()

class URLChecker:
    def __init__(self, urls):
        self.urls = urls

    def check_urls_existence(self, username):
        start_time = datetime.now()
        TotalFound = 0
        for name, url_format in self.urls.items():
            if '{}' in url_format:
                url = url_format.format(username)
                try:
                    response = requests.head(url)
                    if response.status_code == 200:
                        print(f"{Fore.LIGHTCYAN_EX}[{Style.RESET_ALL}+{Fore.LIGHTCYAN_EX}] {Style.RESET_ALL}{name}: {Fore.LIGHTCYAN_EX}Found! {Style.RESET_ALL}{url}")
                        TotalFound += 1
                    else:
                        print(f"{Fore.YELLOW}[{Style.RESET_ALL}-{Fore.YELLOW}] {Style.RESET_ALL}{name}: {Fore.YELLOW}Not found. {Style.RESET_ALL}{url}")
                except requests.ConnectionError:
                    print(f"{Fore.RED}[{Style.RESET_ALL}!{Fore.RED}] {Style.RESET_ALL}{name}: {Fore.RED}Could not be reached. {Style.RESET_ALL}'{url}' {Fore.RED}There is a temporary network issue. OR the URL is not available{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}[{Style.RESET_ALL}-{Fore.YELLOW}] {Style.RESET_ALL}{name}: {Fore.YELLOW}URL template does not contain '{{}}'. {Style.RESET_ALL}{url_format}")
        end_time = datetime.now()
        elapsed_time = end_time - start_time
        elapsed_ms = elapsed_time.total_seconds() * 1000
        elapsed_s = elapsed_time.total_seconds()
        print(f"{Fore.LIGHTCYAN_EX}[{Style.RESET_ALL}*{Fore.LIGHTCYAN_EX}]: {Fore.LIGHTCYAN_EX}Finished, checking usernames. {Fore.GREEN}Total found: {TotalFound} in ({Fore.LIGHTCYAN_EX}{elapsed_ms:.2f} ms, {elapsed_s:.2f} s{Fore.GREEN}){Style.RESET_ALL}\n")

def fetch():
    print("[~] 'URL Checker (fetcher)' was booted from library: 'cmd_usfetch.py'")
    print(f"{Fore.RED}[!] WARNING! The current username fetcher is NOT up-to-date, there could be some errors.\n")
    username = input(f"{Fore.LIGHTCYAN_EX}[{Style.RESET_ALL}?{Fore.LIGHTCYAN_EX}] Enter Username : {Style.RESET_ALL}")
    if username:
        print("\n")
    
    url_checker = URLChecker(links)
    url_checker.check_urls_existence(username)

def Print_lines():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    resources_directory = os.path.join(script_directory, "resources")
    file_path = os.path.join(resources_directory, "Database.py")

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

    # Print the lines under the specified text
        print(f"{Fore.CYAN}[!] Printing lines from the file:")
        for line in lines[1:-1]:
            print(f"{Fore.LIGHTGREEN_EX}=> ", line.strip(), {Style.RESET_ALL})

    except FileNotFoundError:
        print(f"{Fore.RED}[!] File not found.")
    except Exception as e:
        print(f"{Fore.RED}[!] An error occurred:", e)