class Celle():
    def __init__(self):
        self.status = "dod"
    
    def settDod(self):
        self.status = "dod"
    
    def settLevende(self):
        self.status = "levende"
    
    def erLevende(self):
        if self.status == "levende":
            return True
        else:
            return False

    def hentTegnrepresentasjon(self):
        levende = self.erLevende()
        if levende == True:
            return "O"
        else:
            return "."
        