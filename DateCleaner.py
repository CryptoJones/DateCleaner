import os
import re
import sys

def modify_filename(path_string, filename):
    match = re.match(r"(\d{4})(\d{2})(\d{2})(.*)", filename)
    if match:
        new_name = f"{match.group(1)}-{match.group(2)}-{match.group(3)}{match.group(4)}"
        try:
            os.rename(os.path.join(path_string, filename), os.path.join(path_string, new_name))
            print(f"Renamed: {filename} -> {new_name}")
        except OSError as e:
            print(f"Error renaming {filename}: {e}", file=sys.stderr)
    else:
        print(f"Skipped (no date prefix): {filename}")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    if not os.path.isdir(target):
        print(f"Directory not found: {target}", file=sys.stderr)
        sys.exit(1)
    for f in os.listdir(target):
        modify_filename(target, f)
