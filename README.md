# ImageCaptureAway

A Python script to batch download product images from Away Travel's website. Specifically designed to capture luggage color variants.

## Features

- 📸 Download high-quality product images
- 🎨 All color variants included
- 🔄 Automatic naming by color

## Included Colors

- Jet Black
- Navy Blue
- Coast Blue
- Olive Green
- Sea Green
- Cloud Gray
- Clay Pink
- Sorbet Orange
- Tango Red
- Salt White (Gloss)
- Wave Blue (Gloss)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python captureaway.py
```

Images will be saved to the current directory as `{Color Name}.jpg`.

## Output

```
Downloaded Jet Black.jpg
Downloaded Navy Blue.jpg
Downloaded Coast Blue.jpg
...
```

## Note

This script downloads from Away Travel's public CDN. Product IDs may change; update the `colors` dictionary if images are no longer available.

## License

MIT License - see [LICENSE](LICENSE) for details.
