from src.drug_database import DrugDatabase
from src.interaction_engine import InteractionEngine
from src.severity_assessor import SeverityAssessor
from src.alert_system import AlertSystem

# Load database
db = DrugDatabase('data/drug_interactions.csv')
engine = InteractionEngine(db)
assessor = SeverityAssessor()
alerter = AlertSystem()

# User input
user_input = input("Enter medications (comma separated):\n")
medications = [drug.strip().lower() for drug in user_input.split(",")]

# Detect interactions
interactions = engine.check_interactions(medications)

if interactions:
    for inter in interactions:
        severity = assessor.assess(inter['severity'])
        alerter.send_alert(inter['drug1'], inter['drug2'], severity, inter['description'])
else:
    print("✅ No dangerous interactions found.")
