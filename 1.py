def outer(func):
    def inner():
        x=func()
        return x.upper()
    return inner
@outer
def wish():
    return 'hii good morning'
print(wish())