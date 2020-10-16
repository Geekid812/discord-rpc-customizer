from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDateTime
from re import match
from time import time

from presence import update_presence

digits_only = r'^[0-9]*$'

class Signals(object):

    def clicked(self):
        msg = QMessageBox(QMessageBox.Information, "That's the title", "This is some text", QMessageBox.Ok)

        # msg.setText("This is a message box")
        # msg.setInformativeText("This is additional information")
        # msg.setWindowTitle("MessageBox demo")
        # msg.setDetailedText("The details are as follows:")
        # msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()
    
    def toggle_start_time(self):
        self.startTimeEdit.setEnabled(self.startTimeCheck.isChecked() and not self.autoStartTimeCheck.isChecked())
        self.autoStartTimeCheck.setEnabled(self.startTimeCheck.isChecked())

    def toggle_end_time(self):
        self.endTimeEdit.setEnabled(self.endTimeCheck.isChecked())

    def toggle_auto_start_time(self):
        self.startTimeEdit.setEnabled(not self.autoStartTimeCheck.isChecked())
    
    def update_clicked(self):
        form_values = {}
        form_values['state'] = str(self.stateEdit.text()) or None
        form_values['details'] = str(self.detailsEdit.text()) or None
        form_values['large_image_key'] = str(self.largeImageKeyEdit.text()) or None
        form_values['large_image_text'] = str(self.largeImageTextEdit.text()) or None
        form_values['small_image_key'] = str(self.smallImageKeyEdit.text()) or None
        form_values['small_image_text'] = str(self.smallImageTextEdit.text()) or None
        form_values['party_size'] = self.partySizeEdit.value() or None
        form_values['party_max'] = self.partyMaxEdit.value() or None

        use_start_time = self.startTimeCheck.isChecked()
        if use_start_time:
            auto_start = self.autoStartTimeCheck.isChecked()

            if auto_start:
                start_time = int(time())
            else:
                start_time = self.startTimeEdit.dateTime().toSecsSinceEpoch()
            
            form_values['start'] = start_time

        else:
            form_values['start'] = None
        
        use_end_time = self.endTimeCheck.isChecked()
        if use_end_time:
            end_time = self.endTimeEdit.dateTime().toSecsSinceEpoch()
            form_values['end'] = end_time
        
        else:
            form_values['end'] = None

        application_id = self.appIdEdit.text()
        if application_id == "" or not match(digits_only, application_id):
            return self.invalid_input("The application ID is invalid.")
        
        update_presence(application_id, form_values)
        self.info_box("Success", "Your rich presence has been updated!\nMake sure to keep the application running in the background.")
    
    def invalid_input(self, message):
        msg = QMessageBox(QMessageBox.Warning, "Invalid Input", message, QMessageBox.Ok)
        msg.setWindowIcon(QIcon('icon.png'))
        msg.exec_()
        return False
    
    def info_box(self, title, message):
        msg = QMessageBox(QMessageBox.Information, title, message, QMessageBox.Ok)
        msg.setWindowIcon(QIcon('icon.png'))
        msg.exec_()

    def set_datetimes(self):
        start_dt = QDateTime()
        start_dt.setSecsSinceEpoch(int(time()))
        end_dt = start_dt.addSecs(60 * 60)

        self.startTimeEdit.setDateTime(start_dt)
        self.endTimeEdit.setDateTime(end_dt)
