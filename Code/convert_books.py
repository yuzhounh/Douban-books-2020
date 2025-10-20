import os

# Get all files starting with Books_ in the current directory
files = ['Books_1', 'Books_2', 'Books_3']

for filename in files:
    # Read file content
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Delete first 5 lines
    lines = lines[5:]
    
    # Modify the 6th line (now the 1st line) column names
    if lines:
        lines[0] = 'ID,Rating,Votes,Title\n'
    
    # Process all subsequent lines, remove spaces after commas
    for i in range(1, len(lines)):
        lines[i] = lines[i].replace(', ', ',')
    
    # Save as .csv file with UTF-8 with BOM encoding
    output_filename = filename + '.csv'
    with open(output_filename, 'w', encoding='utf-8-sig') as f:
        f.writelines(lines)
    
    print(f'Processed: {filename} -> {output_filename}')

print('All files processed!')
