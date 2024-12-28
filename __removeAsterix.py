def remove_asterisks(input_file, output_file):
    try:
        # Read the content of the input file
        with open(input_file, 'r') as file:
            content = file.read()

        # Remove asterisks from the content
        content_without_asterisks = content.replace('*', '')

        # Write the modified content to the output file
        with open(output_file, 'w') as file:
            file.write(content_without_asterisks)

        print(f"Asterisks removed successfully. Modified content saved to {output_file}.")
    
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")

# Prompting user for input and output file paths
if __name__ == "__main__":
    input_file = input("Enter the path to the input file: ")
    output_file = input("Enter the path to the output file: ")
    remove_asterisks(input_file, output_file)
