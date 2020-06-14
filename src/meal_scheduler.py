#import inventory_pb2

from absl import flags
from absl import logging
from absl import app


def main(_):
    logging.info("Hello World!")
#    salt = inventory_pb2.UnitAmount(
#        ingredient_name='Salt',
#        amount=inventory_pb2.UnitAmount(
#            unit=inventory_pb2.Unit.GRAM,
#            amount=100))
#    logging.info("Salt: %s", salt)


if __name__ == '__main__':
    app.run(main)
