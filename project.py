import os

def recreate_project_from_txt(txt_file, base_path):
    with open(txt_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    file_path = None
    file_content = []
    
    for line in lines:
        if line.startswith("#####"):
            # اگر فایل قبلی وجود دارد آن را ذخیره کنیم
            if file_path:
                write_file(file_path, file_content)
                file_content = []

            # دریافت مسیر فایل جدید
            file_path = os.path.join(base_path, line.strip().replace("#.$.$.$.#", "").strip())

        else:
            # اضافه کردن خط به محتوای فایل فعلی
            file_content.append(line)

    # ذخیره فایل آخر
    if file_path:
        write_file(file_path, file_content)

def write_file(file_path, content):
    # اطمینان از وجود فولدرها
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # نوشتن محتوا در فایل
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(content)
    print(f'File created: {file_path}')

if __name__ == "__main__":
    txt_file = input("Path & FileName.txt: ")  # فایل متنی که ساختار پروژه در آن قرار دارد
    base_path = input("Path : ")  # مسیر فولدر اصلی پروژه

    recreate_project_from_txt(txt_file, base_path)
    print("All files and folders were created.")
