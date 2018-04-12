class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.author = '、'.join(book['author'])
        self.publisher = book['publisher']
        self.price = book['price']
        self.summary = book['summary'] or ''
        self.image = book['image']


class BookCollection:
    def __init__(self):
        self.total = 0
        self.keyword = ''
        self.books = []

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]


# class _BookViewModel:
#
#     @classmethod
#     def package_single(cls, data, keyword):
#         returned = {
#             'books': [],
#             'total': 0,
#             'keyword': {'isbn': keyword}
#         }
#         if data:
#             returned['books'] = [cls.__cut_book_data(data)]
#             returned['total'] = 1
#         return returned
#
#     @classmethod
#     def package_collection(cls, data, keyword):
#         returned = {
#             'books': [],
#             'total': 0,
#             'keyword': keyword
#         }
#         if data:
#             returned['total'] = data['total']
#             returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
#         return returned
#
#     @classmethod
#     def __cut_book_data(cls, data):
#         book = {
#             'title': data['title'],
#             'author': '、'.join(data['author']),
#             'publisher': data['publisher'],
#             'price': data['price'],
#             'summary': data['summary'] or '',
#             'image': data['image']
#         }
#         return book
