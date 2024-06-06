

def remediation(lineage):
    print("Hello World")
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
        # if line.text.startswith("no"):
        #     line_items = line.text.split()
        #     try:
        #         if isinstance(int(line_items[1]), int):
        #             line_items.remove(line_items[1])
        #     except ValueError:
        #         pass
        # lineage.del_child_by_text(line.text)
        # lineage.add_child(" ".join(line_items))
    return lineage