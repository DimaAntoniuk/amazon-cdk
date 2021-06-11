import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="amazon_cdk",
    version="0.0.1",

    description="CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Dmytro Antoniuk",

    package_dir={"": "amazon_cdk"},
    packages=setuptools.find_packages(where="amazon_cdk"),

    install_requires=[
        "aws-cdk.core==1.106.1",
        "aws-cdk.aws_dynamodb==1.106.1"
    ],

    python_requires=">=3.8",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
