from analytics import Research
from config import *
logging.basicConfig(level=logging.DEBUG, filename="analytics.log", filemode="a", format="%(asctime)s %(levelname)s %(message)s" )

def main():
    Analytics = None
    try:
        research = Research(data_file)
        data, count_lines = research.file_reader()
        Analytics = research.Analytics(data)

        count_head, count_tail = Analytics.counts()
        procent_head, procent_tail = research.Analytics.fractions(count_head, count_tail)

        forecasts = research.Analytics.predict_random(num_of_steps)

        predict_tail = sum(row[0] for row in forecasts)
        predict_head = sum(row[1] for row in forecasts)

        report = text.format(
            count_lines,
            count_tail,
            count_head,
            procent_tail,
            procent_head,
            num_of_steps,
            predict_tail,
            predict_head
        )

        Analytics.save_file(report, output_file)
        Analytics.telebot(url, token, chat_id, succsess_report)
    except (ValueError, FileNotFoundError) as e:
        logging.error(e)
        requests.post(f"{url}{token}/sendMessage?chat_id={chat_id}&text={failed_report}")
        print(e)


if __name__ == '__main__':
    main()