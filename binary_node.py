import random
import time
import json
from datetime import datetime


class Binary_node(object):

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Binary_node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Binary_node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data
        else:
            self.data = data


    def remove(self, data):
        parent = None
        node = self.data
        while node and node.data != data:
            parent = node
            if node.data > data:
                node = node.left
            elif self.data < data:
                node = node.right

        if node is None or node.data != data:
            return "Элемент не найден"

        # У удаляемого узла нет детей
        elif node.left is None and node.right is None:
            if parent.data > data:
                parent.left = None
            else:
                parent.right = None
            return True

        # У удаляемого узла есть только левый ребенок
        elif node.left and node.right is None:
			if parent.data > data:
				parent.left = node.left
			else:
				parent.right = node.left
			return True

        # 3-й случай. У удаляемого узла есть только правый ребенок	
        elif node.left is None and node.right:
			if parent.data > data:
				parent.left = node.right
			else:
				parent.right = node.right
			return True

        # 4-й случай. У удаляемого узла есть оба потомка
        else:
			del_node_parent = node
			del_node = node.right
            # Находим самый левый узел у правого потомка
			while del_node.left:
				del_node_parent = del_node
				del_node = del_node.left
				
			node.data = del_node.data
            # Если у самого левого узла есть правай потомок
			if del_node.right:
                # Перезаписываем 
				if del_node_parent.data > del_node.data:
					del_node_parent.left = del_node.right
				elif del_node_parent.data < del_node.data:
					del_node_parent.right = del_node.right
			else:
				if del_node.data < del_node_parent.data:
					del_node_parent.left = None
				else:
					del_node_parent.right = None


    def finding_height(self):
        return 1 + max(self.left.finding_height() if self.left is not None else 0, 
                       self.right.finding_height() if self.right is not None else 0)

    
    def search(self, my_elem):
        if self.data == my_elem:
            return True
        elif self.data > my_elem:
            if self.left is None:
                return False
            else:
                my_bool = self.left.search(my_elem)
        else:
            if self.right is None:
                return False
            else:
                my_bool = self.right.search(my_elem)
        return my_bool
        


    def print_tree_dict(self):
        if self.left:
            elem1 = self.left.print_tree_dict()
        # print(self.data)
        if self.right:
            elem2 = self.right.print_tree_dict()

        if self.right is None and self.left is None:
            return self.data
        elif self.right is not None and self.left is not None:
            return {self.data: [elem1, elem2]}
        elif self.right is None and self.left is not None:
            return {self.data: elem1}
        else:
            return {self.data: elem2}


def main():
    # count = None
    # while count is None:
    #     try:
    #         count = int(input('Введите колличество элементов: '))
    #     except ValueError as e:
    #         print(e)
    count = 10000000
    for i in range(8):

        start = time.time() #datetime.now()

        my_tree = Binary_node(random.randint(2500, 7500))

        for i in range(count):
            elem = random.randint(1, 10000)
            my_tree.insert(elem)

        end = time.time() #datetime.now()

        result = end - start
        print('Время создания дерева: {}'.format(result))
    
    # Распечатка дерева в вложенный словарь
    # tree_dict = my_tree.print_tree_dict()

    # # Запись в json файл
    # json_tree = json.dumps(tree_dict) 
    # with open('data.json', mode='w') as f:
    #     f.write(json_tree)


def test():
    my_list = [7, 23, 2, 4, 8, 12]
    tree = Binary_node(12)
    for i in my_list:
        tree.insert(i)

    tree.print_tree_dict()

    if tree.search(8):
        print('Тест на проверку наличия узла пройден') 
    else:
        print('Тест на проверку наличия узла не пройден') 

    # tree.remove(5)
    if not tree.search(5):
        print('Тест на проверку удаления узла пройден') 
    else:
        print('Тест на проверку удаления узла не пройден') 



if __name__ == '__main__':
    test()

