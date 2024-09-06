from anytree import Node, RenderTree, AbstractStyle
from pathlib import Path
import os

class TableContentsStyle(AbstractStyle):
    def __init__(self):
        super(TableContentsStyle, self).__init__("  ", "- ", "- ")

def main():
    udo = Node("Udo")
    marc = Node("Marc", parent=udo)
    lian = Node("Lian", parent=marc)
    dan = Node("Dan", parent=udo)
    jet = Node("Jet", parent=dan)
    jan = Node("Jan", parent=dan)
    joe = Node("Joe", parent=dan)

    for pre, fill, node in RenderTree(udo, style=TableContentsStyle):
        if node.is_root:
            print(f'# {node.name}')
        else:
            print(f'{pre}{node.name}')

if __name__=="__main__":
    main()