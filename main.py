import os
import sys
from config import *

def main():
    path, output = get_path_from_args()
    data = load_data(path)
    properties = process_properties(data)
    error_logs = process_partition(data, ADDR_ERROR_LOGS, SIZE_RESERVED_ERROR_LOGS, "error")
    other_logs = process_partition(data, ADDR_OTHER_LOGS, SIZE_RESERVED_OTHER_LOGS, "other")
    logs = error_logs + other_logs
    logs.sort(key=lambda x: x[0])
    output_data(output, properties, logs)

def get_path_from_args():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path>")
        sys.exit(1)
    if not os.path.exists(sys.argv[1]):
        print("Specified file does not exist")
        sys.exit(1)
    path = sys.argv[1]
    output = None
    if len(sys.argv) == 4 and sys.argv[2] == "-o":
        output = sys.argv[3]
    return (path, output)

def load_data(path):
    with open(f'./{path}', 'r') as f:
        data = f.readlines()
        data = [x.strip() for x in data]
        return data

def process_properties(data):
    properties = {}
    properties["Storage type"] = process_property_segment(data, ADDR_STORAGE_TYPE, SIZE_STORAGE_TYPE)
    properties["Serial number"] = process_property_segment(data, ADDR_SERIAL_NUMBER, SIZE_SERIAL_NUMBER)
    properties["Flash timestamp"] = process_property_segment(data, ADDR_FLASH_TIMESTAMP, SIZE_FLASH_TIMESTAMP)
    properties["PW cycles"] = process_property_segment(data, ADDR_PW_CYCLES, SIZE_PW_CYCLES)
    properties["Usage cycles"] = process_property_segment(data, ADDR_USAGE_CYCLES, SIZE_USAGE_CYCLES)
    properties["Settings"] = process_property_segment(data, ADDR_SETTINGS, SIZE_SETTINGS)
    return properties

def process_property_segment(data, start, length):
    end = start + length
    segment = data[start:end]
    segment = [int(x, 16) for x in segment]
    return segment

def process_partition(data, start, length, type):
    end = start + length
    log_next = int(''.join(data[start:start + SIZE_LOG_NEXT]), 16)
    log_entries = []

    for i in range(start + SIZE_LOG_NEXT, log_next, SIZE_LOG_ENTRY):
        entry = data[i:i + SIZE_LOG_ENTRY]
        if len(entry) < SIZE_LOG_ENTRY:
            break
        log_entries.append(process_log(entry, type))
    return log_entries


def process_log(entry, type):
    if len(entry) < SIZE_LOG_ENTRY:
        return None
    timestamp = int(''.join(entry[0:4]), 16)
    flag = int(entry[4], 16)
    content = entry[5:]
    content_text = ''.join([chr(int(x, 16)) for x in content])
    return (timestamp, flag, content_text, type)

def format_log(log):
    return f"[{log[3]}] {log[0]} flag {log[1]}: {log[2]}"

def output_data(filename, properties, logs):
    if filename is None:
        for key, value in properties.items():
            print(f"{key}: {value}")
        print("─" * os.get_terminal_size().columns)
        for log in logs:
            print(format_log(log))
    else:
        with open(f'./{filename}', 'w') as f:
            for key, value in properties.items():
                f.write(f"{key}: {value}\n")
            f.write("─" * 20 + "\n")
            for log in logs:
                f.write(format_log(log) + "\n")
        print(f"Data written to {filename}")


if __name__ == '__main__':
    main()