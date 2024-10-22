import os

def save_file_contents(folder_path):
    file_contents = []
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            relative_path = os.path.relpath(file_path, folder_path)  # محاسبه مسیر نسبی
            
            try:
                with open(file_path, 'r', encoding='utf-8') as file_content:
                    # نوشتن عنوان فایل همراه با مسیر نسبی
                    file_contents.append(f'\n#####{relative_path}\n')
                    file_contents.append(file_content.read() + "\n")
            except Exception as e:
                # در صورت بروز خطا در خواندن فایل
                file_contents.append(f'Error reading file {relative_path}: {e}\n')
    
    return file_contents

def save_file_contents_only(folder_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        # نوشتن فقط محتویات فایل‌ها
        file_contents = save_file_contents(folder_path)
        f.write("\n".join(file_contents))

if __name__ == "__main__":
    folder_path = input("Path : ")
    output_file = "project_document_codes.txt"  # نام فایل خروجی

    save_file_contents_only(folder_path, output_file)
    print(f"The file contents have been saved in the file => {output_file}")
