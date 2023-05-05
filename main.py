import math
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, \
    QMessageBox, QTabWidget


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Комбинаторный калькулятор')
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.resize(800, 300)

        # Создание объекта QTabWidget и вкладок
        self.tabs = QTabWidget()
        self.tab_permutations = QWidget()
        self.tab_permutations_repetition = QWidget()
        self.tab_arrangements = QWidget()
        self.tab_combination = QWidget()

        # Добавление вкладок в объект QTabWidget
        self.tabs.addTab(self.tab_permutations, 'Перестановки без повторений (P)')
        self.tabs.addTab(self.tab_permutations_repetition, 'Перестановки c повторениями (P)')
        self.tabs.addTab(self.tab_arrangements, 'Размещения (A)')
        self.tabs.addTab(self.tab_combination, 'Сочетания (C)')

        # Создание элементов интерфейса для вкладки "Перестановки без повторений (P)"
        self.permutation_label = QLabel('Количество элементов:')
        self.permutation_input = QLineEdit()

        self.permutation_btn = QPushButton('Вычислить')

        self.permutation_result_label = QLabel('Результат:')

        # Создание элементов интерфейса для вкладки "Перестановки с повторениями (P)"
        self.permutation_repetition_n_label = QLabel('Количество элементов (n):')
        self.permutation_repetition_n_input = QLineEdit()
        self.permutation_repetition_ns_label = QLabel('Количество элементов (через пробел):')
        self.permutation_repetition_ns_input = QLineEdit()

        self.permutation_repetition_btn = QPushButton('Вычислить')

        self.permutation_repetition_result_label = QLabel('Результат:')

        # Создание элементов интерфейса для вкладки "Размещения (A)"
        self.arrangements_n_label = QLabel('Количество элементов (n):')
        self.arrangements_n_input = QLineEdit()
        self.arrangements_m_label = QLabel('Количество мест (m):')
        self.arrangements_m_input = QLineEdit()

        self.arrangements_btn = QPushButton('Без повторений')
        self.arrangements_repetition_btn = QPushButton('С повторениями')

        self.arrangements_result_label = QLabel('Результат:')

        # Создание элементов интерфейса для вкладки "Сочетания (С)"
        self.combination_n_label = QLabel('Количество элементов (n):')
        self.combination_n_input = QLineEdit()
        self.combination_m_label = QLabel('Количество мест (m):')
        self.combination_m_input = QLineEdit()

        self.combination_btn = QPushButton('Без повторений')
        self.combination_repetition_btn = QPushButton('С повторениями')

        self.combination_result_label = QLabel('Результат:')

        # Создание слоёв для элементов интерфейса внутри каждой вкладки
        permutation_layout = QVBoxLayout()
        permutation_layout.addWidget(self.permutation_label)
        permutation_layout.addWidget(self.permutation_input)
        permutation_layout.addWidget(self.permutation_btn)
        permutation_layout.addWidget(self.permutation_result_label)
        self.tab_permutations.setLayout(permutation_layout)

        permutation_repetition_layout = QVBoxLayout()
        permutation_repetition_layout.addWidget(self.permutation_repetition_n_label)
        permutation_repetition_layout.addWidget(self.permutation_repetition_n_input)
        permutation_repetition_layout.addWidget(self.permutation_repetition_ns_label)
        permutation_repetition_layout.addWidget(self.permutation_repetition_ns_input)
        permutation_repetition_layout.addWidget(self.permutation_repetition_btn)
        permutation_repetition_layout.addWidget(self.permutation_repetition_result_label)
        self.tab_permutations_repetition.setLayout(permutation_repetition_layout)

        arrangements_layout = QVBoxLayout()
        arrangements_layout.addWidget(self.arrangements_n_label)
        arrangements_layout.addWidget(self.arrangements_n_input)
        arrangements_layout.addWidget(self.arrangements_m_label)
        arrangements_layout.addWidget(self.arrangements_m_input)
        arrangements_layout.addWidget(self.arrangements_btn)
        arrangements_layout.addWidget(self.arrangements_repetition_btn)
        arrangements_layout.addWidget(self.arrangements_result_label)
        self.tab_arrangements.setLayout(arrangements_layout)

        combination_layout = QVBoxLayout()
        combination_layout.addWidget(self.combination_n_label)
        combination_layout.addWidget(self.combination_n_input)
        combination_layout.addWidget(self.combination_m_label)
        combination_layout.addWidget(self.combination_m_input)
        combination_layout.addWidget(self.combination_btn)
        combination_layout.addWidget(self.combination_repetition_btn)
        combination_layout.addWidget(self.combination_result_label)
        self.tab_combination.setLayout(combination_layout)

        # Создание основного слоя и добавление объекта QTabWidget в него
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)

        # Подключение функций-обработчиков для копок
        self.permutation_btn.clicked.connect(self.calculate_permutations)
        self.permutation_repetition_btn.clicked.connect(self.calculate_permutations_repetition)
        self.arrangements_btn.clicked.connect(self.calculate_arrangements)
        self.arrangements_repetition_btn.clicked.connect(self.calculate_arrangements_repetition)
        self.combination_btn.clicked.connect(self.calculate_combination)
        self.combination_repetition_btn.clicked.connect(self.calculate_combination_repetition)

    # Определение функций-обработчиков для кнопок
    def calculate_permutations(self):
        try:
            n = int(self.permutation_input.text())
            if not self.is_all_nums_positive(n):
                raise ValueError('n должно быть положительным')
            result = math.factorial(n)
            self.permutation_result_label.setText(f'Результат: {result}')
        except ValueError as e:
            QMessageBox.warning(self, 'Ошибка', str(e))

    def calculate_permutations_repetition(self):
        try:
            n = int(self.permutation_repetition_n_input.text())
            ns = list(map(int, self.permutation_repetition_ns_input.text().split()))
            if not self.is_all_nums_positive(n, *ns):
                raise ValueError('Все числа должны быть положительными')
            elif sum(ns) != n:
                raise ValueError('Количество элементов и сумма элементов должны быть равны!')
            result = math.factorial(n) // math.prod(math.factorial(num) for num in ns)
            self.permutation_repetition_result_label.setText(f'Результат: {result}')
        except ValueError as e:
            QMessageBox.warning(self, 'Ошибка', str(e))

    def calculate_arrangements(self):
        try:
            n = int(self.arrangements_n_input.text())
            m = int(self.arrangements_m_input.text())
            if not self.is_all_nums_positive(n, m):
                raise ValueError("n и m должны быть положительными")
            elif m > n:
                raise ValueError('m должно быть меньше или равно n')
            result = math.perm(n, m)
            self.arrangements_result_label.setText(f"Результат: {result}")
        except ValueError as e:
            QMessageBox.warning(self, 'Ошибка', str(e))

    def calculate_arrangements_repetition(self):
        try:
            n = int(self.arrangements_n_input.text())
            m = int(self.arrangements_m_input.text())
            if not self.is_all_nums_positive(n, m):
                raise ValueError("n и m должны быть положительными")
            result = n ** m
            self.arrangements_result_label.setText(f"Результат: {result}")
        except ValueError as e:
            QMessageBox.warning(self, 'Ошибка', str(e))

    def calculate_combination(self):
        try:
            n = int(self.combination_n_input.text())
            m = int(self.combination_m_input.text())
            if not self.is_all_nums_positive(n, m):
                raise ValueError("n и m должны быть положительными")
            result = math.comb(n, m)
            self.combination_result_label.setText(f"Результат: {result}")
        except ValueError as e:
            QMessageBox.warning(self, 'Ошибка', str(e))

    def calculate_combination_repetition(self):
        try:
            n = int(self.combination_n_input.text())
            m = int(self.combination_m_input.text())
            if not self.is_all_nums_positive(n, m):
                raise ValueError("n и m должны быть положительными")
            result = math.comb(n + m - 1, m)
            self.combination_result_label.setText(f"Результат: {result}")
        except ValueError as e:
            QMessageBox.warning(self, 'Ошибка', str(e))

    # Проверка чисел на не отрицательность
    @staticmethod
    def is_all_nums_positive(*nums):
        return all([num >= 0 for num in nums])


def main():
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
