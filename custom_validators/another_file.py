from nautobot_data_validation_engine.custom_validators import DataComplianceRule, ComplianceError

class TestComplianceThing(DataComplianceRule):
    model = "dcim.region"
    def audit(self):
        return

class GitRackCompliance(DataComplianceRule):
    model = "dcim.rack"
    enforce = True
    def audit(self):
        raise ComplianceError({"name": "nope", "site": "try again"})

class AnotherGitRackCompliance(DataComplianceRule):
    model = "dcim.rack"
    enforce = True
    def audit(self):
        raise ComplianceError({"site": "very wrong"})
