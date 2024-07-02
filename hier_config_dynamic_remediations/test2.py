
def remediation(remediation_config):
    lineage = remediation_config.get_child("startswith", "snmp-server ip")
    thing = []
    for line in lineage.all_children():
        print(line.text)
        new_line = line.text + " testing"
        thing.append((line.text, new_line))
    for delete, add in thing:
        lineage.del_child_by_text(delete)
        lineage.add_child(add)