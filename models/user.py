#!/usr/bin/python3
"""Describe User module"""
from models.base_model import BaseModel


class User(BaseModel):
    """initalize the User with attribute of email password.

    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

