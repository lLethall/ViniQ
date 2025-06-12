import sys
from PySide6.QtWidgets import QApplication
import qdarktheme
from mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    qdarktheme.load_stylesheet (theme="dark")
    qdarktheme.load_palette(theme="dark") 
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())