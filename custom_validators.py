from nautobot_data_validation_engine.custom_validators import AuditRuleset, AuditError

class GitSiteAuditRuleset(AuditRuleset):
    model = "dcim.site"
    enforce = True

    def audit_one(self):
        raise AuditError({"region": "true"})

    def audit_two(self):
        raise AuditError({"tenant": "git test"})

    def audit(self):
        messages = {}
        for fn in [self.audit_one, self.audit_two]:
            try:
                fn()
            except AuditError as ex:
                messages.update(ex.messages_dict)
        if messages:
            raise AuditError(**messages)


custom_validators = [GitSiteAuditRuleset]