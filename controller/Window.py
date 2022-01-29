from PyQt5.QtWidgets import QVBoxLayout, QWidget, QStackedWidget


class Window(QWidget):
    
    def __new__(cls, app):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Window, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, app):
        super().__init__()
        self.app = app
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
