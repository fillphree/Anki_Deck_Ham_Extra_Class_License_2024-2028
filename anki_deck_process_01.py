import sys
import os
import re

def process_file(input_filename):
    # Read the entire file, filtering out any blank lines.
    with open(input_filename, 'r') as infile:
        # Strip newline characters and ignore blank lines.
        lines = [line.rstrip('\n') for line in infile if line.strip()]

    output_lines = []
    i = 0
    # Process lines until end-of-file.
    while i < len(lines):
        line = lines[i]
        # Step 4: If the line is blank, skip it (already removed above).
        
        # Step 5: If the line begins with an uppercase E and ends with a ')'
        if line.startswith("E") and line.endswith(")"):
            # Extract the uppercase letter contained within parentheses.
            match = re.search(r'\(([A-Z])\)', line)
            if match:
                AnswerKey = match.group(1)
            else:
                # If no valid pattern is found, skip this line.
                i += 1
                continue

            # Read the next line as the Question.
            if i + 1 < len(lines):
                Question = lines[i + 1]
            else:
                break  # Exit if there isn't a next line.
            # Write the Question string to the output.
            output_lines.append(Question)

            # Read the next four lines as Line1, Line2, Line3, Line4.
            if i + 5 < len(lines):
                Line1 = lines[i + 2]
                Line2 = lines[i + 3]
                Line3 = lines[i + 4]
                Line4 = lines[i + 5]
            else:
                break  # Not enough lines to process the block.
            # Write each of these lines to the output file.
            output_lines.append(Line1)
            output_lines.append(Line2)
            output_lines.append(Line3)
            output_lines.append(Line4)

            # Step 6: Check each line to see if its first character matches AnswerKey.
            AnswerLine = None
            for candidate in (Line1, Line2, Line3, Line4):
                if candidate and candidate[0] == AnswerKey:
                    AnswerLine = candidate
                    break  # Take the first matching line.
            
            # Optionally, you may want to output AnswerLine. Here, we append it if found.
            if AnswerLine:
                output_lines.append("AnswerLine: " + AnswerLine)

            # Move the index past this block (current line + Question + 4 answer lines).
            i += 6
        else:
            # If the line doesn't match our special format, skip it.
            i += 1

    # Write the output to a new file with a ".new" extension.
    output_filename = input_filename + ".new"
    with open(output_filename, 'w') as outfile:
        for out_line in output_lines:
            outfile.write(out_line + "\n")

    print(f"Processing complete. Output written to '{output_filename}'.")

def main():
    # Ensure that the user provided an input file as an argument.
    if len(sys.argv) != 2:
        print("Usage: python process_file.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        sys.exit(1)

    process_file(input_file)

if __name__ == "__main__":
    main()

