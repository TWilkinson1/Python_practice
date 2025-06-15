import re
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime



LOG_PATTERN = re.compile(r'(?P<ip>\S+) \S+ \S+ \[(?P<timestamp>[^\]]+)\] "(?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d{3}) (?P<size>\d+)')

def parse_log_line(line):
    match = LOG_PATTERN.match(line)
    if match:
        data = match.groupdict()
        data['timestamp'] = datetime.strptime(data['timestamp'], '%d/%b/%Y:%H:%M:%S %z')
        return data
    return None


def read_log_file(filepath):
    with open(filepath, 'r') as f: 
        print(filepath)
        return [parse_log_line(line) for line in f if parse_log_line(line) is not None]
    


def summarise_log(logs):
    ip_counter = Counter(log['ip'] for log in logs)
    print(logs)
    status_counter = Counter(log['status'] for log in logs)
    

    print("Top 5 IP addresses:")
    for ip, count in ip_counter.most_common(5):
        print(f"{ip}: {count} requests")

    print("\nStatus code summary:")
    for status, count in status_counter.items():
        print(f"{status}: {count} occurrences")


if __name__ == "__main__":
    logs = read_log_file('access.log')
    if logs:
        summarise_log(logs)
    else:
        print("No valid log entries found.")

def plot_status_codes(logs):
    status_counter = Counter(log['status']for log in logs)
    statuses, counts = zip(*status_counter.items())
    plt.bar(statuses, counts)
    plt.xlabel('Status Codes')
    plt.ylabel('Number of Requests')
    plt.title('HTTP Status Codes Distribution')
    plt.show()