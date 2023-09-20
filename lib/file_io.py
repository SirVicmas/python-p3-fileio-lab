def write_file(file_name, file_content):
    try:
        with open(file_name + ".txt", "w") as file:
            file.write(file_content)
        print(f"File '{file_name}.txt' has been successfully written.")
    except IOError as e:
        print(f"An error occurred while writing the file: {str(e)}")

def append_to_file(file_name, append_content):
    try:
        with open(file_name + ".txt", "a") as file:
            file.write("\n" + append_content)  # Append content to the end of the file with a newline
        print(f"Content has been successfully appended to '{file_name}.txt'.")
    except IOError as e:
        print(f"An error occurred while appending to the file: {str(e)}")

def read_file(file_name):
    try:
        with open(file_name + ".txt", "r") as file:
            content = file.read()
        return content
    except IOError as e:
        print(f"An error occurred while reading the file: {str(e)}")

# text_file = open('file_directory/file_name.txt')
# text_file = open('file_directory/file_name.txt', encoding='utf-8')

# text_file = open('file_name.txt', encoding='utf-8')
#text_file.close()

# with open('file_name.txt', encoding='utf-8') as text_file:
    #text_file.read()

# The mode attribute of a file can tell you which mode the file had been opened in.

# text_file = open('file_directory/file_name.txt')

# print(text_file.mode)

# Here are some example of how we can define a mode.


# #append mode 
# text_file = open('file_directory/file_name.txt', mode='a', encoding='utf-8')

# #write mode
# text_file = open('file_directory/file_name.txt', mode='w' encoding='utf-8')

# The write and append modes will create a new file if it does not already exist. We can use the .write() method to write and append to the file.

#Writing to a file
# with open('log_file.txt', mode='w', encoding='utf-8') as log_file:
#     log_file.write('Log 1')

# with open('log_file.txt', mode='a', encoding='utf-8') as log_file:
#     log_file.write('Log 2')

