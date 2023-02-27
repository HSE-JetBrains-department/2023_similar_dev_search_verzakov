"""
   class of file info
"""


class FileInfo:
    def __init__(self, name: str = "", added: int = 0, deleted: int = 0):
        """"
            name - name of file
            added - number of added lines
            deleted - number of deleted lines
        """
        self.added = added
        self.deleted = deleted
        self.name = name
    
    def __str__(self):
        return f'file:{self.name} added:{self.added} deleted: {self.deleted}'
    
    def __repr__(self):
        return f'file:{self.name} added:{self.added} deleted: {self.deleted}'
    
    def __eq__(self, another):
        return self.name == another.name and self.added == another.added and self.deleted == another.deleted

    def __lt__(self, another):
        """
            check file name lexicographically
        """
        if self.name != another.name:
            return self.name < another.name
        if self.added != another.added:
            return self.added < another.added
        return self.deleted < another.deleted
