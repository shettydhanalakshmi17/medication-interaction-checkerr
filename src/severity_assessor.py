class SeverityAssessor:
    def assess(self, severity_level):
        severity_map = {
            'high': '🔴 SEVERE',
            'moderate': '🟠 MODERATE',
            'low': '🟢 LOW'
        }
        return severity_map.get(severity_level.lower(), 'Unknown')
