# Audio Compression Testing Software

## Project Description
This project implements software for testing audio compression methods based on splitting the signal into parts (usually in the frequency domain, though other approaches are possible). Each subband undergoes separate compression, followed by a quality evaluation after decompression.

The architecture allows flexible testing of various combinations of compression and quality assessment methods through a well-defined class structure.

This project was carried out as part of a master's thesis on audio compression methods and sound quality evaluation.

## Features
- **Signal splitting** – Use of filter banks to separate the signal into subbands.
- **Compression and decompression** – Testing various compression algorithms on individual subbands.
- **Quality evaluation** – Using objective methods to analyze quality degradation after compression.
- **Modular architecture** – Easily extendable with new compression and evaluation methods.

## Code Structure
- `main.py` – Main script that defines the test samples and combinations of compression and evaluation methods.
- `*Divider.py` – Implementation of DividerBase, including QMF filter banks and other signal splitting methods.
- `*Compressor.py` – Various compression algorithms, including CELP and its modifications, CompressorBase implementation.
- `*CompressionQualityMeasurer.py` – Methods for assessing audio quality after decompression, implementation of CompressionQualityMeasurerBase.

This repository mainly provides the class structure and defines the methodology for testing audio compression methods. The actual compression and evaluation tools are not included and need to be obtained separately.
