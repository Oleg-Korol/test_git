#Example 5.
# Прочитать сохраненный csv и сохранить данные в exel фаил.Удалить колонку возраст

import csv
import pandas as pd
f=pd.read_csv("csvfile.csv")
name = ['Id','name','Phone',]
new_file = f[name]
new_file.to_csv("newFile.csv",index=False)



