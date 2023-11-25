# Класс узла
class Node:
    def __init__(self, data, childs=None):
        self.data = data
        self.childs = childs or []

    def __str__(self):
        return str(self.data)


# Класс дерева
class Tree:
    def __init__(self):
        self.root = None

    # Поиск узла по содержимому, отдаёт узел
    def find_node(self, node, data):
        if node is None or node.data == data:
            return node
        for chile in node.childs:
            result = self.find_node(chile, data)
            if result:
                return result
        return None

    # Создание корня/добавление потомка, если указано содержимое родительского узла
    def add(self, new_data, parent_data=None):
        _node = Node(new_data)
        if parent_data is None:
            self.root = _node
        else:
            parent = self.find_node(self.root, parent_data)
            parent.childs.append(_node)

    # Вывод дерева (вспомогательный)
    def print_tree(self, node, output):
        if node is None:
            return ""
        output += str(node) + ' ['
        for i in range(len(node.childs)):  # Дальше понятно, почему через range
            chile = node.childs[i]
            end = ', ' if i < len(node.childs) - 1 else ''
            output = self.print_tree(chile, output) + end
        output += ']'
        return output.replace('[]', '')

    # Удалялка узлов (принимает корень и удаляемый узел)
    def purge(self, node, node2del):
        if node2del in node.childs:
            node.childs.remove(node2del)
            return
        for chile in node.childs:
            self.purge(chile, node2del)

    # Считаем количество узлов дерева (снаружи дергать через sizetree!)
    def tree_size(self, node, output):
        if node.data:
            output += 1
        for chile in node.childs:
            output = self.tree_size(chile, output)
        return output

    # Отдельная прокладка для передачи пустого output в print_tree
    def __str__(self):
        return self.print_tree(self.root, "")

    # Отдельная прокладка для простого подсчёта узлов в дереве
    def sizetree(self):
        print('Количество элементов в дереве: ', self.tree_size(self.root, 0))

    # Прокладка для поиска узла дерева по содержимому
    def find_by(self, data):
        return self.find_node(self.root, data)

    # Прокладка для удаления узла дерева (с потомками) по содержимому
    def del_by(self, data):
        self.purge(self.root, tree.find_by(data))


# #### ПРИМЕРЫ ### #
tree = Tree()  # Создаём дерево tree
tree.add('A')  # Корневой узел создаётся без указания родителя
tree.add('B', 'A')  # Остальные узлы задаются в формате (потомок, родитель)
tree.add('C', 'A')
tree.add('D', 'A')
tree.add('E', 'B')
tree.add('F', 'B')
tree.add('G', 'C')
tree.add('H', 'C')
tree.add('I', 'F')
tree.add('J', 'F')

print(tree)  # Выводит дерево в понятном формате
tree.sizetree()  # Выводит количество узлов в дереве
tree.del_by('C')  # Удаляет узел (с потомками) по его значению
print(tree)
