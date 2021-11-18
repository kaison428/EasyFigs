from PyQt5.QtCore import *    # core Qt functionality
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *       # extends QtCore with GUI functionality
from PyQt5 import uic

import math as m

from convert_pdf_to_image import convert_pdf_to_image
from detect import *
import webbrowser
import subprocess

import sys  # We need sys so that we can pass argv to QApplication
import os
from os import listdir
from os.path import isfile, join


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs,)

        # Load the UI
        fileh = QFile('resources/UI/main_window.ui')
        fileh.open(QFile.ReadOnly)
        uic.loadUi(fileh, self)
        fileh.close()

        self.pdfPath = ''
        self.imageFolderPath = ''
        self.pdfImage = QImage()
        self.imageNames = []

        self.openPDF_button.clicked.connect(self.openPDFFile)
        self.extract_button.clicked.connect(self.extractFigures)
        self.openFigs_button.clicked.connect(self.openFigs)

    def openPDFFile(self, s):
        self.status_label.setText('')

        fileInfo = QFileDialog.getOpenFileName(self, "Open File", ".pdf", "PDF files (*.pdf)")
        self.pdfPath = fileInfo[0]

        if self.pdfPath:    # No action if nothing is selected
            self.imageFolderPath = convert_pdf_to_image(self.pdfPath)

            self.imageNames = [f for f in listdir(self.imageFolderPath) if isfile(join(self.imageFolderPath, f))]

            firstImagePath = os.path.join(self.imageFolderPath, self.imageNames[0])
            print(firstImagePath)

            with open(firstImagePath, 'rb') as f:
                content = f.read()

            self.pdfImage = QImage()

            self.pdfImage.loadFromData(content)
            self.pdfImage = self.pdfImage.scaled(400, 400, Qt.KeepAspectRatio)

            self.pdfPreview_label.setPixmap(QPixmap.fromImage(self.pdfImage))

        
    def extractFigures(self,s):
        self.status_label.setText('Running...')

        runnable = Runnable(self, self.imageFolderPath)
        runnable.signals.updateProgress.connect(self.update)
        runnable.signals.finish.connect(self.setFigurePreview)

        QThreadPool.globalInstance().start(runnable)

    def setFigurePreview(self):
        self.status_label.setText('Completed!')

        newEXP = [f for f in listdir('runs/detect')]
        path = 'runs/detect/' + newEXP[-1] + '/crops/figures'

        try:
            figureNames = [f for f in listdir(path) if isfile(join(path, f))]

            firstFigurePath = os.path.join(path, figureNames[0])
            print(firstFigurePath)

            with open(firstFigurePath, 'rb') as f:
                content = f.read()

            figImage = QImage()
            figImage.loadFromData(content)
            figImage = figImage.scaled(300, 300, Qt.KeepAspectRatio)

            self.figurePreview_label.setPixmap(QPixmap.fromImage(figImage))

        except:
            print('no figures found')

    def update(self, current, max):
        self.extract_progressbar.setMaximum(max)
        self.extract_progressbar.setValue(current + 1)

        print(max)
        print(current + 1)

    def openFigs(self,s):

        newEXP = [f for f in listdir('runs/detect')]

        try:
            path = 'runs/detect/' + newEXP[-1] + '/crops/figures'
            path = os.path.realpath(path)
            os.startfile(path)
        except:
            print('no figures found')
