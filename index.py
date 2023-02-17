from mixpeek import Mixpeek
import os

mix = Mixpeek(
    api_key="")


def index_every_file(folder_path):
    # Iterate through every file in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # with extra metadata
        p = mix.index(
            file_path,
            save=True
        )
        print(p)


index_every_file("pages")
