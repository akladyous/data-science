import os
import gzip

# Get the current folder path
current_folder = os.getcwd()

# Loop through each file in the folder
for filename in os.listdir(current_folder):
    if filename.endswith(".csv"):
        file_path = os.path.join(current_folder, filename)
        output_path = os.path.join(current_folder, f"{filename}.gz")

        # Open the input CSV file and create a GZipped output file
        with open(file_path, "rb") as file_in, gzip.open(
            output_path, "wb", compresslevel=9
        ) as file_out:
            # Copy the contents of the CSV file to the GZipped output file
            file_out.writelines(file_in)

        # Remove the original CSV file (optional, uncomment if desired)
        os.remove(file_path)
