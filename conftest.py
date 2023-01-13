pytest_plugins = [
    "ecommerce.tests.fixtures",
    "ecommerce.tests.selenium",
    "ecommerce.tests.factories",
    "ecommerce.tests.inventory_fixtures",
    "ecommerce.tests.promotion_fixtures",
    "ecommerce.tests.api_client",
    "celery.contrib.pytest",
]
