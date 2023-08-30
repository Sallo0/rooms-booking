from sqladmin import ModelView

from app.users.models import Users


class UserAdmin(ModelView, model=Users):
    column_list = [Users.id, Users.email]

    column_details_exclude_list = [Users.hashed_password]

    can_delete = False
    can_edit = False

    name = "User"
    name_plural = "Users"
    icon = "fas fa-user"
