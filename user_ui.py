# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

import userUiRescources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon(QIcon.fromTheme(u"emblem-shared"))
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(223, 32, 112);")
        self.actionLopeta = QAction(MainWindow)
        self.actionLopeta.setObjectName(u"actionLopeta")
        icon1 = QIcon(QIcon.fromTheme(u"application-exit"))
        self.actionLopeta.setIcon(icon1)
        self.actionKalle = QAction(MainWindow)
        self.actionKalle.setObjectName(u"actionKalle")
        self.actionVille = QAction(MainWindow)
        self.actionVille.setObjectName(u"actionVille")
        self.actionJaana = QAction(MainWindow)
        self.actionJaana.setObjectName(u"actionJaana")
        self.actionMikko = QAction(MainWindow)
        self.actionMikko.setObjectName(u"actionMikko")
        self.actionTallenna_nimell = QAction(MainWindow)
        self.actionTallenna_nimell.setObjectName(u"actionTallenna_nimell")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.readCarCardLineEdit = QLineEdit(self.centralwidget)
        self.readCarCardLineEdit.setObjectName(u"readCarCardLineEdit")
        self.readCarCardLineEdit.setEnabled(True)
        self.readCarCardLineEdit.setGeometry(QRect(510, 180, 271, 41))
        font = QFont()
        font.setPointSize(12)
        self.readCarCardLineEdit.setFont(font)
        self.readCarCardLineEdit.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"color: rgb(32, 75, 70);")
        self.readCarCardLineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.readCarCardLineEdit.setClearButtonEnabled(True)
        self.takeCarPushButton = QPushButton(self.centralwidget)
        self.takeCarPushButton.setObjectName(u"takeCarPushButton")
        self.takeCarPushButton.setGeometry(QRect(20, 20, 291, 231))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.takeCarPushButton.setFont(font1)
        self.takeCarPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.takeCarPushButton.setToolTipDuration(3000)
        self.takeCarPushButton.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 127);")
        self.keyPictureLabel = QLabel(self.centralwidget)
        self.keyPictureLabel.setObjectName(u"keyPictureLabel")
        self.keyPictureLabel.setGeometry(QRect(570, 280, 171, 111))
        self.keyPictureLabel.setAutoFillBackground(False)
        self.keyPictureLabel.setPixmap(QPixmap(u":/pictures/uiPictures/keys.png"))
        self.keyPictureLabel.setScaledContents(True)
        self.teacherPictureLabel = QLabel(self.centralwidget)
        self.teacherPictureLabel.setObjectName(u"teacherPictureLabel")
        self.teacherPictureLabel.setGeometry(QRect(550, -10, 201, 191))
        self.teacherPictureLabel.setPixmap(QPixmap(u"../kopio/uiPictures/teacher.png"))
        self.teacherPictureLabel.setScaledContents(True)
        self.returnCarPushButton = QPushButton(self.centralwidget)
        self.returnCarPushButton.setObjectName(u"returnCarPushButton")
        self.returnCarPushButton.setGeometry(QRect(20, 280, 291, 231))
        self.returnCarPushButton.setFont(font1)
        self.returnCarPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.returnCarPushButton.setToolTipDuration(3000)
        self.returnCarPushButton.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 127);")
        self.readKeyLineEdit = QLineEdit(self.centralwidget)
        self.readKeyLineEdit.setObjectName(u"readKeyLineEdit")
        self.readKeyLineEdit.setEnabled(True)
        self.readKeyLineEdit.setGeometry(QRect(510, 400, 271, 41))
        self.readKeyLineEdit.setFont(font)
        self.readKeyLineEdit.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"color: rgb(32, 75, 70);")
        self.readKeyLineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.readKeyLineEdit.setClearButtonEnabled(True)
        self.resetPushButton = QPushButton(self.centralwidget)
        self.resetPushButton.setObjectName(u"resetPushButton")
        self.resetPushButton.setGeometry(QRect(20, 280, 291, 231))
        font2 = QFont()
        font2.setPointSize(24)
        self.resetPushButton.setFont(font2)
        self.resetPushButton.setStyleSheet(u"background-color: rgb(0, 33, 72);\n"
"color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditUndo))
        self.resetPushButton.setIcon(icon2)
        self.resetPushButton_2 = QPushButton(self.centralwidget)
        self.resetPushButton_2.setObjectName(u"resetPushButton_2")
        self.resetPushButton_2.setGeometry(QRect(20, 20, 291, 231))
        self.resetPushButton_2.setFont(font2)
        self.resetPushButton_2.setStyleSheet(u"background-color: rgb(0, 33, 72);\n"
"color: rgb(255, 255, 255);")
        icon3 = QIcon(QIcon.fromTheme(u"edit-undo"))
        self.resetPushButton_2.setIcon(icon3)
        self.soundPushButton = QPushButton(self.centralwidget)
        self.soundPushButton.setObjectName(u"soundPushButton")
        self.soundPushButton.setGeometry(QRect(320, -20, 191, 191))
        icon4 = QIcon()
        icon4.addFile(u":/pictures/uiPictures/sound.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.soundPushButton.setIcon(icon4)
        self.soundPushButton.setIconSize(QSize(131, 131))
        self.soundOffPushButton = QPushButton(self.centralwidget)
        self.soundOffPushButton.setObjectName(u"soundOffPushButton")
        self.soundOffPushButton.setGeometry(QRect(320, -20, 191, 191))
        icon5 = QIcon()
        icon5.addFile(u":/pictures/uiPictures/soundOff.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.soundOffPushButton.setIcon(icon5)
        self.soundOffPushButton.setIconSize(QSize(131, 131))
        self.rentLabel = QLabel(self.centralwidget)
        self.rentLabel.setObjectName(u"rentLabel")
        self.rentLabel.setGeometry(QRect(20, 20, 291, 231))
        self.rentLabel.setFont(font1)
        self.rentLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.rentLabel.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"color: rgb(0, 0, 0);")
        self.rentLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.returnLabel = QLabel(self.centralwidget)
        self.returnLabel.setObjectName(u"returnLabel")
        self.returnLabel.setGeometry(QRect(20, 280, 291, 231))
        self.returnLabel.setFont(font1)
        self.returnLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.returnLabel.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"color: rgb(0, 0, 0);")
        self.returnLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.okButtonLabel = QPushButton(self.centralwidget)
        self.okButtonLabel.setObjectName(u"okButtonLabel")
        self.okButtonLabel.setGeometry(QRect(330, 180, 171, 331))
        self.okButtonLabel.setFont(font2)
        self.okButtonLabel.setStyleSheet(u"background-color: rgb(0, 33, 72);\n"
"color: rgb(255, 255, 255);")
        self.personInfoLabel = QLabel(self.centralwidget)
        self.personInfoLabel.setObjectName(u"personInfoLabel")
        self.personInfoLabel.setGeometry(QRect(510, 230, 271, 41))
        self.personInfoLabel.setFont(font)
        self.personInfoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.carInfoLabel = QLabel(self.centralwidget)
        self.carInfoLabel.setObjectName(u"carInfoLabel")
        self.carInfoLabel.setGeometry(QRect(510, 450, 271, 41))
        self.carInfoLabel.setFont(font)
        self.carInfoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cardReadLabel = QLabel(self.centralwidget)
        self.cardReadLabel.setObjectName(u"cardReadLabel")
        self.cardReadLabel.setGeometry(QRect(510, 180, 271, 41))
        self.cardReadLabel.setFont(font)
        self.cardReadLabel.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cardReadLabel.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.cardReadLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.resetPushButton.raise_()
        self.returnLabel.raise_()
        self.resetPushButton_2.raise_()
        self.rentLabel.raise_()
        self.readCarCardLineEdit.raise_()
        self.takeCarPushButton.raise_()
        self.keyPictureLabel.raise_()
        self.teacherPictureLabel.raise_()
        self.returnCarPushButton.raise_()
        self.readKeyLineEdit.raise_()
        self.soundPushButton.raise_()
        self.soundOffPushButton.raise_()
        self.okButtonLabel.raise_()
        self.personInfoLabel.raise_()
        self.carInfoLabel.raise_()
        self.cardReadLabel.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setFont(font2)
        self.statusbar.setToolTipDuration(3000)
        self.statusbar.setStyleSheet(u"\n"
"background-color: rgb(0, 33, 72);\n"
"color: rgb(255, 255, 255);")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.takeCarPushButton.clicked.connect(self.returnCarPushButton.hide)
        self.takeCarPushButton.clicked.connect(self.takeCarPushButton.hide)
        self.takeCarPushButton.clicked.connect(self.returnLabel.hide)
        self.returnCarPushButton.clicked.connect(self.rentLabel.hide)
        self.soundPushButton.clicked.connect(self.readCarCardLineEdit.setFocus)
        self.soundOffPushButton.clicked.connect(self.readCarCardLineEdit.setFocus)
        self.soundPushButton.clicked.connect(self.readKeyLineEdit.setFocus)
        self.soundOffPushButton.clicked.connect(self.readKeyLineEdit.setFocus)
        self.soundOffPushButton.clicked.connect(self.soundOffPushButton.hide)
        self.soundPushButton.clicked.connect(self.soundOffPushButton.show)
        self.readCarCardLineEdit.textEdited.connect(self.cardReadLabel.show)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionLopeta.setText(QCoreApplication.translate("MainWindow", u"Lopeta", None))
#if QT_CONFIG(shortcut)
        self.actionLopeta.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionKalle.setText(QCoreApplication.translate("MainWindow", u"Kalle", None))
        self.actionVille.setText(QCoreApplication.translate("MainWindow", u"Ville", None))
        self.actionJaana.setText(QCoreApplication.translate("MainWindow", u"Jaana", None))
        self.actionMikko.setText(QCoreApplication.translate("MainWindow", u"Mikko", None))
        self.actionTallenna_nimell.setText(QCoreApplication.translate("MainWindow", u"Tallenna nimell\u00e4...", None))
        self.readCarCardLineEdit.setText("")
        self.readCarCardLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Lue ajokortin viivakoodi", None))
#if QT_CONFIG(tooltip)
        self.takeCarPushButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Tallentaa henkil\u00f6n tiedot tietokantaa</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.takeCarPushButton.setText(QCoreApplication.translate("MainWindow", u"LAINAA", None))
        self.keyPictureLabel.setText("")
        self.teacherPictureLabel.setText("")
#if QT_CONFIG(tooltip)
        self.returnCarPushButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Tallentaa henkil\u00f6n tiedot tietokantaa</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.returnCarPushButton.setText(QCoreApplication.translate("MainWindow", u"Palauta", None))
        self.readKeyLineEdit.setText("")
        self.readKeyLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Lue avaimen viivakoodi", None))
        self.resetPushButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.resetPushButton_2.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.soundPushButton.setText("")
        self.soundOffPushButton.setText("")
        self.rentLabel.setText(QCoreApplication.translate("MainWindow", u"LAINAA", None))
        self.returnLabel.setText(QCoreApplication.translate("MainWindow", u"Palauta", None))
        self.okButtonLabel.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.personInfoLabel.setText("")
        self.carInfoLabel.setText("")
        self.cardReadLabel.setText(QCoreApplication.translate("MainWindow", u"Ajokortti Luettu", None))
    # retranslateUi

