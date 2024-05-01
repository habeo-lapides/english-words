def remove_words_ending_in_s(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, 'r') as file:
            # Read the content of the file
            content = file.read()
        # Split the content into words
        words = content.split()
        # Remove words ending in 's'
        words_without_s = [word for word in words if not word.endswith('s')]
        # Join the words back into a string
        modified_content = ' '.join(words_without_s)
        # Open the output file in write mode
        with open(output_file, 'w') as file:
            # Write the modified content to the output file
            file.write(modified_content)
        print("Words ending in 's' removed and written to", output_file)
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading or writing the file.")
# Example usage
input_file = 'filtered_words.txt'  # Specify the path to your input text file
output_file = 'filtered_words_no_s.txt'  # Specify the path to the output text file
remove_words_ending_in_s(input_file, output_file)