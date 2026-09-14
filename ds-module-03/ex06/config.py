# type: ignore
import os
from random import randint
import logging
import requests

data_file = "data.csv"
output_file = "report"
num_of_steps = 3
text = """Report.

We have made {} observations from tossing a coin:
{} of them were tails and {} of them were heads.
The probabilities are {:.2f}% and {:.2f}%, respectively.

Our forecast is that in the next {} observations we will have:
{} tail and {} heads.
"""
logging.basicConfig(level=logging.DEBUG, filename="analytics.log", filemode="a", format="%(asctime)s %(levelname)s %(message)s" )

""" Туториал как запустить бота и найти токен и id
1. Зайти в @BotFather
2. /start
3. /newbot
4. Придумать уникальное имя бота
5. под HTTP API будет токен
6. Зайти в @getmyid_bot
7. current chat ID = chat_id

COMPLETE!
"""
url = "https://api.telegram.org/bot"
token = ""
chat_id = ""

succsess_report = "The report has been successfully created"
failed_report = "The report hasn’t been created due to an error"