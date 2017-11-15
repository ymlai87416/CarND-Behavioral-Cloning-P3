import sys
import traceback
from app.app import Application
from PyQt4.QtCore import QDir, Qt, QUrl, QRegExp
from PyQt4.QtGui import (QWidget, QLabel, QLineEdit, QFileDialog, QMainWindow,
                             QTextEdit, QGridLayout, QApplication, QCheckBox, QGridLayout, QFormLayout,
                             QRadioButton, QTabWidget, QAction, QButtonGroup, QPushButton, QSlider, QStyle,
                             QVBoxLayout, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy, QMessageBox, QPixmap, QDialog)
from PyQt4.QtGui import QIntValidator, QDoubleValidator
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt4 import QtGui, QtCore


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
        sliderLayout = QHBoxLayout()
        self.slider_left = QSlider(Qt.Horizontal)
        self.slider_left.setMinimum(0)
        self.slider_left.setMaximum(0)
        self.slider_left.setValue(0)
        self.slider_left.setTickPosition(QSlider.TicksBelow)
        self.slider_left.setTickInterval(100)
        self.slider_left.valueChanged.connect(self.valueChangeLeft)
        self.label_sl_left = QLineEdit(self)
        self.label_sl_left.setReadOnly(True)
        self.label_sl_left.setMaximumWidth(30)
        sliderLayout.addWidget(self.slider_left)
        sliderLayout.addWidget(self.label_sl_left)
        formLayout.addRow(self.label_left, sliderLayout)

        self.label_right = QLabel("End position: ")
        sliderLayout = QHBoxLayout()
        self.slider_right = QSlider(Qt.Horizontal)
        self.slider_right.setMinimum(0)
        self.slider_right.setMaximum(0)
        self.slider_right.setValue(0)
        self.slider_right.setTickPosition(QSlider.TicksBelow)
        self.slider_right.setTickInterval(100)
        self.slider_right.valueChanged.connect(self.valueChangeRight)
        self.label_sl_right = QLineEdit(self)
        self.label_sl_right.setReadOnly(True)
        self.label_sl_right.setMaximumWidth(30)
        sliderLayout.addWidget(self.slider_right)
        sliderLayout.addWidget(self.label_sl_right)
        formLayout.addRow(self.label_right, sliderLayout)

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
            self.label_sl_left.setText(str(leftIdx))
            self.picture_left.setPixmap(QPixmap(self.lines_src[leftIdx][0]))
        except Exception:
            pass

    def valueChangeRight(self):
        rightIdx = self.slider_right.value()
        try:
            self.label_sl_right.setText(str(rightIdx))
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


class TrainDataStaticCanvas(FigureCanvas):

    def __init__(self, src, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.src = src
        self.axes = fig.add_subplot(111)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        lines = core.readTrainData(self.src)
        measurements = []
        correction = [0, 0.2, -0.2]
        for line in lines:
            measurement = float(line[3])
            for i in range(3):
                source_path = line[i]
                filename = source_path.split('\\')[-1]
                measurements.append(measurement + correction[i])

        self.axes.hist(measurements, 100, normed=1, facecolor='green', alpha=0.75)

class OtherTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def showDialog(self, src):
        d = QDialog()
        b1 = TrainDataStaticCanvas(src, d)
        b1.move(50, 50)
        d.setWindowTitle("Statistic dialog")
        d.setWindowModality(Qt.ApplicationModal)
        d.exec_()


    def initUI(self):
        mainLayout = QFormLayout()
        mainLayout.setHorizontalSpacing(500)
        self.label_src_fix = QLabel("Fix image link ")
        self.button_src_fix = QPushButton("...")
        self.button_src_fix.clicked.connect(self.buttonFixClick)
        mainLayout.addRow(self.label_src_fix, self.button_src_fix)

        self.label_src_stat = QLabel("Find train set steering statistic ")
        self.button_src_stat = QPushButton("...")
        self.button_src_stat.clicked.connect(self.buttonStatisticsClick)
        mainLayout.addRow(self.label_src_stat, self.button_src_stat)

        self.setLayout(mainLayout)

    def buttonFixClick(self):
        src = QFileDialog.getExistingDirectory()
        core.fixImageLink(src)

    def buttonStatisticsClick(self):
        src = QFileDialog.getExistingDirectory()
        self.showDialog(src)

class MainWindow(QMainWindow):
    output_directory = "./output"

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        wid = QWidget(self)
        self.setCentralWidget(wid)
        self.setWindowTitle("CarND Behavioral Cloning train set editor")

        self.folkTab = FolkTab()
        self.removeTab = RemoveTab()
        self.statisticTab = OtherTab()

        tabWidget = QTabWidget()
        tabWidget.addTab(self.folkTab, "Folk data")
        tabWidget.addTab(self.removeTab, "Remove data")
        tabWidget.addTab(self.statisticTab, "Utilities")

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
