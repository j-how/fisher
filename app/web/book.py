from flask import jsonify, request

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web


@web.route('/book/search')
def search():
    """

    :param p: 关键字 isbn
    :param page: 页数
    :return:
    """
    form = SearchForm(request.args)
    if form.validate():
        p = form.p.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(p)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(p)
        else:
            result = YuShuBook.search_by_keyword(p)
        return jsonify(result)
    else:
        return jsonify(form.errors)
