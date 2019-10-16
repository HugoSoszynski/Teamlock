#!/usr/bin/python

"""This file is part of Teamlock.

Teamlock is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Teamlock is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Teamlock.  If not, see <http://www.gnu.org/licenses/>."""

__author__ = "Olivier de Régis"
__credits__ = []
__license__ = "GPLv3"
__version__ = "3.0.0"
__maintainer__ = "Teamlock Project"
__email__ = "contact@teamlock.io"
__doc__ = ''

from django.db import models
import datetime


class MailSettings(models.Model):
    host = models.CharField(max_length=255, default="")


class SecuritySettings(models.Model):
    password_change = models.IntegerField(default=100)
    length_password = models.IntegerField(default=8)
    key_size = models.IntegerField(default=4096)


class GeneralSettings(models.Model):
    company_name = models.CharField(max_length=255)
    install_year = models.IntegerField(default=datetime.datetime.now().year)
