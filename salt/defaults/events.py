# -*- coding: utf-8 -*-
'''
Event constants used by listeners and servers, to be imported elsewhere in Salt code.

Do NOT, import any salt modules (salt.utils, salt.config, etc.) into this file,
as this may result in circular imports.

.. versionadded:: Neon
'''

# Constants for events on the minion bus
MINION_PILLAR_COMPLETE = '/salt/minion/minion_pillar_complete'
MINION_MOD_COMPLETE = '/salt/minion/minion_mod_complete'
