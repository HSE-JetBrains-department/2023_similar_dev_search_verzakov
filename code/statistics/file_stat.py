from pydriller import Repository
from tqdm.auto import tqdm
from typing import Dict, List
from collections import defaultdict
from code.statistics.commit_key import CommitKey
from code.statistics.file_info import FileInfo

"""
    find_info - get info about repo
"""


def find_info(path: str) -> Dict[CommitKey, List[FileInfo]]:
    """
        find_info - func to read info about repo and return Dict[CommitKey, Dict[str, FileInfo]]
        path - path to repo (url or file system repo)
    """
    repo = Repository(path)
    programmers = defaultdict(lambda: defaultdict(FileInfo))

    count = 0
    for _ in repo.traverse_commits():
        count += 1

    for commit in tqdm(repo.traverse_commits(), total=count):
        author = commit.author.name
        email = commit.author.email
        author_key = CommitKey(author, email)

        for file in commit.modified_files:
            programmers[author_key][file.filename].added += file.added_lines
            programmers[author_key][file.filename].deleted += file.deleted_lines

    programmers_ans = defaultdict(lambda: [])
    for author in programmers.keys():
        for file_name, file_info in programmers[author].items():
            file_info.name = file_name
            programmers_ans[author] += [file_info]

    return programmers_ans


def sort_stat(programmers: Dict[CommitKey, List[FileInfo]]) -> (int, CommitKey):
    """
        stat - sort authors by number of changed lines
        programmers - repo info by author and file info
    """
    programmers_stats = []

    for author in programmers:
        edited = 0

        for file in programmers[author]:
            edited += file.added + file.deleted

        programmers_stats += [(edited, author)]

    return sorted(programmers_stats, reverse=True)
