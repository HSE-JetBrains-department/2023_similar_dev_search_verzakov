class FileInfo():
    def __init__(self, added, deleted):
        self.added = added
        self.deleted = deleted
    
    def __str__(self):
        return "added: " + str(self.added) + " deleted: " + str(self.deleted)
    
    def __repr__(self):
        return "added: " + str(self.added) + " deleted: " + str(self.deleted)
    
    def __eq__(self, another):
        return self.added == another.added and self.deleted == another.deleted
