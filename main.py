from PyQt5 import QtCore, QtGui, QtWidgets
from signals import Signals

class Ui_MainWindow(Signals):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(730, 600)
        MainWindow.setFixedSize(730, 600)
        MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))
        MainWindow.setWindowTitle("Discord Rich Presence Customizer")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.updateButton = QtWidgets.QPushButton(self.centralwidget)
        self.updateButton.setGeometry(QtCore.QRect(310, 540, 101, 23))
        self.updateButton.setObjectName("updateButton")

        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(10, 10, 711, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 711, 471))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 691, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)

        self.endTimeEdit = QtWidgets.QDateTimeEdit(self.gridLayoutWidget)
        self.endTimeEdit.setEnabled(False)
        self.endTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(1, 0, 0)))
        self.endTimeEdit.setCalendarPopup(True)
        self.endTimeEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.endTimeEdit.setObjectName("endTimeEdit")
        self.gridLayout.addWidget(self.endTimeEdit, 4, 2, 1, 1)

        spacerItem1 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 12, 1, 1, 1)

        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 9, 1, 1, 1)

        self.startTimeCheck = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.startTimeCheck.setObjectName("startTimeCheck")
        self.gridLayout.addWidget(self.startTimeCheck, 3, 0, 1, 1)

        self.partyMaxLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.partyMaxLabel.setObjectName("partyMaxLabel")
        self.gridLayout.addWidget(self.partyMaxLabel, 13, 2, 1, 1)

        self.largeImageKeyEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.largeImageKeyEdit.setObjectName("largeImageKeyEdit")
        self.gridLayout.addWidget(self.largeImageKeyEdit, 8, 0, 1, 1)

        self.smallImageTextEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.smallImageTextEdit.setObjectName("smallImageTextEdit")
        self.gridLayout.addWidget(self.smallImageTextEdit, 11, 2, 1, 1)

        self.startTimeEdit = QtWidgets.QDateTimeEdit(self.gridLayoutWidget)
        self.startTimeEdit.setEnabled(False)
        self.startTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.startTimeEdit.setCalendarPopup(True)
        self.startTimeEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.startTimeEdit.setObjectName("startTimeEdit")
        self.gridLayout.addWidget(self.startTimeEdit, 4, 0, 1, 1)

        self.largeImageTextLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.largeImageTextLabel.setObjectName("largeImageTextLabel")
        self.gridLayout.addWidget(self.largeImageTextLabel, 7, 2, 1, 1)

        self.largeImageKeyLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.largeImageKeyLabel.setObjectName("largeImageKeyLabel")
        self.gridLayout.addWidget(self.largeImageKeyLabel, 7, 0, 1, 1)

        self.stateLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.stateLabel.setObjectName("stateLabel")
        self.gridLayout.addWidget(self.stateLabel, 0, 0, 1, 1)

        self.smallImageKeyEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.smallImageKeyEdit.setObjectName("smallImageKeyEdit")
        self.gridLayout.addWidget(self.smallImageKeyEdit, 11, 0, 1, 1)

        self.partyMaxEdit = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.partyMaxEdit.setObjectName("partyMaxEdit")
        self.gridLayout.addWidget(self.partyMaxEdit, 14, 2, 1, 1)

        self.stateEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.stateEdit.setObjectName("stateEdit")
        self.gridLayout.addWidget(self.stateEdit, 1, 0, 1, 1)

        self.partySizeEdit = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.partySizeEdit.setObjectName("partySizeEdit")
        self.gridLayout.addWidget(self.partySizeEdit, 14, 0, 1, 1)

        self.largeImageTextEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.largeImageTextEdit.setObjectName("largeImageTextEdit")
        self.gridLayout.addWidget(self.largeImageTextEdit, 8, 2, 1, 1)

        self.detailsLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.detailsLabel.setObjectName("detailsLabel")
        self.gridLayout.addWidget(self.detailsLabel, 0, 2, 1, 1)

        self.detailsEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.detailsEdit.setObjectName("detailsEdit")
        self.gridLayout.addWidget(self.detailsEdit, 1, 2, 1, 1)

        self.smallImageKeyLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.smallImageKeyLabel.setObjectName("smallImageKeyLabel")
        self.gridLayout.addWidget(self.smallImageKeyLabel, 10, 0, 1, 1)

        self.smallImageTextLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.smallImageTextLabel.setObjectName("smallImageTextLabel")
        self.gridLayout.addWidget(self.smallImageTextLabel, 10, 2, 1, 1)

        self.endTimeCheck = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.endTimeCheck.setObjectName("endTimeCheck")
        self.gridLayout.addWidget(self.endTimeCheck, 3, 2, 1, 1)

        self.partySizeLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.partySizeLabel.setObjectName("partySizeLabel")
        self.gridLayout.addWidget(self.partySizeLabel, 13, 0, 1, 1)

        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 2, 1, 1, 1)

        self.autoStartTimeCheck = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.autoStartTimeCheck.setEnabled(False)
        self.autoStartTimeCheck.setObjectName("autoStartTimeCheck")
        self.gridLayout.addWidget(self.autoStartTimeCheck, 5, 0, 1, 1)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 520, 160, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.appIdLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.appIdLabel.setObjectName("appIdLabel")
        self.verticalLayout.addWidget(self.appIdLabel)
        
        self.appIdEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.appIdEdit.setObjectName("appIdEdit")
        self.verticalLayout.addWidget(self.appIdEdit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.bind_signals()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.updateButton.setText(_translate("MainWindow", "Update Presence"))
        self.titleLabel.setText(_translate("MainWindow", "Text"))
        self.startTimeCheck.setText(_translate("MainWindow", "Start Time"))
        self.partyMaxLabel.setText(_translate("MainWindow", "Party Max"))
        self.largeImageTextLabel.setText(_translate("MainWindow", "Large Image Text"))
        self.largeImageKeyLabel.setText(_translate("MainWindow", "Large Image Key"))
        self.stateLabel.setText(_translate("MainWindow", "State"))
        self.detailsLabel.setText(_translate("MainWindow", "Details"))
        self.smallImageKeyLabel.setText(_translate("MainWindow", "Small Image Key"))
        self.smallImageTextLabel.setText(_translate("MainWindow", "Small Image Text"))
        self.endTimeCheck.setText(_translate("MainWindow", "End Time"))
        self.partySizeLabel.setText(_translate("MainWindow", "Party Size"))
        self.autoStartTimeCheck.setText(_translate("MainWindow", "Auto Start Time"))
        self.appIdLabel.setText(_translate("MainWindow", "Application ID"))

    def bind_signals(self):
        self.startTimeCheck.clicked.connect(self.toggle_start_time)
        self.endTimeCheck.clicked.connect(self.toggle_end_time)
        self.autoStartTimeCheck.clicked.connect(self.toggle_auto_start_time)
        self.updateButton.clicked.connect(self.update_clicked)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
