#!/usr/bin/env python3

import re
import sys

def extract_sections(text):
    # Split the text by double newline to identify possible sections
    sections = re.split(r'\n\n+', text)
    
    # Filter out the sections that are not in ALLCAPS
    news_sections = [section for section in sections if section.split("\n")[0].isupper()]
    
    return news_sections

def main():
    # Read text from stdin
    text = sys.stdin.read()
    
    news_sections = extract_sections(text)
    
    for index, section in enumerate(news_sections, 1):
        filename = f'chunk_{index:02}.txt'
        with open(filename, 'w') as f:
            f.write(section)
    
    print(f'{len(news_sections)} news sections written to chunk files.')

if __name__ == '__main__':
    main()
