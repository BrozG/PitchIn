#!/bin/bash
# Convert readme-intro.mp4 to GIF for better README display
# Requires ffmpeg installed

INPUT="resource/readme-intro.mp4"
OUTPUT="resource/demo.gif"

echo "🎬 Converting video to GIF..."

if [ ! -f "$INPUT" ]; then
    echo "❌ Input file not found: $INPUT"
    exit 1
fi

# Check if ffmpeg is installed
if ! command -v ffmpeg &> /dev/null; then
    echo "❌ ffmpeg is not installed. Please install it first:"
    echo "   Ubuntu/Debian: sudo apt install ffmpeg"
    echo "   macOS: brew install ffmpeg"
    echo "   Windows: Download from https://ffmpeg.org/download.html"
    exit 1
fi

# Convert to GIF (optimized for README display)
ffmpeg -i "$INPUT" \
  -vf "fps=10,scale=800:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" \
  -loop 0 \
  "$OUTPUT"

if [ $? -eq 0 ]; then
    echo "✅ Successfully created: $OUTPUT"
    echo "📏 Size: $(du -h "$OUTPUT" | cut -f1)"
    echo "📋 Update your README.md to use:"
    echo "   <img src=\"$OUTPUT\" alt=\"Pitch In Demo\" width=\"800\" />"
else
    echo "❌ Conversion failed"
    exit 1
fi