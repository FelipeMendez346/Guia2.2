import re
import gi
gi.require_version("Gtk","4.0")
from gi.repository import Gtk, GLib

Quit =False

def quit_(Window):
    global Quit
    Quit = True

class MiAplicacion(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="org.Biblioteca.App")

    def do_activate(self):
        ventana = Gtk.ApplicationWindow(application=self)
        print(ventana)
        print(type(ventana))
        ventana.set_title("Hola Mundo!!!")
        ventana.set_default_size(1280,960)

        box=Gtk.Box(orientation=Gtk.Orientation.Vertical,Spacing=6)

        box_entry=Gtk.Box(Orientation=Gtk.Orientation.VERTICAL,spacing=6)

        label_entry = Gtk.Label()
        label_entry.set_text("Ingrese su libro: ")
        self.text_entry=Gtk.Entry()

        self.label_result = Gtk.Label()
        self.label_result.set_text("Espero un resultado")

        box_entry.append(label_entry)
        box_entry.append(self.text_entry)
        box_entry.append(self.label_result)

    def cerrar_dialogo(self,widget,action):
        widget.destroy()
    
    def do_shutdown(self):
        print("Shutdown")
        Gtk.Application.do_shutdown(self)


app=MiAplicacion()
app.run()

