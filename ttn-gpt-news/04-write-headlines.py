#!/usr/bin/env python3

import json
import glob

def combine_json_files():
    # Identify all the files with the pattern clean-chunk_*.json
    file_names = glob.glob('clean-chunk_*.json')
    # Sort the filenames to process them in order
    file_names = sorted(file_names, key=lambda x: int(x.split('_')[-1].split('.')[0]))

    combined_data = []

    for file_name in file_names:
        with open(file_name, 'r') as file:
            # Load the JSON data from the file
            data = json.load(file)
            # Append the data to the main list
            combined_data.extend(data)

    # Save the combined data to headlines.json
    with open('headlines.json', 'w') as outfile:
        json.dump(combined_data, outfile, indent=4)

if __name__ == "__main__":
    combine_json_files()

