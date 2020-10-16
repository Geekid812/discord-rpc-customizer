from PyQt5.QtWidgets import QMessageBox

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
    
    def update_presence(self):
        form_values = {}
        form_values['state'] = self.stateEdit.text()
        form_values['details'] = self.detailsEdit.text()
        form_values['large_image_key'] = self.largeImageKeyEdit.text()
        form_values['large_image_text'] = self.largeImageTextEdit.text()
        form_values['small_image_key'] = self.smallImageKeyEdit.text()
        form_values['small_image_text'] = self.smallImageTextEdit.text()
        form_values['party_size'] = self.partySizeEdit.value()
        form_values['party_max'] = self.partyMaxEdit.value()