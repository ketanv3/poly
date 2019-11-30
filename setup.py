import subprocess
import setuptools


# Install the requirements
subprocess.run(["pip", "install", "-r", "requirements.txt"])

# Run the setup
setuptools.setup(
    name='poly',
    version='1.0.0',
    description='',

    packages=setuptools.find_packages(),
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    scripts=['scripts/poly'],

    license='',
    author='Ketan Verma',
    author_email='ketan9495@gmail.com',
    url='https://github.com/ketanv3/poly'
)
