# PYSIDE6-MALLINE SOVELLUKSEN PÄÄIKKUNAN LUOMISEEN
# KÄÄNNETYSTÄ KÄYTTÖLIITTYMÄTIEDOSTOSTA (mainWindow_ui.py)
# =====================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------
import os # Polkumääritykset
import sys # Käynnistysargumentit

import time

from lendingmodules import dbOperations

from PySide6 import QtWidgets # Qt-vimpaimet
from tietokantaTesti_ui import Ui_MainWindow # Käännetyn käyttöliittymän luokka

# Määritellään luokka, joka perii QMainWindow- ja Ui_MainWindow-luokan
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """A class for creating main window for the application"""
    
    # Määritellään olionmuodostin ja kutsutaan yliluokkien muodostimia
    def __init__(self):
        super().__init__()

        # Luodaan käyttöliittymä konvertoidun tiedoston perusteella MainWindow:n ui-ominaisuudeksi. Tämä suojaa lopun MainWindow-olion ylikirjoitukselta, kun ui-tiedostoa päivitetään
        self.ui = Ui_MainWindow()

        # Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.ui.setupUi(self)

        # OHJELMOIDUT SIGNAALIT
        # ---------------------
        
        # Kun tallennuspainiketta on klikattu, kutsutaan -metodia
        # self.ui.savePushButton.clicked.connect(self.saveData)

        # Kun Lainaa-painiketta on painettu, kutsutaan takeCar-metodia
        self.ui.takeCarPushButton.clicked.connect(self.takeCar)

        # Kun Henkilötunnus-kentästä poistutaan enterillä, 
        # Kun henkilötunnus kentästä poistutaan enterillä, tuodaan näkyviin Rekisterinumero-kenttä

        self.ui.readCarCardLineEdit.returnPressed.connect(self.showKeyLineEdit)

        self.ui.teacherPictureLabel.hide()
        self.ui.keyPictureLabel.hide()
        self.ui.readCarCardLineEdit.hide()
        self.ui.readKeyLineEdit.hide()
        
        # when pressing Palauta painiketta, calling for returnCar-method
        self.ui.returnCarPushButton.clicked.connect(self.returnCar)
        
        # when pressing reset button, calling for resetWindow method
        self.ui.resetPushButton.clicked.connect(self.resetWindowdef)
        self.ui.resetPushButton_2.clicked.connect(self.resetWindowdef)
        
        # Kun henkilötunnus kentästä poistutaan enterillä, tuodaan näkyviin Rekisterinumero-kenttä


    def showKeyLineEdit(self):
        self.ui.readKeyLineEdit.show()
        self.ui.readKeyLineEdit.setfocus()

        self.settingsDictionary = {'server': 'localhost',
                      'port': '5433',
                      'database': 'testaus',
                      'userName': 'postgres',
                      'password': 'Q2werty'}
        
     # Piilotetaan kuvat ja syöttökentät sovelluksen käynnistyksessä
        self.ui.teacherPictureLabel.hide()
        self.ui.keyPictureLabel.hide()
        self.ui.readCarCardLineEdit.hide()
        self.ui.readKeyLineEdit.hide()


    # OHJELMOIDUT SLOTIT
    # ------------------

    # Tallennetaan syötety tiedot tietokantaan
    # def saveData(self):
    #     dbconnection = dbOperations.DbConnection(self.settingsDictionary)
    #     data = {'etunimi': self.ui.firstNameLineEdit.text(),
    #             'sukunimi': self.ui.lastNameLineEdit.text()}
    #     dbconnection.addToTable('person', data)

    #     # Määritellään tilarivin teksti, näyttöaika 3 sek.
    #     message = f'Henkilön {self.ui.firstNameLineEdit.text()} {self.ui.lastNameLineEdit.text()} tiedot tallennettiin'
    #     self.ui.statusbar.showMessage(message, 3000)

    #     # Tyhjennetään kentät
    #     self.ui.firstNameLineEdit.clear()
    #     self.ui.lastNameLineEdit.clear()
        
    def takeCar(self):

        # Tuodaan lainauksen kuvat ja syöttökentät näkyviin
        self.ui.teacherPictureLabel.show()
        self.ui.keyPictureLabel.show()
        self.ui.readCarCardLineEdit.show()
        

        # Näytetään tilarivillä Ohjeteksti
        message = 'Lue ajokortin viivakoodi'
        self.ui.statusbar.showMessage(message)

    def showKeyLineEdit(self):
        self.ui.readKeyLineEdit.show()
        self.ui.readKeyLineEdit.setFocus()
        message = 'ota ajokortti pois lukijasta ja laita avaimenperä lukijaan'
        self.ui.statusbar.showMessage(message)
        self.ui.readKeyLineEdit.returnPressed.connect(self.resetWindowTimed) 
        #message = "Aja turvallisesti."
        #self.ui.statusbar.showMessage(message)

    def returnCar(self):
        """
        Purpose: funktion to return the car
        """
        self.ui.keyPictureLabel.show()
        self.ui.readKeyLineEdit.show()
        message = "Lue avaimenperä lukijaan"
        self.ui.statusbar.showMessage(message)
        self.ui.readKeyLineEdit.returnPressed.connect(self.resetWindowTimed)
        #message = "Hyvää päivän jatkoa"
        #self.ui.statusbar.showMessage(message)
        
    # end def

    def resetWindowdef (self):
        """
        Purpose: closes window to restart it. there maybe be better way to do it
        """
        self.close()
              
              
    def resetWindowTimed (self):
        """
        Purpose: closes window to restart it. there maybe be better way to do it
        """
        time.sleep(3)
        self.close()
        

        

    
    # end def

    # Avataan MessageBox
    # def openWarning(self):
    #     msgBox = QtWidgets.QMessageBox()
    #     msgBox.setIcon(QtWidgets.QMessageBox.Information)
    #     msgBox.setWindowTitle('Tiedot tallennettu')
    #     msgBox.setText(f'Henkilön {self.ui.lastNameLineEdit.text()} tiedot meinivät tietokantaan')
    #     msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
    #     msgBox.exec()


# Luodaan sovellus
app = QtWidgets.QApplication(sys.argv)

# Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
window = MainWindow()
window.show()

# Käynnistetään sovellus ja tapahtumienkäsittelijä
app.exec()

quit()

os.execl(sys.executable, sys.executable, *sys.argv)
