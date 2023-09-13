from Framework.OutputFrame import OutputFrame
from IliasCrawler.Datapoints.Password import Password
from IliasCrawler.Datapoints.Username import Username
from IliasCrawler.Functions.ValidateLogin import ValidateLogin


class LoginValidationFrame(OutputFrame):

    def __init__(self, username: Username, password: Password):
        super().__init__(
            path="IliasCrawler\\resources\\LoginValidationView.ui",
            function=ValidateLogin(username, password)
        )
        self.username = username
        self.password = password

    def addNextFrames(self, loginFrame, pathFrame):
        self.loginFrame = loginFrame
        self.pathFrame = pathFrame

    def decide_next_frame(self, pressedButton):
        if self.function.error:
            return self.loginFrame
        return self.pathFrame
