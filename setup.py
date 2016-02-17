from setuptools import setup, find_packages

setup(
    name='pygraph-cli',
    description='CLI for pygraphviz powered by graphviz',
    url='https://github.com/EntilZha/pygraph',
    author='Pedro Rodriguez',
    author_email='ski.rodriguez@gmail.com',
    maintainer='Pedro Rodriguez',
    maintainer_email='ski.rodriguez@gmail.com',
    license='MIT',
    keywords='graph visualization graphviz python cli',
    packages=find_packages(),
    version='0.0.0',
    install_requires=['graphviz', 'click', 'scalafunctional'],
    entry_points={
        'console_scripts': ['pygraph = pygraph.cli:main']
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

