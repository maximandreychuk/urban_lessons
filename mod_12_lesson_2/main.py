import requests as rq
import logging


def setup_logger(name, log_file, level=logging.INFO):

    handler = logging.FileHandler(log_file, 'w', 'utf-8')
    handler.setFormatter(logging.Formatter(
        '%(levelname)s: %(message)s'))

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


log_1 = setup_logger('RequestsLogger_1', 'success_responses.log')
log_2 = setup_logger('RequestsLogger_2',
                     'bad_responses.log', level=logging.WARNING)
log_3 = setup_logger('RequestsLogger_3',
                     'blocked_responses.log', level=logging.ERROR)


sites = ['https://www.youtube.com/', 'https://www.instagram.com/', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

for site in sites:
    try:
        response = rq.get(site, timeout=3)
        if response.status_code == 200:
            log_1.info(f'{site}, response - {response.status_code}')
        elif response.status_code != 200:
            log_2.warning(f'{site}, response - {response.status_code}')
    except Exception:
        log_3.error(f'{site}, NO CONNECTION')
