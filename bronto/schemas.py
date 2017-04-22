# -*- coding: utf-8 -*-

import colander as c


class InvalidationKey(c.SchemaNode):
    schema_type = c.String


class InvalidationKeyList(c.SequenceSchema):
    invalidation_key = InvalidationKey(name='invalidationKey')


class CacheInvalidateSchema(c.MappingSchema):
    invalidation_keys = InvalidationKeyList(name='invalidationKeys')


cache_invalidate_schema = CacheInvalidateSchema()
invalidation_key_list_schema = InvalidationKeyList()
