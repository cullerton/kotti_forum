from pyramid.view import view_config
from pyramid.view import view_defaults

# from kotti_forum import _
from kotti_forum.fanstatic import css_and_js
from kotti_forum.views import BaseView

from kotti_forum.resources import Forum


@view_defaults(context=Forum)
class ForumViews(BaseView):
    """ Views for :class:`kotti_forum.resources.Forum` """

    @view_config(name='view', permission='view',
                 renderer='kotti_forum:templates/forum.pt')
    def forum_view(self):
        css_and_js.need()
        ideas = self.context.children
        return {
            'ideas': ideas,
        }
