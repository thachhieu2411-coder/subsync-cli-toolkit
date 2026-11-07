# SubSync CLI Toolkit

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/Python-3.9%2B-green.svg)
![Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)
![Coverage](https://img.shields.io/badge/Coverage-94%25-success.svg)

**SubSync CLI Toolkit** is a lightweight, dependency-free Python command-line utility engineered for automated SRT subtitle timestamp synchronization, text normalization, and audio-script drift alignment. Designed specifically for content creators, open-source maintainers, and media automation workflows.

---

## Key Features

- **Accurate Timestamp Shifting:** Millisecond-level positive/negative offset adjustment across all subtitle cue points.
- **Overlap Resolution:** Automatic detection and correction of collision cues where consecutive subtitle display times conflict.
- **Text & Tag Normalization:** Cleans redundant HTML styling tags (`<i>`, `<b>`, `<font>`) and optimizes whitespace formatting for Text-to-Speech (TTS) pipelines.
- **Silence Drift Detection:** Module interface for calculating audio track silence intervals and voice onset delays.
- **Pure Python Design:** Fast execution with standard libraries and minimal external overhead.

---

## Project Structure

    subsync-cli-toolkit/
    ├── examples/
    │   └── sample.srt             # Sample dataset with intentional overlap cues
    ├── tests/
    │   └── test_parser.py         # Unit tests covering parsing and overlap logic
    ├── audio_sync.py              # Silence detection and timeline drift engine
    ├── main.py                    # CLI application entrypoint
    ├── requirements.txt           # Environment specifications
    ├── utils.py                   # Subtitle cleaning and formatting helpers
    ├── CONTRIBUTING.md            # Guidelines for open-source contributors
    └── LICENSE                    # MIT License

---

## Installation

Clone the repository and install required dependencies:

    git clone https://github.com/thachhieu2411-coder/subsync-cli-toolkit.git
    cd subsync-cli-toolkit
    pip install -r requirements.txt

---

## Quick Usage

### 1. Shift Subtitle Timestamps
Shift entire subtitle file forward by 500ms:

    python main.py --input examples/sample.srt --output aligned.srt --shift 500

### 2. Auto-Clean & Fix Overlaps
Automatically resolve overlapping cue timestamps and normalize whitespace:

    python main.py --input examples/sample.srt --output cleaned.srt --clean

### 3. Run Unit Tests
Execute the test suite to verify parser integrity:

    python -m unittest tests/test_parser.py

---

## Contributing

Contributions, bug reports, and feature proposals are welcome! Please review [CONTRIBUTING.md](CONTRIBUTING.md) before submitting pull requests.

## License

This project is open-sourced under the [MIT License](LICENSE).
