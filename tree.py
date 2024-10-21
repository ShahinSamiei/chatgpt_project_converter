import os

def save_directory_structure(folder_path):
    tree_structure = []
    for dirpath, dirnames, filenames in os.walk(folder_path):
        # ساختار درختی را ایجاد می‌کنیم
        level = dirpath.replace(folder_path, '').count(os.sep)
        indent = ' ' * 4 * level
        tree_structure.append(f'{indent}{os.path.basename(dirpath)}/')
        
        subindent = ' ' * 4 * (level + 1)
        for filename in filenames:
            tree_structure.append(f'{subindent}{filename}')
    
    return tree_structure

def save_directory_structure_only(folder_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        # نوشتن ساختار درختی
        tree_structure = save_directory_structure(folder_path)
        f.write("ساختار درختی:\n")
        f.write("\n".join(tree_structure) + "\n")

if __name__ == "__main__":
    folder_path = input("Path : ")
    output_file = "project_structure.txt"  # نام فایل خروجی

    save_directory_structure_only(folder_path, output_file)
    print(f"The folder structure has been saved in the file => {output_file}")
