import sys
import traceback
from app.app import Application
from PyQt4.QtCore import QDir, Qt, QUrl, QRegExp
from PyQt4.QtGui import (QWidget, QLabel, QLineEdit, QFileDialog, QMainWindow,
                             QTextEdit, QGridLayout, QApplication, QCheckBox, QGridLayout, QFormLayout,
                             QRadioButton, QTabWidget, QAction, QButtonGroup, QPushButton, QSlider, QStyle,
                             QVBoxLayout, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy, QMessageBox, QPixmap)
from PyQt4.QtGui import QIntValidator, QDoubleValidator


class FolkTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        mainLayout = QVBoxLayout()

        self.picture_left = QLabel(self)
        self.picture_right = QLabel(self)
        self.picture_left.setMinimumWidth(320)
        self.picture_left.setMinimumHeight(160)
        self.picture_right.setMinimumWidth(320)
        self.picture_right.setMinimumHeight(160)

        pictureLayout = QHBoxLayout()
        pictureLayout.addWidget(self.picture_left)
        pictureLayout.addWidget(self.picture_right)

        formLayout = QFormLayout()

        self.label_left = QLabel("Start position: ")
        self.slider_left = QSlider(Qt.Horizontal)
        self.slider_left.setMinimum(0)
        self.slider_left.setMaximum(0)
        self.slider_left.setValue(0)
        self.slider_left.setTickPosition(QSlider.TicksBelow)
        self.slider_left.setTickInterval(1000)
        self.slider_left.valueChanged.connect(self.valueChangeLeft)
        formLayout.addRow(self.label_left, self.slider_left)

        self.label_right = QLabel("End position: ")
        self.slider_right = QSlider(Qt.Horizontal)
        self.slider_right.setMinimum(0)
        self.slider_right.setMaximum(0)
        self.slider_right.setValue(0)
        self.slider_right.setTickPosition(QSlider.TicksBelow)
        self.slider_right.setTickInterval(1000)
        self.slider_right.valueChanged.connect(self.valueChangeRight)
        formLayout.addRow(self.label_right, self.slider_right)

        self.label_src = QLabel("Source dir: ")
        srcLayout = QHBoxLayout()
        self.button_src = QPushButton("...")
        self.edit_src = QLineEdit(self)
        self.edit_src.setReadOnly(True)
        srcLayout.addWidget(self.edit_src)
        srcLayout.addWidget(self.button_src)
        self.button_src.clicked.connect(self.selectSrcFile)

        formLayout.addRow(self.label_src, srcLayout)

        self.label_dst = QLabel("Destination dir: ")
        dstLayout = QHBoxLayout()
        self.button_dst = QPushButton("...")
        self.edit_dst = QLineEdit(self)
        self.edit_dst.setReadOnly(True)
        dstLayout.addWidget(self.edit_dst)
        dstLayout.addWidget(self.button_dst)
        self.button_dst.clicked.connect(self.selectDstFile)

        formLayout.addRow(self.label_dst, dstLayout)

        spacer = QSpacerItem(400, 10, QSizePolicy.Maximum, QSizePolicy.Expanding)
        self.button_copy = QPushButton()
        self.button_copy.setText("Copy")
        self.button_copy.clicked.connect(self.buttonCopyClick)
        btnLayout = QHBoxLayout()
        btnLayout.addItem(spacer)
        btnLayout.addWidget(self.button_copy)

        mainLayout.addLayout(pictureLayout)
        mainLayout.addLayout(formLayout)
        mainLayout.addLayout(btnLayout)

        self.setLayout(mainLayout)

    def selectDstFile(self):
        dst = QFileDialog.getExistingDirectory()
        self.edit_dst.setText(dst)
        lines_dst = app.readTrainData(dst)

    def selectSrcFile(self):
        src = QFileDialog.getExistingDirectory()
        self.edit_src.setText(src)
        self.lines_src = core.readTrainData(src)
        self.slider_left.setMaximum(len(self.lines_src)-1)
        self.slider_right.setMaximum(len(self.lines_src) - 1)

    def valueChangeLeft(self):
        leftIdx = self.slider_left.value()
        try:
            self.picture_left.setPixmap(QPixmap(self.lines_src[leftIdx][0]))
        except Exception:
            pass

    def valueChangeRight(self):
        rightIdx = self.slider_right.value()
        try:
            self.picture_right.setPixmap(QPixmap(self.lines_src[rightIdx][0]))
        except Exception:
            pass

    def buttonCopyClick(self):
        start = min(self.slider_left.value(), self.slider_right.value())
        end = max(self.slider_left.value(), self.slider_right.value())
        dst = self.edit_dst.text()
        src = self.edit_src.text()
        core.cloneFrom(src, dst, start, end)

class RemoveTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        mainLayout = QVBoxLayout()

        self.picture_left = QLabel(self)
        self.picture_right = QLabel(self)
        self.picture_left.setMinimumWidth(320)
        self.picture_left.setMinimumHeight(160)
        self.picture_right.setMinimumWidth(320)
        self.picture_right.setMinimumHeight(160)

        pictureLayout = QHBoxLayout()
        pictureLayout.addWidget(self.picture_left)
        pictureLayout.addWidget(self.picture_right)

        formLayout = QFormLayout()

        self.label_left = QLabel("Start position: ")
        self.slider_left = QSlider(Qt.Horizontal)
        self.slider_left.setMinimum(0)
        self.slider_left.setMaximum(0)
        self.slider_left.setValue(0)
        self.slider_left.setTickPosition(QSlider.TicksBelow)
        self.slider_left.setTickInterval(100)
        self.slider_left.valueChanged.connect(self.valueChangeLeft)
        formLayout.addRow(self.label_left, self.slider_left)

        self.label_right = QLabel("End position: ")
        self.slider_right = QSlider(Qt.Horizontal)
        self.slider_right.setMinimum(0)
        self.slider_right.setMaximum(0)
        self.slider_right.setValue(0)
        self.slider_right.setTickPosition(QSlider.TicksBelow)
        self.slider_right.setTickInterval(100)
        self.slider_right.valueChanged.connect(self.valueChangeRight)
        formLayout.addRow(self.label_right, self.slider_right)

        self.label_src = QLabel("Source dir: ")
        srcLayout = QHBoxLayout()
        self.button_src = QPushButton("...")
        self.edit_src = QLineEdit(self)
        self.edit_src.setReadOnly(True)
        srcLayout.addWidget(self.edit_src)
        srcLayout.addWidget(self.button_src)
        self.button_src.clicked.connect(self.selectSrcFile)

        formLayout.addRow(self.label_src, srcLayout)

        spacer = QSpacerItem(400, 10, QSizePolicy.Maximum, QSizePolicy.Expanding)
        self.button_copy = QPushButton()
        self.button_copy.setText("Remove")
        self.button_copy.clicked.connect(self.buttonRemoveClick)
        btnLayout = QHBoxLayout()
        btnLayout.addItem(spacer)
        btnLayout.addWidget(self.button_copy)

        mainLayout.addLayout(pictureLayout)
        mainLayout.addLayout(formLayout)
        mainLayout.addLayout(btnLayout)

        self.setLayout(mainLayout)

    def selectSrcFile(self):
        src = QFileDialog.getExistingDirectory()
        self.edit_src.setText(src)
        self.lines_src = core.readTrainData(src)
        self.slider_left.setMaximum(len(self.lines_src) - 1)
        self.slider_right.setMaximum(len(self.lines_src) - 1)
        self.slider_left.setValue(0)
        self.slider_right.setValue(0)

    def valueChangeLeft(self):
        leftIdx = self.slider_left.value()
        try:
            self.picture_left.setPixmap(QPixmap(self.lines_src[leftIdx][0]))
        except Exception:
            pass

    def valueChangeRight(self):
        rightIdx = self.slider_right.value()
        try:
            self.picture_right.setPixmap(QPixmap(self.lines_src[rightIdx][0]))
        except Exception:
            pass

    def buttonRemoveClick(self):
        start = min(self.slider_left.value(), self.slider_right.value())
        end = max(self.slider_left.value(), self.slider_right.value())
        core.removeFrom(self.edit_src.text(), start, end)

        self.lines_src = core.readTrainData(self.edit_src.text())
        self.slider_left.setMaximum(len(self.lines_src) - 1)
        self.slider_right.setMaximum(len(self.lines_src) - 1)
        self.slider_left.setValue(0)
        self.slider_right.setValue(0)

class StatisticTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        mainLayout = QVBoxLayout()

        self.label_src = QLabel("Data set: ")
        srcLayout = QHBoxLayout()
        self.button_src = QPushButton("...")
        self.edit_src = QLineEdit(self)
        srcLayout.addWidget(self.label_src)
        srcLayout.addWidget(self.edit_src)
        srcLayout.addWidget(self.button_src)
        self.button_src.clicked.connect(self.selectSrcFile)

        self.picture_hist = QLabel(self)
        self.picture_hist.setMinimumWidth(300)
        self.picture_hist.setMinimumHeight(300)

        mainLayout.addLayout(srcLayout)
        mainLayout.addWidget(self.picture_hist)

        self.setLayout(mainLayout)

    def selectSrcFile(self):
        self.edit_dst.setText(QFileDialog.getOpenFileName())

class MainWindow(QMainWindow):
    output_directory = "./output"

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        wid = QWidget(self)
        self.setCentralWidget(wid)

        self.folkTab = FolkTab()
        self.removeTab = RemoveTab()
        self.statisticTab = StatisticTab()

        tabWidget = QTabWidget()
        tabWidget.addTab(self.folkTab, "Folk data")
        tabWidget.addTab(self.removeTab, "Remove data")
        #tabWidget.addTab(self.statisticTab, "Data statistic")

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(tabWidget)
        wid.setLayout(mainLayout)

        self.show()

if __name__ == '__main__':

    if False:
        import sys

        def my_except_hook(exctype, value, traceback_):
            file = open("application.log", "a")
            file.write("\n".join(traceback.format_exception(exctype, value, traceback_)))
            file.close()
            if exctype == KeyboardInterrupt:
                print('shit')
            else:
                sys.__excepthook__(exctype, value, traceback)
            sys.exit(-1)

        sys.excepthook = my_except_hook

    app = QApplication(sys.argv)
    core = Application()
    ex = MainWindow()
    sys.exit(app.exec_())
