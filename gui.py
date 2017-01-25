# wypisywanie obrazow
# wypisywanie istneijacych kontenerow
# bindowanie do br
# zmiana statusu up/down
# usuwanie kontenerow
# (masowe )tworzenie kontenerow z obrazow
# dane kontenera
#

import gtk

import utils

class PyApp(gtk.Window):
    def __init__(self, title="Title"):
        super(PyApp, self).__init__()

        self.connect("destroy", gtk.main_quit)
        self.set_title(title)
        self.set_size_request(750, 550)
        self.set_position(gtk.WIN_POS_CENTER)

        self.NUM_OF_BRIDGES = 0

        # sections - image
        self.sw_image = gtk.ScrolledWindow()
        self.sw_image.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        self.store_image = gtk.ListStore(str)

        self.update_image_data()

        self.tv_image = gtk.TreeView(self.store_image)
        self.tv_image.connect("row-activated", lambda *a: None)
        self.tv_image.set_rules_hint(True)
        self.sw_image.add(self.tv_image)

        self.attach_columns(self.tv_image, ['image'])

        # sections - containers
        self.sw_container = gtk.ScrolledWindow()
        self.sw_container.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        self.store_container = gtk.ListStore(str, str, str)

        self.update_container_data()

        self.tv_container = gtk.TreeView(self.store_container)
        self.tv_container.connect("row-activated", lambda *a: None)
        self.tv_container.set_rules_hint(True)
        self.sw_container.add(self.tv_container)

        self.attach_columns(
                self.tv_container,
                # ['container', 'interface', 'ip address', 'state'])
                ['container', 'ip address', 'state'])

        self.b_start = gtk.Button("run")
        self.b_stop = gtk.Button("stop")
        self.b_remove = gtk.Button("remove")
        self.b_bind = gtk.Button("attach")
        self.b_spawn = gtk.Button("spawn")

        self.e_spawn = gtk.Entry()
        # self.btn1.connect('clicked', lambda widget: None)
        self.b_start.connect('clicked', lambda x: self.update_container_data())

        table = gtk.Table(6, 6, True)

        table.attach(self.sw_image, 0, 1, 0, 6)
        table.attach(self.sw_container, 1, 5, 0, 6)

        # buttons
        table.attach(self.b_start, 5, 6, 0, 1)
        table.attach(self.b_stop, 5, 6, 1, 2)
        table.attach(self.b_bind, 5, 6, 2, 3)
        table.attach(self.b_remove, 5, 6, 3, 4)
        table.attach(self.e_spawn, 5, 6, 4, 5)
        table.attach(self.b_spawn, 5, 6, 5, 6)

        self.add(table)
        self.show_all()

    def attach_columns(self, tv, columns):
        for i, header in enumerate(columns):
            renderer = gtk.CellRendererText()
            column = gtk.TreeViewColumn(header, renderer, text=i)
            column.set_sort_column_id(i)
            tv.append_column(column)

    def update_image_data(self):
        self.store_image.clear()
        names = utils.get_images_names()
        for n in names:
            self.store_image.append([n])

    def update_container_data(self):
        self.store_container.clear()
        names = utils.get_containers_names()
        data = [utils.inspect_container(i) for i in names]
        for d in data:
            key = d.keys()[0]
            row = [key, d[key][0], d[key][1]]
            self.store_container.append(row)


PyApp(title='Manager')
gtk.main()
