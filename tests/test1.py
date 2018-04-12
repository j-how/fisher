from werkzeug.local import LocalStack

l = LocalStack()
l.push(42)
l.push(23)

l.pop()