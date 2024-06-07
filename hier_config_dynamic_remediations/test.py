

def remediation(lineage):
    print(lineage)
    thing = {}
    for line in lineage.all_children():
        print(line.text)
        line_items = line.text.split()
        address = line_items[-1]
        if address in thing:
            thing[address].append(line.text)
        else:
            thing.update({address:[line.text]})
    for key,value in thing.items():
        if len(value) > 1:
            for line in value:
                lineage.del_child_by_text(line)
    if len(list(lineage.all_children())) == 0:
        parent = lineage.parent
        parent.del_child_by_text(lineage.text)
    return lineage