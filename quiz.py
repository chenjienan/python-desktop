import PyQt5.QtWidgets as pyqt
import PyQt5.QtGui as gui
import random

OPERATORS = "+-*/"

class Desktop(pyqt.QDialog):
    
    def __init__(self, q_num):
        pyqt.QDialog.__init__(self)
        self.q_num = q_num
        self.q_remain = q_num
        self.score = 0        
        self.cur_q_num = 0

        self.setWindowTitle("Math Quiz")
        self.setGeometry(200, 200, 380, 200)
        font = gui.QFont()
        font.setPointSize(18)
        
        # create a virtical layout grid
        layout = pyqt.QVBoxLayout()

        self.question_num = pyqt.QLabel()
        self.question = pyqt.QLabel()
        self.answer = pyqt.QLineEdit()
        self.answer.setPlaceholderText("Please enter your answer")

        self.setup_question()
        button = pyqt.QPushButton("Next")
        
        layout.addWidget(self.question_num)
        layout.addWidget(self.question)
        layout.addWidget(self.answer)
        layout.addWidget(button)
        self.setLayout(layout)
        self.setFont(font)

        button.clicked.connect(self.confirm)

    def confirm(self):
        user_ans = self.answer.text()

        reply = pyqt.QMessageBox.question(
            self, 
            'Message', 
            'Your answer is ' + user_ans, 
            pyqt.QMessageBox.Yes,
            pyqt.QMessageBox.No)

        if reply == pyqt.QMessageBox.Yes:
            if int(user_ans) == self.res:
                pyqt.QMessageBox.information(self, "Information", "Correct")
                self.score += 1
            else:
                pyqt.QMessageBox.information(self, "Information", "Wrong")
            self.q_remain -= 1
            
            if self.q_remain <= 0:
                mark = format(self.score / self.q_num * 100, '.2f')
                pyqt.QMessageBox.information(self, "Information", "Score: " + str(mark))
                pyqt.QApplication.quit()               
            else:
                self.setup_question()
        else:
            print('No clicked.')

    def setup_question(self):
        q, res = self.get_question_and_ans()
        self.question.setText(q)
        self.cur_q_num += 1
        self.question_num.setText("Question " + str(self.cur_q_num))
        self.res = res
        print(q, res)

    def get_question_and_ans(self):
        num_1 = random.randint(1, 100)
        num_2 = random.randint(1, 100)
        op = OPERATORS[random.randint(0, len(OPERATORS)-1)]
        q = '{} {} {} = ?'.format(num_1, op, num_2)
        if op == '+':
            result = num_1 + num_2
        elif op == '-':
            result = num_1 - num_2
        elif op == '*':
            result = num_1 * num_2
        else:
            result = num_1 // num_2

        return q, result

if __name__ == "__main__":
    print("application started")
    APP = pyqt.QApplication([])
    DIALOG = Desktop(3)
    DIALOG.show()
    APP.exec_()
    print("application ended")