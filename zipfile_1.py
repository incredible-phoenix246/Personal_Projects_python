#/usr/bin/python3

import zipfile

# Prompt the user to specify the action (open or create)
action = input("Enter 'open' to open an existing zip file or 'create' to create a new zip file: ")

if action.lower() == 'open':
    # Prompt the user to enter the path to the zip file to open
    zip_file_path = input("Enter the path to the zip file you want to open: ")

    try:
        # Open the specified zip file
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            # List the contents of the zip file
            print("Contents of the zip file:")
            for file_info in zip_ref.infolist():
                print(file_info.filename)

    except FileNotFoundError:
        print("File not found. Please enter a valid path to the zip file.")
    except zipfile.BadZipFile:
        print("The specified file is not a valid zip archive.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

elif action.lower() == 'create':
    # Prompt the user to enter the name for the new zip file
    new_zip_file = input("Enter the name for the new zip file (e.g., new_archive.zip): ")

    try:
        # Create a new zip file
        with zipfile.ZipFile(new_zip_file, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
            # Prompt the user to add files to the zip archive
            while True:
                file_to_add = input("Enter the path to a file you want to add (or 'done' to finish): ")
                if file_to_add.lower() == 'done':
                    break
                try:
                    zip_ref.write(file_to_add)
                    print(f"{file_to_add} added to the zip archive.")
                except FileNotFoundError:
                    print(f"File not found: {file_to_add}")
                except Exception as e:
                    print(f"An error occurred: {str(e)}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

else:
    print("Invalid action. Please enter 'open' or 'create'.")
import zipfile

# Prompt the user to enter the path to the zip file
zip_file_path = input("Enter the path to the zip file you want to open: ")

try:
    # Open the specified zip file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # List the contents of the zip file
        print("Contents of the zip file:")
        for file_info in zip_ref.infolist():
            print(file_info.filename)

        # Extract all files from the zip file to a directory
        extract_path = "extracted_contents/"
        zip_ref.extractall(extract_path)
        print("Files extracted to:", extract_path)
except FileNotFoundError:
    print("File not found. Please enter a valid path to the zip file.")
except zipfile.BadZipFile:
    print("The specified file is not a valid zip archive.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
