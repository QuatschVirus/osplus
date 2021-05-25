# osplus
A python package for additional, simple features like easy config files, logging, and notifications
NOTE: Since i'm too dumb to upload this to PyPi to make it installable via pip, i'm happy about any offering of help. I already created a setup.py file, since i found advice that was sort of understandable, but i will provide a guide on how to install it manually.

# Installation
You can install these packages manually by moving the files into a directory.

## Windows:
1. Download the desired files from a release (i recommend the latest stable). If you have WinRAR or 7zip installed, you can download the corresponding files.
2. Unpack the downloaded file with your favourite tool (or directly with Windows Explorer by right-clicking it, and selecting `Extract all`) in a new subfolder.
3. Press `WIN` + `R`. Type `appdata` and press `Enter`. It will open a explorer window, which should show 3 Folders: `Local`, `LocalLow` and `Roaming`. Open the `Local` folder.
4. Navigate to `\Programs\Python`. Now, open the folder corresponding to your Python version (example: with version 3.9 installed, you should open the folder `Python39`) and go into `Lib`
5. Now, move your extracted folder to your just opened window. This can be done by:
  - Drag & dropping it
  - Selecting your extracted folder, press `Strg` + `X`. Now, go back into your `Lib` folder and press `Strg` + `V`.
6. Done. You can test, if it's installed correctly by running a commandline and running the command `py` (or `python`/`python3`). Now, type `import osplus`
If you get an error, it didn't work. You can report any issues in the [GitHub Issue Tracker](https://github.com/QuatschVirus/osplus/issues)

## Linux/Ubuntu:
1. Open a command window (SSH works too). Run `cd ~` and `wget https://github.com/QuatschVirus/osplus/raw/main/archives/osplus.tar.gz`
2. Now, extract and decompress the file. Run `tar -xvzf osplus.tar.gz`.
3. Copy the created folder `osplus` into the `/usr/lib/python3` directory by running `sudo cp -v osplus /usr/lib/python3`
4. Done! You can test it by running `python3` and `import osplus`
If If you get an error, it didn't work. You can report any issues in the [GitHub Issue Tracker](https://github.com/QuatschVirus/osplus/issues)
To get out of the python interpreter, run `exit()`
