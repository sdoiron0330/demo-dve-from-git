from nautobot_data_validation_engine.audit_rulesets import AuditRuleset, AuditError

class GitSiteAuditRuleset(AuditRuleset):
    model = "dcim.site"

    def audit(self):
        raise AuditError({"tenant": "git test"})

audit_rulesets = [GitSiteAuditRuleset]