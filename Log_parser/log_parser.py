import re
from collections import Counter
from datetime import datetime

LOG_PATTERN = re.compile(r'(?P<ip>\S+) \S+ \[(?P<timestams>[^\]]+)\]" (?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d{3}) (?P<size>\d+)')

def parse_log_line(line):

def read_log_file():

def summarise_log()