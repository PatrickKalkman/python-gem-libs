from pydantic import BaseModel, ValidationError


class Person(BaseModel):
    name: str
    age: int
    email: str


# Valid input
valid_input = {"name": "John Doe", "age": 30, "email": "john.doe@example.com"}

try:
    person = Person(**valid_input)
    print(person)
except ValidationError as e:
    print(e)

# Invalid input
invalid_input = {
    "name": "John Doe",
    "age": "thirty",  # Invalid data type
    "email": "john.doe@example.com",
}

try:
    person = Person(**invalid_input)
    print(person)
except ValidationError as e:
    print(e)
