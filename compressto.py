import os, sys, time, glob, argparse, win32gui, win32con
from PIL import Image

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir_from", type=str, default="",
                        help="The directory where the original images are.")
    parser.add_argument("--dir_to", type=str, default="",
                        help="The directory where you want to save your "
                        "converted images.")
    parser.add_argument("--quality", type=int, default=90,
                        help="The quality of your converted image between "
                        "0-100. Lower quality results in smaller file sizes.")
    parser.add_argument("--format", type=str, default="jpg",
                        help="The extension of the resulting images. "
                        "Currently tested with 'jpg' and 'png'. Files with "
                        "'jpg' extension tend to be smaller in size.")
    parser.add_argument("--matching", type=str, default="",
                        help="A substring that must exist in the name of a "
                        "file in order to be converted. If unused, all the "
                        "files in the --dir_from will be converted.")
    parser.add_argument("--str_del", type=str, default="",
                        help="A substring you want to remove from the "
                        "filename.")
    parser.add_argument("--str_put", type=str, default="",
                        help="A substring to replace --str_del with.")
    parser.add_argument("--delete", type=bool, default=False,
                        help="Whether you want to delete the original files "
                        "once conversion is complete or not.")
    parser.add_argument("--infinite", type=bool, default=False,
                        help="Enables constant scanning on the source folder. "
                        "If enabled, program must be terminated manually.")
    parser.add_argument("--interval", type=int, default=60,
                        help="The time interval (in seconds) in which the "
                        "program will scan for images if the --infinite flag "
                        "is enabled.")
    parser.add_argument("--hide", type=bool, default=False,
                        help="Hides the program's console window. If the "
                        "--infinite flag is enabled, then the program must "
                        "be terminated from the Task Manager or other methods.")
    parser.add_argument("--verbose", type=bool, default=True,
                        help="If disabled, the program won't output any text.")
    args = parser.parse_args()
    if args.hide:
        hide = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hide , win32con.SW_HIDE)
    if args.verbose: print("  _   _       __  __  ___  __   __ ___ _\n"
                           " / ` / ) )\/) )_) )_) )_  (_ ` (_ ` ) / )\n"
                           "(_. (_/ (  ( /   / \ (__ .__) .__) ( (_/\n")
    compress_images(args)

def compress_images(args):
    if args.dir_from != "":
        os.chdir(args.dir_from)
    if args.verbose: print(f"Looking for images in: {args.dir_from}...")
    count = 0
    if args.infinite:
        while True:
            count += search_images(args)
            time.sleep(args.interval)
            if args.verbose: print("Searching again...")
    else: count += search_images(args)
    if args.verbose:
        print(f"Converted {count} images!" if count else "Nothing to convert!")

def search_images(args):
    files = os.listdir()
    images = [file for file in files if file.endswith(("jpg", "png"))]
    count = 0
    for image in images:
        if args.matching=="" or args.matching in image:
            try:
                img = Image.open(image)
                image_final = image.replace(args.str_del, args.str_put)[:-4]
                file_final = f"{args.dir_to}\\{image_final}.{args.format}"
                if not os.path.exists(file_final):
                    if args.verbose: print(f"Saving: {image}")
                    img.save(file_final, optimize=True, quality=args.quality)
                    if args.verbose:
                        print(f"Saved: {image_final}.{args.format}!")
                    if args.delete:
                        os.remove(image)
                        if args.verbose: print(f"Removed source: {image}")
                    count += 1
            except: pass
    return count


if __name__ == "__main__":
    main()
