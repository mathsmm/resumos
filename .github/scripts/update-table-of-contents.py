# https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python
# Copiado da resposta do usuário "abstrus".
# 
# EXEMPLO DE USO:
#
# # With a criteria (skip hidden files)
# def is_not_hidden(path):
#     return not path.name.startswith(".")
#
# paths = DisplayablePath.make_tree(Path('doc'), criteria=is_not_hidden)
# for path in paths:
#     print(path.displayable())
#
# EXEMPLO DE SAÍDA:
#
# doc/
# ├── _static/
# │   ├── embedded/
# │   │   ├── deep_file
# │   │   └── very/
# │   │       └── deep/
# │   │           └── folder/
# │   │               └── very_deep_file
# │   └── less_deep_file
# ├── about.rst
# ├── conf.py
# └── index.rst
import os
from pathlib import Path

class DisplayablePath(object):
    display_filename_prefix_middle = '-'
    display_filename_prefix_last = '-'
    display_parent_prefix_middle = '  '
    display_parent_prefix_last = '  '

    def __init__(self, path, parent_path, is_last):
        self.path = Path(str(path))
        self.parent = parent_path
        self.is_last = is_last
        if self.parent:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0

    @property
    def displayname(self):
        if self.path.is_dir():
            return self.path.name + '/'
        return self.path.name

    @classmethod
    def make_tree(cls, root, parent=None, is_last=False, criteria=None):
        root = Path(str(root))
        criteria = criteria or cls._default_criteria

        displayable_root = cls(root, parent, is_last)
        yield displayable_root

        children = sorted(list(path
                               for path in root.iterdir()
                               if criteria(path)),
                          key=lambda s: str(s).lower())
        count = 1
        for path in children:
            is_last = count == len(children)
            if path.is_dir():
                yield from cls.make_tree(path,
                                         parent=displayable_root,
                                         is_last=is_last,
                                         criteria=criteria)
            else:
                yield cls(path, displayable_root, is_last)
            count += 1

    @classmethod
    def _default_criteria(cls, path):
        return True

    @property
    def displayname(self):
        if self.path.is_dir():
            return self.path.name + '/'
        return self.path.name

    def displayable(self):
        if self.parent is None:
            return self.displayname

        _filename_prefix = (self.display_filename_prefix_last
                            if self.is_last
                            else self.display_filename_prefix_middle)

        parts = ['{!s} {!s}'.format(_filename_prefix,
                                    self.displayname)]

        parent = self.parent
        while parent and parent.parent is not None:
            parts.append(self.display_parent_prefix_middle
                         if parent.is_last
                         else self.display_parent_prefix_last)
            parent = parent.parent

        return ''.join(reversed(parts))

def main():
    exclusions = ['img']
    inclusions = ['resumos']
    def criteria(path: Path):
        for exc in exclusions:
            if str(path).lower().find(exc.lower()) != -1:
                return False
        for inc in inclusions:
            if str(path).lower().find(inc.lower()) != -1:
                return True
        return False
    
    replace_dict = {
        '/': '',
        '.md': '',
        '_': ' '
    }

    paths = DisplayablePath.make_tree(Path(os.getcwd()+'\\resumos'), criteria=criteria)
    for path in paths:
        if 'resumos' in path.path.name:
            continue
        md_line = path.displayable()
        for old, new in replace_dict.items():
            md_line = md_line.replace(old, new)
        print(md_line)

if __name__=="__main__":
    main()