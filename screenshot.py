#!/usr/bin/env python
# PyMtGoxMon v1.0 - Python-based monitor for MtGox BTC trading!
# Copyright (C) 2013 Albert Huang.
# Under GPL v3.
# 
# Screenshot module for PyMtGoxMon. Requires pygtk to run!
# screenshot.py
import gtk.gdk

def screenshot(file_name):
	w = gtk.gdk.get_default_root_window()
	sz = w.get_size()
	print "The size of the window is %d x %d" % sz
	pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
	pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
	if (pb != None):
		pb.save(file_name,"png")
		print "Screenshot saved to %s." % file_name
	else:
		print "Unable to get the screenshot."
