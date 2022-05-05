import PyQt5.QtWidgets as PyWidget
import PyQt5.QtGui as PyGui


class MainWindow(PyWidget.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World!!")

        self.setLayout(PyWidget.QVBoxLayout())

        my_label = PyWidget.QLabel("Type Something Into The Box Below", self)
        my_label.setFont(PyGui.QFont('Helvetica', 24))
        self.layout().addWidget(my_label)

        my_text = PyWidget.QTextEdit(self,
                                plainText="This is real text!",
                                acceptRichText=False,
                                lineWrapColumnOrWidth=75,
                                placeholderText="Hello World!",
                                readOnly=False
                                )

        self.layout().addWidget(my_text)

        my_button = PyWidget.QPushButton("Press Me!",
                                    clicked=lambda: press_it())
        self.layout().addWidget(my_button)

        self.show()

        def press_it():
            my_label.setText(f'You Typed {my_text.toPlainText()}!')
            my_text.setPlainText("You Pressed The Button!")


app = PyWidget.QApplication([])
mw = MainWindow()
app.exec_()