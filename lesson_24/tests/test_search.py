import logging
import pytest
import requests


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("test_search.log", mode="a", encoding="utf-8")
console_handler = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)



class TestCarsSearch:

    @pytest.mark.parametrize(
        "sort_by,limit",
        [
            ("price", 9),
            ("year", 3),
            ("engine_volume", 10),
            ("brand", 5),
            ("price", 7),
            ("year", 6),
            ("brand", 20),
        ]
    )
    def test_search_cars(self, session, sort_by, limit):

        response = session.get(
            "http://127.0.0.1:8080/cars",
            params={
                "sort_by": sort_by,
                "limit": limit
            }
        )

        logger.info(
            f"GET /cars?sort_by={sort_by}&limit={limit}"
        )

        logger.info(
            f"Response status code: {response.status_code}"
        )
        assert response.status_code == 200

        cars = response.json()

        logger.info(
            f"Returned cars count: {len(cars)}"
        )

        assert isinstance(cars, list)
        assert len(cars) <= limit

        logger.info(
            f"Returned cars count: {len(cars)}"
        )

        if sort_by == "price":
            values = [car["price"] for car in cars]
            assert values == sorted(values)

        elif sort_by == "year":
            values = [car["year"] for car in cars]
            assert values == sorted(values)

        elif sort_by == "engine_volume":
            values = [car["engine_volume"] for car in cars]
            assert values == sorted(values)

        elif sort_by == "brand":
            values = [car["brand"] for car in cars]
            assert values == sorted(values)

        logger.info(
            f"Sorting check passed for '{sort_by}'"
        )

    def test_search_without_token(self):

        response = requests.get(
            "http://127.0.0.1:8080/cars"
        )

        logger.info(
            f"Unauthorized request status: {response.status_code}"
        )

        assert response.status_code == 401