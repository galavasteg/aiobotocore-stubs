from typing import List

from setuptools import find_packages, setup


def get_long_description():
    with open('README.md', encoding='utf8') as readme_file:
        return readme_file.read()


def parse_requirements() -> List[str]:
    def exclude_empty_or_comment(text: str) -> bool:
        return bool(text and text[0] != '#')

    with open('requirements.txt', 'r', encoding='utf-8') as r_file:
        dependencies = list(filter(exclude_empty_or_comment, map(str.strip, r_file.readlines())))

    return dependencies


packages = find_packages()
requirements = parse_requirements()

setup(
    name='x5-aiobotocore-stubs',
    version='0.0.1',
    python_requires='>=3.8',
    install_requires=requirements,
    license='BSD',
    description='aiobotocore stubs for typing',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    packages=packages,
    package_data={'aiobotocore-stubs': ['*.pyi', 'py.typed']},
    data_files=[('', ['LICENSE'])],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python :: 3.8',
        'Typing :: Typed',
    ],
    zip_safe=False,
)
