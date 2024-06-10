import argparse
import requests

import pyfiglet
print("***************************************************************************************************************************************************")
from colorama import Fore, Style
print(Fore.RED)

def tiger_art():
    # Large ASCII art of a tiger
    print("""
                                                                         __,__
                                                                .--.  .-"     "-.  .--.
                                                              / .. \/  .-. .-.  \/ .. \
                                                             | |  '|  /   Y   \  |'  | |
                                                             | \   \  \ 0 | 0 /  /   / |
                                                              \ '- ,\.-"""""""-./, -' /
                                                               ''-' /_   ^ ^   _\ '-''
                                                                   |  \._   _./  |
                                                                   \   \ '~' /   /
                                                                    '._ '-=-' _.'
                                                                       '-----'
    """)

tiger_art()
print("***************************************************************************************************************************************************")
parser = argparse.ArgumentParser(description="Check status codes of HTTP and HTTPS domains.")
parser.add_argument("-f", help="Path to the text file containing domains to check")
args = parser.parse_args()

# Read the domains from the file
file = open(args.f, "r")
domains = file.readlines()
for domain in domains:
    domain = domain.strip()
    try:
        # Check Status for HTTP
        http_response = requests.head("http://" + domain, allow_redirects=True, timeout=10)
        http_status_code = http_response.status_code

        # Check HTTPS
        https_response = requests.head("https://" + domain, allow_redirects=True, timeout=10)
        https_status_code = https_response.status_code

        # Print status codes
        if http_status_code == 200:
            print(f"Domain: http://{domain}-Status Code: 200 (OK)")
        elif https_status_code in [301, 302]:
            print(f"Domain: https{domain}-Status Code: {http_status_code} (Redirect)")
        
        elif http_status_code == 403:
            print(f"Domain: http://{domain}-Status Code: 403 (Forbidden)")
        else:
            print(f"Domain: http://{domain}-Status Code: {http_status_code}")
	    

#        if https_status_code == 200:
#            print(f"Domain: https://{domain}-Status Code: 200 (OK)")
#        elif https_status_code in [301, 302]:
#            print(f"Domain: https://{domain}-Status Code: {https_status_code} (Redirect)")
#        elif https_status_code == 403:
#            print(f"Domain: https://{domain}-Status Code: 403 (Forbidden)")
#        else:
#            print(f"Domain: https://{domain}-Status Code: {https_status_code}")

    except requests.RequestException as e:
            print(f"Domain: {domain} - Error: {e}")

file.close()
