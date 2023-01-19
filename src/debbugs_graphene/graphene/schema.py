import graphene
from . import model
from .. import types


class Query(graphene.ObjectType):
    bug = model.Bug()
    bug_log = model.BugLog()

    @staticmethod
    def resolve_bug(parent, info):
        return model.Bug.get_query(info)

    @staticmethod
    def resolve_bug_log(parent, info):
        return types.BugLog(
            msg_num=1,
            header="header",
            body="body",
            attachments=[],
        )


schema = graphene.Schema(query=Query)
