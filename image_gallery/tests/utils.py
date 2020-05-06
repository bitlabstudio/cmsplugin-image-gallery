from filer.models import Folder


def generate_filer_folder():
    folder = Folder()
    folder.save()
    return folder
