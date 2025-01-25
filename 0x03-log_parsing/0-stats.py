#!/usr/bin/python3
"""
Log Parsing
"""

import sys

def print_stats(stats: dict, file_size: int) -> None:
    """
    Prints the statistics including file size and status code counts.
    """
    print(f"File size: {file_size}")
    for code, count in sorted(stats.items()):
        if count > 0:
            print(f"{code}: {count}")

def process_line(line: str, stats: dict) -> int:
    """
    Processes a single log line, updating stats and returning the file size increment.
    """
    try:
        parts = line.split()
        status_code = parts[-2]
        file_size = int(parts[-1])
        
        if status_code in stats:
            stats[status_code] += 1
        return file_size
    except (IndexError, ValueError):
        return 0

if __name__ == "__main__":
    total_file_size = 0
    log_count = 0
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {code: 0 for code in status_codes}

    try:
        for line in sys.stdin:
            log_count += 1
            total_file_size += process_line(line, stats)
            
            if log_count % 10 == 0:
                print_stats(stats, total_file_size)
        
        # Print final stats after processing all lines
        print_stats(stats, total_file_size)
    
    except KeyboardInterrupt:
        # Handle interruption gracefully and print stats before exiting
        print_stats(stats, total_file_size)
        raise

