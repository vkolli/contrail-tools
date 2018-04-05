#!/usr/bin/env bash

TOOLS_WS=${TOOLS_WS:-$(pwd)}
source $TOOLS_WS/testers/utils
source $TOOLS_WS/testers/utils_virtual
testbeds=(${TESTBED_CONFIG//,/ })
# AVAILABLE_TESTBEDS is a comma separated list of testbed filenames or paths
get_testbed
launch_testbed_hybrid_5_0
unlock_testbed $TBFILE_NAME
