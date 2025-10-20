import os

def convert_doulist_info(input_file):
    """
    Convert Doulists_info file to CSV format with UTF-8 BOM encoding
    """
    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Delete first 4 lines
    lines = lines[4:]
    
    # Modify the 5th line (now index 0) - replace column names
    lines[0] = "Doulist ID,Number of books,Doulist name\n"
    
    # For all subsequent lines, remove spaces after commas
    for i in range(1, len(lines)):
        # Remove spaces after commas
        lines[i] = lines[i].replace(', ', ',')
    
    # Generate output filename
    base_name = os.path.basename(input_file)
    output_file = base_name + '.csv'
    
    # Write to CSV file with UTF-8 BOM encoding
    with open(output_file, 'w', encoding='utf-8-sig') as f:
        f.writelines(lines)
    
    print(f"Converted {input_file} to {output_file}")

# Example usage
if __name__ == "__main__":
    # Process a single file
    input_file = "Doulists_info"  # or "5G" or any other filename
    convert_doulist_info(input_file)