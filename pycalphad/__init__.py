#first import dill, which populates itself into pickle's dispatch
import dill
import pickle
# save the MethodDescriptorType from dill
MethodDescriptorType = type(type.__dict__['mro'])
if getattr(pickle, '_Pickle'):
    MethodDescriptorWrapper = pickle._Pickler.dispatch[MethodDescriptorType]
else:
    MethodDescriptorWrapper = pickle.Pickler.dispatch[MethodDescriptorType]
# cloudpickle does the same, so let it update the dispatch table
import cloudpickle
# now, put the saved MethodDescriptorType back in
if getattr(pickle, '_Pickle'):
    pickle._Pickler.dispatch[MethodDescriptorType] = MethodDescriptorWrapper
else:
    pickle.Pickler.dispatch[MethodDescriptorType] = MethodDescriptorWrapper

import pycalphad.variables as v
from pycalphad.model import Model
from pycalphad.io.database import Database

# Trigger format extension hooks
import pycalphad.io.tdb

from pycalphad.core.calculate import calculate
from pycalphad.core.equilibrium import equilibrium
from pycalphad.core.equilibrium import EquilibriumError, ConditionError
from pycalphad.plot.binary import binplot
from pycalphad.plot.eqplot import eqplot
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
