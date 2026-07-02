import os
import psycopg2
import pytest
from dotenv import load_dotenv
import logging


LOG_PATH = os.path.join(os.path.dirname(__file__), "test_db.log")

logger = logging.getLogger("db_tests")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(LOG_PATH, mode="w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

load_dotenv()

@pytest.fixture(scope="session")
def conn():
    connection = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
    )
    yield connection
    connection.close()

