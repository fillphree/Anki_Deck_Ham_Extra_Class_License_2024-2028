import sys
import os

def process_file(input_filename):
    # Build the output filename with a ".new_html" extension.
    output_filename = input_filename + ".new_html"

    # Read all lines from the input file and remove blank lines.
    with open(input_filename, 'r') as infile:
        all_lines = [line.rstrip('\n') for line in infile if line.strip()]

    output_lines = []
    i = 0
    # Process the file 6 lines at a time.
    while i < len(all_lines):
        # If fewer than 6 lines remain, break out of the loop.
        if i + 6 > len(all_lines):
            break

        # Step 5: Assign the next 6 lines to variables.
        Question_var = all_lines[i]      # Line 1
        Answer1      = all_lines[i+1]      # Line 2
        Answer2      = all_lines[i+2]      # Line 3
        Answer3      = all_lines[i+3]      # Line 4
        Answer4      = all_lines[i+4]      # Line 5
        AnswerKey    = all_lines[i+5]      # Line 6

        # Concatenate variables to create HTML strings.
        Question_var_html = "<div>" + Question_var + "</div><div><BR></div>"
        Answer1_html = "<div>" + Answer1 + "</div><div><BR></div>"
        Answer2_html = "<div>" + Answer2 + "</div><div><BR></div>"
        Answer3_html = "<div>" + Answer3 + "</div><div><BR></div>"
        Answer4_html = "<div>" + Answer4 + "</div><div><BR></div>"

        # Step 6: Write the HTML strings for Question and Answers 1-4.
        output_lines.append(Question_var_html)
        output_lines.append(Answer1_html)
        output_lines.append(Answer2_html)
        output_lines.append(Answer3_html)
        output_lines.append(Answer4_html)

        # Step 7: Append the string "back_of_card".
        output_lines.append("back_of_card")

        # Step 8: Build the concatenated "category" variables.
        Question_var_cat = "<div>" + Question_var + "</div><div><BR></div>"
        
        if Answer1[0] == AnswerKey[12]:
            Answer1_cat = '<div><font color="#000000">' + Answer1 + '</font></div><div><BR></div>'
        else:
            Answer1_cat = '<div><font color="#d5dbdb">' + Answer1 + '</font></div><div><BR></div>'

        if Answer2[0] == AnswerKey[12]:
            Answer2_cat = '<div><font color="#000000">' + Answer2 + '</font></div><div><BR></div>'
        else:
            Answer2_cat = '<div><font color="#d5dbdb">' + Answer2 + '</font></div><div><BR></div>'

        if Answer3[0] == AnswerKey[12]:
            Answer3_cat = '<div><font color="#000000">' + Answer3 + '</font></div><div><BR></div>'
        else:
            Answer3_cat = '<div><font color="#d5dbdb">' + Answer3 + '</font></div><div><BR></div>'

        if Answer4[0] == AnswerKey[12]:
            Answer4_cat = '<div><font color="#000000">' + Answer4 + '</font></div><div><BR></div>'
        else:
            Answer4_cat = '<div><font color="#d5dbdb">' + Answer4 + '</font></div><div><BR></div>'

        # Step 9: Append the "category" HTML strings to the output.
        output_lines.append(Question_var_cat)
        output_lines.append(Answer1_cat)
        output_lines.append(Answer2_cat)
        output_lines.append(Answer3_cat)
        output_lines.append(Answer4_cat)

        # Step 10: Move to the next block of 6 lines.
        i += 6

    # Write all output lines to the new file.
    with open(output_filename, 'w') as outfile:
        for line in output_lines:
            outfile.write(line + "\n")

    print(f"Processing complete. Output written to '{output_filename}'.")

def main():
    # Ensure an input file was provided.
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

