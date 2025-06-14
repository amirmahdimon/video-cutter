import os
import subprocess
from tqdm import tqdm

def parse_time(time_str):
    """
    Convert time string to seconds. Handles both 'HH:MM:SS' and decimal seconds formats.
    
    Args:
        time_str (str): Time in 'HH:MM:SS' (e.g., '00:00:41.11') or decimal seconds (e.g., '41.11').
    
    Returns:
        float: Time in seconds.
    
    Raises:
        ValueError: If the time format is invalid.
    """
    parts = time_str.split(':')
    if len(parts) == 1:  # Decimal seconds like '41.11'
        return float(parts[0])
    elif len(parts) == 3:  # 'HH:MM:SS' like '00:00:41.11'
        h, m, s = parts
        h = int(h)
        m = int(m)
        s = float(s)  # Support decimal seconds
        return h * 3600 + m * 60 + s
    else:
        raise ValueError("Invalid time format")

def get_video_duration(video_path):
    """
    Get the duration of the video using FFmpeg.
    
    Args:
        video_path (str): Path to the video file.
    
    Returns:
        float: Duration in seconds, or 0 if not found.
    """
    cmd = ['ffmpeg', '-i', video_path]
    result = subprocess.run(cmd, stderr=subprocess.PIPE, text=True)
    for line in result.stderr.split('\n'):
        if 'Duration:' in line:
            duration_str = line.split('Duration: ')[1].split(',')[0]
            return parse_time(duration_str)
    return 0

def cut_video(video_path, timeline_file, output_dir="output_clips"):
    """
    Cut the video based on timelines from a text file.
    
    Args:
        video_path (str): Path to the input video file.
        timeline_file (str): Path to the text file with timelines.
        output_dir (str): Directory to save output clips (default: 'output_clips').
    """
    # Read timelines from the text file
    with open(timeline_file, 'r') as f:
        timelines = [line.strip() for line in f if line.strip()]

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get total duration of the video
    total_duration = get_video_duration(video_path)

    # Process each timeline with a progress bar
    for i, timeline in enumerate(tqdm(timelines, desc="Cutting videos")):
        try:
            start_str, end_str = timeline.split(' - ')
            start = parse_time(start_str)
            end = parse_time(end_str)

            # Validate the timeline
            if start < 0 or end > total_duration or start >= end:
                print(f"Invalid timeline: {timeline}")
                continue

            # Define output path for the clip
            output_path = os.path.join(output_dir, f"clip_{i+1}.mp4")

            # Run FFmpeg command to cut the video
            cmd = [
                'ffmpeg',
                '-i', video_path,
                '-ss', str(start),  # Start time
                '-to', str(end),    # End time
                '-c', 'copy',       # Copy without re-encoding for speed
                '-y',               # Overwrite output file if it exists
                output_path
            ]
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except ValueError as e:
            print(f"Format error in timeline: {timeline}")
            continue

if __name__ == "__main__":
    # Set file paths (update these as needed)
    video_path = "video.mp4"        # Path to your video file
    timeline_file = "timeline.txt"  # Path to your timeline text file
    output_dir = "output_clips"     # Directory for output clips

    cut_video(video_path, timeline_file, output_dir)
    print("Video cutting completed!")