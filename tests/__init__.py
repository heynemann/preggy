# -*- coding: utf-8 -*-


class Comparable(object):

    def __init__(self, foo='bar'):
        self.foo = foo

    def __hash__(self):
        return hash(self.foo)

    def __lt__(self, other):
        return self.foo < other.foo

    def __le__(self, other):
        return self.foo <= other.foo

    def __eq__(self, other):
        return self.foo == other.foo

    def __ne__(self, other):
        return self.foo != other.foo

    def __gt__(self, other):
        return self.foo > other.foo

    def __ge__(self, other):
        return self.foo >= other.foo

    def __cmp__(self, other):
        return cmp(self.foo, other.foo)


class AnotherComparable(object):

    def __init__(self, baz='qux'):
        self.baz = baz

    def __hash__(self):
        return hash(self.baz)

    def __lt__(self, other):
        return self.baz < other.baz

    def __le__(self, other):
        return self.baz <= other.baz

    def __eq__(self, other):
        return self.baz == other.baz

    def __ne__(self, other):
        return self.baz != other.baz

    def __gt__(self, other):
        return self.baz > other.baz

    def __ge__(self, other):
        return self.baz >= other.baz

    def __cmp__(self, other):
        return cmp(self.baz, other.baz)


class Containable(object):

    def __init__(self, foo='bar'):
        self.foo = foo

    def __contains__(self, other):
        return self.foo == other