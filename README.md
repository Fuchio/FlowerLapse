# FlowerLapse
FlowerLapse is a fully configurable tool to create timelapses. It depends on just OpenCV for all image related stuff (reading/writing, combining, overlays, etc.) and AP Scheduler to schedule the framegrabber and timelapse generator jobs. There currently is a bug in AP Scheduler that prevents the possibility to create and Interval AND Cron trigger, this means that if you specify seconds = 40, the job will run once a minute but every time at 1:40, 2:40, 3:40 etc. So the true interval will still be one minute. Clean divisions of 1 hour or 1 minute are recommended (30s, 20s, 15s, 10s etc.).

# Usage
## Flowerlapse.py (image generation and daily timelapses)
After installation (see how to install below) navigate to the FlowerLapse directory and run the following command:\
`python flowerlapse.py`\

This runs FlowerLapse with the following DEFAULT settings. An example with custom settings looks like this:\
`python flowerlapse.py cam_id 2 --min_between 2 --path C:/User/Fuchio/Desktop --timelapse_id cool_timelapse`\

To test your camera use one of the lines below:\
`python flowerlapse.py -test_image`: Takes a single frame and shows if possible (NOT TESTED ON LINUX SERVER).\
`python flowerlapse.py -test_stream`: Shows a videostream of the current camera.\
Both can be ran by specifying a different camera id with --cam_id.

## Flowerlapse.py Features
`--cam_id`: ID of your camera. Should be 0 if only one is connected. Default = 0.\
`--timelapse_id`: ID of the timelapse, used to create directories. Default = randomly generated.\
`--sec_between`: Seconds between each image. Default = 30. **Mutually exclusive with min_between**\
`--min_between`: Minutes between each image. Default = 0 (not used). **Mutually exclusive with sec_between**\
`--start_hour`: Hour to start taking pictures Between 0 and 24. Default = 8.\
`--end_hour`: Hour to end taking pictures. Between 0 and 24. Default = 22.\
`--timezone`: Timezone for correct start and end hour settings. Default = CET.\
`--fps`: FPS for the daily timelapse. Default = 30.\
`--path`: Base path to save your timelapse.\
`--extension`: Image extension to save the images. Default = jpg.\
`-overlay_off`: BOOL add -overlay_off to the flowerlapse.py call to create timelapse without timestamp overlay.\
`-test_image`: BOOL add -test_image to run the single image test instead of timelapse generation.\
`-test_stream`: BOOL add -test_stream to run the video stream test instead of timelapse generation.\

## Concatenate.py (extended timelapse generation)
Navigate to the FlowerLapse directory and run the following command:\
`python concatenate.py --timelapse_id <your_timelapse_id>`\
The features for concatenate.py work the same as flowerlapse. See possibilities below.\

## Concatenate.py Features
`--timelapse_id`: **REQUIRED** ID of all the timelapse where all daily timelapses will be taken from.\
`--path`: **Required if** specified with flowerlapse.py. Base path where your timelapse is saved.\
`--start_date`: TODO\
`--end_date`: TODO\
`--fps`: FPS for the total timelapse. Default = 30.\

# NOTES:
- Daily timelapses are created at 23:55 of that day.\

# Installation
Clone this repo with:\
`git clone https://github.com/Fuchio/FlowerLapse.git`\
Install requirements:\
`pip install -r requirements.txt`\
Navigate to /FlowerLapse/ and you should be able to run the code!\

If you get "opencv importerror libclass.so.3" run the following:\
`sudo apt-get install libatlas-base-dev`\

TODO features list:\
- Possibility to restart an existing timelapse\
- Multiple options for video extension if requested, just .mp4 now\
- Add # of image and length of timelapse calculations to summary.py\
- Settable (x, y) resolution\
- Possibility to specify a start and end date for the total timelapse\
- ~~Use default camera resolution instead of 640x480~~\
- ~~Add overlay with current datetime and flowerlapse~~\


 # License:
 A Commons Clause license is used on top of Apache 2.0. This means you can still do pretty much anything with the code except taking it and selling it as is. If you build a complete application around this you are still free to sell the software.
