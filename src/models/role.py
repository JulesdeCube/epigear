from src.models.permission_group import PermissionGroup
from discord.colour import Color
from discord import Role as RoleDiscord


class Role:
    name: str
    id: int
    color: Color
    permission: PermissionGroup
    hoist: bool
    mentionable: bool
    role_discord: RoleDiscord

    def __init__(self, name: str, color_code: int = 0x000000, permission: PermissionGroup = None,
                 hoist: bool = False, mentionable: bool = False):
        self.name = name
        self.color = Color(color_code)
        self.permissions = permission
        self.hoist = hoist
        self.mentionable = mentionable
        self.id = -1

    def __str__(self):
        return 'role infos : \n name = {} \n color = {} ' \
               '\n hoist = {} \n mentionable = {}'.format(self.name, self.color, self.hoist, self.mentionable)

    def set_role(self, role: RoleDiscord):
        self.id = role.id
        self.role_discord = role
