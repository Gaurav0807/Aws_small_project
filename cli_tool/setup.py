from setuptools import setup,find_packages

setup(
    name="cli_tool",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "typer",
        "boto3"
    ],
    entry_points={
        "console_scripts":["cli_tool=cli_tool.main:app"]
    }

)