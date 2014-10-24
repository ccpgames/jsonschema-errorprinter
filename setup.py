from setuptools import setup

setup(
    name='jsonschema-errorprinter',
    version="1.0.0",
    py_modules=['jsonschemaerror'],
    license='MIT License',
    description='Validation Error Pretty-Printer for the jsonschema library.',
    long_description=open('README.md').read(),
    author='Matthias Gudmundsson',
    author_email='matti@ccpgames.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
    ],
    platforms=['any'],
    install_requires = ['jsonschema'],
    download_url='https://github.com/ccpgames/jsonschema-errorprinter/archive/master.zip',
    url='https://github.com/ccpgames/jsonschema-errorprinter',
)
