#!/bin/bash

link=" https://tinyurl.com/EVAL-PEERCluster5"
output_image="qrcode.png"

# Generate QR code
qrencode -s 50 -o "$output_image" "$link"

echo "QR code generated for: $link"
echo "Image saved as: $output_image"
