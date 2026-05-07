# import os
# import shutil
# import re
# main_folder = "images"
# output_folder = "output"
# os.makedirs(output_folder, exist_ok=True)
# image_extensions = (".jpg", ".jpeg", ".png", ".webp", ".bmp")
# def natural_sort_key(file_name):
#     return [
#         int(text) if text.isdigit() else text.lower()
#         for text in re.split(r"(\d+)", file_name)
#     ]
# image_counter = 1
# subfolders = sorted(os.listdir(main_folder), key=natural_sort_key)
# for folder_name in subfolders:
#     folder_path = os.path.join(main_folder, folder_name)
#     if not os.path.isdir(folder_path):
#         continue
#     if folder_name.lower() == "output":
#         continue
#     current_output_folder = os.path.join(output_folder, folder_name)
#     os.makedirs(current_output_folder, exist_ok=True)
#     image_files = [
#         file_name
#         for file_name in os.listdir(folder_path)
#         if file_name.lower().endswith(image_extensions)
#     ]
#     image_files = sorted(image_files, key=natural_sort_key)

#     print(f"\nProcessing folder: {folder_name}")
#     print(f"Images found: {len(image_files)}")
#     for image_file in image_files:
#         old_image_path = os.path.join(folder_path, image_file)
#         file_extension = os.path.splitext(image_file)[1].lower()
#         new_image_name = f"{image_counter}{file_extension}"
#         new_image_path = os.path.join(current_output_folder, new_image_name)
#         shutil.copy2(old_image_path, new_image_path)

#         print(f"{image_file}  ->  {new_image_name}")
#         image_counter += 1

# print("\nDone!")
# print(f"Total images renamed: {image_counter - 1}")
# print(f"Saved inside: {output_folder}")



import os
import shutil
import re

main_folder = "images"
output_folder = "output"


start_number = 1

os.makedirs(output_folder, exist_ok=True)

image_extensions = (".jpg", ".jpeg", ".png", ".webp", ".bmp")

def natural_sort_key(file_name):
    return [
        int(text) if text.isdigit() else text.lower()
        for text in re.split(r"(\d+)", file_name)
    ]


image_counter = start_number

subfolders = sorted(os.listdir(main_folder), key=natural_sort_key)

for folder_name in subfolders:
    folder_path = os.path.join(main_folder, folder_name)

    if not os.path.isdir(folder_path):
        continue

    if folder_name.lower() == "output":
        continue

    current_output_folder = os.path.join(output_folder, folder_name)
    os.makedirs(current_output_folder, exist_ok=True)

    image_files = [
        file_name
        for file_name in os.listdir(folder_path)
        if file_name.lower().endswith(image_extensions)
    ]

    image_files = sorted(image_files, key=natural_sort_key)

    print(f"\nProcessing folder: {folder_name}")
    print(f"Images found: {len(image_files)}")

    for image_file in image_files:
        old_image_path = os.path.join(folder_path, image_file)

        file_extension = os.path.splitext(image_file)[1].lower()

        new_image_name = f"{image_counter}{file_extension}"

        new_image_path = os.path.join(current_output_folder, new_image_name)

        shutil.copy2(old_image_path, new_image_path)

        print(f"{image_file}  ->  {new_image_name}")

        image_counter += 1

print("\nDone!")
print(f"Started from: {start_number}")
print(f"Ended at: {image_counter - 1}")
print(f"Total images renamed: {image_counter - start_number}")
print(f"Saved inside: {output_folder}")
