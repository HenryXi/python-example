import os

def remove_blank_line(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    with open(file_path, 'w') as f:
        for line in lines:
            if line.strip():
                f.write(line)


def find_files(directory):
    file_list=[]
    for root, dirs, files in os.walk(directory):
        for file in files:
            if ".md" in file:
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                    if len(lines) > 500:
                        file_list.append(file_path)

                    f.close()

        for dir in dirs:
            find_files(os.path.join(root, dir))

    return file_list

file_list = find_files('/Users/xixiaoyong/code/wiki/99-日志/2024')

for file in file_list:
    print(file)
    # remove_blank_line(file)