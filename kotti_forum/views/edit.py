import colander
# from deform.widget import RichTextWidget
from kotti.views.edit import ContentSchema
from kotti.views.edit import DocumentSchema
from kotti.views.form import AddFormView
from kotti.views.form import EditFormView
from pyramid.view import view_config

from kotti_forum import _

from kotti_forum.resources import Forum
from kotti_forum.resources import Idea


class ForumSchema(ContentSchema):
    """Schema for Forum"""

    title = colander.SchemaNode(
        colander.String(),
        title=_(u'Forum Name'),
    )


class IdeaSchema(DocumentSchema):
    """Schema for Idea"""
    pass

    # title = colander.SchemaNode(
    #     colander.String(),
    #     title=_(u'Idea'),
    # )

    # body = colander.SchemaNode(
    #     colander.String(),
    #     title=_(u'Idea'),
    #     widget=RichTextWidget(
    #         # theme='advanced', width=790, height=500
    #         height=500
    #     ),
    #     missing="",
    # )


@view_config(name='edit', context=Forum, permission='edit',
             renderer='kotti:templates/edit/node.pt')
class ForumEditForm(EditFormView):
    schema_factory = ForumSchema


@view_config(name=Forum.type_info.add_view, permission='add',
             renderer='kotti:templates/edit/node.pt')
class ForumAddForm(AddFormView):
    schema_factory = ForumSchema
    add = Forum
    item_type = u"Forum"


@view_config(name='edit', context=Idea, permission='edit',
             renderer='kotti:templates/edit/node.pt')
class IdeaEditForm(EditFormView):
    schema_factory = IdeaSchema


@view_config(name=Idea.type_info.add_view, permission='add',
             renderer='kotti:templates/edit/node.pt')
class IdeaAddForm(AddFormView):
    schema_factory = IdeaSchema
    add = Idea
    item_type = u"Idea"
