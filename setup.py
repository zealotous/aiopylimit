from distutils.core import setup
setup(
  name = 'aiopylimit',
  packages = ['aiopylimit'],
  description = 'A distributed rate limiting library for python using leaky bucket algorithm and Redis(asyncio version)',
  use_scm_version=True,
  author='David Markey',
  setup_requires=['setuptools_scm'],
  author_email='david@dmarkey.com',
  url='https://github.com/dmarkey/aiopylimit',
  keywords=['rate limiting', 'throttle', 'redis'],
  classifiers=[],
)
