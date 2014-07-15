'''
REQUIRES eyed3 to be installed
import_mp3(filepath)
        Takes file in filepath and movies it into the music library in the following format:
                base/Artist/Album/song.mp3
        Some error checking included for file transfers into directory
'''

import eyed3
import re
import os
from shutil import move
from time import sleep

def import_mp3(filepath):
	basedir = "D:\Library\Automatically Add to iTunes"
	librarybase = "D:\Library\Music"
	errordir=os.path.join(basedir,"Errors")

	x = eyed3.load(filepath)
	artist = x.tag.artist
	album = x.tag.album
	print "\tIdentified as: %s by %s" % (album, artist)
	#re.sub(r'<>:"\/|?*', '', album)
	#re.sub(r'<>:"\/|?*', '', artist)
	newpath = os.path.join(librarybase, artist, album)
	if not os.path.exists(newpath):
		os.makedirs(newpath)
	mp3path = os.path.join(newpath, os.path.basename(filepath))
	for x in range(0,5):
                try:
                        os.rename(filepath, mp3path)
                        print "\tMoved %s to %s" % (filepath, mp3path)
                        return
                except Exception as e:
                        if 32 == e.args[0] or 13 == e.args[0]:
                                print "\tError 32. File in use. Try again in 5 seconds"
                                sleep(5)
                        elif 183 == e.args[0]:
                                print "\tError 183. File already exists in library"
                                if not os.path.exists(errordir):
                                        os.makedirs(errordir)
                                move(filepath, os.path.join(errordir,os.path.basename(filepath)))
                                return
