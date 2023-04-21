from nautobot_data_validation_engine.custom_validators import AuditRuleset, AuditError

class GitSiteAuditRuleset(AuditRuleset):
    model = "dcim.site"

    def audit(self):
        raise AuditError({"tenant": "git test", "region": "hello"})

audit_rulesets = [GitSiteAuditRuleset]