                                            Domain Status Checker

This Python script checks the status codes of HTTP and HTTPS domains listed in a text file and prints the results to the console.
![image](https://github.com/ketansonwane1/Domain-Status-Code-Checker/assets/141003493/09fc5a2d-a73c-4997-965e-1066bf3a74bf)


## Overview

The Domain Status Checker script is a simple tool built in Python that allows you to quickly check the status of multiple domains, including their HTTP and HTTPS endpoints. It's particularly useful for website administrators, developers, or anyone who needs to monitor the status of a list of domains.

## Features

- **HTTP and HTTPS Support**: The script can check both HTTP and HTTPS endpoints for each domain.
- **Status Code Information**: It provides detailed status code information, including OK, Redirect (301/302), Forbidden (403), and other status codes.
- **Error Handling**: The script handles common request errors gracefully and provides error messages for domains that couldn't be checked.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x: The script is written in Python 3.
- Requests library: This script utilizes the Requests library for making HTTP requests. Install it using `pip install requests`.
- Colorama library: The Colorama library is used for terminal text colorization. Install it using `pip install colorama`.

## Usage

1. **Clone the Repository**: Begin by cloning the repository to your local machine:

    ```bash
    gi clone https://github.com/ketansonwane1/Domain-Status-Checker/

    ```

2. **Navigate to the Project Directory**: Use the `cd` command to move into the project directory:

    ```bash
    cd your_repository
    ```

3. **Run the Script**: Execute the script using Python, specifying the path to the text file containing the list of domains to check:

    ```bash
    python domain_status_checker.py -f domains.txt
    ```

    Replace `domains.txt` with the path to your text file containing the list of domains.

## Contributing

Contributions to this project are welcome! If you'd like to contribute, follow these steps:

1. **Fork the Repository**: Fork the repository to your GitHub account.
2. **Create a Branch**: Create a new branch for your feature or bug fix.
3. **Make Changes**: Make your changes to the codebase.
4. **Commit Changes**: Commit your changes with clear and concise commit messages.
5. **Push Changes**: Push your changes to your forked repository.
6. **Open a Pull Request**: Submit a pull request with your changes, describing the rationale and any considerations.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- ASCII art of a tiger created using [pyfiglet](https://github.com/pwaller/pyfiglet)
- [Colorama](https://github.com/tartley/colorama) library for terminal text colorization

## Contact

If you have any questions, issues, or suggestions regarding the script, feel free to contact the project maintainer at ketansonwane421@gmail.com.

---

This README provides comprehensive information about the script, its usage, contributing guidelines, license, acknowledgments, and contact details. Feel free to customize it further to suit your specific needs.
