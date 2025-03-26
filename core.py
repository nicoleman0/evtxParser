import os
import sys

from Evtx.Evtx import Evtx


def parse_evtx(file_path, output_path):
    """
    Parses an EVTX file and writes the XML representation of each record to an output file.

    Args:
        file_path (str): The path to the input EVTX file.
        output_path (str): The path to the output XML file.
    """
    try:
        with Evtx(file_path) as log, open(output_path, 'w', encoding='utf-8') as output_file:
            for record in log.records():
                output_file.write(record.xml() + "\n")
        print(f"Parsed data written to {output_path}")
    except FileNotFoundError:
        print(f"Error: Input file not found at {file_path}", file=sys.stderr)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    input_path = os.path.join(os.path.expanduser(
        "~"), "unit42", "Microsoft-Windows-Sysmon-Operational.evtx")
    output_path = "output_file.xml"
    if os.path.exists(input_path):
        parse_evtx(input_path, output_path)
    else:
        print(f"Error: Input file not found at {input_path}", file=sys.stderr)
