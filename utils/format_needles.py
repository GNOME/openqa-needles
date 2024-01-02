"""
Script to ensure needle JSON files have consistent formatting.
"""

import os
import json


# This matches the indent used by the openQA web UI's needle editor.
JSON_INDENT = 2


def process_json_files(directory):
    files_with_difference = []

    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)

            with open(file_path, 'r', encoding='utf-8') as file:
                original_content = file.read()

            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                pretty_json = json.dumps(data, indent=JSON_INDENT) + "\n"

                if pretty_json != original_content:
                    files_with_difference.append(filename)
                    print(f"Difference found in file: {filename}")
                    # Show the diff, but you might want a better way to display differences.
                    print(f"Diff: {pretty_json} vs. {original_content}")
                    with open(file_path, 'w', encoding='utf-8') as outfile:
                        outfile.write(pretty_json)

    if files_with_difference:
        print("\nFiles that were reformatted:")
        for file in files_with_difference:
            print(file)
    else:
        print("All files are properly formatted.")


process_json_files(".")
