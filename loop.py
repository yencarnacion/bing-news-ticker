#!/usr/bin/env python3

import time
import os
from datetime import datetime

# List of .py files to execute
files_to_execute = [
    "ai-health.py",
    "pr-news-es.py",
    "top-news.py",
    "business-news.py",
    "other-news.py",
    "pr-news-en.py",
    "tech-news.py"
]

# Time interval (initially 10 minutes)
x = 600

while True:
    for file in files_to_execute:
        # Get the current time
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Print the name of the file being executed along with the current time
        print(f"[{current_time}] Running {file}...")
        
        # Execute the .py file
        os.system(f"python3 ./{file}")
        
        # Wait for x seconds before executing the next file
        time.sleep(x)
