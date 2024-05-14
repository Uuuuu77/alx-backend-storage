#!/usr/bin/env python3

""" lists all documents in a collection """


def list_all(mongo_collection):
    """ List all documents in a collection """
    docs = [doc for doc in mongo_collection.find()]

    return docs
