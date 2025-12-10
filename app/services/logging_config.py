import logging

logging.basicConfig(
    filename='app/routes/services_journal.log',
    level= logging.WARNING,
    format="%(levelname)s -%(asctime)s -%(name)s -%(message)s"

)
logger= logging.getLogger('services_journal')