import csv
import json
from helpers import datetime_to_str


def write_to_csv(results, filename):

    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each
    output rowcorresponds to the information in a single close approach
    from the `results`stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data
     should be saved.
    """

    fieldnames = (
        "datetime_utc",
        "distance_au",
        "velocity_km_s",
        "designation",
        "name",
        "diameter_km",
        "potentially_hazardous",
    )

    # Write the results to a CSV file
    with open(filename, "w") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        if results is not None:
            for result in results:
                writer.writerow(
                    {
                        "datetime_utc": datetime_to_str(result.time),
                        "distance_au": float(result.distance),
                        "velocity_km_s": float(result.velocity),
                        "designation": str(result._designation),
                        "name": str(result.neo.name)
                        if str(result.neo.name) is None
                        else str(""),
                        "diameter_km": float(result.neo.diameter)
                        if str(result.neo.diameter) is None
                        else float("nan"),
                        "potentially_hazardous": str(result.neo.hazardous),
                    }
                )
        return


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the
    output is a list containing dictionaries, each mapping `CloseApproach`
    attributes to their values and the 'neo' key mapping to a dictionary of
    the associated NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where
    the data should be saved.
    """
    # Write the results to a JSON file.
    with open(filename, "w") as file:
        outfile = []
        for result in results:
            contents = dict(
                datetime_utc=datetime_to_str(result.time),
                distance_au=float(result.distance),
                velocity_km_s=float(result.velocity),
                neo={
                    "designation": str(result.neo.designation),
                    "name": str(result.neo.name)
                    if str(result.neo.name) is None
                    else str(""),
                    "diameter_km": float(result.neo.diameter)
                    if str(result.neo.diameter) is None
                    else float("nan"),
                    "potentially_hazardous": bool(result.neo.hazardous),
                },
            )
            outfile.append(contents)
        json.dump(outfile, file, indent=2)
