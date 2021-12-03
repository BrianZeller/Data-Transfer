class LogHandler:

    def __init__(self) -> None:
        self.__logFileName = "log.txt"
        self.__errorLogFileName = "errorLog.txt"

        with open(self.__logFileName, "w+") as log:
            log.close()

        with open(self.__errorLogFileName, "w+") as log:
            log.close()

    def writePostFailure(self, name, response):
        with open(self.__logFileName, "a") as log:
            log.write("POST_ERROR: {} failed to post to Insightly, receiving response {}\n".format(name, response))
            log.close()
    
    def writeOrganizationNotFound(self, name, organization):
        with open(self.__logFileName, "a") as log:
            log.write("ORGANIZATION: {} - {} was not found in Insightly\n".format(name, organization))
            log.close()

    def writeError(self,row, error, msg):
        with open(self.__errorLogFileName, "a") as log:
            log.write("{}: Row {} {}".format(error, row, msg))
            log.close()
    
