"""Extract data on NEO and CA's from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file,
formatted as described in the project instructions, into a
collection of `NearEarthObject`s. The `load_approaches`
function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a
collection of `CloseApproach` objects. The main module calls
these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.
"""


import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing
    data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # Load NEO data from the given CSV file.
    filename = neo_csv_path
    NearEarthObjects = []
    with open(filename, "r") as f:
        csvfile = csv.DictReader(f, delimiter=",")
        for row in csvfile:
            NearEarthObjects.append(NearEarthObject(**row))
    return NearEarthObjects


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data
    about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # Load close approach data from the given JSON file.
    with open(cad_json_path, "r") as infile:
        CloseApproachObjects = []
        data = json.load(infile)
        for row in data["data"]:
            info = dict(zip(data["fields"], row))
            closeObject = CloseApproach(**info)
            CloseApproachObjects.append(closeObject)
    return CloseApproachObjects
