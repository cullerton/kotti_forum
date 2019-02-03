from kotti.resources import get_root
from kotti.resources import Content
from kotti.resources import Document
from kotti.resources import TypeInfo
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer


class ForumTypeInfo(TypeInfo):

    def addable(self, context, request):
        """add once, and only at the root"""
        at_root = context == get_root()
        already_added = self in [
                c.type_info for c in context.children]
        return at_root and not already_added


class Forum(Content):
    id = Column(Integer(), ForeignKey('contents.id'), primary_key=True)

    type_info = ForumTypeInfo(
        name=u'Forum',
        title=u'Forum',
        add_view=u'add_forum',
        addable_to=[u'Document'],
    )


class Idea(Document):
    id = Column(Integer(), ForeignKey('documents.id'), primary_key=True)

    type_info = Document.type_info.copy(
        name=u'Idea',
        title=u'Idea',
        add_view=u'add_choice',
        addable_to=[u'Forum'],
    )

    def __init__(self, idea='', **kwargs):
        super(Idea, self).__init__(**kwargs)
        self.idea = idea
