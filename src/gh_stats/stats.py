from collections import Counter


class Statblock:
    def __init__(self):
        self.username = ""
        self.count = 0

        self.month_count = 0
        self.month = ""  # String so it can hold leading zeros
        self.month_name = ""

        self.projects = Counter()
