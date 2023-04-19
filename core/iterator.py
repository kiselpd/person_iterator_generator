class FlatIterator:

    def __init__(self, list_of_list):
        self._list_of_list = list_of_list


    def __iter__(self):
        self._tmp_list_item = 0
        self._tmp_item = 0

        while self._tmp_list_item < len(self._list_of_list):
            if not self._list_of_list[self._tmp_list_item]:
                self._tmp_list_item += 1
            else:
                break
            
        return self


    def __next__(self):
        if self._tmp_list_item == len(self._list_of_list):
            raise StopIteration

        if self._tmp_item == len(self._list_of_list[self._tmp_list_item]):
            self._tmp_list_item += 1
            self._tmp_item = 0
            tmp_item = self.__next__()
        else:
            tmp_item = self._list_of_list[self._tmp_list_item][self._tmp_item]
            self._tmp_item += 1

        return tmp_item
    

def flat_generator(list_of_lists):

    ...
    yield
    ...    