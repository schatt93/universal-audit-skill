# Module Reference

Modules are selected on the merits of the actual artifact in **Stage A** — the skill does **not** run all of them. Codes are one-letter (`A`–`Z`) or two-letter (`AA`–`AQ`); **`AI` is intentionally skipped** to avoid colliding with Module K (AI/ML). **Modules X and Y run on any file.**

## Group 1 — System & Quality (A–W)

| | Module | Scope |
|---|---|---|
| A | Security | authN/Z, secrets, injection/XSS/SSRF, attack surface (STRIDE, OWASP, NIST SSDF) |
| B | Privacy & Data Protection | lawful basis, minimization, retention, PII in logs (GDPR/DPDP, LINDDUN, ISO 27701) |
| C | UI/UX & Interaction Design | IA, affordances, all UI states (Nielsen heuristics) |
| D | Accessibility | perceivable/operable/understandable/robust (WCAG, ARIA, EN 301 549, WCAG-EM) |
| E | Performance & Efficiency | latency, scalability, caching, Core Web Vitals (ISO 25010) |
| F | Reliability, Resilience & Ops (SRE) | SLO/SLI, failover, DR (RTO/RPO), FMEA, chaos |
| G | Code Quality & Maintainability | complexity, smells, ISO 25010/5055, DORA/SPACE |
| H | Software Architecture & Design | coupling/cohesion, SOLID, C4, Well-Architected, ADRs |
| I | API & Integration | versioning, idempotency, error contracts, OpenAPI/contract tests |
| J | Data, Modeling & Analytics | schema, statistical validity, lineage (ISO 25012, DAMA-DMBOK) |
| K | AI / ML / LLM Systems | eval, bias, robustness, prompt-injection, agency (NIST AI RMF, OWASP LLM/Agentic, ISO 42001) |
| L | Test & QA Coverage | unit→E2E, negative/boundary, mutation, coverage |
| M | Compatibility & Cross-Platform | browsers/devices/runtimes, graceful degradation |
| N | Internationalization & Localization | encoding, formats, RTL, text expansion (CLDR) |
| O | Documentation & Content Quality | accuracy, readability, citation integrity, originality |
| P | SEO & Discoverability | metadata, structured data, crawlability |
| Q | Compliance, Legal & Regulatory | control-mapping to the named regime(s); COBIT, SOC 2 |
| R | Dependency & Supply-Chain | CVEs, licenses, SCA, SBOM, SLSA, OpenSSF Scorecard |
| S | Infrastructure, Cloud & IaC | least-privilege IAM, exposure, CIS Benchmarks, IaC scanning |
| T | Observability & Telemetry | logs/metrics/traces, OpenTelemetry, SLO alerting |
| U | Cost / FinOps & Sustainability | cost model, unbounded spend, right-sizing, energy/carbon |
| V | Brand, Design-System & Visual Consistency | tokens, component reuse, voice/tone |
| W | Business / Product / Project Governance | requirement quality, RACI, risk register, CMMI maturity |

## Group 2 — File-Format & Asset (X–AE)

| | Module | Scope |
|---|---|---|
| X | File Integrity & Format Conformance | magic-byte vs extension, corruption, spec conformance (JHOVE, veraPDF) |
| Y | Metadata, Properties & Provenance | EXIF/XMP, C2PA/Content Credentials, **PII leakage** (GPS/author/device) |
| Z | Image & Graphics | resolution, color/ICC, compression, SVG sanitization |
| AA | Audio | codec, loudness (LUFS, EBU R128), clipping, transcripts |
| AB | Video & Motion | container/codec, color/HDR, captions, streaming readiness |
| AC | 3D, CAD & Geometry | units/scale, manifold/watertight, UVs/materials (glTF, STEP, IFC) |
| AD | Archives, Packages & Binaries | zip-bombs, Zip-Slip, code-signing, malware/polyglot |
| AE | Specialized Formats | geospatial (CRS/EPSG), scientific/medical (DICOM PHI), fonts, e-books |

## Group 3 — Specialized Professional Domains (AF–AQ)

| | Module | Scope |
|---|---|---|
| AF | Financial Controls & SOX / ICFR | COSO, PCAOB AS 2201, ITGCs, material-weakness evaluation |
| AG | Hardware, Firmware & Safety-Critical | IEC 61508, ISO 26262, DO-178C/254, SOTIF, ISO 21434 |
| AH | Scientific & Research Data Integrity | reproducibility, FAIR, ALCOA++, 21 CFR Part 11, ICH E6(R3) |
| AJ | Legal, Contract & Regulatory Review | clause/playbook review, obligation matrices (non-attorney) |
| AK | ESG & Sustainability Assurance | ISSB S1/S2, CSRD/ESRS, GHG Protocol, ISAE 3000 |
| AL | Smart Contract & Blockchain Security | reentrancy, access control, oracle/flash-loan (SWC, Slither, Echidna) |
| AM | Financial-Services Model Risk | independent validation, **SR 26-2** (supersedes SR 11-7 & SR 21-8) |
| AN | Medical-Device & Health Software | IEC 62304, ISO 14971, ISO 13485, FDA QMSR, EU MDR/IVDR |
| AO | Security Ops, IR & Forensics | NIST SP 800-61 r3 (CSF 2.0), chain of custody, MITRE ATT&CK |
| AP | Quality Management & Process | ISO 9001, Six Sigma/DMAIC, CAPA, SPC, 8D |
| AQ | Investment Research & Market-Analysis | reasonable basis, conflicts/certification, GIPS, FINRA 2241, MAR Art. 20, SEBI RA |

> The domain space is open-ended — beyond these, the universal passes (B1–B4) plus runtime standards-validation still apply. Universality comes from the **method**, not an exhaustive module list.
