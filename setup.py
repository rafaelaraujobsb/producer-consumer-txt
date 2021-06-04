import io
import re

from setuptools import find_packages, setup


dev_requirements = [
    'bandit',
    'pylama',
    'isort',
    'pytest',
]

unit_test_requirements = [
    'pytest',
]

run_requirements = [
    "fastapi==0.65.1",
    "uvicorn[base]==0.14.0",
    "celery==5.1.0",
    "gunicorn==20.1.0",
    "loguru==0.5.3",
    "urllib3==1.26.5",
]

with io.open('./producer_consumer_txt/__init__.py', encoding='utf8') as version_f:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_f.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")

with io.open('README.md', encoding='utf8') as readme:
    long_description = readme.read()

setup(
    name="producer_consumer_txt",
    version=version,
    author="Rafael Araujo",
    author_email="bsb.rafaelaraujo@gmail.com.br",
    packages=find_packages(exclude='tests'),
    include_package_data=True,
    url="https://github.com/rafaelaraujobsb/producer-consumer-txt",
    license="COPYRIGHT",
    description="API to send a json to a queue and be stored in a txt.",
    long_description=long_description,
    zip_safe=False,
    install_requires=run_requirements,
    extras_require={
         'dev': dev_requirements,
         'unit': unit_test_requirements,
    },
    python_requires='>=3.8',
    classifiers=[
        'Intended Audience :: Information Technology',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8'
    ],
    keywords=(),
    entry_points={
        'console_scripts': [
            'producer_consumer_txt = producer_consumer_txt.__main__:start'
        ],
    },
)
