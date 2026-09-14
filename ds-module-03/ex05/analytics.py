import os
from random import randint

class Research:
    """
    Чтение из файла и вывод содержимого
    """
    def __init__(self, file_path):
        self.file_path = file_path
    def file_reader(self, has_header = True):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"{self.file_path} не существует")

        with open (self.file_path, 'r') as file:
            content = file.readlines()
            if not content:
                raise ValueError("Файл пуст")
            
            if has_header:
                header = content[0].replace('\n','').split(',')
                if len(header) != 2 or header[0] != 'head' or header[1] != 'tail':
                    raise ValueError("Неверные данные заголовка") 
                data = content[1:]
            else:
                data = content

            result = []
            count_lines = 0
            for line in data:
                line = line.strip()
                if not line: continue
                value = line.split(',')
                count_lines += 1

                if len(value) != 2 or not value[0] or not value[1]:
                    raise ValueError("Данные должны содержать лишь 2 значения в строке")

                if {value[0], value[1]} != {'0', '1'}:
                    raise ValueError("Данные должны содержать только 0 или 1")
                
                if value[1] == value[0]: 
                    raise ValueError("1 или 0 должны быть единственными в строке")
                
                result.append([int(value[0]), int(value[1])])

            return result, count_lines
        
    class Calculations:
        """
        Подсчет кол-ва орлов и решек и их процентного соотношения
        """
        def __init__(self, data):
            self.data = data

        def counts(self):
            count_head = sum(row[0] for row in self.data)
            count_tail = sum(row[1] for row in self.data)
            return count_head, count_tail
        @staticmethod
        def fractions(count_head, count_tail):
            total = count_head + count_tail
            procent_head = (count_head / total) * 100
            procent_tail = (count_tail / total) * 100
            return procent_head, procent_tail
        
    class Analytics(Calculations):
        """
        Класс для прогноза выпада орла и решки, вывод последней строки файла
        """
        @staticmethod
        def predict_random(num_of_steps = 3):
            forecasts = []
            for i in range(num_of_steps):
                first = randint(0,1)
                forecasts.append([first, 1 - first])
            return forecasts
            
        def predict_last(self):
            return self.data[-1]
        
        def save_file(self, report, output_file = 'save', extension = 'txt'):
            filepath = f"{output_file}.{extension}"
            with open(filepath, 'w') as file:
                file.write(report)
        @staticmethod
        def fractions_of_predict(forecasts):
            predict_tail = sum(row[0] for row in forecasts)
            predict_head = sum(row[1] for row in forecasts)
            return predict_tail, predict_head