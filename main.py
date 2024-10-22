import os


def save_directory_structure(folder_path):
    tree_structure = []
    for dirpath, dirnames, filenames in os.walk(folder_path):
        level = dirpath.replace(folder_path, '').count(os.sep)
        indent = ' ' * 4 * level
        tree_structure.append(f'{indent}{os.path.basename(dirpath)}/')

        subindent = ' ' * 4 * (level + 1)
        for filename in filenames:
            tree_structure.append(f'{subindent}{filename}')

    return tree_structure


def save_file_contents(folder_path):
    file_contents = []
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            relative_path = os.path.relpath(
                file_path, folder_path)

            try:
                with open(file_path, 'r', encoding='utf-8') as file_content:
                    file_contents.append(
                        f'\n{"-"*20}\n{relative_path}\n{"-"*20}\n')
                    file_contents.append(file_content.read() + "\n")
            except Exception as e:
                file_contents.append(f'Error reading file {
                                     relative_path}: {e}\n')

    return file_contents


def save_directory_structure_and_content(folder_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        tree_structure = save_directory_structure(folder_path)
        f.write("ساختار درختی:\n")
        f.write("\n".join(tree_structure) + "\n\n")

        file_contents = save_file_contents(folder_path)
        f.write("محتویات فایل‌ها:\n")
        f.write("\n".join(file_contents))


if __name__ == "__main__":
    folder_path = input("Path : ")
    output_file = "project_structure_and_codes.txt"

    save_directory_structure_and_content(folder_path, output_file)
    print(f"The folder structure and its contents have been saved in the file => {
          output_file}")
