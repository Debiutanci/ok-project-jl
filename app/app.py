from . import utils
from . import cubes


def app():
    bucket = utils.Bucket(10,15)
    print(bucket)
    for cube_data in cubes.cubes_data():
        cube_obj = utils.Cube(cube_data, 3)
        bucket.insert_cube(cube_obj)

    print(bucket)
    # identifiers = utils.identifier_generator()
    # print(next(identifiers))
    # print(next(identifiers))
    # print(next(identifiers))

    # print()
    # print(utils.identifier_generator())
    # print(utils.identifier_generator())
