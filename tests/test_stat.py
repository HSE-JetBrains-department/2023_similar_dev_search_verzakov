import unittest
from typing import Dict, List
from code.statistics.commit_key import CommitKey
from code.statistics.file_info import FileInfo
from code.statistics.file_stat import find_info, sort_stat


def check_two_programmers_info(test_case, first: Dict[CommitKey, List[FileInfo]],
                               second: Dict[CommitKey, List[FileInfo]]):
    test_case.assertEqual(len(first), len(second))

    for author in first.keys():
        fl = sorted(first[author])
        sl = sorted(second[author])
        test_case.assertEqual(fl, sl)


class CheckFindInfo(unittest.TestCase):
    def test_first_repo(self):
        info = find_info("tests/repos/2022_similar_dev_search_skrypnikov")

        programmers = {
            CommitKey("Egor", "egorbu@gmail.com"): [
                FileInfo('.gitignore', 152, 0)
            ],
            CommitKey("egor skrypnikov", "eskrypn@gmail.com"): [
                FileInfo('.gitignore', 8, 3),
                FileInfo('README.md', 28, 0),
                FileInfo('__init__.py', 5, 3),
                FileInfo('analysis.py', 344, 121),
                FileInfo('build_enry.sh', 29, 0),
                FileInfo("classes.py", 275, 45),
                FileInfo('enry_scikit-learn.json', 1, 1),
                FileInfo('enry_stage.py', 15, 15),
                FileInfo('repoparse.py', 982, 562),
                FileInfo('requirements.txt', 10, 3),
                FileInfo('shared.py', 48, 48),
                FileInfo('treesitter_stage.py', 34, 34),
                FileInfo('utils.py', 120, 18),
            ]
        }

        check_two_programmers_info(self, programmers, info)

    def test_second_repo(self):
        info = find_info("tests/repos/2022_similar_dev_search_kononov")

        programmers = {
            CommitKey("Alexey Kononov", "62846387+Alex5041@users.noreply.github.com"): [
                FileInfo('README.md', 49, 15),
                FileInfo('main.py', 138, 23),
            ],
            CommitKey("Egor", "egorbu@gmail.com"): [
                FileInfo('.gitignore', 152, 0),
            ],
            CommitKey("Alex5041", "kononal@gmail.com"): [
                FileInfo('.gitignore', 1, 0),
                FileInfo('README.md', 141, 12),
                FileInfo('__init__.py', 0, 0),
                FileInfo('dev_stats.py', 300, 130),
                FileInfo('enry.py', 122, 126),
                FileInfo('extract.py', 318, 294),
                FileInfo('globals.py', 28, 28),
                FileInfo('lint.yml', 42, 2),
                FileInfo('make_stats.py', 46, 1),
                FileInfo('parsefile.py', 112, 0),
                FileInfo('pipeline.py', 111, 111),
                FileInfo('script.py', 183, 74),
                FileInfo('search.py', 81, 25),
                FileInfo('setup.py', 27, 3),
                FileInfo('stargazers.json', 104, 101),
                FileInfo('stargazers.py', 124, 36),
                FileInfo('test.py', 39, 26),
                FileInfo('test_dev_stats.py', 27, 27),
                FileInfo('tree-sitter.py', 37, 37),
                FileInfo('treesitter.py', 117, 117),
                FileInfo('utils.py', 101, 10),
            ],
            CommitKey("Lint Action", "lint-action@samuelmeuli.com"): [
                FileInfo('dev_stats.py', 59, 33),
                FileInfo('extract.py', 46, 31),
                FileInfo('make_stats.py', 6, 4),
                FileInfo('parsefile.py', 46, 20),
                FileInfo('script.py', 112, 47),
                FileInfo('search.py', 28, 16),
                FileInfo('setup.py', 8, 3),
                FileInfo('stargazers.py', 12, 8),
                FileInfo('test.py', 17, 4),
                FileInfo('utils.py', 8, 4),
            ]
        }

        check_two_programmers_info(self, programmers, info)

    def test_third_repo(self):

        info = find_info("tests/repos/2022_similar_dev_search_petropavlovskiy")

        programmers = {
            CommitKey("Egor", "egorbu@gmail.com"): [
                FileInfo('.gitignore', 152, 0),
            ],
            CommitKey("alf3ratz", "49417479+alf3ratz@users.noreply.github.com"): [
                FileInfo('.gitignore', 2, 0),
                FileInfo('Dockerfile', 8, 8),
                FileInfo('README.md', 36, 3),
                FileInfo('action.yml', 16, 16),
                FileInfo('ci.yml', 106, 108),
                FileInfo('enry_processor.py', 29, 0),
                FileInfo('entrypoint.sh', 5, 5),
                FileInfo('git_processor.py', 59, 13),
                FileInfo('git_test.py', 11, 11),
                FileInfo('helpers.py', 176, 38),
                FileInfo('main.py', 46, 25),
                FileInfo('preview.png', 0, 0),
                FileInfo('requirements.txt', 23, 15),
                FileInfo('setup.py', 23, 10),
                FileInfo('treesitter.py', 48, 0),
            ],
            CommitKey("alf3ratz", "apetropavlovskij@yandex.ru"): [
                FileInfo('Dockerfile', 49, 25),
                FileInfo('README.md', 28, 25),
                FileInfo('__init__.py', 24, 16),
                FileInfo('ci.yml', 162, 290),
                FileInfo('dev-search-result.json', 1635, 1635),
                FileInfo('dev_search_result.json', 660329, 0),
                FileInfo('docker-push.yml', 188, 189),
                FileInfo('enry_processor.py', 16, 13),
                FileInfo('enry_test.py', 45, 108),
                FileInfo('git_processor.py', 12, 6),
                FileInfo('git_test.py', 83, 213),
                FileInfo('helpers.py', 75, 188),
                FileInfo('list_of_repositories.txt', 8, 3),
                FileInfo('main.py', 115, 51),
                FileInfo('qwerty.java', 33, 66),
                FileInfo('repository_url.txt', 3, 3),
                FileInfo('requirements.txt', 4, 2),
                FileInfo('setup.py', 50, 46),
                FileInfo('simple_test.py', 35, 15),
                FileInfo('star.json', 79, 0),
                FileInfo('start_app.mp4', 0, 0),
                FileInfo('treesitter.py', 161, 122),
                FileInfo('treesitter_cloner.py', 20, 0),
                FileInfo('treesitter_test.py', 57, 137),
            ]
        }

        check_two_programmers_info(self, programmers, info)

    def test_sorted_stat(self):
        info = sort_stat(find_info("tests/repos/2022_similar_dev_search_kononov"))
        stat = [
            (3221, CommitKey("Alex5041", "kononal@gmail.com")),
            (512, CommitKey("Lint Action", "lint-action@samuelmeuli.com")),
            (225, CommitKey("Alexey Kononov", "62846387+Alex5041@users.noreply.github.com")),
            (152, CommitKey("Egor", "egorbu@gmail.com")),
        ]
        self.assertEqual(info, stat)
