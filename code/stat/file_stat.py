from pydriller  import Repository
from tqdm.auto import tqdm
from commit_key import CommitKey
from file_info import FileInfo

def findInfo(path):
    repo = Repository(path)
    programmers = {}
    
    count = 0
    for commit in repo.traverse_commits():
        count += 1
    
    for commit in tqdm(repo.traverse_commits(), total=count):
    
        author = commit.author.name
        email = commit.author.email

        key = CommitKey(author, email)

        if key not in programmers:
            programmers[key] = {}

        for file in commit.modified_files:

            if file.filename not in programmers[key]:
                programmers[key][file.filename] = FileInfo(0, 0)

            programmers[key][file.filename].added += file.added_lines
            programmers[key][file.filename].deleted += file.deleted_lines
    return programmers

def stat(programmers):
    programmers_stats = []

    for author in programmers:
        edited = 0

        for file in programmers[author]:
            edited += programmers[author][file].added + programmers[author][file].deleted

        programmers_stats += [(edited, author)]
    
    return sorted(programmers_stats, reverse = True)
