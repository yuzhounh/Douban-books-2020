import os
import csv

# Specify Tags directory path
tags_dir = 'Tags'

# Get all files in the directory
files = [f for f in os.listdir(tags_dir) if os.path.isfile(os.path.join(tags_dir, f))]

# Process each file
for filename in files:
    file_path = os.path.join(tags_dir, filename)
    
    # Read file content
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Delete the first 5 lines
    if len(lines) <= 5:
        print(f"Warning: File {filename} has insufficient lines, skipping")
        continue
    
    # Keep the 6th line and onwards
    remaining_lines = lines[5:]
    
    # Modify the first line (originally the 6th line) column names
    # Replace "ID, rating, votes, title" with "ID,Rating,Votes,Title"
    if remaining_lines:
        remaining_lines[0] = 'ID,Rating,Votes,Title\n'
        
    # Remove spaces after commas in rows after the column names
    for i in range(1, len(remaining_lines)):
        remaining_lines[i] = remaining_lines[i].replace(', ', ',')
    
    # Generate new CSV filename
    csv_filename = f"{filename}.csv"
    csv_path = os.path.join(tags_dir, csv_filename)
    
    # Save as CSV file
    with open(csv_path, 'w', encoding='utf-8-sig') as f:
        f.writelines(remaining_lines)
    
    print(f"Processed: {filename} -> {csv_filename}")

print("\nAll files processed!")