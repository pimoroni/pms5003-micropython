from setuptools import setup

setup(
    name='pms5003-micropython',
    version='0.0.7',
    description='MicroPython library for the Plantower PMS5003 Particulate Matter Sensor.',
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    url='https://www.pimoroni.com',
    project_urls={
        'github': 'https://github.com/pimoroni/pms5003-micropython',
    },
    author='Philip Howard',
    author_email='phil@pimoroni.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: Implementation :: MicroPython',
    ],
    keywords=[
        'micropython',
        'electronics',
    ],
    packages=['pms5003'],
)
