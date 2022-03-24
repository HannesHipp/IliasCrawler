from PyQt5.QtWidgets import QVBoxLayout, QWidget, QStackedWidget


class Window(QWidget):
    
    def __init__(self, q_app):
        super().__init__()
        self.q_app = q_app
        self.stackedWidget = QStackedWidget()
        mainLayout = QVBoxLayout()    
        mainLayout.setSpacing(0)
        mainLayout.setContentsMargins(0, 0, 0, 0)   
        mainLayout.addWidget(self.stackedWidget)
        self.setFixedSize(800,500)
        self.setLayout(mainLayout)   
        self.show()     

    def add_frame(self, frame):
        index = self.stackedWidget.count()
        frame.index = index
        self.stackedWidget.addWidget(frame)

    def select_frame(self, frame):
        if frame.index is None:
            self.add_frame(frame)
        self.stackedWidget.setCurrentIndex(frame.index)
        self.q_app.processEvents()
