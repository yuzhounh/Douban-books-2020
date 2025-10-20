import os

def convert_tags_info(input_file):
    """
    Convert Tags_info file to CSV format
    - Remove the first 4 lines
    - Change the 5th line column names to "Number of books,Tag name"
    - Remove spaces after English commas
    - Save as UTF-8 with BOM encoded .csv file
    """
    # Read file
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Remove the first 4 lines
    lines = lines[4:]
    
    # Modify the first line (originally the 5th line) column names
    lines[0] = "Number of books,Tag name\n"
    
    # Process subsequent lines, remove spaces after commas
    for i in range(1, len(lines)):
        lines[i] = lines[i].replace(', ', ',')
    
    # Generate output filename
    base_name = os.path.basename(input_file)
    output_file = base_name + '.csv'
    
    # Save as UTF-8 with BOM encoding
    with open(output_file, 'w', encoding='utf-8-sig') as f:
        f.writelines(lines)
    
    print(f"Converted: {input_file} -> {output_file}")

# Usage example
if __name__ == "__main__":
    # Process single file
    input_file = "Tags_info"  # or other filename like "5G"
    if os.path.exists(input_file):
        convert_tags_info(input_file)
    else:
        print(f"File does not exist: {input_file}")
