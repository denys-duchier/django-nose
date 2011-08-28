VERSION = (0, 1, 3)
__version__ = '.'.join(map(str, VERSION))

from django_nose.runner import NoseTestSuiteRunner


# Django < 1.2 compatibility.
run_tests = run_gis_tests = NoseTestSuiteRunner
