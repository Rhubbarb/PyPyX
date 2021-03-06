#!/bin/bash

### ImageMagick

if [ "$1" != "" ]
then

fn="$1"

convert \
		-units PixelsPerInch \
		-density 180 \
		-alpha activate \
		-antialias \
		"${fn}.pdf" \
		"${fn}_trans.png"

convert \
		-flatten \
		"${fn}_trans.png" \
		"${fn}.png"

rm "${fn}_trans.png"

fi
