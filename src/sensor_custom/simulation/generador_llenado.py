from decimal import Decimal, ROUND_HALF_UP
import random


class GeneradorLlenado:

    @staticmethod
    def get_valor():
        valor = Decimal(str(random.uniform(0.1, 0.17)))
        return valor.quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)