from Evtx.Evtx import Evtx
from Evtx.Views import evtx_file_xml_view


def parse_evtx(file_path, output_path):
    with Evtx(file_path) as log, open(output_path, 'w', encoding='utf-8') as output_file:
        for record in log.records():
            output_file.write(record.xml() + "\n")
    print(f"Parsed data written to {output_path}")


if __name__ == "__main__":
    input_path = "/home/nicholas-coleman/unit42/Microsoft-Windows-Sysmon-Operational.evtx"
    output_path = "output_file.xml"
    parse_evtx(input_path, output_path)
