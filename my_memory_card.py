from PyQt5 import QtWidgets, QtGui
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGroupBox, QButtonGroup, QWidget, QHBoxLayout, QPushButton, QLabel, QVBoxLayout, QRadioButton
from random import shuffle, randint

class Questions():
    def __init__(self, questions, right_answer, wrong1, wrong2, wrong3):
        self.questions = questions
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])
main_win = QWidget()

image = QtGui.QIcon('9b5ef4aba54a4f6cfdceb9def0445c2c.jpg')
main_win.setWindowTitle('стопапупа')
main_win.setWindowIcon(image)

# Создаем виджеты
RadioGroupBox = QGroupBox('это векторинапо древнему ифриту!!!!!')
rbtn_1 = QRadioButton('нажми сюда чтобы выйти из вектарины')
rbtn_2 = QRadioButton('нажми сюда если еврей')
rbtn_3 = QRadioButton('нажми сюда если любишь путина')
rbtn_4 = QRadioButton('нажми сюда чтобы начать вектарину')
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

answer_GroupBox = QGroupBox('правильный ответ')
ans_r = QLabel('прав\неправ')
ans_r2 = QLabel('правильный ответ')
layo_ans = QVBoxLayout()
layo_ans.addWidget(ans_r)
layo_ans.addWidget(ans_r2)
answer_GroupBox.setLayout(layo_ans)
answer_GroupBox.setFixedSize(570, 200)

layoutH1 = QHBoxLayout()
layoutH2 = QVBoxLayout()
layoutH3 = QVBoxLayout()
layoutH2.addWidget(rbtn_1)
layoutH2.addWidget(rbtn_2)
layoutH3.addWidget(rbtn_3)
layoutH3.addWidget(rbtn_4)
layoutH1.addLayout(layoutH2)
layoutH1.addLayout(layoutH3)
RadioGroupBox.setLayout(layoutH1)

main_layout = QVBoxLayout()
layoutwin1 = QVBoxLayout()
layoutwin2 = QVBoxLayout()
layoutwin3 = QVBoxLayout()
question = QLabel('Вопрос')
button = QPushButton('ответить')
layoutwin1.addWidget(question)
RadioGroupBox.setFixedSize(570, 200)
layoutwin1.addWidget(RadioGroupBox)
layoutwin1.addWidget(answer_GroupBox)
answer_GroupBox.hide()
layoutwin1.addWidget(button)
main_layout.addLayout(layoutwin1)
main_layout.addLayout(layoutwin2)
main_layout.addLayout(layoutwin3)

# --- Стилизация в современном темном стиле с жирным шрифтом ---
style = """
QWidget {
    background-color: #121212;
    color: #e0e0e0;
    font-family: "Segoe UI", "Arial Black", "Consolas", sans-serif;
    font-weight: bold;
    font-size: 16px;
}

QGroupBox {
    border: 2px solid #bb86fc;
    border-radius: 10px;
    margin-top: 10px;
    color: #bb86fc;
    background-color: #1e1e1e;
}

QLabel {
    color: #e0e0e0;
    font-weight: bold;
    font-size: 18px;
}

QPushButton {
    background-color: #3700b3;
    border: none;
    border-radius: 12px;
    padding: 12px;
    color: #ffffff;
    font-weight: bold;
    font-size: 18px;
    min-width: 200px;
}

QPushButton:hover {
    background-color: #6200ee;
}

QRadioButton {
    spacing: 10px;
    font-size: 16px;
    color: #e0e0e0;
}

QRadioButton::indicator {
    width: 20px;
    height: 20px;
}

QRadioButton::indicator:unchecked {
    border: 2px solid #bb86fc;
    background: transparent;
    border-radius: 10px;
}

QRadioButton::indicator:checked {
    background-color: #bb86fc;
    border: 2px solid #bb86fc;
    border-radius: 10px;
}
"""

main_win.setStyleSheet(style)

def show_result():
    RadioGroupBox.hide()
    answer_GroupBox.show()
    button.setText('следующий вопрос')
    RadioGroupBox.setFixedSize(570, 100)
    answer_GroupBox.setFixedSize(570, 200)

def show_qustion():
    RadioGroupBox.show()
    answer_GroupBox.hide()
    button.setText('ответить')
    RadioGroup.setExclusive(False)
    for btn in answers:
        btn.setChecked(False)
    RadioGroup.setExclusive(True)
    answer_GroupBox.setFixedSize(570, 100)
    RadioGroupBox.setFixedSize(570, 200)

def ask(q: Questions):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.questions)
    ans_r2.setText(q.right_answer)
    show_qustion()

main_win.total = 0
main_win.score = 0

def show_correct(res):
    ans_r.setText(res)
    show_result()

