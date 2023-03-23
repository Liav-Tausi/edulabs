class LinkedIn:
    def __init__(self):
        self.__db: dict = dict()

    @property
    def db(self):
        return self.__db

    def _validate_data(self, *args):
        for arg in args:
            if arg not in self.db:
                raise Exception('not in db')

    def add_member(self, name):
        self.db[name] = dict()
        return self.db

    def add_friendship(self, name1, name2):
        self._validate_data(name1, name2)
        self.db[name1][name2] = dict()

    def is_friend_of_friend(self, name1, name2) -> bool:
        self._validate_data(name1, name2)
        for friend_of in self.db[name1]:
            for friend in self.db[friend_of]:
                if friend == name2:
                    return True
                else:
                    return False

    def dfs(self, from_node, to_node, _len=None) -> bool:
        return self._dfs_rec(from_node, to_node, set(), list(), _len)

    def _dfs_rec(self, from_node, to_node, visited, path, _len) -> bool or int:

        if from_node == to_node:
            return True

        path.append(from_node)
        visited.add(from_node)
        for node in self.db[from_node]:
            if node not in visited:
                if self._dfs_rec(node, to_node, visited, path, _len):
                    if _len:
                        return len(path)
                    else:
                        return path
        return False


if __name__ == '__main__':
    linked_in = LinkedIn()
    linked_in.add_member('David')
    linked_in.add_member('James')
    linked_in.add_member('Ron')
    linked_in.add_member('Julia')
    linked_in.add_member('Mor')
    linked_in.add_member('Nathan')
    linked_in.add_member('Jim')
    linked_in.add_member('Dor')
    linked_in.add_member('James')

    linked_in.add_friendship('David', 'James')
    linked_in.add_friendship('James', 'Jim')
    linked_in.add_friendship('Jim', 'Mor')
    linked_in.add_friendship('Jim', 'Dor')
    linked_in.add_friendship('Mor', 'Julia')
    linked_in.add_friendship('Mor', 'Nathan')
    linked_in.add_friendship('Julia', 'Ron')

    # print(linked_in.is_friend_of_friend('David', 'Jim'))

    print(linked_in.dfs('David', 'Nathan'))
