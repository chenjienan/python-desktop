'''
# all Qt class begin with the letter Q
'''

# QWidget class is the base class of all user interface elements
# from PyQt5.QtWidgets import *
import PyQt5.QtWidgets as pyqt


class DeskTop(pyqt.QDialog):
    '''
    demo basic pyqt widget components
    '''
    def __init__(self):
        pyqt.QDialog.__init__(self)

        layout = pyqt.QVBoxLayout()

        self.label = pyqt.QLabel("Hello, world!")
        line_edit = pyqt.QLineEdit()
        button = pyqt.QPushButton("Close")

        layout.addWidget(self.label)
        layout.addWidget(line_edit)
        layout.addWidget(button)

        self.setLayout(layout)

        # click event
        # connect: event attach to the event
        button.clicked.connect(self.close)
        line_edit.textChanged.connect(self.change_text_label)

    def change_text_label(self, text):
        '''
        change text
        '''
        self.label.setText(text)

APP = pyqt.QApplication([])
DIALOG = DeskTop()
DIALOG.show()
APP.exec_()
