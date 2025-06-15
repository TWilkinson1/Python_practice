import re
from collections import Counter
from datetime import datetime

LOG_PATTERN = re.compile(r'(?P<ip>\S+) \S+ \[(?P<timestams>[^\]]+)\]" (?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d{3}) (?P<size>\d+)')

def parse_log_line(line):
    match = LOG_PATTERN.match(line)
    if match:
        data = match.groupdict()
        data['timestamp'] = datetime.strptime(data['timestams'], '%d/%b/%Y:%H:%M:%S %z')
        return data
    return None

def read_log_file():

def summarise_log()