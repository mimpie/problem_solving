class Item:
    def __init__(self, weight: int, price: int):
        self.__weight = weight
        self.__price = price

    def get_weight(self):
        return self.__weight

    def get_price(self):
        return self.__price


class Bag:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__items = set()
        self.__total_weight = 0
        self.__total_price = 0

    def get_total_price(self):
        return self.__total_price

    def get_remain_capacity(self):
        return self.__capacity - self.__total_weight

    def put_item(self, item: Item):
        self.__items.add(item)
        self.__total_weight += item.get_weight()
        self.__total_price += item.get_price()

    def pop_item(self, item: Item):
        self.__items.remove(item)
        self.__total_weight -= item.get_weight()
        self.__total_price -= item.get_price()

    def can_put_item(self, item: Item):
        return item.get_weight() <= self.get_remain_capacity()


class Case:
    def __init__(self, bag: Bag, items: list):
        self.__bag = bag
        self.__items = items

    def get_max_price(self):
        return self.__find_max_price(self.__items)

    def __find_max_price(self, remain_items: list):
        if not remain_items:
            return self.__bag.get_total_price()
        if self.__bag.can_put_item(remain_items[0]):
            return max(self.__find_max_price_with_current_item(remain_items),
                       self.__find_max_price_without_current_item(remain_items))
        else:
            return self.__find_max_price_without_current_item(remain_items)

    def __find_max_price_with_current_item(self, remain_items: list):
        self.__bag.put_item(remain_items[0])
        result = self.__find_max_price(remain_items[1:])
        self.__bag.pop_item(remain_items[0])
        return result

    def __find_max_price_without_current_item(self, remain_items: list):
        return self.__find_max_price(remain_items[1:])


class FileInput:
    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__cases = []
        self.__deserialize()

    def __deserialize(self):
        with open(self.__file_name, 'r') as f:
            lines = f.readlines()

        i = 0
        while i < len(lines):
            number_of_items = int(lines[i])
            bag_capacity = int(lines[i + 1])
            item_weights = list(map(int, lines[i + 2].split()))
            item_prices = list(map(int, lines[i + 3].split()))
            items = [Item(item_weights[j], item_prices[j]) for j in range(number_of_items)]
            case = Case(Bag(bag_capacity), items)
            self.__cases.append(case)
            i += 5

    def get_cases(self):
        return self.__cases


cases = FileInput("./input.txt").get_cases()
for case in cases:
    print(case.get_max_price())
