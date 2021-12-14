class Item:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def set_next(self, item):
        self.next = item

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data


class CustomList:
    def __init__(self, *data):
        self.size = len(data)

        if self.size == 0:
            self.head = Item()
        else:
            self.head = Item(data[0])
            cur_item = self.head

            for value in data[1:]:
                new_item = Item(value)
                cur_item.set_next(new_item)
                cur_item = new_item

    def append(self, value):
        if self.head.get_data() is None:
            self.head.set_data(value)
        else:
            new_item = Item(value)
            cur_item = self.head

            while cur_item.get_next():
                cur_item = cur_item.get_next()

            cur_item.set_next(new_item)

        self.size += 1

    def add_start(self, value):
        if self.head.get_data() is None:
            self.head.set_data(value)
        else:
            new_item = Item(value)
            new_item.set_next(self.head)
            self.head = new_item

        self.size += 1

    def remove(self, value):
        cur_item = self.head

        while cur_item.get_next():
            if cur_item.get_next().get_data() == value:
                cur_item.set_next(cur_item.get_next().get_next())
                self.size -= 1
                break

            cur_item = cur_item.get_next()
        else:
            raise ValueError

    def __getitem__(self, index):
        if self.size <= index:
            raise IndexError

        cur_item = self.head
        while index != 0:
            cur_item = cur_item.get_next()
            index -= 1

        return cur_item.get_data()

    def __setitem__(self, index, data):
        if self.size <= index:
            raise IndexError

        cur_item = self.head
        while index != 0:
            cur_item = cur_item.get_next()
            index -= 1

        cur_item.set_data(data)

    def __delitem__(self, index):
        if self.size <= index:
            raise IndexError

        if index == 0:
            if self.head.get_next() is None:
                self.head = Item()
            else:
                self.head = self.head.get_next()
        else:
            cur_item = self.head
            while index != 1:
                cur_item = cur_item.get_next()
                index -= 1

            cur_item.set_next(cur_item.get_next().get_next())

        self.size -= 1

    def find(self, value):
        cur_item = self.head

        for i in range(self.size):
            if cur_item.get_data() == value:
                return i

            cur_item = cur_item.get_next()

        raise ValueError

    def clear(self):
        self.head = Item()
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        self.cur = self.head
        return self

    def __next__(self):
        if self.cur is None or self.cur.get_data() is None:
            raise StopIteration
        result = self.cur.get_data()
        self.cur = self.cur.get_next()
        return result

    def __str__(self):
        elms = []
        cur_item = self.head
        for _ in range(self.size):
            elms.append(str(cur_item.get_data()))
            cur_item = cur_item.get_next()

        return '; '.join(elms)