class AlertSystem:
    def send_alert(self, drug1, drug2, severity, description):
        print(f"{severity} → {drug1.title()} + {drug2.title()}: {description}")
