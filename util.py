import os


def remove(path):

    try:
        os.remove(path)
    except IOError:
        pass


def symlink(real, link):
    real = os.path.abspath(real)

    # Create directory link will reside in if it does not exist
    link_dir = os.path.dirname(link)
    if not os.path.exists(link_dir):
        os.mkdir(link_dir)

    # Delete target if it exists
    remove(link)

    os.symlink(real, link)
