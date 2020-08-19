import os

if __name__ == "__main__":
    file_dir = os.path.dirname(__file__)
else:
    file_dir = os.path.dirname(__file__)


def convert_unit(size_in_bytes, unit):
    """ Convert the size from bytes to other units like KB, MB or GB"""
    if unit == "kb":
        return size_in_bytes / 1024
    elif unit == "mb":
        return size_in_bytes / (1024 * 1024)
    elif unit == 'gb':
        return size_in_bytes / (1024 * 1024 * 1024)
    else:
        return size_in_bytes


def get_file_size(file_name, size_type='mb'):
    """ Get file in size in given unit like KB, MB or GB"""
    size = os.stat(os.path.join(file_dir, file_name)).st_size
    return str(round(convert_unit(size, size_type), 3)) + " " + size_type.upper()
    # size = os.path.getsize(file_name)


def get_folder_size(unit):
    total_size = 0
    for dir_path, dir_names, file_names in os.walk(file_dir):
        for f in file_names:
            fp = os.path.join(dir_path, f)
            total_size += os.path.getsize(fp)
    return str(round(convert_unit(total_size, unit), 3)) + " " + unit.upper()
