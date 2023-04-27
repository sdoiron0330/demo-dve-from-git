from nautobot_data_validation_engine.custom_validators import DataComplianceRule

class TestComplianceThing(DataComplianceRule):
    model = "dcim.region"
    def audit(self):
        return
