import logging# configure logging file
logging.basicConfig(
    filename='app/routes/routes_journal.log',
    level= logging.WARNING,
    format="%(levelname)s :%(asctime)s :%(name)s :%(message)s"

)
logger= logging.getLogger('routes_journal')