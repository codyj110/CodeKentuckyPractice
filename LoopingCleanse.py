import pandas as pd

import CleanseByod

data = pd.read_csv('BYOD.csv');

cb = CleanseByod.Cleanse()
newData = cb.removeParen(data)




print(data)
print(newData)





