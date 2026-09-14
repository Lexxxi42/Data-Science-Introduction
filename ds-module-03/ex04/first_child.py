import sys, os
from random import randint

class Research:
    def __init__(self, file_path):
        self.file_path = file_path
# Чтение из файла и вывод содержимого 
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
            for line in data:
                line = line.strip()
                if not line: continue
                value = line.split(',')

                if len(value) != 2 or not value[0] or not value[1]:
                    raise ValueError("Данные должны содержать лишь 2 значения в строке")

                if {value[0], value[1]} != {'0', '1'}:
                    raise ValueError("Данные должны содержать только 0 или 1")
                
                if value[1] == value[0]: 
                    raise ValueError("1 или 0 должны быть единственными в строке")
                
                result.append([int(value[0]), int(value[1])])

            return result
        
# подсчет кол-ва орлов и решек и их процентного соотношения
    class Calculations:

        def __init__(self, data):
            self.data = data

        def counts(self):
            count_head = sum(row[0] for row in self.data)
            count_tail = sum(row[1] for row in self.data)
            return count_head, count_tail
        
        def fractions(count_head, count_tail):
            total = count_head + count_tail
            procent_head = (count_head / total) * 100
            procent_tail = (count_tail / total) * 100
            return procent_head, procent_tail
        
# прогнозы выпада орла и решки, вывод последней строки файла
    class Analytics(Calculations):
        @staticmethod
        def predict_random(number_forecasts = 3):
            forecasts = []
            for i in range(number_forecasts):
                first = randint(0,1)
                forecasts.append([first, 1 - first])
            return forecasts
            
        def predict_last(self):
            return self.data[-1]

if __name__ == '__main__':
    if len(sys.argv) == 2:
        try:
            research = Research(sys.argv[1])
            data = research.file_reader()

            Calculations = research.Calculations(data)
            count_head, count_tail = Calculations.counts()
            procent_head, procent_tail = research.Calculations.fractions(count_head, count_tail)

            Analytics = research.Analytics(data)
            forecasts = research.Analytics.predict_random()
            predict_last = Analytics.predict_last()

            print(data)
            print(count_head, count_tail)
            print(procent_head, procent_tail)
            print(forecasts)
            print(predict_last)


        except (ValueError, FileNotFoundError) as e:
            print(e)
    else:
        print("Введите существующий файл.\nПример ввода:\tpython3 first_constructor.py data.csv")