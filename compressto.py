import os, sys, glob, argparse
from PIL import Image

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir_from", type=str, default="", help="lol")
    parser.add_argument("--dir_to", type=str, default="", help="lol")
    parser.add_argument("--quality", type=int, default=90, help="lol")
    parser.add_argument("--format", type=str, default="jpg", help="lol")
    parser.add_argument("--str_remove", type=str, default="", help="lol")
    parser.add_argument("--str_put", type=str, default="", help="lol")
    parser.add_argument("--delete", type=bool, default=False, help="lol")
    parser.add_argument("--infinite", type=bool, default=False, help="lol")
    args = parser.parse_args()
    print("C O M P R E S S T O !")
    compress_images(args)

def compress_images(args):
    if args.dir_from != "":
        os.chdir(args.dir_from)
    print(f"Looking for images in: {args.dir_from}...")
    count = 0
    if args.infinite:
        while True: count += search_images(args)
    else: count += search_images(args)
    print(f"Converted {count} images!" if count else "Nothing to convert!")

def search_images(args):
    files = os.listdir()
    images = [file for file in files if file.endswith(("jpg", "png"))]
    count = 0
    for image in images:
        try:
            img = Image.open(image)
            image_final = image.replace(args.str_remove, args.str_put)[:-4]
            file_final = f"{args.dir_to}\\{image_final}.{args.format}"
            if not os.path.exists(file_final):
                print(f"Saving: {image}")
                img.save(file_final, optimize=True, quality=args.quality)
                print(f"Saved: {image_final}.{args.format}!")
                if args.delete:
                    os.remove(image)
                    print(f"Removed source: {image}")
                count += 1
        except: pass
    return count

if __name__ == "__main__":
    main()
