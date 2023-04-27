from nautobot_data_validation_engine.custom_validators import DataComplianceRule

class TestComplianceThing(DataComplianceRule):
    def audit(self):
        return
