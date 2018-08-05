import os


def remove(path):

    try:
        os.remove(path)
    except IOError:
        pass


def symlink(real, link):

    # Add name of real file to link if link is merely a directory
    if os.path.isdir(link):
        link = os.path.join(link, os.path.basename(real))

    # Expand potentially real path to be absolute
    real = os.path.abspath(real)

    # Create directory link will reside in if it does not exist
    link_dir = os.path.dirname(link)
    if not os.path.exists(link_dir):
        os.mkdir(link_dir)

    # Delete target if it exists
    remove(link)

    os.symlink(real, link)
