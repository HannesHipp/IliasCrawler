from Framework.InputFrame import Frame
from Framework.GuiModuls.TextField import TextField


class LoginFrame(Frame):

    def __init__(self, username, password):
        super().__init__(
            path="IliasCrawler\\resources\\LoginView.ui",
            buttonNames=['button_login']
        )
        self.username = username
        self.password = password
        self.addModule(
            TextField(username, self.textfield_username),
            TextField(password, self.textfield_password)
        )

    def addNextFrames(self, loginValidationFrame):
        self.loginValidationFrame = loginValidationFrame

    def decideNextFrame(self, pressedButton):
        return self.loginValidationFrame
