# -*- coding: utf-8 -*-

"""
Created on 2019-02-01
:author:  ()
"""

pytest_plugins = "kotti"

from pytest import fixture


@fixture(scope='session')
def custom_settings():
    import kotti_forum.resources
    kotti_forum.resources  # make pyflakes happy
    return {
        'kotti.configurators': 'kotti_tinymce.kotti_configure '
                               'kotti_forum.kotti_configure'}
