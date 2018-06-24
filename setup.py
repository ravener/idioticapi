import setuptools

description = "A simple idiot's guide api wrapper in python"
long_description = open("README.md").read()
version="1.0.1"

packages = ['idioticapi']

setuptools.setup(
    name='idioticapi',
    version=version,
    description=description,
    long_description=long_description,
    url='https://github.com/freetnt5852/idioticapi',
    author='Free TNT',
    author_email='darksoulgamer5852@gmail.com',
    license='MIT',
    packages=packages,
    include_package_data=True,
    install_requires=['aiohttp>=2.0.0']
)