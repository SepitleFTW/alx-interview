import sys
import signal

# Initialize variables
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    global total_size, status_counts
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Register signal handler for keyboard interruption (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) != 7:
                continue

            ip, dash, date, request, status, size = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5]

            # Check format
            if dash != "-" or not date.startswith("[") or not date.endswith("]") or not request.startswith('"GET') or not request.endswith('HTTP/1.1"'):
                continue

            # Convert status and size to integers
            status = int(status)
            size = int(size)

            # Update total size
            total_size += size

            # Update status counts
            if status in status_counts:
                status_counts[status] += 1

            line_count += 1

            # Print stats after every 10 lines
            if line_count % 10 == 0:
                print_stats()

        except ValueError:
            continue

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
