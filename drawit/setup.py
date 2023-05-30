from distutils.core import setup
setup(
   name='drawIT',
   version='0.10.15',
   license='Apache License 2.0',
   python_requires='>=3.10.5',
   install_requires=[
      'pandas>=1.4.2',
      'PyYAML>=6.0',
      'requests>=2.31.0',
      'urllib3>=1.26.9'
   ]
)
