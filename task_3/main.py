
from collections import Counter
from pathlib import Path
from datetime import datetime
import sys


def load_logs(file_path: str) -> list:

    list_of_logs_entries = []

    with open (file_path, "r", encoding="utf-8") as fh:
        for line in fh.readlines():
            entry = parse_log_line(line)
            list_of_logs_entries.append(entry)

    return list_of_logs_entries
                 
                

def parse_log_line(line: str) -> dict:

    # Function segregates all entries in log file and checks if  log entries are of correct format 

    log_entries = {}
    message = []

    log_entries["date"] = line.split(" ")[0]
    try:
        datetime.strptime(log_entries["date"], "%Y-%m-%d")
    except:
        raise ValueError ("Not correct log file format")
      
    log_entries["time"] = line.split(" ")[1]
    try:
        datetime.strptime(log_entries["time"], "%H:%M:%S")
    except:
        raise ValueError ("Not correct log file format")
        
    log_entries["type"] = line.split(" ")[2]
    if log_entries["type"] not in ["INFO", "ERROR", "DEBUG", "WARNING"]:
            raise ValueError ("Not correct log file format")
    
    message = " ".join(line.strip("\n").split(" ")[3:])
    log_entries["message"] = message

    return log_entries


def filter_logs_by_level(logs: list, level: str) -> list :

    level = level.upper()

    print (f"\nДеталі логів для рівня {level} :")
    
    for entry in logs:
         if entry["type"] == level:
                print (f"{entry['date']} {entry['time']} - {entry['message']}" )
     


def count_logs_by_level(logs: list) -> dict:
    counts = Counter(entry["type"] for entry in logs)
    return dict(counts)


def display_log_counts(counts: dict):

    print(f"Рівень логування | Кількість")
    print("----------------------------")
    for entry_key, entry_value in counts.items():
        print(f"{entry_key :<16s} |   {entry_value}")


def main():
    try:
        logs = load_logs(Path(sys.argv[1]))
        entry_counts = count_logs_by_level(logs)
        display_log_counts(entry_counts)
        if len(sys.argv) == 3 and sys.argv[2].upper() in ["INFO", "ERROR", "DEBUG", "WARNING"]:
            filter_logs_by_level(logs, sys.argv[2])
            
    except FileNotFoundError:
        print("File not found")

    except Exception as e:
        print (f"Error: {e}")


if __name__ == "__main__":
    main()
