from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        return None

    def search(self, index):
        if index < 0 or index >= len(self.items):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.items[index]
