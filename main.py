import sys
from PyQt5.QtWidgets import QApplication
from welcome_window import WelcomeWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    
    window = WelcomeWindow()
    window.show()
    
    sys.exit(app.exec_())