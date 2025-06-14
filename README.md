video-cutter
A free and simple Python script to cut long videos into smaller clips based on timestamps provided in a text file. It uses FFmpeg to efficiently cut the video without re-encoding, making it fast and preserving the original quality.

Prerequisites

Python 3: Required to run the script.
FFmpeg: A required dependency for video processing.
tqdm: A Python library for progress feedback.


Installation

Install Python 3:

If you don’t have Python 3 installed, download and install it from python.org.


Install FFmpeg:

macOS:brew install ffmpeg


Windows:
Download FFmpeg from ffmpeg.org.
Extract the files and add the bin directory to your system’s PATH.


Linux:
Use your package manager, e.g., sudo apt install ffmpeg for Ubuntu.




Install tqdm:

Open a terminal and run:pip3 install tqdm






Usage

Prepare your video file:

Place your video file in the same directory as the script.
Important: The video file is not included in this repository. You must provide your own video file and ensure it is named video.mp4. If your video has a different name or extension, update the video_path variable in the script accordingly.


Create a timeline file:

Create a text file named timeline.txt in the same directory as the script.
Add the desired timestamps for cutting the video, one per line, in the format start_time - end_time. For example:00:00:10 - 00:00:20
00:01:30 - 00:01:45.5
41.11 - 50.25




Run the script:

Open a terminal and navigate to the directory containing the script.
Execute the script with Python 3:python3 video_cutter.py


A progress bar will display the cutting progress.


Check output:

The cut video clips will be saved in a directory named output_clips within the same directory.




Notes

The script supports timestamps in both HH:MM:SS format (e.g., 00:00:41.11) and decimal seconds (e.g., 41.11).
Invalid timelines (e.g., negative times, end before start) will be skipped with a warning message.
The original video file remains unchanged.

