from PyQt5.QtWidgets import (QMainWindow, QLabel, QPushButton, 
                            QVBoxLayout, QWidget)
from test_window import TestWindow

class WelcomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Тест Руфье")
        self.setFixedSize(600, 400)
        self.initUI()
    
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        
        title = QLabel("Добро пожаловать в программу по определению состояния здоровья!")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        title.setWordWrap(True)
        
        description = QLabel("""Дачное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.  
Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.  
У испытуемого, находящегося в положении лежа на спине в течение 5 мин, определяют частоту пульса за 15 секунд;  
затем в течение 45 секунд испытуемый выполняет 30 приседаний.  
После окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд,  
а потом — за последние 15 секунд первой минуты периода восстановления.""")
        description.setWordWrap(True)
        
        warning = QLabel("""Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в  
ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.""")
        warning.setWordWrap(True)
        warning.setStyleSheet("color: red;")
        
        start_button = QPushButton("Начать тест")
        start_button.setStyleSheet("font-size: 14px; padding: 10px;")
        start_button.clicked.connect(self.open_test_window)
        
        layout.addWidget(title)
        layout.addWidget(description)
        layout.addWidget(warning)
        layout.addStretch()
        layout.addWidget(start_button)
        
        central_widget.setLayout(layout)
    
    def open_test_window(self):
        self.test_window = TestWindow()
        self.test_window.show()
        self.close()