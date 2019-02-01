from kotti.resources import Content
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer


class Forum(Content):
    id = Column(Integer(), ForeignKey('contents.id'), primary_key=True)

    type_info = Content.type_info.copy(
        name=u'Forum',
        title=u'Forum',
        add_view=u'add_forum',
        addable_to=[u'Document'],
    )


class Idea(Content):
    id = Column(Integer(), ForeignKey('contents.id'), primary_key=True)

    type_info = Content.type_info.copy(
        name=u'Idea',
        title=u'Idea',
        add_view=u'add_choice',
        addable_to=[u'Forum'],
    )

    def __init__(self, idea='', **kwargs):
        super(Idea, self).__init__(**kwargs)
        self.idea = idea
