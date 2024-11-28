import argparse
import os
import subprocess
from PIL import Image, ExifTags

def extract_exif(image_path):
    """Extract EXIF metadata from an image."""
    try:
        with Image.open(image_path) as img:
            info_dict = {
                "Filename": img.filename.split("/")[-1],
                "Image Size": img.size,
                "Image Height": img.height,
                "Image Width": img.width,
                "Image Format": img.format,
                "Image Mode": img.mode,
                "Image is Animated": getattr(img, "is_animated", False),
                "Frames in Image": getattr(img, "n_frames", 1)
            }

            for label,value in info_dict.items():
                print(f"{label:25}: {value}")
            exif_data = img._getexif()
            if exif_data:
                print("EXIF Metadata (via Pillow):")
                metadata = {}
                for tag_id, value in exif_data.items():
                    tag_name = ExifTags.TAGS.get(tag_id, f"Unknown({tag_id})")
                    metadata[tag_name] = value

                creation_date = metadata.get("DateTime", "Unknown")
                print(f"Creation Date: {creation_date}")
                for tag, value in metadata.items():
                    print(f"  {tag}: {value}")
                return
    except Exception as e:
        print(f"Error using Pillow: {e}")

def extract_other_metadata(image_path):
    """Extract additional metadata using hachoir-metadata."""
    exe_process = "hachoir-metadata"
    try:
        process = subprocess.Popen(
            [exe_process, image_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
        )
        print("\nMetadata via hachoir-metadata:")
        for line in process.stdout:
            print(line.strip())
    except FileNotFoundError:
        print("Hachoir-metadata is not installed or not found in PATH.")
    except Exception as e:
        print(f"Error using hachoir-metadata: {e}")

def main():
    parser = argparse.ArgumentParser(description="Scorpion: Extracts EXIF and metadata from image files.")
    parser.add_argument("files", nargs="+", help="Image files to analyze: .jpg, .jpeg, .png, .gif, .bmp")
    
    args = parser.parse_args()
    
    supported_formats = (".jpg", ".jpeg", ".png", ".gif", ".bmp")
    for file_path in args.files:
        if not os.path.isfile(file_path):
            print(f"Not found: {file_path}")
            continue
        if not file_path.lower().endswith(supported_formats):
            print(f"Unsupported file format: {file_path}")
            continue
        print(f"Processing file: {file_path}")
        extract_exif(file_path)
        extract_other_metadata(file_path)

if __name__ == "__main__":
    main()
