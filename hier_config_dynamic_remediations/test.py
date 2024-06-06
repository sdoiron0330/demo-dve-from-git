

def remediation(lineage):
    print("Hello World")
    print(lineage)
    for line in lineage.all_children():
        print(line.text)
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