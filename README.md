# mp4-to-gif

A simple script to convert short videos to GIFs.

## Instructions

1. Install dependencies in your environment (recommended):
```commandline
pip install -r requirements.txt
```

1.5 Install latest version of [ImageMagick](https://imagemagick.org/script/download.php) (optional, recommended) for higher quality GIFs

2. Place your video in the project root.

3. Run the following:
```commandline
python mp42gif.py -f FILENAME.mp4 -c 90 -o OUTPUT_FILENAME.gif 
```

4. The `-c` (compression) and `-o` (output filename) flags are optional. Omitting the compression flag will not apply any compression to the output. Omitting the output filename will use the same filename as the source file.
