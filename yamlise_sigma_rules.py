#!/usr/bin/env python3
"""
Creating Custom Object Type for Sigma Rules
"""
import os
import yaml
from stix2 import CustomObject, properties, Bundle

def create_bundle(json):
    """
    Writes the Sigma rules into a file.
    """
    file = open('sigma_rules_stix_bundle.json', 'w')
    file.write(Bundle(json).serialize(pretty=False))

@CustomObject('x-sigma-rules', [
    ('action', properties.StringProperty()), ## needs updating its not part of the schema
    ('title', properties.StringProperty()),
    ('status', properties.StringProperty()),
    ('description', properties.StringProperty()),
    ('references', properties.ListProperty(properties.StringProperty())), ##posible list here
    ('reference', properties.ListProperty(properties.StringProperty())), ##should be looked at there are two differences
    ('author', properties.StringProperty()),
    ('date', properties.StringProperty()),
    ('logsource', properties.DictionaryProperty()),
    ('detection', properties.DictionaryProperty()),
    ('fields', properties.ListProperty(properties.StringProperty())),
    ('falsepositives', properties.ListProperty(properties.StringProperty())),
    ('level', properties.StringProperty()),
    ('tags', properties.ListProperty(properties.StringProperty())),  ##needs updating
    ('analysis', properties.DictionaryProperty()), ##needs updating
    ])
class Sigma(object):
    """
    Place Holder
    """
    def __init__(self, Sigma_class=None, **kwargs):
        pass

sigma_rules_stix_bundle = []
for dirpath, dirnames, filenames in os.walk("sigma/rules/"):
    for files in filenames:
        file = yaml.safe_load_all(open(os.path.join(dirpath, files), 'r'))
        # print(file)
        for element in file:
            # print(element)
            sigma_rules_stix_bundle.append(Sigma(**element))
create_bundle(sigma_rules_stix_bundle)
