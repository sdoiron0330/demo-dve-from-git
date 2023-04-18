from nautobot_data_validation_engine import AuditRuleset

class GitSiteAuditRuleset(AuditRuleset):
    model = "dcim.site"

    def audit_site(self, instance):
        self.success(instance, attribute="name", validated_attribute_value=instance.name)