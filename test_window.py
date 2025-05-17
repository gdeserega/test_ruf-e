from PyQt5.QtWidgets import (QMainWindow, QLabel, QLineEdit, QPushButton, 
                            QVBoxLayout, QHBoxLayout, QWidget, QSpinBox, 
                            QMessageBox)
from PyQt5.QtCore import QTimer, Qt

class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Тест Руфье - проведение теста")
        self.setFixedSize(600, 500)
        
        self.pulse1 = None
        self.pulse2 = None
        self.pulse3 = None
        self.age = 0
        
        self.initUI()
        self.initTimers()
    
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        
        # Личные данные
        personal_layout = QVBoxLayout()
        personal_title = QLabel("Личные данные:")
        personal_title.setStyleSheet("font-weight: bold;")
        
        name_layout = QHBoxLayout()
        name_label = QLabel("Ф.И.О.:")
        self.name_input = QLineEdit()
        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name_input)
        
        age_layout = QHBoxLayout()
        age_label = QLabel("Полных лет:")
        self.age_input = QSpinBox()
        self.age_input.setRange(7, 120)
        age_layout.addWidget(age_label)
        age_layout.addWidget(self.age_input)
        
        personal_layout.addWidget(personal_title)
        personal_layout.addLayout(name_layout)
        personal_layout.addLayout(age_layout)
        
        # Тест 1
        test1_layout = QVBoxLayout()
        test1_title = QLabel("Тест 1: Измерение пульса в покое")
        test1_title.setStyleSheet("font-weight: bold;")
        
        test1_instruction = QLabel("Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку 'Начать первый тест', чтобы запустить таймер.")
        test1_instruction.setWordWrap(True)
        
        self.test1_button = QPushButton("Начать первый тест")
        self.test1_button.clicked.connect(self.start_test1)
        
        self.test1_timer_label = QLabel("00:00:15")
        self.test1_timer_label.setAlignment(Qt.AlignCenter)
        self.test1_timer_label.setStyleSheet("font-size: 24px;")
        self.test1_timer_label.hide()
        
        self.pulse1_input = QLineEdit()
        self.pulse1_input.setPlaceholderText("Пульс за первые 15 секунд")
        
        test1_layout.addWidget(test1_title)
        test1_layout.addWidget(test1_instruction)
        test1_layout.addWidget(self.test1_button)
        test1_layout.addWidget(self.test1_timer_label)
        test1_layout.addWidget(self.pulse1_input)
        
        # Тест 2
        test2_layout = QVBoxLayout()
        test2_title = QLabel("Тест 2: Приседания")
        test2_title.setStyleSheet("font-weight: bold;")
        
        test2_instruction = QLabel("Выполните 30 приседаний за 45 секунд. Нажмите кнопку 'Начать делать приседания'.")
        test2_instruction.setWordWrap(True)
        
        self.test2_button = QPushButton("Начать делать приседания")
        self.test2_button.clicked.connect(self.start_test2)
        
        self.test2_timer_label = QLabel("00:00:45")
        self.test2_timer_label.setAlignment(Qt.AlignCenter)
        self.test2_timer_label.setStyleSheet("font-size: 24px;")
        self.test2_timer_label.hide()
        
        test2_layout.addWidget(test2_title)
        test2_layout.addWidget(test2_instruction)
        test2_layout.addWidget(self.test2_button)
        test2_layout.addWidget(self.test2_timer_label)
        
        # Тест 3
        test3_layout = QVBoxLayout()
        test3_title = QLabel("Тест 3: Измерение пульса после нагрузки")
        test3_title.setStyleSheet("font-weight: bold;")
        
        test3_instruction = QLabel("Лягте на спину и замерьте пульс сначала за первые 15 секунд, затем за последние 15 секунд минуты.")
        test3_instruction.setWordWrap(True)
        
        self.test3_button = QPushButton("Начать финальный тест")
        self.test3_button.clicked.connect(self.start_test3)
        
        self.test3_timer_label = QLabel("00:01:00")
        self.test3_timer_label.setAlignment(Qt.AlignCenter)
        self.test3_timer_label.setStyleSheet("font-size: 24px;")
        self.test3_timer_label.hide()
        
        self.pulse2_input = QLineEdit()
        self.pulse2_input.setPlaceholderText("Пульс за первые 15 секунд после нагрузки")
        
        self.pulse3_input = QLineEdit()
        self.pulse3_input.setPlaceholderText("Пульс за последние 15 секунд")
        
        test3_layout.addWidget(test3_title)
        test3_layout.addWidget(test3_instruction)
        test3_layout.addWidget(self.test3_button)
        test3_layout.addWidget(self.test3_timer_label)
        test3_layout.addWidget(self.pulse2_input)
        test3_layout.addWidget(self.pulse3_input)
        
        # Кнопка отправки
        submit_button = QPushButton("Отправить результаты")
        submit_button.clicked.connect(self.submit_results)
        
        # Сборка основного layout
        layout.addLayout(personal_layout)
        layout.addLayout(test1_layout)
        layout.addLayout(test2_layout)
        layout.addLayout(test3_layout)
        layout.addWidget(submit_button)
        
        central_widget.setLayout(layout)
    
    def initTimers(self):
        # Таймер для первого теста
        self.test1_timer = QTimer()
        self.test1_timer.timeout.connect(self.update_test1_timer)
        self.test1_seconds = 15
        
        # Таймер для второго теста
        self.test2_timer = QTimer()
        self.test2_timer.timeout.connect(self.update_test2_timer)
        self.test2_seconds = 45
        
        # Таймер для третьего теста
        self.test3_timer = QTimer()
        self.test3_timer.timeout.connect(self.update_test3_timer)
        self.test3_seconds = 60
    
    def start_test1(self):
        self.test1_button.setEnabled(False)
        self.test1_timer_label.show()
        self.test1_timer.start(1000)
    
    def update_test1_timer(self):
        self.test1_seconds -= 1
        minutes = self.test1_seconds // 60
        seconds = self.test1_seconds % 60
        self.test1_timer_label.setText(f"00:{minutes:02d}:{seconds:02d}")
        
        if self.test1_seconds <= 0:
            self.test1_timer.stop()
            self.test1_timer_label.hide()
            self.test1_button.setEnabled(True)
            QMessageBox.information(self, "Тест завершен", "Введите ваш пульс за 15 секунд в поле ниже.")
    
    def start_test2(self):
        if not self.pulse1_input.text():
            QMessageBox.warning(self, "Ошибка", "Сначала выполните первый тест!")
            return
            
        self.test2_button.setEnabled(False)
        self.test2_timer_label.show()
        self.test2_timer.start(1000)
    
    def update_test2_timer(self):
        self.test2_seconds -= 1
        minutes = self.test2_seconds // 60
        seconds = self.test2_seconds % 60
        self.test2_timer_label.setText(f"00:{minutes:02d}:{seconds:02d}")
        
        if self.test2_seconds <= 0:
            self.test2_timer.stop()
            self.test2_timer_label.hide()
            self.test2_button.setEnabled(True)
            QMessageBox.information(self, "Тест завершен", "Теперь выполните финальный тест.")
    
    def start_test3(self):
        if not self.pulse1_input.text():
            QMessageBox.warning(self, "Ошибка", "Сначала выполните все предыдущие тесты!")
            return
            
        self.test3_button.setEnabled(False)
        self.test3_timer_label.show()
        self.test3_timer.start(1000)
    
    def update_test3_timer(self):
        self.test3_seconds -= 1
        minutes = self.test3_seconds // 60
        seconds = self.test3_seconds % 60
        
        # Подсветка периодов измерения
        if self.test3_seconds > 45 or self.test3_seconds <= 15:
            self.test3_timer_label.setStyleSheet("font-size: 24px; color: green;")
        else:
            self.test3_timer_label.setStyleSheet("font-size: 24px; color: black;")
            
        self.test3_timer_label.setText(f"00:{minutes:02d}:{seconds:02d}")
        
        if self.test3_seconds == 45:
            QMessageBox.information(self, "Измерение", "Измерьте пульс за первые 15 секунд!")
        elif self.test3_seconds == 15:
            QMessageBox.information(self, "Измерение", "Измерьте пульс за последние 15 секунд!")
        elif self.test3_seconds <= 0:
            self.test3_timer.stop()
            self.test3_timer_label.hide()
            self.test3_button.setEnabled(True)
            QMessageBox.information(self, "Тест завершен", "Введите результаты измерений.")
    
    def submit_results(self):
        # Проверка данных
        if not all([self.name_input.text(), self.age_input.value(), 
                   self.pulse1_input.text(), self.pulse2_input.text(), 
                   self.pulse3_input.text()]):
            QMessageBox.warning(self, "Ошибка", "Заполните все поля!")
            return
            
        try:
            pulse1 = int(self.pulse1_input.text())
            pulse2 = int(self.pulse2_input.text())
            pulse3 = int(self.pulse3_input.text())
            age = self.age_input.value()
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Введите корректные числа для пульса!")
            return
            
        # Расчет индекса Руфье
        ruffier_index = (4 * (pulse1 + pulse2 + pulse3) - 200) / 10
        
        # Определение результата
        if age >= 15:
            if ruffier_index < 0: result = "высокая"
            elif ruffier_index < 5: result = "выше среднего"
            elif ruffier_index < 10: result = "средняя"
            elif ruffier_index < 15: result = "ниже среднего"
            else: result = "низкая"
        else:
            if ruffier_index < 5: result = "высокая"
            elif ruffier_index < 10: result = "выше среднего"
            elif ruffier_index < 15: result = "средняя"
            elif ruffier_index < 20: result = "ниже среднего"
            else: result = "низкая"
        
        # Открытие окна результатов
        from results_window import ResultsWindow
        self.results_window = ResultsWindow(ruffier_index, result)
        self.results_window.show()
        self.close()