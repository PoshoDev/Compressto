from PIL import Image
import os, sys
import glob

def main(args):
    compress_images(*args)

def compress_images(dir_from="", dir_to="", quality=90,
                    format=".jpg", str_remove="", str_put=""):
    if dir_from != "":
        os.chdir(dir_from)
    files = os.listdir()
    images = [file for file in files if file.endswith(("jpg", "png"))]
    count = 0
    for image in images:
        img = Image.open(image)
        image_final = image.replace(str_remove, str_put)[:-4]
        file_final = f"{dir_to}\\{image_final}.{format}"
        if not os.path.exists(file_final):
            print(f"Saving: {image}")
            img.save(file_final, optimize=True, quality=quality)
            print(f"Saved: {image_final}.{format}!")
            count += 1
    print(f"Converted {count} images!" if count else "Nothing to convert!")

if __name__ == "__main__":
    main(sys.argv[1:])
