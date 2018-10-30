"""
Dash Google Authentication.
"""

import pkg_resources
try:
    __version__ = pkg_resources.get_distribution(__name__.replace('.', '-')).version
except pkg_resources.DistributionNotFound:
    __version__ = None
del pkg_resources

from .google_oauth import GoogleOAuth
