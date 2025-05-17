from PyQt5.QtWidgets import (QMainWindow, QLabel, QVBoxLayout, 
                            QWidget, QPushButton)
from PyQt5.QtCore import Qt

class ResultsWindow(QMainWindow):
    def __init__(self, ruffier_index, result):
        super().__init__()
        self.setWindowTitle("Результаты теста Руфье")
        self.setFixedSize(400, 300)
        self.ruffier_index = ruffier_index
        self.result = result
        self.initUI()
    
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        
        title = QLabel("Результаты")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)
        
        index_label = QLabel(f"Индекс Руфье: {self.ruffier_index:.1f}")
        index_label.setStyleSheet("font-size: 16px;")
        index_label.setAlignment(Qt.AlignCenter)
        
        result_label = QLabel(f"Работоспособность сердца: {self.result}")
        result_label.setStyleSheet("font-size: 16px;")
        result_label.setAlignment(Qt.AlignCenter)
        
        restart_button = QPushButton("Пройти тест снова")
        restart_button.setStyleSheet("padding: 8px;")
        restart_button.clicked.connect(self.restart_test)
        
        layout.addWidget(title)
        layout.addStretch()
        layout.addWidget(index_label)
        layout.addWidget(result_label)
        layout.addStretch()
        layout.addWidget(restart_button)
        
        central_widget.setLayout(layout)
    
    def restart_test(self):
        from welcome_window import WelcomeWindow
        self.welcome_window = WelcomeWindow()
        self.welcome_window.show()
        self.close()