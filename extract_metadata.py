from PIL import Image
import os

input_dir = "path/to/png/files"
output_file = "path/to/output.txt"

with open(output_file, "w") as f:
    # Iterate over each file in the input directory
    for filename in os.listdir(input_dir):
        # Check if the file is a PNG file
        if filename.endswith(".png"):
            # Open the image file
            image_path = os.path.join(input_dir, filename)
            image = Image.open(image_path)

            # Extract the metadata
            metadata = image.info

            # Write the metadata to the text file
            f.write(f"File: {filename}\n")
            f.write(f"Metadata: {metadata}\n")
            f.write("\n")

            # Close the image file
            image.close()
