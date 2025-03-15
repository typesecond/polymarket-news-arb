import yt_dlp
import subprocess
import os 
import threading


class YtAudioExtractor: 
    def __init__(self, output_dir="audio_chunks", segment_duration=10): 
        """
            initialize audio extractor
        """
        self.output_dir = output_dir
        self.segment_duration = segment_duration
        self.process = None
        self.is_running = False

        # output dir for audio
        os.makedirs(output_dir, exist_ok=True)


    def extractor(self, URL): 

        self.is_running = True

        segment_pattern = os.path.join (
                self.output_dir,
                f"chunk_%Ym%d%_%H%M%S.wav"

            ) 


        cmd = [ 
            "ffmpeg" 
        

