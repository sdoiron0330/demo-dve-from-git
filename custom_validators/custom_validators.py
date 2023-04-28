from nautobot_data_validation_engine.custom_validators import DataComplianceRule, ComplianceError

class GitSiteCompliance(DataComplianceRule):
    model = "dcim.site"
    enforce = False

    def audit_one(self):
        raise ComplianceError({"region": "bruh 3"})
    def audit_two(self):
        raise ComplianceError({"tenant": "git test"})

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
