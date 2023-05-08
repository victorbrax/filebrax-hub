from datetime import datetime
import os

def get_size(folder_path):
    
    total_size = 0
    for path, dirs, files in os.walk(folder_path):
        for f in files:
            fp = os.path.join(path, f)
            total_size += os.path.getsize(fp)
    return total_size

def format_size(size_bytes):
    """Format a size given in bytes to a more human-readable form."""
    power = 1024
    power_labels = {0: '', 1: 'K', 2: 'M', 3: 'G', 4: 'T', 5: 'P'}
    size = float(size_bytes)
    index = 0
    while size >= power and index < len(power_labels):
        size /= power
        index += 1
    size_str = '{:.2f}'.format(size)
    label = power_labels[index] + 'B'
    return f'{size_str} {label}'


def format_date(timestamp):
    """Format a date given in seconds since the epoch to a more human-readable form."""
    return datetime.fromtimestamp(timestamp).strftime('%d/%m/%y %H:%M')
