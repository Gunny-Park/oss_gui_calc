import sys
from PyQt5.QtWidgets import *
import math

operand = []
operator = []

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_operation = QGridLayout()
        layout_clear_equal = QHBoxLayout()
        layout_number = QGridLayout()
        layout_equation_solution = QFormLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        label_equation = QLabel("")
        #label_solution = QLabel("Number: ")
        self.equation = QLineEdit("")
        self.solution = QLineEdit("")

        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        layout_equation_solution.addRow(label_equation, self.equation)
        #layout_equation_solution.addRow(label_solution, self.solution)

        ### 사칙연상 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("÷")

        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))

        ### =, clear, backspace 버튼 생성
        button_equal = QPushButton("=")
        button_clear = QPushButton("Clear")
        button_backspace = QPushButton("Backspace")

        ### =, clear, backspace 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)

        ### =, clear, backspace 버튼을 layout_clear_equal 레이아웃에 추가
        layout_clear_equal.addWidget(button_clear)
        layout_clear_equal.addWidget(button_backspace)
        layout_clear_equal.addWidget(button_equal)

        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
            if number >0:
                x,y = divmod(number-1, 3)
                layout_number.addWidget(number_button_dict[number], x+2, y)
            elif number==0:
                layout_number.addWidget(number_button_dict[number], 5, 1)

        ### 소숫점 버튼과 00 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        layout_number.addWidget(button_dot, 5, 2)

        button_double_zero = QPushButton("00")
        button_double_zero.clicked.connect(lambda state, num = "00": self.number_button_clicked(num))
        layout_number.addWidget(button_double_zero, 5, 0)

        ### 사칙연산 레이아웃 
        layout_number.addWidget(button_equal, 5, 4)
        layout_number.addWidget(button_division, 1, 4)
        layout_number.addWidget(button_product, 2, 4)
        layout_number.addWidget(button_minus, 3, 4)
        layout_number.addWidget(button_plus, 4, 4)

        ### new_btn
        button_mod = QPushButton("%")
        button_mod.clicked.connect(lambda state, operation = "%": self.button_operation_clicked(operation))

        button_ce = QPushButton("CE")
        button_ce.clicked.connect(self.button_clear_clicked)
        button_c = QPushButton("C")
        button_c.clicked.connect(self.button_clear_clicked)
        button_sqr = QPushButton("√x")
        button_sqr.clicked.connect(lambda state, operation = "√x": self.button_oper_clicked(operation))
        button_pow = QPushButton("x²")
        button_pow.clicked.connect(lambda state, operation = "x²": self.button_oper_clicked(operation))
        button_rev = QPushButton("1/x")
        button_rev.clicked.connect(lambda state, operation = "1/x": self.button_oper_clicked(operation))
        layout_number.addWidget(button_ce, 0, 1)        
        layout_number.addWidget(button_c, 0, 2)
        layout_number.addWidget(button_backspace, 0, 4)
        layout_number.addWidget(button_mod, 0, 0)
        layout_number.addWidget(button_sqr, 1, 2)
        layout_number.addWidget(button_pow, 1, 1)
        layout_number.addWidget(button_rev, 1, 0)

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation_solution)
        #main_layout.addLayout(layout_clear_equal)
        main_layout.addLayout(layout_number)
        #main_layout.addLayout(layout_operation)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        equation = self.equation.text()
        equation += str(num)
        self.equation.setText(equation)

    def button_operation_clicked(self, operation):
        data = int(self.equation.text())
        operand.append(data)
        operator.append(str(operation))
        self.equation.setText("")

    def button_oper_clicked(self, operation):
        data = int(self.equation.text())
        operand.append(data)
        operator.append(str(operation))
        if operator[0] == "√x":
            solution = math.sqrt(operand[0])
        elif operator[0] == "x²":
            solution = operand[0] * operand[0]
        elif operator[0] == "1/x":
            solution = 1 / operand[0]
        else:
            solution = 'error'
        self.equation.setText(str(solution))

    def button_equal_clicked(self):
        data = int(self.equation.text())
        operand.append(data)
        #self.equation.setText("")
        if operator[0] == "+":
            solution = (operand[0] + operand[1])
        elif operator[0] == "-":
            solution = (operand[0] - operand[1])
        elif operator[0] == "*":
            solution = (operand[0] * operand[1])
        elif operator[0] == "/":
            solution = (operand[0] / operand[1])
        elif operator[0] == "%":
            solution = (operand[0] % operand[1])
        else:
            solution = 'error'
        self.equation.setText(str(solution))

    def button_clear_clicked(self):
        self.equation.setText("")
        operand.clear()
        operator.clear()

        #self.solution.setText("")

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())