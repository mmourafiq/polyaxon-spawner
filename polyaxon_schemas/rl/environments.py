# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from marshmallow import Schema, fields, post_load

from polyaxon_schemas.base import BaseConfig, BaseMultiSchema


class BaseEnvironmentSchema(Schema):
    env_id = fields.Str()


class BaseEnvironmentConfig(BaseConfig):
    def __init__(self, env_id):
        self.env_id = env_id


class GymEnvironmentSchema(BaseEnvironmentSchema):
    class Meta:
        ordered = True

    @post_load
    def make_load(self, data):
        return GymEnvironmentConfig(**data)


class GymEnvironmentConfig(BaseEnvironmentConfig):
    IDENTIFIER = 'Gym'
    SCHEMA = GymEnvironmentSchema


class RegularizerSchema(BaseMultiSchema):
    __multi_schema_name__ = 'environment'
    __configs__ = {
        GymEnvironmentConfig.IDENTIFIER: GymEnvironmentConfig,
    }