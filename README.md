# Signed square support on projective rays

This package contains an ten-page mathematical note and a portable finite audit of its arithmetic core.

## Read

- `Signed_square_support_on_projective_rays.docx`: editable note with three theorems and proofs, an exact fixed-allocation refinement, defect bounds, a conditional quasi-Riemann interface, and a precise production gate.
- `I42_SIGNED_SCALE_ROLE_PROJECTIVE_RAY.md`: original supplied source report, unchanged.
- `verification.json`: results from the included verifier.
- `I54_ORIGINAL_TEXT.md` and `I109_WEIGHT_BINDING_TEXT.md`: complete transcriptions of the located original mathematical sources, with provenance and scope wrappers.
- `SOURCE_COVERAGE.md`: included source evidence, privacy transformations, and precisely named unresolved dependencies.
- `I54_CONVERSATION_EVIDENCE.md`, `I109_REPORT_TRANSCRIPTION.md`, and `I109_CONVERSATION_EVIDENCE.md`: recovered supporting evidence with source type and limitations.
- `QR_APPLICATIONS_ADDENDUM_TEXT.txt`: complete privacy-scrubbed text transcription of the three-page conditional applications addendum.
- `PACKAGE_VALIDATION.json`: clean-extraction, rerun, optimized-mode rejection, and privacy-scan outcomes.

## Reproduce

Run `python3 verify_ray.py` using Python 3.8 or later, without optimization flags (the script explicitly refuses `-O` and `-OO`). No dependencies, network access, or external data are required. The verifier writes `verification.json` beside itself. Typical runtime is under a few seconds on a modern computer.

The checks are retrospective and deterministic. The script independently implements the explicit identities; it is not the original I42 verifier. The 12 hostile witnesses are not represented as the source report's unavailable 28-mutation suite. No private production rows are synthesized or claimed recovered.

## Scope

The proofs establish the stated arithmetic identities for all positive integers under their hypotheses. Finite checks cover only their declared bounds. Neither proves a uniform weighted production estimate, identifies the ray scale with a prime-source argument, verifies a zero-free-region manuscript, or implies a prime theorem.

The fixed-allocation identity was reported in the later I54 discussion and is independently proved here. The conditional quasi-Riemann input is attributed to the inspected 7 October 2026 applications addendum; its proof and constants are not certified in this package. The note does not claim novelty priority or publication acceptance.

`SHA256SUMS.json` records all included files except itself.

## Revision 2

Adds the supporting source texts and a source-coverage inventory, refuses assertion-disabled execution, replaces the boundary witness with the actual chi6-filtered [5,7] case, and labels the scale/source substitution illustrative. No mathematical theorem or numerical-domain count changed.

## Revision 3

The original I54 report and I109 weight-binding companion were located and inspected. The source-coverage inventory and manuscript now distinguish recovered documents from the still-unproved legacy production bridge. The allocation-divisor hypothesis was already explicit. Historical verifier code and audit records were inspected, not rerun.
