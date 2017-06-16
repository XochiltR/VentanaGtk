#coding=utf8

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

ventana=Gtk.Window()
ventana.set_title("Curso de python")
ventana.connect("delete-event", Gtk.main_quit)
ventana.show()

caja=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
caja.show()
ventana.add(caja)

etiqueta= Gtk.Label("Hey everybody")
etiqueta.show()
caja.pack_start(etiqueta, True, False,0)


boton= Gtk.Button("Salir")
boton.show()
boton.connect("clicked",Gtk.main_quit)
caja.pack_start(boton, False, False,0)
         



Gtk.main()
