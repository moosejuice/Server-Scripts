'''
REQUIRES watchdog to be installed
To imitate what iTunes does to the Automatically Add to iTunes folder
Detects new mp4 files and mp3 files in this directory.
mp4 files are treated as movies and added to the movie library
mp3 files are added to the music library as Music/Artist/Album/song.mp3
'''
from time import sleep
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler 
from organize_mp3 import import_mp3
from organize_mp4 import import_mp4
import os


class MyHandler(PatternMatchingEventHandler):
    patterns = ["*.mp4", "*.mp3"]

    def process(self, event):
        """
        event.event_type 
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        # the file will be processed there
        print event.src_path, event.event_type  # print now only for degug

    #def on_modified(self, event):
    #print "Modified File"

    def on_created(self, event):
                print "Processing :", os.path.basename(event.src_path)
		if event.src_path.endswith(".mp4"):
			sleep(4)
			import_mp4(event.src_path)
		else:
			sleep(1)
			import_mp3(event.src_path)
                print "\n"


if __name__ == "__main__":
    print "Initializing watch script"
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(MyHandler(), path="D:\Library\Automatically Add to iTunes")
    observer.start()
    print "Watch started on D:\Library\Automatically Add to iTunes"
 
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        event_handler.stop()
        observer.stop()
    observer.join()

