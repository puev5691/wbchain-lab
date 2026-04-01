#!/data/data/com.termux/files/usr/bin/bash
cd "$(dirname "$0")"
cp deploy/wblab/fork-run-cerber.js fork-run.js
cd Source
node run-node.js CREATEONSTART
