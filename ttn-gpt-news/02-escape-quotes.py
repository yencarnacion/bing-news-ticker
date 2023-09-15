#!/usr/bin/env python3

import glob
import os

def escape_quotes(file_name, output_file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            contents = file.read()
            
            # Escape different types of quotes
            contents = contents.replace('"', '&quot;')
            contents = contents.replace('“', '&quot;')
            contents = contents.replace('”', '&quot;')
            
            with open(output_file_name, 'w', encoding='utf-8') as output_file:
                output_file.write(contents)

            print(f"Processed {file_name} and saved to {output_file_name}")
            
    except FileNotFoundError:
        print(f"File {file_name} not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    files = glob.glob('chunk_*.txt')  # This will get all files starting with 'chunk_'
    for file_name in files:
        output_file_name = "clean-" + file_name
        escape_quotes(file_name, output_file_name)
