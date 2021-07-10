import sys
from PySide2.QtCore import QRegExp
from PySide2.QtGui import QDoubleValidator, QRegExpValidator
from PySide2.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QGridLayout, QErrorMessage

class AppWindow(QDialog):
    def __init__(self, parent=None):
        super(AppWindow, self).__init__(parent)
        self.setWindowTitle("sw_task_01-plotter")
        
        # Create widgets
        self.input_function = QLineEdit()
        self.input_function.setPlaceholderText("Enter your function...")

        self.submit = QPushButton("Submit")

        self.min_x = QLineEdit()
        self.min_x.setPlaceholderText("minimum x")

        self.max_x = QLineEdit()
        self.max_x.setPlaceholderText("maximum x")

        # Create layout and add widgets
        layout = QGridLayout()
        layout.addWidget(self.input_function, 0, 0, 1, 0)

        layout.addWidget(self.min_x, 1, 0)
        layout.addWidget(self.max_x, 1, 1)
        layout.addWidget(self.submit, 1, 2)

        # Set dialog layout
        self.setLayout(layout)

        # Add submit button handler
        self.submit.clicked.connect(self.handleSubmitFunction)

    # Greets the user
    def handleSubmitFunction(self):
        print("Submit handler")


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    app_window = AppWindow()

    app_window.show()
    # Run the main Qt loop
    sys.exit(app.exec_())