import sys
import os
import csv

def process_file(input_filename):
    # Create output filename with a .csv extension.
    output_filename = os.path.splitext(input_filename)[0] + ".csv"

    # Read all non-blank lines from the input file.
    with open(input_filename, 'r', encoding='utf-8') as infile:
        lines = [line.rstrip('\n') for line in infile if line.strip()]

    cell_count = 0
    rows = []
    i = 0
    # Process the file 11 lines at a time.
    while i < len(lines):
        # If there are fewer than 11 lines remaining, break out of the loop.
        if i + 11 > len(lines):
            break

        # Read the next 11 lines.
        block = lines[i : i+11]

        # Lines 1 to 5 (indices 0 to 4) will go into column A.
        cell_A = " ".join(block[0:5])
        # Lines 7 through 11 (indices 6 to 10) will go into column B.
        cell_B = " ".join(block[6:11])
        # (Line 6, index 5, is ignored.)

        # Append the row to our list.
        rows.append([cell_A, cell_B])
        cell_count += 1

        # Move to the next block of 11 lines.
        i += 11

    # Write the rows to a CSV file using UTF-8 encoding.
    with open(output_filename, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        # Optionally, write a header row.
        writer.writerow(["Column A", "Column B"])
        for row in rows:
            writer.writerow(row)

    print(f"Processing complete. {cell_count} cells processed. Output written to '{output_filename}'.")

def main():
    # Verify that exactly one argument (the input filename) is provided.
    if len(sys.argv) != 2:
        print("Usage: python process_to_csv.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        sys.exit(1)

    process_file(input_file)

if __name__ == "__main__":
    main()

