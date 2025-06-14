<!DOCTYPE html>
<html lang="en">
<body>
    <section>
        <h2>Prerequisites</h2>
        <ul>
            <li><strong>Python 3</strong>: Required to run the script.</li>
            <li><strong>FFmpeg</strong>: A required dependency for video processing.</li>
            <li><strong>tqdm</strong>: A Python library for progress feedback.</li>
        </ul>
    </section>
    <section>
        <h2>Installation</h2>
        <ol>
            <li>
                <h3>Install Python 3</h3>
                <p>If you don’t have Python 3 installed, download and install it from <a href="https://www.python.org/" target="_blank">python.org</a>.</p>
            </li>
            <li>
                <h3>Install FFmpeg</h3>
                <ul>
                    <li><strong>macOS</strong>:
                        <pre><code>brew install ffmpeg</code></pre>
                    </li>
                    <li><strong>Windows</strong>:
                        <p>Download FFmpeg from <a href="https://ffmpeg.org/download.html" target="_blank">ffmpeg.org</a>. Extract the files and add the <code>bin</code> directory to your system’s PATH.</p>
                    </li>
                    <li><strong>Linux</strong>:
                        <p>Use your package manager, e.g., <code>sudo apt install ffmpeg</code> for Ubuntu.</p>
                    </li>
                </ul>
            </li>
            <li>
                <h3>Install tqdm</h3>
                <p>Open a terminal and run:</p>
                <pre><code>pip3 install tqdm</code></pre>
            </li>
        </ol>
    </section>
    <section>
        <h2>Usage</h2>
        <ol>
            <li>
                <h3>Prepare your video file</h3>
                <p>Place your video file in the same directory as the script.</p>
                <p><strong>Important</strong>: The video file is not included in this repository. You must provide your own video file and ensure it is named <code>video.mp4</code>. If your video has a different name or extension, update the <code>video_path</code> variable in the script accordingly.</p>
            </li>
            <li>
                <h3>Create a timeline file</h3>
                <p>Create a text file named <code>timeline.txt</code> in the same directory as the script. Add the desired timestamps for cutting the video, one per line, in the format <code>start_time - end_time</code>. For example:</p>
                <pre><code>00:00:10 - 00:00:20
00:01:30 - 00:01:45.5
41.11 - 50.25</code></pre>
            </li>
            <li>
                <h3>Run the script</h3>
                <p>Open a terminal and navigate to the directory containing the script. Execute the script with Python 3:</p>
                <pre><code>python3 video_cutter.py</code></pre>
                <p>A progress bar will display the cutting progress.</p>
            </li>
            <li>
                <h3>Check output</h3>
                <p>The cut video clips will be saved in a directory named <code>output_clips</code> within the same directory.</p>
            </li>
        </ol>
    </section>

    <section>
        <h2>Notes</h2>
        <ul>
            <li>The script supports timestamps in both <code>HH:MM:SS</code> format (e.g., <code>00:00:41.11</code>) and decimal seconds (e.g., <code>41.11</code>).</li>
            <li>Invalid timelines (e.g., negative times, end before start) will be skipped with a warning message.</li>
            <li>The original video file remains unchanged.</li>
        </ul>
    </section>
</body>
</html>
