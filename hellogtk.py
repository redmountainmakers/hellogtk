#/usr/bin/env python

import gtk

GLADE_FILE = "hellogtk.glade"

class HelloGTK():

    def __init__(self, gladeFileName):
        self.builder = gtk.Builder() # create a gui builder object
        self.builder.add_from_file(gladeFileName) # give it the file name
        
        # keep track of our mainWindow
        self.mainWindow = self.builder.get_object("mainWindow")
        
        # point all gui function calls to the HelloGTK gui object
        self.builder.connect_signals(self)

    def main(self):
        self.mainWindow.show() # show the main window
        gtk.main() # start the gtk event processing loop
    
    def on_mainWindow_destroy(self, widget, data=None):
        gtk.main_quit(self, widget, data) # quit the gtk event loop

if __name__ == '__main__':
    gui = HelloGTK(GLADE_FILE)
    gui.main()
