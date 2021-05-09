from cerberus import Validator

# data validation library. validates dictionary against schema
# https://docs.python-cerberus.org/en/stable/validation-rules.html#type


schema = {
    "fname": {'type': 'string', 'required': True},
    "lname": {'type': 'string'}
}
#validator = Validator(schema, require_all=True)
validator = Validator(schema)


response = {"fname": "Kermit", "lname": "Frog"}
if not validator.validate(response):
    print(validator.errors)



schema = {
    "muppets": {
        "type": "list",
        "schema": {
            "type": "dict",
            "schema": {
                "fname": {
                    "type": "string",
                    "required": True
                },
                "lname": {
                    "type": "string"
                }
            }
        }
    }
}
validator = Validator(schema)

response = {"muppets": [{"fname": "Kermit", "lname": "Frog"}, {"fname": "Fozzie", "lname": "Bear"}]}
if not validator.validate(response):
    print(validator.errors)

#is_valid = validator.validate(response)
#assert_that(is_valid, description=validator.errors).is_true()
