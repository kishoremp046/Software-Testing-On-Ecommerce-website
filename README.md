# BeYoung Website Automation Tests

## Overview
This repository contains automated test scripts for the [BeYoung](https://www.beyoung.in/) website using Selenium and Python's `unittest` framework. The scripts perform UI testing by verifying page elements, navigation, search functionality, and cart operations.

## Features Tested
- **Title Verification**: Checks if the page title contains "Beyoung".
- **Browser Actions**: Maximizing, navigating forward/backward.
- **Section Navigation**: Clicking on sections like MEN, WOMEN, COMBOS, etc.
- **Search Functionality**: Performing searches and verifying results.
- **Scrolling & Item Selection**: Scrolling through pages and selecting specific items.
- **Cart Operations**: Adding items to the cart and verifying them.

## Prerequisites
Ensure you have the following installed:
- Python (>= 3.x)
- Google Chrome Browser
- Chrome WebDriver (managed via `webdriver-manager`)
- Required Python Packages:
  ```sh
  pip install selenium webdriver-manager
  ```

## How to Run Tests
Clone the repository:
```sh
git clone https://github.com/your-username/beyoung-automation.git
cd beyoung-automation
```
Run the tests using:
```sh
python -m unittest test_beyoung.py
```

## Test File Structure
- **`test_beyoung.py`**: Main test script with multiple test cases.
- **`requirements.txt`**: List of dependencies (optional).

## Notes
- The test script opens the BeYoung website and interacts with UI elements.
- Some elements require waiting due to dynamic loading; implicit/explicit waits are used.
- The test execution logs will be displayed in the console.

## Contributions
Feel free to fork this repository and submit pull requests for improvements.

## License
This project is licensed under the MIT License.

