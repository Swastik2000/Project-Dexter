import os
import shutil

def move_ui_test_reports_to_specific_folder():
    downloads_dir = os.path.expanduser("~/Downloads")
    specific_folder_path = "~/Programming/Databricks/html-reports/"

    if not os.path.exists(specific_folder_path):
        os.makedirs(specific_folder_path)

    for entry in os.listdir(downloads_dir):
        full_path = os.path.join(downloads_dir, entry)
        if os.path.isdir(full_path) and entry.startswith("UI_Test_Reports"):
            destination_path = os.path.join(specific_folder_path, entry)
            shutil.move(full_path, destination_path)
        elif os.path.isfile(full_path) and entry.startswith("UI_Test_Reports"):
            shutil.move(full_path, specific_folder_path)

        # Handle files inside UI_Test_Reports directories
        elif os.path.isdir(full_path):
            for sub_entry in os.listdir(full_path):
                sub_full_path = os.path.join(full_path, sub_entry)
                if sub_entry.startswith("UI_Test_Reports") and os.path.isfile(sub_full_path):
                    destination_path = os.path.join(specific_folder_path, sub_entry)
                    shutil.move(sub_full_path, destination_path)

if __name__ == "__main__":
    move_ui_test_reports_to_specific_folder()
