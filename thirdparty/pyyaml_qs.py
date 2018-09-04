import yaml


py_obj = yaml.load("""
invoice: 100
date   : 2015-12-29T08:09:10.011Z
bill-to: &id001
    name   : Billing Name
    address:
        lines: |
            123 Main Street
            Suite #100
        city    : Anytown
        state   : LA
        postal  : 70056
ship-to: *id001
items  :
    - model-no    : CX2600
      quantity    : 1
      description : Atari VCS
      unit-price  : 199.00
      price       : 199.00
    - model-no    : CX30
      quantity    : 2
      description : Paddle Controllers
      unit-price  : 25.00
      price       : 50.00
    - model-no    : CX2610
      quantity    : 1
      description : Warlords
      unit-price  : 19.95
      price       : 19.95
    - model-no    : CX2638
      quantity    : 1
      description : Missile Command
      unit-price  : 29.95
      price       : 29.95
subtotal      : 298.90
tax           : 20.92
shipping      : 19.95
rewards-member: false
total         : 339.77
email         : ~
comments      : >
    Thank you for your order!
    Be sure to stop by The Video Store on Terry Pkwy!
""")

print(py_obj)
print(yaml.dump(py_obj))
