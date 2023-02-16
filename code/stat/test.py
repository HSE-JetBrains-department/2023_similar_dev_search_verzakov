from pprint import pprint
from file_stat import findInfo
from file_info import FileInfo
from commit_key import CommitKey
import unittest

# pprint(findInfo("tests/repos/2022_similar_dev_search_petropavlovskiy"))

class CheckFindInfo(unittest.TestCase):
    
    def test_first_repo(self):
        info = findInfo("tests/repos/2022_similar_dev_search_skrypnikov")
        
        programmers = {}
        
        author1 = CommitKey("Egor", "egorbu@gmail.com")
        files1 = {}
        files1[".gitignore"] = FileInfo(152, 0)
        programmers[author1] = files1
        
        author2 = CommitKey("egor skrypnikov", "eskrypn@gmail.com")
        files2 = {
            '.gitignore': FileInfo(8, 3),
            'README.md': FileInfo(28, 0),
            '__init__.py': FileInfo(5,3),
            'analysis.py': FileInfo(344, 121),
            'build_enry.sh': FileInfo(29, 0),
            'classes.py': FileInfo(275, 45),
            'enry_scikit-learn.json':  FileInfo(1, 1),
            'enry_stage.py': FileInfo(15, 15),
            'repoparse.py': FileInfo(982, 562),
            'requirements.txt': FileInfo(10, 3),
            'shared.py': FileInfo(48, 48),
            'treesitter_stage.py': FileInfo(34, 34),
            'utils.py': FileInfo(120, 18),
        }
        programmers[author2] = files2
        
        self.assertEqual(len(info), len(programmers))
        
        for author in info.keys():
            self.assertEqual(len(info[author]), len(programmers[author]))
            
            for key in info[author].keys():
                self.assertEqual(info[author][key], programmers[author][key])
    
    def test_second_repo(self):
        info = findInfo("tests/repos/2022_similar_dev_search_kononov")
        
        programmers = {}
        
        author1 = CommitKey("Alexey Kononov", "62846387+Alex5041@users.noreply.github.com")
        files1 = {
            'README.md': FileInfo(49, 15),
            'main.py': FileInfo(138, 23),
        }
        programmers[author1] = files1
        
        author2 = CommitKey("Egor", "egorbu@gmail.com")
        files2 = {
            '.gitignore': FileInfo(152, 0),
        }
        programmers[author2] = files2
        
        author3 = CommitKey("Alex5041", "kononal@gmail.com")
        files3 = {
            '.gitignore': FileInfo(1, 0),
            'README.md': FileInfo(141, 12),
            '__init__.py': FileInfo(0, 0),
            'dev_stats.py': FileInfo(300, 130),
            'enry.py': FileInfo(122, 126),
            'extract.py': FileInfo(318, 294),
            'globals.py': FileInfo(28, 28),
            'lint.yml': FileInfo(42, 2),
            'make_stats.py': FileInfo(46, 1),
            'parsefile.py': FileInfo(112, 0),
            'pipeline.py': FileInfo(111, 111),
            'script.py': FileInfo(183, 74),
            'search.py': FileInfo(81, 25),
            'setup.py': FileInfo(27, 3),
            'stargazers.json': FileInfo(104, 101),
            'stargazers.py': FileInfo(124, 36),
            'test.py': FileInfo(39, 26),
            'test_dev_stats.py': FileInfo(27, 27),
            'tree-sitter.py': FileInfo(37, 37),
            'treesitter.py': FileInfo(117, 117),
            'utils.py': FileInfo(101, 10),
        }
        programmers[author3] = files3
        
        author4 = CommitKey("Lint Action", "lint-action@samuelmeuli.com")
        files4 = {
            'dev_stats.py': FileInfo(59, 33),
            'extract.py': FileInfo(46, 31),
            'make_stats.py': FileInfo(6, 4),
            'parsefile.py': FileInfo(46, 20),
            'script.py': FileInfo(112, 47),
            'search.py': FileInfo(28, 16),
            'setup.py': FileInfo(8, 3),
            'stargazers.py': FileInfo(12, 8),
            'test.py': FileInfo(17, 4),
            'utils.py': FileInfo(8, 4),
        }
        programmers[author4] = files4
        
        self.assertEqual(len(info), len(programmers))
        
        for author in info.keys():
            self.assertEqual(len(info[author]), len(programmers[author]))
            
            for key in info[author].keys():
                self.assertEqual(info[author][key], programmers[author][key])
    
    def test_third_repo(self):
        
        info = findInfo("tests/repos/2022_similar_dev_search_petropavlovskiy")
        
        programmers = {}
        
        author1 = CommitKey("Egor", "egorbu@gmail.com")
        files1 = {
            '.gitignore': FileInfo(152, 0),
        }
        programmers[author1] = files1
        
        author2 = CommitKey("alf3ratz", "49417479+alf3ratz@users.noreply.github.com")
        files2 = {
            '.gitignore': FileInfo(2, 0),
            'Dockerfile': FileInfo(8, 8),
            'README.md': FileInfo(36, 3),
            'action.yml': FileInfo(16, 16),
            'ci.yml': FileInfo(106, 108),
            'enry_processor.py': FileInfo(29, 0),
            'entrypoint.sh': FileInfo(5, 5),
            'git_processor.py': FileInfo(59, 13),
            'git_test.py': FileInfo(11, 11),
            'helpers.py': FileInfo(176, 38),
            'main.py': FileInfo(46, 25),
            'preview.png': FileInfo(0, 0),
            'requirements.txt': FileInfo(23, 15),
            'setup.py': FileInfo(23, 10),
            'treesitter.py': FileInfo(48, 0),
        }
        programmers[author2] = files2
        
        author3 = CommitKey("alf3ratz", "apetropavlovskij@yandex.ru")
        files3 = {
            'Dockerfile': FileInfo(49, 25),
            'README.md': FileInfo(28, 25),
            '__init__.py': FileInfo(24, 16),
            'ci.yml': FileInfo(162, 290),
            'dev-search-result.json': FileInfo(1635, 1635),
            'dev_search_result.json': FileInfo(660329, 0),
            'docker-push.yml': FileInfo(188, 189),
            'enry_processor.py': FileInfo(16, 13),
            'enry_test.py': FileInfo(45, 108),
            'git_processor.py': FileInfo(12, 6),
            'git_test.py': FileInfo(83, 213),
            'helpers.py': FileInfo(75, 188),
            'list_of_repositories.txt': FileInfo(8, 3),
            'main.py': FileInfo(115, 51),
            'qwerty.java': FileInfo(33, 66),
            'repository_url.txt': FileInfo(3, 3),
            'requirements.txt': FileInfo(4, 2),
            'setup.py': FileInfo(50, 46),
            'simple_test.py': FileInfo(35, 15),
            'star.json': FileInfo(79, 0),
            'start_app.mp4': FileInfo(0, 0),
            'treesitter.py': FileInfo(161, 122),
            'treesitter_cloner.py': FileInfo(20, 0),
            'treesitter_test.py': FileInfo(57, 137),
        }
        programmers[author3] = files3
        
        self.assertEqual(len(info), len(programmers))
        
        for author in info.keys():
            self.assertEqual(len(info[author]), len(programmers[author]))
            
            for key in info[author].keys():
                self.assertEqual(info[author][key], programmers[author][key])
    
if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
