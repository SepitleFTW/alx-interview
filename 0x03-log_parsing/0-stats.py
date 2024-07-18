#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import re
import sys

def extract_input(input_line):
    '''Extracts sections of a line of an HTTP request log.
    '''
    log_fmt = (
        r'(?P<ip>\S+)\s+'
        r'-\s+'
        r'\[(?P<date>[^\]]+)\]\s+'
        r'"GET\s+/projects/260\s+HTTP/1\.1"\s+'
        r'(?P<status_code>\d{3})\s+'
        r'(?P<file_size>\d+)\s*'
    )
    resp_match = re.fullmatch(log_fmt, input_line)
    if resp_match is not None:
        return {
            'status_code': resp_match.group('status_code'),
            'file_size': int(resp_match.group('file_size')),
        }
    return None

def print_statistics(total_file_size, status_codes_stats):
    '''Prints the accumulated statistics of the HTTP request log.
    '''
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        count = status_codes_stats.get(status_code, 0)
        if count > 0:
            print('{:s}: {:d}'.format(status_code, count), flush=True)

def update_metrics(line, total_file_size, status_codes_stats):
    '''Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.

    Returns:
        int: The new total file size.
    '''
    line_info = extract_input(line)
    if line_info:
        status_code = line_info['status_code']
        if status_code in status_codes_stats:
            status_codes_stats[status_code] += 1
        total_file_size += line_info['file_size']
    return total_file_size

def run():
    '''Starts the log parser.
    '''
    line_num = 0
    total_file_size = 0
    status_codes_stats = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
    try:
        for line in sys.stdin:
            total_file_size = update_metrics(line.strip(), total_file_size, status_codes_stats)
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)

if __name__ == '__main__':
    run()
