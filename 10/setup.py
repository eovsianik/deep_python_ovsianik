from setuptools import Extension, setup


def main():
    setup(
        name="cjson",
        version="1.0.0",
        author="Elizaveta",
        ext_modules=[
            Extension(
                name="cjson",
                sources=["./src/_cjson.c", "./src/cjson/cJSON.c"],
                include_dirs=["./src/cjson"],
            )
        ],
    )


if __name__ == "__main__":
    main()
