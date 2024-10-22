import os


def recreate_project_from_txt(txt_file, base_path):
    with open(txt_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    file_path = None
    file_content = []

    for line in lines:
        if line.startswith("#####"):
            if file_path:
                write_file(file_path, file_content)
                file_content = []

            file_path = os.path.join(
                base_path, line.strip().replace("#.$.$.$.#", "").strip())

        else:
            file_content.append(line)

    if file_path:
        write_file(file_path, file_content)


def write_file(file_path, content):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(content)
    print(f'File created: {file_path}')


if __name__ == "__main__":
    txt_file = input("Path & FileName.txt: ")
    base_path = input("Path : ")

    recreate_project_from_txt(txt_file, base_path)
    print("All files and folders were created.")
