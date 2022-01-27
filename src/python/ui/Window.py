from PyQt5.QtWidgets import QVBoxLayout, QWidget, QStackedWidget


class Window(QWidget):
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Window, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        super().__init__()
        self.stackedWidget = QStackedWidget()
        mainLayout = QVBoxLayout()    
        mainLayout.setSpacing(0)
        mainLayout.setContentsMargins(0, 0, 0, 0)   
        mainLayout.addWidget(self.stackedWidget)
        self.setFixedSize(800,500)
        self.setLayout(mainLayout)        

    def add_frame(self, frame):
        index = self.stackedWidget.count()
        frame.index = index
        self.stackedWidget.addWidget(frame)
