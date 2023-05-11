import os

# path = input("Enter the path to search: ")  # this didn't work for me, that why I hardcoded the path
path = "/Users/oruda/Documents"
threshold = 1000
results = {"folders": 0, "files": 0,
           "largest_file": None, "smallest_file": None,
           "longest_filename": None, "shortest_filename": None}

try:
    for root, folders, files in os.walk(path):
        results["folders"] += len(folders)
        results["files"] += len(files)
        if files:
            sizes = [(os.path.getsize(os.path.join(root, name)), name) for name in files]
            results["largest_file"] = max(sizes)[1]
            results["smallest_file"] = min(sizes)[1]
        if files:
            lengths = [(len(name), name) for name in files]
            results["longest_filename"] = max(lengths)[1]
            results["shortest_filename"] = min(lengths)[1]
        if results["folders"] + results["files"] > threshold:
            break
except KeyboardInterrupt:
    with open("interrupted_paths.txt", "w") as temporary_file:
        for root, folders, files in os.walk(path):
            for folder in folders:
                temporary_file.write(os.path.join(root, folder) + "\n")
            for file in files:
                temporary_file.write(os.path.join(root, file) + "\n")

print(f"Folders: {results['folders']}")
print(f"Files: {results['files']}")
print(f"Largest file: {results['largest_file']}")
print(f"Smallest file: {results['smallest_file']}")
print(f"Longest filename: {results['longest_filename']}")
print(f"Shortest filename: {results['shortest_filename']}")
