from analytics import Research
from config import *

def main():
    try:
        research = Research(data_file)
        data, count_lines = research.file_reader()

        count_head, count_tail = research.Analytics(data).counts()
        procent_head, procent_tail = research.Analytics.fractions(count_head, count_tail)

        forecasts = research.Analytics.predict_random(num_of_steps)

        predict_tail, predict_head = research.Analytics.fractions_of_predict(forecasts)

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

        research.Analytics(data).save_file(report, output_file)

    except (ValueError, FileNotFoundError) as e:
        print(e)

if __name__ == '__main__':
    main()