# Compressto 🎩
Batch image compression, conversion and other tools; with continuous search options.

## Usage

Compressto works from the command line. Example as follows:

```powershell
compressto.exe --dir_from="source_folder" --dir_to="destination_folder" --quality=50 --format=jpg --str_del="Hello" --str_put="GoodBye"
```

The above script will convert the images from "source_folder" and convert them into .jpg files in the "destination_folder" at 50% of quality while renaming parts of their filenames. Such as:

| source_folder    | destination_folder |
| ---------------- | ------------------ |
| HelloWorld.png   | GoodByeWorld.jpg   |
| DontSayHello.png | DontSayGoodBye.jpg |
| IhateMyself.png  | IhateMyself.jpg    |



## Options

You can use multiple flags as parameters in order to work with Compressto. Here's a list of said flags:

| Flag         | Type    | Default | Description                                                  |
| ------------ | ------- | ------- | ------------------------------------------------------------ |
| -h, --help   | -       | -       | Brings up the help message.                                  |
| --dir_from   | String  | ""      | The directory where the original images are.                 |
| --dir_to     | String  | ""      | The directory where you want to save your converted images.  |
| --quality    | Int     | 90      | The quality of your converted image between **0-100**. Lower quality results in smaller file sizes. |
| --format     | String  | "jpg"   | The extension of the resulting images. Currently tested with **'jpg'** and **'png'**. Files with 'jpg' extension tend to be smaller in size. |
| --matching    | String | ""    | A substring that must exist in the name of a file in order to be converted. If unused, all the files in the --dir_from will be converted.              |
| --str_del | String  | ""      | A substring you want to remove from the filename.            |
| --str_put    | String  | ""      | A substring to replace **--str_del** with.                |
| --delete     | Boolean | False   | Whether you want to delete the original files once conversion is complete or not. |
| --infinite   | Boolean | False   | Enables constant scanning on the source folder. If enabled, program must be terminated manually. |
| --interval   | Int     | 60      | The time interval **(in seconds)** in which the program will scan for images if the **--infinite** flag is enabled. |
| --hide       | Boolean | False   | Hides the program's console window. If the **--infinite** flag is enabled, then the program must be terminated from the Task Manager or other methods. |
| --verbose    | Boolean | True    | If disabled, the program won't output any text.              |
