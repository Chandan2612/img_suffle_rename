import os
import shutil
import re

main_folder = "images"
output_folder = "output"
start_number = 300

image_extensions = (".jpg", ".jpeg", ".png", ".webp", ".bmp")


def natural_sort_key(file_name):
    return [
        int(text) if text.isdigit() else text.lower()
        for text in re.split(r"(\d+)", file_name)
    ]


# Delete old output first
if os.path.exists(output_folder):
    shutil.rmtree(output_folder)

os.makedirs(output_folder, exist_ok=True)


# -----------------------------
# MANUAL FOLDER ORDER
# -----------------------------
subfolders = [
    "ananya  169",
    "ananya 93 - Copy",
    "ananya 99",
    "ananya 101 - Copy",
]

# Keep only folders that really exist
subfolders = [
    folder_name
    for folder_name in subfolders
    if os.path.isdir(os.path.join(main_folder, folder_name))
]

print("\nActual folder processing order:")
for index, folder_name in enumerate(subfolders, start=1):
    print(f"{index}. {folder_name}")

image_counter = start_number

for folder_name in subfolders:
    folder_path = os.path.join(main_folder, folder_name)

    current_output_folder = os.path.join(output_folder, folder_name)
    os.makedirs(current_output_folder, exist_ok=True)

    image_files = [
        file_name
        for file_name in os.listdir(folder_path)
        if file_name.lower().endswith(image_extensions)
    ]

    image_files = sorted(image_files, key=natural_sort_key)

    if not image_files:
        print(f"\nSkipping empty folder: {folder_name}")
        continue

    folder_start = image_counter

    print(f"\nProcessing folder: {folder_name}")
    print(f"Images found: {len(image_files)}")

    for image_file in image_files:
        old_image_path = os.path.join(folder_path, image_file)

        file_extension = os.path.splitext(image_file)[1].lower()
        new_image_name = f"{image_counter}{file_extension}"
        new_image_path = os.path.join(current_output_folder, new_image_name)

        shutil.copy(old_image_path, new_image_path)

        print(f"{image_file} -> {new_image_name}")
        image_counter += 1

    folder_end = image_counter - 1
    print(f"Folder range: {folder_start} - {folder_end}")

print("\nDone!")
print(f"Started from: {start_number}")
print(f"Ended at: {image_counter - 1}")
print(f"Total images renamed: {image_counter - start_number}")
print(f"Saved inside: {output_folder}")
