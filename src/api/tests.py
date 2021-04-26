from django.test import TestCase
from .utils.maze_utils import find_paths


class TestApi(TestCase):

    def test_find_paths(self):

        grid1 = ['--m', '-x-', '-p-']
        res1 = [['DOWN', 'DOWN', 'LEFT']]

        grid2 = ['---m', '----', '-x--', '-px-']
        res2 = [['DOWN', 'LEFT', 'LEFT', 'LEFT', 'DOWN', 'DOWN', 'RIGHT'],
                ['LEFT', 'DOWN', 'LEFT', 'LEFT', 'DOWN', 'DOWN', 'RIGHT'],
                ['LEFT', 'LEFT', 'DOWN', 'LEFT', 'DOWN', 'DOWN', 'RIGHT'],
                ['LEFT', 'LEFT', 'LEFT', 'DOWN', 'DOWN', 'DOWN', 'RIGHT']]

        grid3 = ['---m', '----', '--x-', '--px']
        res3 = [['DOWN', 'LEFT', 'LEFT', 'DOWN', 'DOWN', 'RIGHT'],
                ['LEFT', 'DOWN', 'LEFT', 'DOWN', 'DOWN', 'RIGHT'],
                ['LEFT', 'LEFT', 'DOWN', 'DOWN', 'DOWN', 'RIGHT']]

        self.assertEqual(find_paths(grid1, 3, (0, 2), (2, 1)), res1)
        self.assertEqual(find_paths(grid2, 4, (0, 3), (3, 1)), res2)
        self.assertEqual(find_paths(grid3, 4, (0, 3), (3, 2)), res3)


