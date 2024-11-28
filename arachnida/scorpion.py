import argparse
import os

def extract_exif(file_path):
    pass

def main():
    parser = argparse.ArgumentParser(description="Scorpion: Extracts EXIF and metadata from image files.")
    parser.add_argument("files", nargs="+", help="image files to analyze: .jpg, .jpeg, .png, .gif, .bmp")
    
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
if __name__ == "__main__":
    main()