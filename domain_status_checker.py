import argparse
import requests
import concurrent.futures
import nmap

def check_domain(domain, timeout):
    results = []
    try:
        # Check HTTP
        http_response = requests.head("http://" + domain, allow_redirects=True, timeout=timeout)
        http_status_code = http_response.status_code
        http_headers = http_response.headers

        # Check HTTPS
        https_response = requests.head("https://" + domain, allow_redirects=True, timeout=timeout)
        https_status_code = https_response.status_code
        https_headers = https_response.headers

        # Vulnerability Scan using nmap
        scanner = nmap.PortScanner()
        scanner.scan(domain)
        vulnerabilities = scanner.all_hosts()

        # Additional checks can be added here based on headers, response content, etc.
        results.append({
            'domain': domain,
            'http_status_code': http_status_code,
            'http_headers': http_headers,
            'https_status_code': https_status_code,
            'https_headers': https_headers,
            'vulnerabilities': vulnerabilities
        })
    except requests.RequestException as e:
        results.append({'domain': domain, 'error': str(e)})
    return results

def main():
    parser = argparse.ArgumentParser(description="Check status codes of HTTP and HTTPS domains and perform vulnerability scanning.")
    parser.add_argument("-f", help="Path to the text file containing domains to check", required=True)
    parser.add_argument("--timeout", type=int, default=10, help="Timeout for HTTP requests (default: 10)")
    parser.add_argument("--workers", type=int, default=10, help="Number of concurrent workers (default: 10)")
    args = parser.parse_args()

    # Read the domains from the file
    with open(args.f, "r") as file:
        domains = [line.strip() for line in file]

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        future_to_domain = {executor.submit(check_domain, domain, args.timeout): domain for domain in domains}
        for future in concurrent.futures.as_completed(future_to_domain):
            domain = future_to_domain[future]
            try:
                results.extend(future.result())
            except Exception as e:
                results.append({'domain': domain, 'error': str(e)})

    # Output results
    for result in results:
        if 'error' in result:
            print(f"Domain: {result['domain']} - Error: {result['error']}")
        else:
            print(f"Domain: {result['domain']} - HTTP Status Code: {result['http_status_code']} - HTTPS Status Code: {result['https_status_code']}")
            print(f"HTTP Headers: {result['http_headers']}")
            print(f"HTTPS Headers: {result['https_headers']}")
            print(f"Vulnerabilities: {result['vulnerabilities']}")

if __name__ == "__main__":
    main()

