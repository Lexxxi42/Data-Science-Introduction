# Запуск скрипта python3 first_nest.py data.csv
from config import *

class Research:
    def __init__(self, file_path):
        self.file_path = file_path

# Чтение из файла и вывод содержимого 
    def file_reader(self, has_header = True):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"{self.file_path} не существует")
        logging.info(f"Получен путь к файлу {self.file_path}")
        
        with open (self.file_path, 'r') as file:
            content = file.readlines()
            if not content:
                raise ValueError("Файл пуст")
            logging.info(f"Файл {self.file_path} прочитан")

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
            logging.info(f"Файл {self.file_path} успешно обработан")
            return result, count_lines
        
# подсчет кол-ва орлов и решек и их процентного соотношения
    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self):
            count_head = sum(row[0] for row in self.data)
            count_tail = sum(row[1] for row in self.data)
            logging.info(f"head = {count_head}; tail = {count_tail}")
            return count_head, count_tail
        
        def fractions(count_head, count_tail):
            total = count_head + count_tail
            procent_head = (count_head / total) * 100
            procent_tail = (count_tail / total) * 100
            logging.info(f"Найдено процентное соотношение head-tail: {procent_head :.2f}% - {procent_tail :.2f}%")
            return procent_head, procent_tail
        
# прогнозы выпада орла и решки, вывод последней строки файла
    class Analytics(Calculations):
        @staticmethod
        def predict_random(num_of_steps = 3):
            forecasts = []
            for i in range(num_of_steps):
                first = randint(0,1)
                forecasts.append([first, 1 - first])
            logging.info(f"Предсказания рассчитаны: {forecasts}")
            return forecasts
            
        def predict_last(self):
            logging.info(f"Обнаружена последняя строка файла: {self.data[-1]}")
            return self.data[-1]
        
        def save_file(self, report, output_file = 'save', extension = 'txt'):
            filepath = f"{output_file}.{extension}"
            with open(filepath, 'w') as file:
                file.write(report)
            logging.info(f"Информация записана в файл {filepath}")

        def telebot(self, url, token, chat_id, message):
            result_of_request = requests.post(f"{url}{token}/sendMessage?chat_id={chat_id}&text={message}")
            if result_of_request.status_code == 200:
                logging.info(f"Сообщение \"{message}\" отправлено в Telegram")
            else:
                logging.warning(f"Не удалось отправить сообщение \"{message}\". Status code: {result_of_request.status_code}")
