import os


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print("dir_path", dir_path)
    directory = dir_path
    destination = os.path.join(dir_path, "submit_version")
    # Get all files in the directory
    files = os.listdir(directory)
    # filter only file
    files = [file for file in files if os.path.isfile(os.path.join(directory, file))]
    # and filter our if file is not .py
    files = [file for file in files if file.endswith(".py")]
    # Iterate over the files
    for file in files:
        # Check if the file is a regular file
        if os.path.isfile(os.path.join(directory, file)):
            # Read the file
            with open(os.path.join(directory, file), "r") as f:
                print("file", file)
                content = f.read()
                # Do something with the file content
                # print(content)
                # find comment "# summit" then remove comment of that line
                lines = content.split("\n")
                for i in range(len(lines)):

                    if "# submit" in lines[i]:
                        lines[i] = lines[i].replace("# ", "", 1)
                content = "\n".join(lines)
                # save to destination
                # change file name add -submit_version
                file = file.replace(".py", "-submit_version.py")
                with open(os.path.join(destination, file), "w") as f:
                    f.write(content)


if __name__ == "__main__":
    main()
