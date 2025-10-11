#!/bin/bash
set -e

# Create a core named "mycore" with the default "_default" configset
echo "Creating Solr core: mycore"
/opt/solr/bin/solr create_core -c mycore -d _default
