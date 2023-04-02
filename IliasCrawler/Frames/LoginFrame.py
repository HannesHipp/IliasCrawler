from Framework.DataElements.TextField import TextField
from Framework.InputFrame import InputFrame


class LoginFrame(InputFrame):

    def __init__(self, username, password):
        super().__init__(
            path="IliasCrawler\\resources\\LoginView.ui",
            datapoints=[username, password],
            buttonNames=['button_login']
        )
        self.username = username
        self.password = password
        TextField(username, self.textfield_username)
        TextField(password, self.textfield_password)

    def addNextFrames(self, loginValidationFrame):
        self.loginValidationFrame = loginValidationFrame

    def decideNextFrame(self):
        return self.loginValidationFrame
