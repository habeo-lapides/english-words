with open('words_4.txt', 'r') as file:
    # Read all the lines from the file
    lines = file.readlines()

# Create a new list to store the filtered words
filtered_words = []

# Iterate over each line in the file
for line in lines:
    # Split the line into words
    words = line.strip().split()
    
    # Iterate over each word
    for word in words:
        # Check if the word has between 4 and 8 characters (inclusive)
        if 4 <= len(word) <= 8:
            filtered_words.append(word)

# Open the output file for writing
with open('filtered_words.txt', 'w') as file:
    # Write the filtered words to the output file
    file.write(' '.join(filtered_words))