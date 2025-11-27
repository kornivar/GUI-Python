# class UserEntity:
#     def __init__(self, id, username, email, password_hash):
#         self.id = id
#         self.username = username
#         self.email = email
#         self.password_hash = password_hash

# class UserDTO:
#     def __init__(self, id, username, email):
#         self.id = id
#         self.username = username
#         self.email = email

# class UserMapper:
#     @staticmethod
#     def to_dto(user_entity):
#         return UserDTO(id=user_entity.id, username=user_entity.username, email=user_entity.email)

#     @staticmethod
#     def to_entity(user_dto, password_hash):
#         return UserEntity(id=user_dto.id, username=user_dto.username, email=user_dto.email, password_hash=password_hash)

from View.BView import BookView
from Controller.BController import BookController

controller = BookController()
dtos = controller.get_all_books()

view = BookView()
view.render_books(dtos)