def checkanswer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
    elif any(btn.isChecked() for btn in answers[1:]):
        show_correct('Неверно!')
    else:
        show_correct('Выберите ответ!')

    print(f'Статистика:\nВсего вопросов: {main_win.total}\nПравильных ответов: {main_win.score}')
    if main_win.total > 0:
        print(f'Рейтинг: {(main_win.score / main_win.total) * 100:.2f}%')

def next_questions():
    main_win.total += 1
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)

def click_on():
    if button.text() == 'ответить':
        checkanswer()
    else:
        next_questions()

questions_list = []
q1 = Questions('Quid est ifrit?', 'Daemon', 'Animal', 'Planta', 'Stella')
q2 = Questions('Ubi habitat ifrit?', 'In igni', 'In aqua', 'In terra', 'In aere')
q3 = Questions('Estne ifrit corporeus?', 'Ita', 'Minime', 'Parum', 'Nescio')
q4 = Questions('Quid agit ifrit?', 'Magiam', 'Laborat', 'Curat', 'Canit')
q5 = Questions('Ifrit est bonus an malus?', 'Malus', 'Bonus', 'Indifferens', 'Ignotus')
q6 = Questions('Cum quid ifrit pugnabit?', 'Magia', 'Gladio', 'Arcu', 'Fistula')
q7 = Questions('Potestne ifrit volare?', 'Ita', 'Minime', 'Saepe', 'Raro')
q8 = Questions('What est vulnerabilis erat ifrit?', 'Aqua', 'Ignis', 'Ventus', 'Terra')
q9 = Questions('Quot habet ifrit manus?', 'Duas', 'Tres', 'Quattuor', 'Sex')
q10 = Questions('Ifrit dicitur esse?', 'Fortis', 'Debilis', 'Celer', 'Lentus')
q11 = Questions('Estne ifrit immortalis?', 'Ita', 'Minime', 'Saepe', 'Nunquam')
q12 = Questions('Cum quid ifrit communicat?', 'Incantationibus', 'Verbis', 'Silentiis', 'Cantibus')
q13 = Questions('Quid significat verbum "ifrit"?', 'Daemon ignis', 'Angelus', 'Homo', 'Bestia')
q14 = Questions('Ifrit saepe invenitur in?', 'Arabia', 'Europa', 'Asia', 'Africa')
q15 = Questions('Potestne ifrit humanam formam accipere?', 'Ita', 'Minime', 'Saepe', 'Nunquam')
q16 = Questions('Ifrit amicus est?', 'Rarus', 'Frequens', 'Semper', 'Nunquam')
q17 = Questions('Quid est arma ifrit?', 'Ignis', 'Gladius', 'Fornax', 'Aqua')
q18 = Questions('Ifrit potest magiam facere?', 'Ita', 'Minime', 'Nescio', 'Raro')
q19 = Questions('Quis potest domare ifrit?', 'Magus', 'Miles', 'Servus', 'Nauta')
q20 = Questions('Ifrit saepe videtur in?', 'Somnis', 'Ludis', 'Bellis', 'Oppidum')
q21 = Questions('Quid timet ifrit?', 'Aqua', 'Ignis', 'Bestia', 'Homo')
q22 = Questions('Quid est virtus ifrit?', 'Potentia', 'Celeritas', 'Sapientia', 'Patientia')
q23 = Questions('Ifrit potest loqui?', 'Ita', 'Minime', 'Semper', 'Nunquam')
q24 = Questions('Ifrit potest mutare formam?', 'Ita', 'Minime', 'Semper', 'Nunquam')
q25 = Questions('What est corpus ifrit?', 'Ignis', 'Aqua', 'Terra', 'Aer')
q26 = Questions('Ifrit potest infra terra vivere?', 'Minime', 'Ita', 'Fortasse', 'Raro')
q27 = Questions('Ifrit numquam?', 'Ambulat', 'Volat', 'Tacet', 'Clamat')
q28 = Questions('Est ifrit periculosus?', 'Ita', 'Minime', 'Saepe', 'Nunquam')
q29 = Questions('Quid est cibus ifrit?', 'Ignis', 'Carne', 'Herbis', 'Fructus')
q30 = Questions('Ifrit est pars?', 'Mythologiae', 'Historiae', 'Scientiae', 'Philosophiae')

questions_list.extend([q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,
                       q11, q12, q13, q14, q15, q16, q17, q18, q19, q20,
                       q21, q22, q23, q24, q25, q26, q27, q28, q29, q30])

question.setFixedSize(570, 50)
button.setFixedSize(570, 160)
button.clicked.connect(click_on)

main_win.setLayout(main_layout)
main_win.resize(600, 500)
main_win.show()

app.exec()
