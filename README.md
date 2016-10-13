# AI-Smart-Mirror
Smart Mirror with a smart AI 🤖

Watch the video on how to make it here:
https://youtu.be/ejnE6DM-hqU

# Setup Guide

## Magic Mirror
Download the stable version of Node.js: 
https://nodejs.org/en/

Clone the latest MagicMirror code from:
https://github.com/MichMich/MagicMirror

Navigate inside the MagicMirror folder
```shell
cd MagicMirror
```

Install MagicMirror dependencies
```shell
sudo npm install
```
 
Verify it starts
```shell
npm start
```
 
Navigate out of the MagicMirror folder
```shell
cd ..
```
 
Clone this repository (AI Smart Mirror)
```shell
git clone git@github.com:HackerHouseYT/AI-Smart-Mirror.git
```

Copy the folders in `AI-Smart-Mirror/magic_mirror` to `MagicMirror/modules`

Copy the `config.js` file in `AI-Smart-Mirror/magic_mirror` to `MagicMirror/config`
 
## AI
 
Make sure Ruby is installed: https://www.ruby-lang.org/en/documentation/installation/
 
Install Homebrew: http://brew.sh/
 
Navigate to the AI-Smart-Mirror folder
```shell
cd AI-Smart-Mirror
```

Install ffmpeg
```
brew install ffmpeg
```

Use `setup.sh` to create a virtual environment and install dependencies
```shell
sudo ./setup.sh
```

Activate the virual evironment
```shell
source hhsmartmirror/bin/activate
```

Replace wit.ai and darksky.net tokens in the `bot.py` file

Make sure MagicMirror is running, then start the AI
```shell
python bot.py
```

## Setup Facial Recognition
Refer to this guide: https://www.learnopencv.com/install-opencv-3-on-yosemite-osx-10-10-x/

Install openCV with 
```shell
brew tap homebrew/science
brew install opencv
```

Open a new terminal tab with `command+t`

Check the version with
```shell
cd /usr/local/Cellar/opencv
ls
```
Return to the tab with AI-Smart-Mirror

Deactivate the virtual environment
```shell
deactivate
```

Navigate to the `site-packages` folder in the virtual environment
```shell
cd hhsmartmirror/lib/python2.7/site-packages
```

Link the `cv.py` and `cv2.so` files and replace `$VERSION` with the version you found
```shell
ln -s /usr/local/Cellar/opencv/$VERSION/lib/python2.7/site-packages/cv.py cv.py
ln -s /usr/local/Cellar/opencv/$VERSION/lib/python2.7/site-packages/cv2.so cv2.s
```

Check that the files are there
```shell
ls
```
Return the the AI-Smart-Mirror directory
```shell
cd ../../../..
```

Reactivate the virtual evironment
```shell
source hhsmartmirror/bin/activate
```

Start the app
```shell
python bot.py
```
 
