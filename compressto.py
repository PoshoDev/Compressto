from PIL import Image
import os, sys
import glob

def main(args):
    compress_images(r"C:\Users\green\Pictures\Ryujinx",
                    r"D:\Posho\Media\Games\Saves\Pokemon-Saves\Pokémon Legends Arceus\Screenshots",
                    90, "jpg", "ryujinx_capture", "PokémonLegendsArceus")

def compress_images(dir_from="", dir_to="", quality=90,
                    format=".jpg", str_remove="", str_put=""):
    if dir_from != "":
        os.chdir(dir_from)
    files = os.listdir()
    images = [file for file in files if file.endswith(("jpg", "png"))]
    copied = 0
    for image in images:
        print(image)
        img = Image.open(image)
        image_name = image[:-4]
        print(f"Image name: {image_name}")
        image_final = image_name.replace(str_remove, str_put)
        print(str_remove)
        print(str_put)
        print(quality)
        print(f"Final name: {image_final}")
        return
        print(f"Trying to save: {dir_to}\\{image_final}.jpg")
        img.save(f"{dir_to}\\{image_final}.jpg", optimize=True, quality=quality)

if __name__ == "__main__":
    main(sys.argv[1:])
