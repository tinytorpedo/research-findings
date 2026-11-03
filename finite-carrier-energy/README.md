# Finite carrier bounds for signed arithmetic energy

Paper and retrospective audit packet, 3 November 2026.

## Files

- [Paper (PDF)](Finite_carrier_energy.pdf)
- [Editable paper (DOCX)](Finite_carrier_energy.docx)
- [Audit packet (ZIP)](Finite_carrier_energy_audit.zip): manuscript source, typeset paper, verifier, U=40 and U=80 results, analytic audit, seven recovered source transcriptions, provenance and internal SHA-256 manifest.
- [SHA-256 checksums](SHA256SUMS): checksums of the three separately delivered files, published unchanged.

## Reproduce

Extract the audit ZIP into a working directory, then run with Python 3 and its standard library:

```sh
python3 verify_energy.py 40
python3 verify_energy.py 80
```

Run with assertions enabled; do not use `-O` or `-OO`. Both commands write their respective result JSON next to the script. Fresh runs on 3 November 2026 passed and reproduced both delivered JSON files byte for byte. The checks test exact finite source identities, Gram algebra, signs and endpoint sensitivity. They do not certify the asymptotic estimates or inherited role gates.

## Scope

The manuscript presents the bare-source logarithmic sixth-power bound using stated classical inputs. The repeated-decorator fifth-power refinement remains conditional on explicitly displayed inherited marked-role, physical-map and core-mass inputs. No unspecified native/production transfer or complete fifth-power energy theorem is claimed. The accompanying audit is internal retrospective review, not external peer review or a novelty assessment.

## Artifact and privacy notes

The standalone PDF and the PDF within the original audit ZIP have different bytes and separate hashes. Both have 12 pages and identical extracted text. The standalone DOCX matches the bundled DOCX exactly. The original delivered artifacts are preserved rather than silently repackaged.

Recursive inspection covered ZIP sources, DOCX XML, and extracted text from both PDFs; no personal filesystem paths, private file identifiers, emails or common credential patterns were detected. Historical unpublished/private-preparation statements inside the packet describe its preparation-time status, before this public release.
