'''
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
'''
def import_mp3():
	basedir = "D:\Library\Automatically Add to iTunes"
	librarybase = "D:\Library\Music"
	newpath = librarybase
	print "Before main loop"
	print basedir
	print librarybase
	for r,d,f in os.walk(basedir):
		print "Walking %s" % basedir
		for file in f:
			print "Processing %s" % file
			filepath = os.path.join(r, file)
			x = eyed3.load(filepath)
			artist = x.tag.artist
			album = x.tag.album
			print "%s by %s" % (album, artist)
			#re.sub(r'<>:"\/|?*', '', album)
			#re.sub(r'<>:"\/|?*', '', artist)
			newpath = os.path.join(librarybase, artist, album)
			if not os.path.exists(newpath):
				os.makedirs(newpath)
			mp3path = os.path.join(newpath, file)
			os.rename(filepath, mp3path)
			print "Moved %s to %s" % (filepath, mp3path)
			
def import_mp4():
	basedir = "D:\Library\Automatically Add to iTunes"
	librarybase="D:\Library\Movies"
	newpath = librarybase
	print "Before main loop"
	for r,d,f in os.walk(basedir):
		print "Walking %s" % basedir
		for file in f:
			name=os.path.basename(file)
			foldername=name[:-4].replace("_","")
			foldername=foldername.split("(")[0]
			newpath=librarybase+"\\"+foldername
			
			if not os.path.exists(newpath):
				os.makedirs(newpath)
			
			for x in range(0,3):
				try:
					os.rename(filepath, librarybase+"\\"+name)
					return
				except Exception as e:
					print e
					print "Trying again in 5 seconds"
					sleep(5)
					
'''
