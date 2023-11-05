import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QFormLayout, QPushButton, \
    QLineEdit
from PyQt5 import QtGui





class Ventana1(QMainWindow):

    # Metodo constructor de la ventana
    def __init__(self,parent=None):
        super(Ventana1,self).__init__(parent)

        # poner el titulo
        self.setWindowTitle("Formulario de registro")

        # Ponemos el icono
        self.setWindowIcon(QtGui.QIcon('imagenes/cliente.jpg'))

        # Establecemos las propiedades de ancho por alto
        self.ancho = 900
        self.alto = 600

        # Establecemos el tamaño de la venata
        self.resize(self.ancho, self.alto)

        # Centrar la ventana en la pantalla
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Fijar el tamaño de la ventana para evitar cambiarlo
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # Establecemos el fondo principal
        self.fondo = QLabel(self)

        # Definimos la imagen de fondo
        self.imagenFondo = QPixmap('imagenes/empresa.jpg')

        # Definimos la iamgen de fondo
        self.fondo.setPixmap(self.imagenFondo)

        # Establecemos el modo para escalar la imagen
        self.fondo.setScaledContents(True)

        # Hacemos que se adapte al tamaño de la imagen
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # Establecemos la ventana de fondo como ventana central
        self.setCentralWidget(self.fondo)

        # Establecemos la distribucion de los elementos en layout horizontal
        self.horizontal = QHBoxLayout()
        # Le ponemos las margenes
        self.horizontal.setContentsMargins(30, 30, 30, 30)


        # --- LAYOUT IZQUIERDO ---

        # Creamos el layout del lado izquierdo
        self.ladoIzquierdo = QFormLayout()

        # Hacemos el letrero
        self.letrero1 = QLabel()

        # Le escribimos el texto
        self.letrero1.setText("Información del cliente")

        # Le asignamos el tipo de letra
        self.letrero1.setFont(QFont("Andale Mono",20))

        # Le asignamos color de texto
        self.letrero1.setStyleSheet("color: #000080;")

        # Agregamos el letrero en la primera fila
        self.ladoIzquierdo.addRow(self.letrero1)


        # Hacemos el letrero2
        self.letrero2 = QLabel()

        # Establecemos el ancho del label
        self.letrero2.setFixedWidth(340)

        # Le escribimos el texto
        self.letrero2.setText("Por favor ingrese la informacion del cliente"
                              "\nen el formulario de abajo. Los campos marcados"
                              "\ncon asterisco son obligatorios.")

        # Le asignamos el tipo de letra
        self.letrero2.setFont(QFont("Andale Mono", 10))

        # Le asignamos color de texto y margenes
        self.letrero2.setStyleSheet("color: #000080; margin-botton: 40px;"
                                    "margin-top: 20px;"
                                    "padding-botton: 10px;"
                                    "border: 2px solid #000080;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # Agregamos el letrero2 en la fila siguiente
        self.ladoIzquierdo.addRow(self.letrero2)


        # HACEMOS LOS CAMPO
        # Hacemos el campo para ingresar el nombre
        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Nombre Completo*", self.nombreCompleto)

        # Hacemos el campo para ingresar el usuario
        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Usuario*", self.usuario)

        # Hacemos el campo para ingresar el password
        self.password = QLineEdit()
        self.password.setFixedWidth(250)
        self.password.setEchoMode(QLineEdit.Password)

        # Agregamos estos en el formulario
        self.ladoIzquierdo.addRow("Password*", self.password)


        # Hacemos el campo para ingresar el password2
        self.password2 = QLineEdit()
        self.password2.setFixedWidth(250)
        self.password2.setEchoMode(QLineEdit.Password)

        # Agregamos estos en el formulario
        self.ladoIzquierdo.addRow("Password*", self.password2)


        # Hacemos el campo para ingresar el documento
        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        # Agregamos el documento en el formulario
        self.ladoIzquierdo.addRow("Documento*", self.documento)

        # Hacemos el campo para ingresar el correo
        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)

        # Agregamos el correo en el formulario
        self.ladoIzquierdo.addRow("Correo*", self.correo)


        # BOTON REGISTRAR
        # Hacemos el boton registrar los datos
        self.botonRegistrar = QPushButton("Registrar")

        # Establecemos el ancho del boton
        self.botonRegistrar.setFixedWidth(90)

        # Le ponemos los estilos
        self.botonRegistrar.setStyleSheet("background-color: #008845;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)



        # BOTON LIMPIAR
        # Hacemos el boton limpiar los datos
        self.botonLimpiar = QPushButton("Limpiar")

        # Establecemos el ancho del boton
        self.botonLimpiar.setFixedWidth(90)

        # Le ponemos los estilos
        self.botonLimpiar.setStyleSheet("background-color: #008845;"
                                        "color: #FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        # Agregamos los dos botones al layout ladoIzquierdo
        self.ladoIzquierdo.addRow(self.botonRegistrar, self.botonLimpiar)

        # Agregamos el layout ladoIzquierdo al layout hotizontal
        self.horizontal.addLayout(self.ladoIzquierdo)




        # --- OJO IMPORTANTE PONER AL FINAL ---

        # indicamos que el layout principal del fondo es horizontal
        self.fondo.setLayout(self.horizontal)


    def accion_botonLimpiar(self):
        pass


    def accion_botonRegistrar(self):
        pass





if __name__ == "__main__":
    # Hacemos que la aplicacion de genere
    app = QApplication(sys.argv)

    # Crear un objeto de tipo Ventana1 con el nombre ventana1
    ventana1 = Ventana1()

    # Hacemos que el objeto ventana 1 se vea
    ventana1.show()

    # codigo para terminar la aplicación
    sys.exit(app.exec_())

