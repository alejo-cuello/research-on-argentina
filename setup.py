import os

from setuptools import setup, find_packages

def readme() -> str:
    """Utility function to read the README.md.

    Used for the `long_description`. It's nice, because now
    1) we have a top level README file and
    2) it's easier to type in the README file than to put a raw string in below.

    Args:
        nothing

    Returns:
        String of readed README.md file.
    """
    return open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='research-on-argentina',
    version='0.1.0',
    author='alejo-cuello',
    author_email='alejocuello.ib@gmail.com',
    description='A data project about Argentina Development Indicators.',
    python_requires='>=3',
    license='MIT',
    url='https://github.com/alejo-cuello/research-on-argentina/',
    packages=find_packages(),
    long_description=readme(),
)