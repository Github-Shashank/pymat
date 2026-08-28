def check_matrix(m):
    n = len(m[0])
    for i in m:
        if len(i) != n :
            return i
    else:
        return True


def is_equal_order(self, other):
    return self.order == other.order


def is_valid_index(self, index):
    if not len(index) == 2:
        return False

    r, c = index
    rows, cols = self.order

    return 0 <= r < rows and 0 <= c < cols


def is_multiplicable(self, other):
    if self.order[1] == other.order[0]:
        return True
    else:
        return False