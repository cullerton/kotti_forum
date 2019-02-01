from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('kotti_forum')


def kotti_configure(settings):
    """ Add a line like this to you .ini file::

            kotti.configurators =
                kotti_forum.kotti_configure

        to enable the ``kotti_forum`` add-on.

    :param settings: Kotti configuration dictionary.
    :type settings: dict
    """

    settings['pyramid.includes'] += ' kotti_forum'
    settings['kotti.alembic_dirs'] += ' kotti_forum:alembic'
    settings['kotti.available_types'] += (
          ' kotti_forum.resources.Forum' +
          ' kotti_forum.resources.Idea')
    settings['kotti.fanstatic.view_needed'] += ' kotti_forum.fanstatic.css_and_js'


def includeme(config):
    """ Don't add this to your ``pyramid_includes``, but add the
    ``kotti_configure`` above to your ``kotti.configurators`` instead.

    :param config: Pyramid configurator object.
    :type config: :class:`pyramid.config.Configurator`
    """

    config.add_translation_dirs('kotti_forum:locale')
    config.add_static_view('static-kotti_forum', 'kotti_forum:static')

    config.scan(__name__)
