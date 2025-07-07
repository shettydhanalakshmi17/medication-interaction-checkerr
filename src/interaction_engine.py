class InteractionEngine:
    def __init__(self, database):
        self.data = database.get_all_interactions()

    def check_interactions(self, meds):
        interactions = []
        for i in range(len(meds)):
            for j in range(i + 1, len(meds)):
                m1, m2 = meds[i], meds[j]
                match = self.data[
                    ((self.data['drug1'] == m1) & (self.data['drug2'] == m2)) |
                    ((self.data['drug1'] == m2) & (self.data['drug2'] == m1))
                ]
                if not match.empty:
                    for _, row in match.iterrows():
                        interactions.append({
                            'drug1': row['drug1'],
                            'drug2': row['drug2'],
                            'severity': row['severity'],
                            'description': row['description']
                        })
        return interactions
