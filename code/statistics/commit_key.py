"""
    Class to contain author info
"""


class CommitKey:
    def __init__(self, author: str, email: str):
        """
            author - name of author
            email - email of author
        """
        self.author = author
        self.email = email
    
    def __eq__(self, another):
        """
            Check author and email attributes
        """
        attrs = hasattr(another, 'author') and hasattr(another, 'email')
        if not attrs:
            return False
        
        return self.author == another.author and self.email == another.email
    
    def __lt__(self, another):
        """
            check author and email lexicographically
        """
        if self.author != another.author:
            return self.author < another.author
        return self.email < another.email
    
    def __repr__(self):
        return f'author: {self.author} email: {self.email}'
    
    def __str__(self):
        return f'author: {self.author} email: {self.email}'
    
    def __hash__(self):
        return hash(self.author) ^ hash(self.email)
