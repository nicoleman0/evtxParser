# EVTX Parser

This script parses Windows Event Log (EVTX) files and extracts the XML representation of each event record.

## Overview

The script utilizes the `python-evtx` library to read and process EVTX files. It iterates through each record in the log file and extracts its XML content. The XML data is then written to a designated output file.

## Features

*   **EVTX Parsing:** Reads and parses EVTX files.
*   **XML Extraction:** Extracts the XML representation of each event record.
*   **Output to File:** Writes the extracted XML data to a specified output file.
*   **Error Handling:** Includes error handling for file not found and other exceptions.

## Prerequisites

*   **Python 3:** This script is written in Python 3.
*   **python-evtx Library:** You need to install the `python-evtx` library. You can install it using pip:

    ```bash
    pip install python-evtx
    ```

## Installation

1.  **Clone the repository:** Clone it to your local machine using HTTPS or SSH.
2. **Install the dependency:** Run `pip install python-evtx`

## Usage

1.  **Place your EVTX file:** Place the EVTX file you want to parse in a location you can access.
2.  **Modify the script:**
    *   Unless you want to parse the default file (which will result in an error), modify the `input_path` variable in the main block of `core.py` to point to your EVTX file.
    *   Redefine the `output_path` variable to change the name of the output file.
3.  **Run the script:** Execute the `core.py` script from your terminal:

    ```bash
    python core.py
    ```

4.  **Check the output:** After the script finishes, you'll find the output XML file (default: `output_file.xml`) in the same directory where you ran the script. This file will contain the XML representation of each event record from the EVTX file.

FYI: The script, by default, will print an error to the console.

This is because there is no "sample" EVTX file to parse through.

## Code Structure

*   **`core.py`:**
    *   **`parse_evtx(file_path, output_path)`:** This function handles the core logic of parsing the EVTX file and writing the XML output.
    *   **`if __name__ == "__main__":`:** This block defines the entry point of the script, sets the default input and output paths, and calls `parse_evtx` if the input file exists.

## Error Handling

The script also includes some basic error handling:

*   **`FileNotFoundError`:** If the specified input EVTX file is not found, an error message is printed to the standard error stream.
*   **`Exception`:** If any other error occurs during the parsing process, a general error message is printed.

## Notes

*   The script assumes that the EVTX file is a valid Windows Event Log file.
*   The output XML file can be quite large, depending on the size of the input EVTX file.
*   The script WILL overwrite the output file if it already exists!
*   You will need to change the default input path to point to a valid path on your system.

## Contributing

If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request!
