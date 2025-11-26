import unittest
from img_transfer import find_md_img


class MyTestCase(unittest.TestCase):
    def test_find_md_img(self, ):
        # self.assertEqual(True, False)  # add assertion here
        md_path = '/home/shaneshi/Documents/Notes/daily_notes/markdown上传博客园.md'
        with open(md_path, encoding='utf-8') as f:
            md = f.read()
            self.assertEqual(find_md_img(md), [])


if __name__ == '__main__':
    unittest.main()
