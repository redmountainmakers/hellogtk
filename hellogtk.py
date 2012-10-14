#/usr/bin/env python

import gtk

GLADE_FILE = "hellogtk.glade"

class HelloGTK():

    def __init__(self, gladeFile):
        self.builder = gtk.Builder() # create a gui builder object
        self.builder.add_from_file(gladeFile) # give it the file name
        
        # keep track of our mainWindow
        self.mainWindow = self.builder.get_object("mainWindow")
        
        self.mainWindow.set_name('HelloGTK')
        
        # point all gui function calls to the HelloGTK gui object
        self.builder.connect_signals(self)

    def main(self):
        self.mainWindow.show()
        gtk.main()
    
    def on_mainWindow_destroy(self, widget, data=None):
        gtk.main_quit(self, widget, data)

if __name__ == '__main__':
    gui = HelloGTK(GLADE_FILE)
    gui.main()
