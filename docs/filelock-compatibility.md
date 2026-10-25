# Filelock Compatibility Evidence

Checked on 2026-10-25 against the official GitHub Advisory Database endpoint
`GET /advisories?ecosystem=pip&affects=filelock&per_page=100` (eight advisories).
The table records affected ranges, not inferred exploitability of a caller.

| Advisory | Published affected range | First patched version |
| --- | --- | --- |
| [GHSA-w853-jp5j-5j7f](https://github.com/advisories/GHSA-w853-jp5j-5j7f) | `<3.20.1` | 3.20.1 |
| [GHSA-qmgc-5h2g-mvrw](https://github.com/advisories/GHSA-qmgc-5h2g-mvrw) | `<3.20.3` | 3.20.3 |
| [GHSA-v4x8-3wr5-3wq8](https://github.com/advisories/GHSA-v4x8-3wr5-3wq8) | `>=3.20.4,<=4.2.0` | 4.2.1 |
| [GHSA-9vhv-jxww-xfm5](https://github.com/advisories/GHSA-9vhv-jxww-xfm5) | `>=3.20.4,<=4.2.0` | 4.2.1 |
| [GHSA-567q-5qvw-pf92](https://github.com/advisories/GHSA-567q-5qvw-pf92) | `>=3.22.0,<=4.2.0` | 4.2.1 |
| [GHSA-jqc4-5cvw-7w85](https://github.com/advisories/GHSA-jqc4-5cvw-7w85) | `>=4.1.0,<=4.2.0` | 4.2.1 |
| [GHSA-2g95-wg33-c5x2](https://github.com/advisories/GHSA-2g95-wg33-c5x2) | `>=4.1.0,<=4.2.0` | 4.2.1 |
| [GHSA-crv4-6mhj-j5jh](https://github.com/advisories/GHSA-crv4-6mhj-j5jh) | `>=4.1.0,<=4.2.0` | 4.2.1 |

Exact 3.20.3 falls outside every recorded affected range. PyPI's release metadata
requires Python >=3.10 for 3.20.3 and >=3.11 for 4.2.1/4.2.4. Consequently this
fork uses 3.20.3 only on Python 3.10 and requires >=4.2.1,<5 on newer Python.
The fork itself requires Python >=3.10; it does not advertise older support.

This is a reviewed dependency selection in actual package metadata. No scanner
exception or resolver-only override is used. Future advisories can invalidate a
pin and must still fail the consuming application's normal security checks.
Classic ComboLock and NamedLock calls remain unchanged; the compatibility suite
checks real process/thread exclusion, context reuse and requested permissions.
