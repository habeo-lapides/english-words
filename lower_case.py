def lowercase_file(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, 'r') as file:
            # Read the content of the file
            content = file.read()
        # Convert all letters to lowercase
        lowercase_content = content.lower()
        # Open the output file in write mode
        with open(output_file, 'w') as file:
            # Write the lowercase content to the output file
            file.write(lowercase_content)
        print("Lowercasing complete.")
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading or writing the file.")
# Example usage
input_file = 'words_4.txt'  # Specify the path to your input text file
output_file = 'words_4_lower.txt'  # Specify the path to the output text file
lowercase_file(input_file, output_file)