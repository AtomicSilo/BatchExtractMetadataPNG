# BatchExtractMetadataPNG
To extract metadata from multiple PNG files and store the data in a text file, you can use a combination of Python and the Python Imaging Library (PIL) or its fork, Pillow. Here's a step-by-step guide to help you accomplish this:
Note: added the code above. Download, change the directory, and run.

1. Install the required libraries:
```
pip install pillow
```
2. Create a Python script (e.g., extract_metadata.py) and import the necessary modules:
```
from PIL import Image
import os

```

4. Define the directory path where your PNG files are located and the output text file path:
```
input_dir = "path/to/png/files"
output_file = "path/to/output.txt"

```

6. Open the output text file in write mode:
```
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

```

8. Once you've added the desired logic for handling the metadata, save and run the Python script:
```
python extract_metadata.py

```


The script will iterate through all the PNG files in the specified directory, extract their metadata using PIL/Pillow, and write the file name and metadata to the output text file. Each file's metadata will be separated by a blank line.

Make sure to replace "path/to/png/files" with the actual path to your PNG files directory and "path/to/output.txt" with the desired path and name for the output text file.
