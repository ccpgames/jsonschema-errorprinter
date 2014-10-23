# -*- coding: utf-8 -*-
"""
    Json Schema Validation Error Pretty-printer.
    ---------------------------------------------------

    Makes a user friendly error message from a ValidationError.

"""
import logging
import json
import cStringIO

from jsonschema import validate as _validate
from jsonschema import FormatChecker, ValidationError

log = logging.getLogger("jsonschemaerror")


def check_json(json_object, schema, media_type_name="?"):
    try:
        _validate(json_object, schema, format_checker=FormatChecker())
    except ValidationError as e:
        report = generate_validation_error_report(e, json_object)
        return "Schema check failed for '%s'\n%s" % (media_type_name, report)


def generate_validation_error_report(
    e,
    json_object,
    lines_before=7,
    lines_after=7
    ):
    """
    Generate a detailed report of a schema validation error.

    'e' is a jsonschema.ValidationError exception that errored on
    'json_object'.

    Steps to discover the location of the validation error:
    1. Traverse the json object using the 'path' in the validation exception
       and replace the offending value with a special marker.
    2. Pretty-print the json object indendented json text.
    3. Search for the special marker in the json text to find the actual
       line number of the error.
    4. Make a report by showing the error line with a context of
      'lines_before' and 'lines_after' number of lines on each side.
    """

    if json_object is None:
        return "Request requires a JSON body"
    if not e.path:
        return str(e)
    marker = "3fb539deef7c4e2991f265c0a982f5ea"

    # Find the object that is erroring, and replace it with the marker.
    ob_tmp = json_object
    for entry in list(e.path)[:-1]:
        ob_tmp = ob_tmp[entry]

    orig, ob_tmp[e.path[-1]] = ob_tmp[e.path[-1]], marker

    # Pretty print the object and search for the marker.
    json_error = json.dumps(json_object, indent=4)
    io = cStringIO.StringIO(json_error)
    errline = None

    for lineno, text in enumerate(io):
            if marker in text:
                errline = lineno
                break

    if errline is not None:
        # Re-create report.
        report = []
        ob_tmp[e.path[-1]] = orig
        json_error = json.dumps(json_object, indent=4)
        io = cStringIO.StringIO(json_error)

        for lineno, text in enumerate(io):
            if lineno == errline:
                line_text = "{:4}: >>>".format(lineno+1)
            else:
                line_text = "{:4}:    ".format(lineno+1)
            report.append(line_text + text.rstrip("\n"))

        report = report[max(0, errline-lines_before):errline+1+lines_after]

        s = "Error in line {}:\n".format(errline+1)
        s += "\n".join(report)
        s += "\n\n" + str(e).replace("u'", "'")
    else:
        s = str(e)
    return s
