import argparse
import threading
import socket
import requests
from colorama import Fore

def banner():
    print("************************************************************************************************************************************************************")
    print(Fore.CYAN)
    print('''      
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
    
        |------------------------------------------------------------Coded by Ketan-------------------------------------------------------------------|
    ''') 
    print("                                                       Github: https://github.com/ketansonwane1                                                          ")
    print("************************************************************************************************************************************************************")

def print_status(message, color=Fore.WHITE):
    print(f"{color}{message}{Fore.RESET}")

def dns_resolution(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return None

def check_http_status(domain, timeout):
    try:
        http_response = requests.head(f"http://{domain}", allow_redirects=True, timeout=timeout)
        return http_response.status_code
    except requests.RequestException:
        return None

def check_https_status(domain, timeout):
    try:
        https_response = requests.head(f"https://{domain}", allow_redirects=True, timeout=timeout)
        return https_response.status_code
    except requests.RequestException:
        return None

def check_port(ip_address, port, timeout):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((ip_address, port))
            return result == 0
    except socket.error:
        return False

def scan_domain(domain, ports, timeout):
    ip_address = dns_resolution(domain)
    if ip_address:
        #print_status(f"Scanning domain: {domain} [{ip_address}]", Fore.GREEN)
        http_status = check_http_status(domain, timeout)
        https_status = check_https_status(domain, timeout)
        #if http_status:
            #print_status(f"Domain: http://{domain} - Status Code: {http_status}")
        #if https_status:
            #print_status(f"Domain: https://{domain} - Status Code: {https_status}")
        for port in ports:
            if check_port(ip_address, port, timeout):
                print_status(f"Port {port} is open on {domain} Status Code is {http_status} ", Fore.GREEN)
                print_status(f"Port {port} is open on {domain} Status Code is {https_status} ", Fore.GREEN)
            else:
                print_status(f"Port {port} is closed on {domain} Status Code is {http_status}", Fore.RED)
                print_status(f"Port {port} is closed on {domain} Status Code is {https_status}",Fore.RED)
    else:
        print_status(f"Domain: {domain} - DNS resolution failed", Fore.YELLOW)

def main():
    banner()
    print("Port Scanning is started")
    parser = argparse.ArgumentParser(description="Check status codes of HTTP and HTTPS domains.")
    parser.add_argument("-f", help="enter Valid filename")
    parser.add_argument("-p", nargs="+", type=int, help="ports to scan", default=[80, 443])  
    parser.add_argument("-t", type=float, help="timeout for port scanning", default=10.0)
    args = parser.parse_args()

    with open(args.f, "r") as file:
        domains = [line.strip() for line in file.readlines()]

    threads = []
    for domain in domains:
        thread = threading.Thread(target=scan_domain, args=(domain, args.p, args.t))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print_status("--------------------------------------------------------------------Thank-you------------------------------------------------------------------------------", Fore.GREEN)
main()
