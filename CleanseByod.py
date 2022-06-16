class Cleanse:

    def __int__(self):
        pass

    def removeParen(self, dataFrame):
        newData = dataFrame.replace(to_replace='\(', value='', regex=True)
        return newData.replace(to_replace='\)', value='', regex=True)