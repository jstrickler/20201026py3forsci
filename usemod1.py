#    from pkg.pkg import module
from myproject.utils import johnlib
import sys

# search path for modules (sys.path)
# 1. current folder
# 2. folders in env variable PYTHONPATH (if it exists)
# 3. folders under <    sys.prefix>/lib


johnlib.spam()
johnlib.toast()

for path in sys.path:
    print(path)


