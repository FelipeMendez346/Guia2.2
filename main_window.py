#importacion de librerias a utilizar
import re
import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gdk

class Biblioteca(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="org.ejemplo.App")

    def do_activate(self):
        self.window = Gtk.ApplicationWindow(application=self)
        self.window.set_title("Registro de Libros")
        self.window.set_default_size(480, 360)

        # Crear un box al cual se le agregaran los recuadros
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.window.set_child(box)

        # agrego el widget del titulo junto a su entrada
        self.titulo_entry = Gtk.Entry()
        self.titulo_entry.set_text("Titulo del libro")
        box.append(self.titulo_entry)

        # agregacion del widget autor junto a su entrada
        self.autor_entry = Gtk.Entry()
        self.autor_entry.set_text("Autor/a")
        box.append(self.autor_entry)

        # comboboxtext para organicar los generos
        self.genero_combo = Gtk.ComboBoxText()
        self.genero_combo.append("Ficcion", "Ficcion")
        self.genero_combo.append("Ciencia", "Ciencia")
        self.genero_combo.append("Historia", "Historia")
        self.genero_combo.append("Infantil", "Infantil")
        box.append(self.genero_combo)

        # check de disponibilidad
        self.disponible_check = Gtk.CheckButton(label="Disponible")
        box.append(self.disponible_check)

        # button de registro
        self.registrar_button = Gtk.Button(label="Registrar")
        self.registrar_button.connect("clicked", self.on_registrar_clicked)
        box.append(self.registrar_button)

        self.window.show()
    # funcion al apretar el boton de registrar y checkeo de datos
    def on_registrar_clicked(self, button):
        titulo = self.titulo_entry.get_text()
        autor = self.autor_entry.get_text()
        genero = self.genero_combo.get_active_text()
        disponible = self.disponible_check.get_active()
        if not re.fullmatch(r"[A-Za-z]+", titulo):
            self.mostrar_dialogo("Error","No se ha podido ingresar el titulo del libro por ingreso de numeros o simbolos inapropiados")
            return
        if not re.fullmatch(r"[A-Za-z]+", autor):
            self.mostrar_dialogo("Error","No se ha podido ingresar el autor por ingreso numeros o simbolos inapropiados")
            return
        if (genero==None):
            self.mostrar_dialogo("Error","No se ha podido ingresar el genero,porfavor ingreselo")
            return
        else:

            self.mostrar_dialogo("Éxito", f"El libro '{titulo}' se ha registrado con éxito.")
    #funcion para crear una burbuja de texto/dialog 
    def mostrar_dialogo(self, title, message):
        dialogo = Gtk.MessageDialog(
            transient_for=self.window,
            modal=True,
            title=title,
            text=message,
            buttons=Gtk.ButtonsType.OK,
        )
        dialogo.connect("response",self.cerrar_dialogo)
        dialogo.present()
    #cierra la burbuja de texto
    def cerrar_dialogo(self, widget, action):
        widget.destroy()


#inicia la aplicacion
if __name__ == "__main__":
    app = Biblioteca()
    app.run()
