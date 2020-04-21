import decimal
from decimal import Decimal, FloatOperation


# always quote literal fractional values. avoids intermediate step of creating base 2 float object
print(f'{Decimal(0.8) - Decimal(0.7)}')
print(f'{Decimal("0.8") - Decimal("0.7")}')

# raise exception if Decimal and float mixed
# decimal.getcontext().traps[FloatOperation] = True
