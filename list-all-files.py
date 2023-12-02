import os

def list_files_in_directory(directory_path):
    if not os.path.exists(directory_path):
        print(f"Directory '{directory_path}' does not exist.")
        return

    if not os.path.isdir(directory_path):
        print(f"'{directory_path}' is not a directory.")
        return

    files_list = os.listdir(directory_path)
    files = [file for file in files_list if os.path.isfile(os.path.join(directory_path, file))]

    if len(files) == 0:
        print(f"No files found in directory '{directory_path}'.")
    else:
        print(f"Files in directory '{directory_path}':")
        for file in files:
            print(file)

if __name__ == "__main__":
    specific_directory_path = "~/Programming/Databricks/html-reports/"
    list_files_in_directory(specific_directory_path)
