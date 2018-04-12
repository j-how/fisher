from flask import current_app, jsonify

from app import cache
from app.libs.httper import HTTP


class YuShuBook:

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        """
        通过isbn搜索
        :param isbn:
        :return: 单个书籍
        """
        url = current_app.config['ISBN_URL'].format(isbn)
        result = HTTP.get(url)
        self.__fill_single(result)
        return jsonify(self.books)

    def search_by_keyword(self, keyword, page=1):
        """
        通过关键字搜索
        :param keyword: 关键字
        :param page: 从第几页开始 默认1
        :return: 可能为多个书籍
        """
        url = current_app.config['KEYWORD_URL'].format(keyword, current_app.config['PER_PAGE'],
                                                       self.calculate_start(page))
        result = HTTP.get(url)
        self.__fill_collection(result)

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        if data:
            self.total = data['total']
            self.books = data['books']
