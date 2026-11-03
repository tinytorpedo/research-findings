# Finite covering certificate for twin-prime candidates

## Contents

- `covering_certificate_manuscript.docx`: manuscript, titled *An auditable covering certificate for twin prime candidates in a finite square band*, by Justin Ayars. Author-review draft dated 2 November 2026, with AI assistance disclosed.
- `native-cover-certificate-note-20261102-v2.zip`: frozen core reproducibility packet.
- `native-cover-independent-audit-addendum-20261102.zip`: subsequent internal audit, independent sieve check, mutation tests, and Linux reproduction logs.
- `SHA256SUMS`: checksums of these three public-release artifacts.

## Result and limits

For the known band between 37² and 41², the strict domain has 51 centers, of which 15 survive the roughness filter. The calculation gives 9 active incidences, 1 double hit, and exactly 7 twin-prime centers. The four information-restricted covering relaxations have exact maxima 15, 15, 9, and 8.

This is a retrospective, AI-assisted internal reproducibility study. It is not independent human peer review, a new inclusion–exclusion theorem, a uniform Jacobsthal bound, a proof of infinitely many twin primes, or predictive validation on unseen data. The 644-band component checks consistency of archived records, not fresh arithmetic for those bands.

## Reproduce

Use Python 3.10 or later, with 3.12 recommended, and only its standard library. Do not use `-O`, which disables assertions. Extract the addendum, then run:

```sh
python -B native-cover-independent-audit-addendum/audit.py native-cover-certificate-note-20261102-v2.zip new-audit-directory
```

The output directory must not exist. The audit verifies the core ZIP hash, runs the core's strict byte-for-byte reproduction, independently checks the finite arithmetic using an Eratosthenes sieve, and verifies rejection of four corrupted cases. No network access or package installation is needed.

For the core alone, extract its ZIP, enter `native-cover-certificate-note-20261102-v2`, and run:

```sh
python -B reproduce.py ../new-core-reproduction
```

## Documentation clarifications

- This public manuscript corrects the Python requirement to 3.10+ and updates its companion ZIP checksum.
- Creation-time files in the core describe Linux validation as pending. The later addendum records the Linux pass.
- Personal filesystem paths and Space identifiers were removed from public copies. Historical failed-check records remain, with path placeholders.
- Original delivered artifacts remain preserved privately. Public copies have refreshed checksums; arithmetic implementations and frozen numerical evidence are unchanged. Their historical status statements describe their creation-time context.

## Publication preparation check

On 3 November 2026, a fresh Linux run of the addendum passed the core strict-byte reproduction, independent sieve/boundary/orientation check, and all four mutation rejection controls. This remains internal computational validation, not external peer review.
