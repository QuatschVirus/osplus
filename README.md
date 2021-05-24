# osplus
A python package for additional, simple features like easy config files, logging, and notefications (full only)
NOTE: Since i'm too dumb to upload this to PyPi to make it installable via pip, i'm happy about any offering of help. 😁 I already created a setup.py file, since i found advice that was sort of understandable, but i will provide a guide on how to install it manually.
It has two packages: Full (osplus) and Lite (ospluslite). This is due to the fact that some instances (for example the preinstalled one on Raspberry Pi OS Lite) don't tkinter, because they are text-only systems. So, ospluslite doesn't include the graphical features. Since i'm too lazy to write it everywhere where i mention it: **Every "osplus" in code examples can be replaced with "ospluslite", as long as not marked otherwise**

# Installation
You can install these packages manually by moving the files into a directory. You can also manually install all dependencies by running the pip command with the -r parameter and the requirements.txt file as target. I will try to provide a batch script for windows and eventually a bash script for linux/ubuntu. I don't know a corresponding type for mac, help is wanted.

So if you are able to run a batch/bash script, you can just doubleclick on it or run a console in the downloaded and unpacked folder (or navigating there using `cd`) and typing `install.bat` (windows) or `install.sh` (linux/ubuntu)

## Alternative:
### Windows:
1. Download the desired files from a release (i recommend the latest stable). If you have WinRAR or 7zip installed, you can download the corresponding files directly.
2. Unpack the downloaded file with your favourite tool (or directly with Windows Explorer by right-clicking it, and selecting `Extract all`) in a new subfolder.
3. Press `WIN` + `R`. Type `appdata` and press `Enter`. It will open a explorer window, which should show 3 Folders: `Local`, `LocalLow` and `Roaming`. Open the `Local` folder.
4. Navigate to `\Programs\Python`. Now, open the folder corresponding to your Python version (example: with version 3.9 installed, you should open the folder `Python39`) and go into `Lib`
5. Now, move your extracted folder to your just opened window. This can be done by:
  - Drag & dropping it
  - Selecting your extracted folder, press `Strg` + `X`. Now, go back into your `Lib` folder and press `Strg` + `V`.
6. Done. You can test, if it's installed correctly by running a commandline and running the command `py` (or `python`/`python3`). Now, type `import osplus`
If you get an error, it didn't work. You can report any issues in the [GitHub Issue Tracker](https://github.com/QuatschVirus/osplus/issues)

### Linux/Ubuntu:
1. Open a command window (SSH works too). Run `cd ~` and `wget https://github.com/QuatschVirus/osplus/raw/main/osplus/latest.tar.gz` (`wget https://github.com/QuatschVirus/osplus/raw/main/ospluslite/latest.tar.gz` for Lite version)
2. Now, extract and decompress the file. Run `tar -xvzf osplus.tar.gz`.
3. Copy the created folder `osplus` into the `/usr/lib/python3` directory by running `sudo cp -v osplus /usr/lib/python3`
4. Done! You can test it by running `python3` and `import osplus`
If If you get an error, it didn't work. You can report any issues in the [GitHub Issue Tracker](https://github.com/QuatschVirus/osplus/issues)
To get out of the python interpreter, run `exit()`
