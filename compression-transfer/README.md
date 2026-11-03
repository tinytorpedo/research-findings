# Phase pair and ellipse predictors for lossless compression

A retrospective evidence study of complete archive size, exact reconstruction, and transfer. Published 3 November 2026.

## Files

- [Paper (PDF)](Phase_pair_and_ellipse_compression.pdf)
- [Editable paper (DOCX)](Phase_pair_and_ellipse_compression.docx)
- [Reproducibility packet (ZIP)](Phase_pair_and_ellipse_reproducibility.zip)
- [SHA-256 checksums](SHA256SUMS)

The three reviewed deliverables are published unchanged. The packet contains transcribed measurements, selected historical hashes, a portable arithmetic audit and its results, review and replication protocol, and the receipt for 37 retained-artifact decoding checks.

## Reproduce the included arithmetic audit

Extract the ZIP, then run with Python 3 and its standard library:

```sh
python3 audit_measurements.py
```

This recalculates accounting and measurement consistency. A fresh pre-publication run passed all 27 checks and matched the delivered result JSON. It is not a codec, a new corpus encode, an archive-decode test, or verification of historical object hashes. The 37 decoding checks described in `FRESH_REPLAY.txt` are a separate recorded replay and were not rerun for this publication.

## Scope and rights

The study reports narrow, data-dependent gains, neutral controls and negative results. Development CSV, independent simulated transfer, operator-informed response tables, retrospective fixed-family comparisons, and the distinct audio adaptation remain separate. The two-byte I19 result is marginal; I20 is unexecuted.

No private simulation payloads, audio, original benchmark archives, third-party source code or datasets are redistributed. This packet does not grant rights in underlying datasets or implementations and is not a public runnable codec release. See the included replication protocol for missing inputs and prerequisites.

## Integrity and privacy

The standalone DOCX matches the bundled DOCX exactly. The standalone and bundled PDFs differ bytewise but have identical extracted text and six pages; their original delivered bytes and separate checksums are preserved. Recursive inspection of the ZIP and DOCX XML, and text inspection of both PDFs, found no personal filesystem paths, private file identifiers, emails or common credential patterns.
