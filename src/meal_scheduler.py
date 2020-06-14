from example.proto import person_pb2
import sys

from absl import app
from absl import logging
from absl import flags


def main(_):
    logging.info("Hello World!")
    salt = person_pb2.Person(name='John')
    logging.info("person: %s", salt)

    logging.info("%s", sys.path)

    #import inventory_pb2
    #from meal_scheduler.src import inventory_pb2

    from src import inventory_pb2

    salt = inventory_pb2.InventoryLine(
        ingredient_name='Salt',
        amount=inventory_pb2.UnitAmount(
            # enums cannot be used like this for some stupid reason:
            # --> AttributeError: 'EnumTypeWrapper' object has no attribute 'GRAM'
            # unit=inventory_pb2.Unit.GRAM,
            amount=100))
    logging.info("Salt: %s", salt)


if __name__ == '__main__':
    app.run(main)
