from nautobot_data_validation_engine.custom_validators import DataComplianceRule, ComplianceError
import re

class GitSiteCompliance(DataComplianceRule):
    model = "dcim.site"
    enforce = False

    def audit_one(self):
        if not re.match(r"^.+\d+$", self.context["object"].name):
            raise ComplianceError({"name": "All site names should end with a number."})
    def audit_two(self):
        if not self.context["object"].region:
            raise ComplianceError({"region": "All sites should have a region set2222."})

    def audit(self):
        messages = {}
        for fn in [self.audit_one, self.audit_two]:
            try:
                fn()
            except ComplianceError as ex:
                messages.update(ex.message_dict)
        if messages:
            raise ComplianceError(messages)


custom_validators = [GitSiteCompliance]
