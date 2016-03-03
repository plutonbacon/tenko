#!/usr/bin/env python

# Third-party dependencies
import hug

# Internal dependencies
from api import apiv1

@hug.not_found()
def not_found_handler(output=hug.output_format.json):
    return 'Not found'

@hug.get('/', output=hug.output_format.json)
def root_handler():
    """Display the current version of the Tenko server."""
    return '1.0.0.dev'

@hug.extend_api()
def sensors_resource():
    return [apiv1]