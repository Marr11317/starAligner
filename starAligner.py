import os
import sys

walk_dir = sys.argv[1]

print('walk_dir = ' + walk_dir)

# If your current working directory may change during script execution, it's recommended to
# immediately convert program arguments to an absolute path. Then the variable root below will
# be an absolute path as well. Example:
# walk_dir = os.path.abspath(walk_dir)
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

for root, subdirs, filenames in os.walk(walk_dir):
    print('--\nroot = ' + root)

    # for subdir in subdirs:
    #     print('\t- subdirectory ' + subdir)

    for filename in filenames:
        if filename.endswith(".ts"):
            file_path = os.path.join(root, filename)
            print('\t- file %s (full path: %s)' % (filename, file_path))

            result = ""
            with open(file_path, 'r') as f:
                line = f.readline()
                while (line):
                    if (line.lstrip().startswith("/**")):
                        count = line.index("/")

                        result += line
                        line = f.readline()
                        while (line.lstrip().startswith("*")):
                            line = (count + 1) * " " + line.lstrip()
                            result += line
                            line = f.readline()

                    result += line
                    line = f.readline()

            with open(file_path, 'w') as f:
                f.write(result)
