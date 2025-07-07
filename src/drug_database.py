import pandas as pd

class DrugDatabase:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.standardize()

    def standardize(self):
        self.df['drug1'] = self.df['drug1'].str.lower().str.strip()
        self.df['drug2'] = self.df['drug2'].str.lower().str.strip()

    def get_all_interactions(self):
        return self.df
