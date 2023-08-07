#! /usr/bin/env python3

import os 
import re
import csv

# Initialize dictionaries
error_dict = {}
user_dict = {}

# Parse log entries in syslog.log file
with open("syslog.log", "r") as file:
    for line in file:
        match_error = re.search(r"ERROR (.+?) \((\w+)\)$", line)
        match_info = re.search(r"INFO (.+?) \((\w+)\)$", line)

        if match_error:
            error = match_error.group(1)
            username = match_error.group(2)
            error_dict[error] = error_dict.get(error, 0) + 1
            if username in user_dict:
                user_dict[username]["ERROR"] += 1
            else:
                user_dict[username] = {"INFO": 0, "ERROR": 1}
        elif match_info:
            info = match_info.group(1)
            username = match_info.group(2)
            if username in user_dict:
                user_dict[username]["INFO"] += 1
            else:
                user_dict[username] = {"INFO": 1, "ERROR": 0}

# Sort error dictionary by count
sorted_errors = sorted(error_dict.items(), key=lambda x: x[1], reverse=True)
sorted_errors.insert(0, ("Error", "Count"))

# Sort user dictionary by username
sorted_users = sorted(user_dict.items())

# Create error_message.csv
with open("error_message.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(sorted_errors)

# Create user_statistics.csv
with open("user_statistics.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Username", "INFO", "ERROR"])
    for user, data in sorted_users:
        writer.writerow([user, data["INFO"], data["ERROR"]])
