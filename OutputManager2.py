import os, shutil

def add_collection(library_name, collection_name):
    pass


def delete_library(library_name):
    path = "C:/Users/irixa/PycharmProjects/GODA/Directory/{}".format(library_name)
    shutil.rmtree(path)


def delete_collection(library_name, collection_name):
    path = "C:/Users/irixa/PycharmProjects/GODA/Directory/{}/Collections/{}.csv".format(library_name, collection_name)
    os.remove(path)
    path2 = "C:/Users/irixa/PycharmProjects/GODA/Directory/{}.txt".format(collection_name)
    os.remove(path2)
