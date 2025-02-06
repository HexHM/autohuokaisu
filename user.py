# PYSIDE6-MALLINE SOVELLUKSEN PÄÄIKKUNAN LUOMISEEN
# KÄÄNNETYSTÄ KÄYTTÖLIITTYMÄTIEDOSTOSTA (mainWindow_ui.py)
# =====================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------
import os # Polkumääritykset
import sys # Käynnistysargumentit

import time
import json

from PySide6 import QtWidgets # Qt-vimpaimet
from lendingmodules import sound, cipher, dbOperations


# mainWindow_ui:n tialle käännetyn pääikkunan tiedoston nimi
# ilman .py-tiedostopäätettä
from user_ui import Ui_MainWindow # Käännetyn käyttöliittymän luokka

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

        # Ohjelman käynnistyksessö piilotetaamn tarpeettomat elementit
        self.ui.teacherPictureLabel.hide()
        self.ui.readCarCardLineEdit.hide()
        self.ui.keyPictureLabel.hide()
        self.ui.readKeyLineEdit.hide()
        self.ui.okButtonLabel.hide()
        self.ui.carInfoLabel.hide()
        self.ui.personInfoLabel.hide()
        self.ui.cardReadLabel.hide()
        
            # Rutiini, joka lukee asetukset, jos ne ovat olemassa
        try:
            # Avataam asetustiedosto ja muutetaan se Python sanakirjaksi
            with open('settings.json', 'rt') as settingsFile: # With sulkee tiedoston automaattisesti
                
                jsonData = settingsFile.read()
                self.currentSettings = json.loads(jsonData)
            
            # Puretaan salasana tietokantaoperaatioita varten  
            self.plainTextPassword = cipher.decryptString(self.currentSettings['password'])
        except Exception as error:
            self.openWarning()

        self.soundOn = True
        

        # OHJELMOIDUT SIGNAALIT
        # ---------------------
        
        # Kun Tulosta-painiketta on klikattu, kutsutaan updatePrintedLabel-metodia
        # self.ui.tulostaPushButton.clicked.connect(self.updatePrintedLabel)
    
        self.ui.takeCarPushButton.clicked.connect(self.takeCar)
        self.ui.readCarCardLineEdit.returnPressed.connect(self.showKeyLineEdit)
        self.ui.resetPushButton.clicked.connect(self.resetWindowdef)
        self.ui.resetPushButton_2.clicked.connect(self.resetWindowdef)
        self.ui.returnCarPushButton.clicked.connect(self.returnCar)
        self.ui.readKeyLineEdit.returnPressed.connect(self.okPushButton)  
        
        
        
        message= 'Aloita painamalla nappia'
        self.ui.statusbar.showMessage(message)
   
   
   
    # OHJELMOIDUT SLOTIT
    # ------------------
    def takeCar(self):
        """function to rent car
        """
        self.ui.teacherPictureLabel.show()
        self.ui.readCarCardLineEdit.show()
        self.ui.readCarCardLineEdit.setFocus()
        message = 'Lue ajokortin viivakoodi'
        self.ui.statusbar.showMessage(message)

        
    def returnCar(self):
        """
        Purpose: function to return the car
        """
        self.ui.keyPictureLabel.show()
        self.ui.readKeyLineEdit.show()
        self.ui.returnCarPushButton.hide()
        self.ui.takeCarPushButton.hide()
        message = "Lue avaimenperä lukijaan"
        self.ui.statusbar.showMessage(message)
        self.ui.statusbar.showMessage(message)
        self.ui.readKeyLineEdit.returnPressed.connect(self.okPushButton)




    # Muutetaan tulostettuLabel:n sisältö: teksti ja väri
    # def updatePrintedLabel(self):
    #     self.ui.tulostettuLabel.setText('Tulostettu')
    #     self.ui.tulostettuLabel.setStyleSheet(u"color: rgb(0, 255, 0);")

    # Avataan MessageBox
    # Malli mahdollista virheilmoitusta varten
    def openWarning(self, title: str, text:str, detailedText:str) -> None: 
        """Opens a message box for errors

        Args:
            title (str): The title of the message box
            text (str): Error message
            detailedText (str): Detailed error message typicallyfrom source
        """
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle(title)
        msgBox.setText('Ota yhteyttä henkilökuntaan')
        msgBox.setDetailedText(detailedText)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()
        
    def openOk(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle('Kaikki onnistui')
        msgBox.setText('Hyvää päivän jatkoa')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()
        
        
    def showKeyLineEdit(self):
        """Shows line edit and focuses on it so that people
        can read the barcode of the key
        """
        
        self.ui.keyPictureLabel.show()
        self.ui.readKeyLineEdit.show()
        self.ui.personInfoLabel.show()
        self.ui.readKeyLineEdit.setFocus()
        message = 'ota ajokortti pois lukijasta ja laita avaimenperä lukijaan'
        self.ui.statusbar.showMessage(message)
        self.ui.readKeyLineEdit.returnPressed.connect(self.okPushButton)
#        self.ui.readKeyLineEdit.returnPressed.connect(self.openOk)  
        
        
    # def focusKey(self):
    #     while True:
    #         int=input
    #         if int=="":
    #             break
        

    def resetWindowdef (self):
        """
        Purpose: restarts window
        """
        self.ui.teacherPictureLabel.setText("")
        self.ui.readCarCardLineEdit.setText("")
        self.ui.keyPictureLabel.setText("")
        self.ui.readKeyLineEdit.setText("")
        self.ui.carInfoLabel.setText("")
        self.ui.personInfoLabel.setText("")
        self.ui.personInfoLabel.hide()
        self.ui.carInfoLabel.hide()
        self.ui.teacherPictureLabel.hide()
        self.ui.readCarCardLineEdit.hide()
        self.ui.keyPictureLabel.hide()
        self.ui.readKeyLineEdit.hide()
        self.ui.okButtonLabel.hide()
        self.ui.cardReadLabel.hide()
        self.ui.cardReadLabel.setText("Ajokortti luettu")
        self.ui.rentLabel.show()
        self.ui.returnLabel.show()
        self.ui.returnCarPushButton.show()
        self.ui.takeCarPushButton.show()
        message = 'Aloita painamalla nappia'
        self.ui.statusbar.showMessage(message)


    
    def saveLendingData(self):
        #Tallentaa tiedot
        
        # Luetaan tietokanta-asetukset paikallisiin muuttujiin
        dbSettings = self.currentSettings
        plainTextPassword = self.plainTextPassword
        dbSettings['password'] = plainTextPassword # Vaidetaan selväkieliseksi
        
        try:
            dbConnection = dbOperations.DbConnection(dbSettings)
            ssn = self.ui.readCarCardLineEdit.text()
            key = self.ui.readKeyLineEdit.text()
            dataDictionary = {'hetu': ssn,
                          'rekisterinumero': key}
            dbConnection.addToTable('lainaus', dataDictionary)
            
        except Exception as e:
            title = 'Lainaustietojen tallentaminen ei onnistu'
            text = 'Ajokortin tai auton tiedot virheelliset, ota yhteys henkilökuntaan'
            detailedText = str(e)
            self.openWarning(title, text, detailedText)
        
        
        # Luetaan tietokanta-asetukset paikallisiin muuttujiin
        dbSettings = self.currentSettings
        plainTextPassword = self.plainTextPassword
        dbSettings['password'] = plainTextPassword # Vaidetaan selväkieliseksi

        # Luodaan tietokantayhteys-olio
        dbConnection = dbOperations.DbConnection(dbSettings)
        ssn = self.ui.readCarCardLineEdit.text()
        key = self.ui.readKeyLineEdit.text()
        dataDictionary = {'hetu': ssn,
                          'rekisterinumero': key}
        dbConnection.addToTable('lainaus', dataDictionary)
        
    def saveReturnData(self):
        key = self.ui.readKeyLineEdit.text()
        pass

    
    
    # Tallennetaan lainauksen tiedot ja palautetaan käyttöliittymä
    def okPushButton(self):
        self.ui.okButtonLabel.show()
        self.ui.carInfoLabel.show()
        self.ui.statusbar.showMessage("Jos tiedot on oikein paina OK-nappia")
        #tallenna tiedot + message box
        #self.ui.okButtonLabel.clicked.connect(self.openOk)
        self.ui.okButtonLabel.clicked.connect(self.resetWindowdef)
        
    
    def unMute(self):
        self.soundOn = True
        self.ui.soundPushButton.connect(self.mute)
        pass
    
    
    def mute(self):
        self.soundOn = False
        self.ui.soundOffPushButton.connect(self.unMute)
        
        pass
    
    def setLastEditedElement(self):
        self.lastEditedElementName = "firstNameLineEdit"
        
    def showLastElementName(self):
        message = f"viimeksi käytetty kenttä on {self.lastEditedElementName}"
        self.ui.statusbar.showMessage(message)
        element = self.findChild(QtWidgets.QLineEdit, self.lastEditedElementName)
        element.setFocus()
    
        self.ui.firstNameLineEdit.editingFinished.connect(self.setLastEditedElement)
        self.ui.lastFocusButton.returnpressed.connect(self.showLastElementName)
        
                
         
         
    
# LUODAAN VARSINAINEN SOVELLUS
# ============================
app = QtWidgets.QApplication(sys.argv)

# Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
window = MainWindow()
window.show()

# Käynnistetään sovellus ja tapahtumienkäsittelijä
app.exec()

#quit()

#os.execl(sys.executable, sys.executable, *sys.argv)

