from Framework.Frame import Frame
from Framework.GuiModuls.TextField import TextField


class LoginFrame(Frame):

    def __init__(self, username, password):
        super().__init__(
            path="IliasCrawler\\resources\\LoginView.ui",
            next_frame_button_names=['button_login']
        )
        self.username = username
        self.password = password
        self.add_module(TextField(username, self.textfield_username))
        self.add_module(TextField(password, self.textfield_password))

    def addNextFrames(self, loginValidationFrame):
        self.loginValidationFrame = loginValidationFrame

    def decide_next_frame(self, pressedButton):
        return self.loginValidationFrame
