import json

from flask import request, flash, render_template

from app import cache
from app.forms.book import SearchForm
from app.libs.cache import cache_key
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookCollection
from . import web


@web.route('/book/search')
@cache.cached(timeout=300, key_prefix=cache_key)
def search():
    """
    搜索接口
    :param p: 关键字 isbn
    :param page: 页数
    :return: 根据isbn或者关键字返回相应字段
    """
    form = SearchForm(request.args)
    books = BookCollection()
    if form.validate():
        p = form.p.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(p)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(p)
        else:
            yushu_book.search_by_keyword(p, page)

        books.fill(yushu_book, p)
        # return json.dumps(books, default=lambda o: o.__dict__)
        # return jsonify(books)
    else:
        flash('请重新输入关键字')
        # return jsonify(form.errors)

    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    pass
