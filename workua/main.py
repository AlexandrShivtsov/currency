import csv
import json
import sqlite3
from random import randint
from time import sleep

from bs4 import BeautifulSoup

from fake_useragent import UserAgent

import requests


def sleep_fanc():
    sleep(randint(1, 2))


def write_to_json(jobs_id, title, salary, description_job):
    jobs_info = {
            'jobs_id': jobs_id,
            'title': title,
            'salary': salary,
            'description_job': description_job,
      }
    with open('jobs.json', 'a', encoding='utf8') as JSON_file:
        json.dump(jobs_info, JSON_file, indent=3)


def write_to_db(job_id, title_job, salary, description_job):
    conn = sqlite3.connect('work_ua.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS jobs_on_work_ua(
                           jobs_id TEXT,
                           title_job TEXT,
                           salary TEXT,
                           description_job TEXT);
                        """)

    cur.execute("""INSERT INTO jobs_on_work_ua(jobs_id, title_job, salary, description_job)
                           VALUES(?, ?, ?, ?)""", (job_id, title_job, salary, description_job))
    conn.commit()


BASE_URL = 'https://www.work.ua/jobs/'
page = 0

with open('jobs.csv', 'w', encoding='UTF8') as CSV_file:
    writer = csv.writer(CSV_file)
    writer.writerow(('jobs_id', 'title', 'salary', 'description_job'))

    while True:
        page += 1
        params = {
              'pages': page
        }
        ua = UserAgent()
        headers = {
              'User-Agent': ua.random,
        }
        sleep_fanc()
        response = requests.get(BASE_URL, params=params, headers=headers)

        html = response.text
        supe = BeautifulSoup(html, 'html.parser')
        job_list = supe.find('div', {'id': 'pjax-job-list'})
        if job_list is None:
            break
        cards = job_list.findAll('div', {'class': 'card card-hover card-visited wordwrap job-link js-hot-block'})

        for card in cards:
            link = card.find('a')
            href = link['href']
            title_job = link.text
            job_id = href.split('/')[-2]

            response_detile = requests.get(f'{BASE_URL}/{job_id}', headers=headers)
            html_detile = response_detile.text
            supe_detile = BeautifulSoup(html_detile, 'html.parser')

            try:
                salary = supe_detile.find('b', {'class': 'text-black'}).text
            except Exception:
                salary = 'Заработная плата не указана'

            description_job = supe_detile.find('div', {'id': 'job-description'}).find('p').text

            writer.writerow((job_id, title_job, salary, description_job))
            write_to_json(job_id, title_job, salary, description_job)
            write_to_db(job_id, title_job, salary, description_job)
