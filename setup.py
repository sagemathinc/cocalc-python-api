from setuptools import setup

from cocalc_api import __version__

setup(name='cocalc_api',
      version=__version__,
      description='Client for the CoCalc API',
      url='https://github.com/sagemathinc/cocalc-python-api',
      author_email='office@sagemath.com',
      license='Apache 2.0',
      packages=['cocalc_api'],
      zip_safe=False)
