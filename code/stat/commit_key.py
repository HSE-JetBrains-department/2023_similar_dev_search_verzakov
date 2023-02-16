class CommitKey():
    def __init__(self, author, email):
        self.author = author
        self.email = email
    
    def __eq__(self, another):
        attrs = hasattr(another, 'author') and hasattr(another, 'email')
        if not attrs:
            return False
        
        return self.author == another.author and self.email == another.email
    
    def __lt__(self, another):
        return self.author < another.author and self.email < another.email
    
    def __repr__(self):
        return "author: " + self.author + " email: " + self.email
    
    def __str__(self):
        return "author: " + self.author + " email: " + self.email
    
    def __hash__(self):
        return hash(self.author)^hash(self.email)
