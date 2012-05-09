from distutils.core import setup

setup(
    name='cherrypy-wsgiserver',
    version='0.1dev',
    packages=['wsgiserver', ],
    license='LICENSE',
    description='Wsgiserver configured for cherrypy and django',
    long_description=open('README.md').read(),
    author='Calvin Cheng',
    author_email='calvin@calvinx.com',
    maintainer='Calvin Cheng',
    maintainer_email='calvin@calvinx.com',
    url='https://github.com/od-eon/cherrypy-wsgiserver'
)
