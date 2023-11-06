# Test Search Thyssenkrupp with Python and pytest

This README provides instructions for installing the required Python packages and running a pytest test case named `test_search_thyssenkrupp` that searches for the keyword "Thyssenkrupp."

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python: You can download and install Python 3.9 or above from [python.org](https://www.python.org/downloads/).
- `pip`: The Python package manager, which is usually included with Python.

## Installation

1. Clone this repository or download the code to your local machine.

2. Open a terminal or command prompt and navigate to the project directory.

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate

## Install the required packages using the requirements.txt file:
Run the  Command Below
  ```bash
    pip install -r requirements.txt

## Running the Test
Make sure you are in the project directory and your virtual environment is activated.

To run the test_search_thyssenkrupp test using pytest, execute the following command:
    pytest -k test_google_search.py
