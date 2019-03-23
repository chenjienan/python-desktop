'''
Downloader application
'''
import urllib.request
import PyQt5.QtWidgets as pyqt
import PyQt5.QtCore as qc


class Downloader(pyqt.QDialog):
    '''
    init PyQt object
    '''
    def __init__(self):
        pyqt.QDialog.__init__(self)

        # create a virtical layout grid
        layout = pyqt.QVBoxLayout()

        # URL input
        self.url = pyqt.QLineEdit()
        self.url.setPlaceholderText("URL")

        # path input
        self.save_location = pyqt.QLineEdit()
        self.save_location.setPlaceholderText("File save location")

        # progress bar
        self.progress = pyqt.QProgressBar()
        self.progress.setValue(0)
        self.progress.setAlignment(qc.Qt.AlignHCenter)

        # download button
        download_button = pyqt.QPushButton("Download")

        # borwse files
        browse_button = pyqt.QPushButton("Browse")

        # add elements to the layout gird
        layout.addWidget(self.url)
        layout.addWidget(self.save_location)
        layout.addWidget(browse_button)
        layout.addWidget(self.progress)
        layout.addWidget(download_button)

        self.setLayout(layout)
        self.setWindowTitle("Downloader")
        self.setFocus()

        # add event handling
        download_button.clicked.connect(self.download)
        browse_button.clicked.connect(self.browse_file)


    def browse_file(self):
        '''
        browse file logic
        '''
        location = pyqt.QFileDialog.getSaveFileName(
            self, caption="Save File As",
            directory=".",
            filter="All Files (*.*)")

        self.save_location.setText(location[0])


    def download(self):
        '''
        event handler for download button click
        '''
        url = self.url.text()
        save_location = self.save_location.text()

        try:
            urllib.request.urlretrieve(url, save_location, self.report)
        except Exception:
            pyqt.QMessageBox.warning(self, "Warning", "Download failed")
            return self.reset()

        pyqt.QMessageBox.information(self, "Information", "Download is competed!")
        self.reset()


    def report(self, block_num, block_size, total_size):
        '''
        download logic
        '''
        read = block_num * block_size
        if total_size > 0:
            percent = read * 100 / total_size
            self.progress.setValue(int(percent))

    def reset(self):
        '''
        reset the UI
        '''
        self.progress.setValue(0)
        self.url.setText("")
        self.save_location.setText("")

# Whenever the Python interpreter reads a source file
# 1. it sets a few special variables like __name__
# 2. it executes all of the code found in the file

# in short, use this block to prevent code from being run when the module is imported
if __name__ == '__main__':          # I have the highest priority to be executed first
    print("application started.")
    APP = pyqt.QApplication([])
    DIALOG = Downloader()
    DIALOG.show()
    APP.exec_()
    print("application ended.")
