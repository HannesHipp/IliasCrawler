from Framework.DataElements.LoadingAnimation import LoadingAnimation
from Framework.OutputFrame import OutputFrame
from IliasCrawler.Datapoints.Password import Password
from IliasCrawler.Datapoints.Username import Username
from IliasCrawler.Functions.ValidateLogin import ValidateLogin


class LoginValidationFrame(OutputFrame):

    def __init__(self, username: Username, password: Password):
        super().__init__(
            path="IliasCrawler\\resources\\LoginValidationView.ui",
            datapoints=[username, password],
            buttonNames=[],
            function=ValidateLogin(username, password)
        )
        self.username = username
        self.password = password
        LoadingAnimation(username, self.text)

    def addNextFrames(self, pathFrame):
        self.pathFrame = pathFrame

    def decideNextFrame(self):
        if self.username.valid and self.password.valid:
            return self.pathFrame
        else:
            return self.prevFrame