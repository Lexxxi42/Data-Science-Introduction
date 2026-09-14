import sys, os

class Research:
    def __init__(self, file_path):
        self.file_path = file_path
        
    def file_reader(self):
        f = self.file_path

        if not os.path.exists(f):
            raise FileNotFoundError("Этот файл не существует")
        
        with open (f, 'r') as file:
            content = file.readlines()
            if not content:
                raise ValueError("Файл пуст")
            
            for line in content:
                line = line.replace('\n','').split(',')
                if not ''.join(line).strip(): continue
                if len(line) != 2:
                    raise ValueError("Данные должны содержать лишь 2 значения в строке")
                
            for line in content[0]:
                header = content[0].replace('\n','').split(',')
                if header[0] != 'head' or header[1] != 'tail':
                    raise ValueError("Неверные данные заголовка")
            
            for line in content[1:]:
                line = line.replace('\n','').split(',')
                if not ''.join(line).strip(): continue

                if {line[0], line[1]} != {'0', '1'}:
                    raise ValueError("Данные должны содержать только 0 или 1")
                if line[1] == line[0]: 
                    raise ValueError("1 или 0 должны быть единственными в строке")
            
            return content
        
if __name__ == '__main__':
    if len(sys.argv) == 2:
        try:
            research = Research(sys.argv[1])
            print(*research.file_reader())
        except (ValueError, FileNotFoundError) as e:
            print(e)
    else:
        print("Введите существующий файл.\nПример ввода:\tpython3 first_constructor.py data.csv")