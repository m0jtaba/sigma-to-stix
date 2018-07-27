#!/usr/bin/env python3
"""
Creating Custom Relationship Object Type for Sigma Rules
"""

import json
from stix2 import Relationship, Bundle

def main():
    """
    main
    """
    create_relationship()

def create_bundle(data):
    """
    Creates a bundle for the Sigma Rules relationship
    """
    file = open('sigma_rule_relationships.json', 'w')
    file.write(str(Bundle(data)))

def create_relationship():
    """
    Creates a relationship object for the Sigma Rules
    """
    stix_custom_relationship = []
    with open('attack_pattern.json', 'rt') as attack_pattern:
        attack_patterns = json.load(attack_pattern)
        for attack_pattern in attack_patterns:
            if 'attack-pattern' in attack_pattern['attack_pattern']:
                with open('sigma_rules_stix_bundle.json', 'rt') as sigma_rules_stix_bundle:
                    sigma_rules = json.load(sigma_rules_stix_bundle)
                    for sigma_rule in sigma_rules['objects']:
                        ## problem somewhere here could be fixed using .casefold() instead of .lower()
                        if 'tags' in sigma_rule:
                            for attacks in sigma_rule['tags']:
                                if attacks.lower().split("attack.")[-1] == attack_pattern['technique_id'].lower():
                                    relationship = Relationship(relationship_type="sigma_rules",
                                                                source_ref=sigma_rule['id'],
                                                                target_ref=attack_pattern['attack_pattern'],
                                                                created_by_ref="identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
                                                                description="Example",
                                                                revoked=False,
                                                                labels="Example",
                                                                external_references=[
                                                                    {
                                                                        "description": "Example",
                                                                        "source_name": "Example",
                                                                        "url": "https://example.com"
                                                                    }
                                                                ],
                                                                object_marking_refs=["marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"]
                                                                # granular_markings=["Example"],
                                                               )
                                    # print(relationship)
                                    stix_custom_relationship.append(relationship)
                                    print(stix_custom_relationship)
        create_bundle(stix_custom_relationship)

if __name__ == "__main__":
    main()
