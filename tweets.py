import re
import json

def txt_to_json(file_path):
    # Regular expression to split the file by IDs
    pattern = re.compile(r'ID\d+')
    
    # Read the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split the content by ID
    tweets = pattern.split(content)[1:]  # Skip the first split as it's before the first ID
    ids = pattern.findall(content)
    
    # Combine IDs with their corresponding tweet content
    json_data = []
    for tweet, id_ in zip(tweets, ids):
        json_data.append({"ID": id_, "content": tweet.strip()})
    
    # Write the output to a JSON file
    with open('output.json', 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)

    print("JSON file created successfully.")

# Example usage:
txt_to_json('path_to_your_file/Tweets.txt')
