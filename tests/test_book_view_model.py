import unittest

from app import create_app
from app.spider.yushu_book import YuShuBook


class TestBookViewModel(unittest.TestCase):
    def setUp(self):
        app = create_app()
        app.app_context()
        app.app_context().push()

    def test_package_single(self):
        data = YuShuBook.search_by_keyword('shiro')
        from app.view_models.book import BookViewModel
        result = BookViewModel.package_collection(data, 'test')
        print(result)
