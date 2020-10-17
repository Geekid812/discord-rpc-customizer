from PyQt5 import QtCore, QtGui, QtWidgets

version = '1.0.0'

class AboutDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(390, 110)
        Dialog.setFixedSize(390, 110)

        self.appNameLabel = QtWidgets.QLabel(Dialog)
        self.appNameLabel.setGeometry(QtCore.QRect(10, 10, 381, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.appNameLabel.setFont(font)
        self.appNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.appNameLabel.setObjectName("appNameLabel")

        self.appInfoLabel = QtWidgets.QLabel(Dialog)
        self.appInfoLabel.setGeometry(QtCore.QRect(0, 40, 391, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.appInfoLabel.setFont(font)
        self.appInfoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.appInfoLabel.setObjectName("appInfoLabel")

        self.repoButton = QtWidgets.QPushButton(Dialog)
        self.repoButton.setGeometry(QtCore.QRect(150, 70, 101, 23))
        self.repoButton.setObjectName("repoButton")

        self.retranslateUi(Dialog)
        self.bind_signals()
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About Discord RPC"))
        self.appNameLabel.setText(_translate("Dialog", "Discord Rich Presence Customizer"))
        self.appInfoLabel.setText(_translate("Dialog", "Made by Geekid812 - Version " + version))
        self.repoButton.setText(_translate("Dialog", "GitHub Repository"))

    def bind_signals(self):
        self.repoButton.clicked.connect(lambda: QtGui.QDesktopServices.openUrl(QtCore.QUrl("https://github.com/geekid812/discord-rpc-customizer")))
