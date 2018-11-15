from collections import namedtuple
from itertools import combinations


# https://stackoverflow.com/a/9044111
# User: Raymond Hettinger
# https://stackoverflow.com/users/1001643/raymond-hettinger
Range = namedtuple('Range', ['start', 'end'])

def overlap_days(r1, r2):
    """number of overlap days of two ranges"""
    latest_start = max(r1.start, r2.start)
    earliest_end = min(r1.end, r2.end)
    delta = (earliest_end - latest_start).days + 1
    overlap = max(0, delta)
    return overlap

def ranges_overlap(ranges):
    """check if ranges overlap with each other"""
    for r1, r2 in combinations(ranges, 2):
        if overlap_days(r1, r2):
            return True
    return False

def in_range(r1, r2):
    """check if r1 is in the range of r2"""
    return r1.start >= r2.start and r1.end <= r2.end

def all_in_range(ranges, r2):
    """check if all ranges are in range of r2"""
    return all(in_range(r1, r2) for r1 in ranges)
