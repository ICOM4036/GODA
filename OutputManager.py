"""
    OUTPUT MANAGER
    - WRITE FILES
    - EXPORT FILES
    - MANAGE OUTPUT
"""
import os


def save_library(library):
    """
    SAVE A LIBRARY IN PROJECT FILES
    :param library: LIBRARY - LIBRARY TO BE SAVED
    :return: VOID
    """
    directory = 'Libraries'
    export_library(library, directory)


def export_library(library, directory):
    """
    EXPORT A LIBRARY TO A SPECIFIED DIRECTORY
    :param library: LIBRARY - LIBRARY TO BE EXPORTED
    :param directory: STRING - DIRECTORY WHERE LIBRARY WILL BE EXPORTED TO
    :return: VOID
    """
    collections = library.get_collection_list()
    directory = directory+'/'+library.get_name()
    if not os.path.exists(directory):
        os.makedirs(directory)

    cl = open(directory+'/'+library.get_name()+'.txt', 'w+')
    cl.write(library.get_name()+'\n')
    for c in collections:
        cl.write(directory+'/'+c.get_name()+'.txt\n')
        f = open(directory+'/'+c.get_name()+'.txt', 'w+')
        f.write(directory+'/Collections/'+c.get_name()+'.csv\n'
                +c.get_name()+'\n'
                +c.get_obj_def().get_obj_type()+'\n')
        a = c.get_obj_def().get_obj_attributes()
        d = c.get_obj_def().get_obj_data_types()
        for i in range(0, len(a)):
            f.write(a[i]+':'+d[i])
            if i < len(a)-1:
                f.write(',')
        f.close()
        export_collection(c, directory+'/Collections')
    cl.close()


def export_collection(collection, directory):
    """
    EXPORT A COLLECTION TO A SPECIFIED DIRECTORY
    :param collection: COLLECTION - COLLECTION TO BE EXPORTED
    :param directory: STRING - DIRECTORY WHERE COLLECTION WILL BE EXPORTED TO
    :return:
    """
    colname = collection.get_name()
    objs = collection.get_obj_list()
    if not os.path.exists(directory):
        os.makedirs(directory)
    f = open(directory+'/'+colname+'.csv', "w+")
    for x in objs:
        val = x.get_values()
        for a in range(0, len(val)):
            f.write(str(val[a]))
            if a < len(val)-1:
                f.write(',')
        f.write('\n')
    f.close()

