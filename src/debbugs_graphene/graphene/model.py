import graphene_pydantic
from .. import types


class Bug(graphene_pydantic.PydanticObjectType):
    class Meta:
        model = types.Bug


class BugLog(graphene_pydantic.PydanticObjectType):
    class Meta:
        model = types.BugLog
