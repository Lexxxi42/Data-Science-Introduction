import sys, os

class Research:
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
        
    class Calculations:
        def counts(data):
            count_head = sum(row[0] for row in data)
            count_tail = sum(row[1] for row in data)
            return count_head, count_tail
        
        def fractions(count_head, count_tail):
            total = count_head + count_tail
            procent_head = (count_head / total) * 100
            procent_tail = (count_tail / total) * 100
            return procent_head, procent_tail
        
if __name__ == '__main__':
    if len(sys.argv) == 2:
        try:
            research = Research(sys.argv[1])
            data = research.file_reader()
            count_head, count_tail = research.Calculations.counts(data)
            procent_head, procent_tail = research.Calculations.fractions(count_head, count_tail)

            print(data)
            print(count_head, count_tail)
            print(procent_head, procent_tail)

        except (ValueError, FileNotFoundError) as e:
            print(e)
    else:
        print("Введите существующий файл.\nПример ввода:\tpython3 first_constructor.py data.csv")