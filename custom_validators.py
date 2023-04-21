from nautobot_data_validation_engine.custom_validators import AuditRuleset, AuditError

class GitSiteAuditRuleset(AuditRuleset):
    model = "dcim.site"
    enforce = True

    def audit(self):
        raise AuditError({"tenant": "git test"})

custom_validators = [GitSiteAuditRuleset]