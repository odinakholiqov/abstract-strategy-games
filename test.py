class FileActions:
    def __init__(self, name: str):
        self.sheet = {}
        self.file_name = name
        with open(name, encoding='utf-8') as file:
            for line in file:
                key, value = line.split('-')
                self.sheet[key.strip()] = float(value)

    def add(self):
        name = input('Введите название продукта:')
        price = input('Введите цену продукта:')
        self.sheet[name] = float(price)
        self._commit()
        print(f'Продукт добавлен: {name} - {price}')

    def change(self):
        name = self._get_existing_name()
        if name:
            price = input('Введите цену продукта:')
            self.sheet[name] = float(price)
            self._commit()
            print(f'Продукт изменен: {name} - {price}')

    def delete(self):
        name = self._get_existing_name()
        if name:
            del self.sheet[name]
            self._commit()
            print(f'Продукт удален: {name}')

    def total(self):
        result = sum(list(self.sheet.values()))
        print(f'Сумма = {result}')

    def _commit(self):
        with open(self.file_name, 'wt', encoding='utf-8') as file:
            for key, value in self.sheet.items():
                file.write(f'{key} - {value}\n')

    def _get_existing_name(self):
        while True:
            name = input('Введите название продукта ("Enter" для отмены):')
            if not name:
                return ''
            if name not in self.sheet:
                print(f'Нет такого продукта! Имеются: {tuple(self.sheet.keys())}')
                continue
            return name


if __name__ == '__main__':
    file_actions = FileActions('vegetables.txt')
    actions = {'Добавить': file_actions.add, 'Изменить': file_actions.change, 'Удалить': file_actions.delete,
               'Сумма': file_actions.total}
    while True:
        separator_length = len(str(file_actions.sheet)) + 8
        print('=' * separator_length)
        print(f'Товары: {file_actions.sheet}')
        action = input(f'Введите действие {tuple(actions.keys())}, нажмитe "Enter" для выхода":')
        if not action:
            break
        if action not in actions:
            continue
        actions[action]()