import pandas as pd

def load_file(filepath):
    data = pd.read_excel(filepath)
    include = ['float', 'int']
    stats = data.describe(include=include)

    return stats

file_path = 'E:\Coding\Projects\Basic stats of an Excel File\Maven Business School(final).xlsx'
statistics = load_file(file_path)
print(statistics)