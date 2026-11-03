# Public release preparation

Personal filesystem paths and Space file identifiers were removed from the public copies. The original delivered versions were preserved privately. Core file checksum manifests were refreshed; the addendum core-ZIP checksum and manuscript companion checksum were updated. The manuscript Python minimum was corrected to 3.10. No arithmetic implementation or numerical output was altered.

Sanitized source files:

- `native-cover-certificate-note-20261102-v2/V1_REFERENCE.json`
- `native-cover-certificate-note-20261102-v2/AUDIT_STATUS.md`
- `native-cover-certificate-note-20261102-v2/PORTABILITY_CORRECTION.md`
- `native-cover-certificate-note-20261102-v2/V2_VALIDATION.json`
- `native-cover-independent-audit-addendum/README.md`
- `native-cover-independent-audit-addendum/logs/mutation-boundary_include1680.log`
- `native-cover-independent-audit-addendum/logs/mutation-wrong_capacity.log`
- `native-cover-independent-audit-addendum/logs/mutation-same_clock_pair.log`
- `native-cover-independent-audit-addendum/logs/mutation-wrong_overlap_orientation.log`

All public ZIP contents and DOCX XML parts were scanned for personal paths, Space identifiers, and common credential patterns. A fresh full addendum audit against these public ZIP bytes passed on Linux on 3 November 2026: strict core reproduction, independent sieve and boundary/orientation checks, and rejection of all four deliberate mutations.
