# wypisywanie obrazow
# wypisywanie istneijacych kontenerow
# bindowanie do br
# zmiana statusu up/down
# usuwanie kontenerow
# (masowe )tworzenie kontenerow z obrazow
# dane kontenera
#

import gtk

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()

        self.connect("destroy", gtk.main_quit)
        self.set_title("Title")
        self.set_size_request(250, 150)
        self.set_position(gtk.WIN_POS_CENTER)


        self.btn1 = gtk.Button("b1")
        self.btn2 = gtk.Button("b2")
        self.btn1.connect('clicked', lambda widget: None)

        table = gtk.Table(5, 4, True)
        table.attach(self.btn1, 0, 1, 0, 2)
        table.attach(self.btn2, 1, 2, 0, 2)

        # vbox = gtk.VBox(False, 1)
        # vbox.pack_start(table, False, False, 0)
        # self.add(vbox)
        self.add(table)
        self.show_all()

PyApp()
gtk.main()
