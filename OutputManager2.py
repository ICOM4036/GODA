import os, shutil
import csv

def add_collection(library_name, collection_name):
    pass

def create_library(library_name):
    library_path = "C:/Users/irixa/PycharmProjects/GODA/Directory/%s" % (library_name)

    try:
        os.makedirs(library_path)
    except OSError as e:
        print("A library with that name already exists")
        return

    # Create a CollectionsList csv file
    with open('{}/{}.txt'.format(library_path, library_name), 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)

    # Create a subdirectory to contain all collections
    coll_path = "{}/Collections".format(library_path)
    os.makedirs(coll_path)


def create_collection(library_name, collection_name):
    pass


def delete_library(library_name):
    path = "C:/Users/irixa/PycharmProjects/GODA/Directory/{}".format(library_name)
    shutil.rmtree(path)


def delete_collection(library_name, collection_name):
    path = "C:/Users/irixa/PycharmProjects/GODA/Directory/{}/Collections/{}.csv".format(library_name, collection_name)
    try:
        os.remove(path)
        path2 = "C:/Users/irixa/PycharmProjects/GODA/Directory/{}.txt".format(collection_name)
        os.remove(path2)
    except Exception:
        pass
