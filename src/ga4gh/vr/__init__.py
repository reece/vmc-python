# flake8: noqa
"""Public interface to the GA4GH Variation Representation reference
implementation

"""


__all__ = """models normalize schema_path vr_deref vr_enref""".split()


from pkg_resources import get_distribution, DistributionNotFound


#if "vrs" not in __file__:
#    import warnings
#    raise FutureWarning("`ga4gh.vr` is being renamed to `ga4gh.vrs`. Migrate to `ga4gh.vrs`"
#                            " now. The old name will be removed in the next release.")


try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:    # pragma: nocover
    __version__ = "unknown"
finally:
    del get_distribution, DistributionNotFound


from ._internal.enderef import vr_deref, vr_enref
from ._internal.models import models, schema_path
from .normalize import normalize
