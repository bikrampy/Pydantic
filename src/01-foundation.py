def calculateAge(current: int, years: int) -> int:
    return current + years
# print(calculateAge('20', 20));

from pydantic import BaseModel;
class User(BaseModel):
    user_id: int
    user_name: str
    is_active: bool

input_data = {
    'user_id': 1,
    'user_name': 'Bikram',
    'is_active': True,
}
user = User(**input_data);
print(user.user_id);
print(user.user_name);
print(user.is_active);

input_data2 = {
    'user_id': '2',
    'user_name': 'Saswata',
    'is_active': 'True',
}
user2 = User(**input_data2);
print(user2.user_id);
print(user2.user_name);
print(user2.is_active);

# input_data3 = {
#     'user_id': '2a',
#     'user_name': 123456,
#     'is_active': '123abc',
# }
# user3 = User(**input_data3);
# print(user3.user_id);
# print(user3.user_name);
# print(user3.is_active);
