# Changelog

## [v1.2.0] - 2025-12-21
### Added
- **`PICO_DOC_STANDARD.md`**: Human-readable source of truth with definitions and versioning.
- **`PICO_DOC_SCHEMA.yaml`**: Machine-readable validation rules for automation.
- **`PICO_GOLDEN_PROJECT.md`**: Reference implementation (Project 0291) for visual comparison.
- **Audit Status Block**: Mandatory footer for every project file to track compliance.
- **Definitions Section**: Explicit terms for "Project", "Interactive Component", etc.

### Changed
- **Pin Standards**: Enforced specific pins for LEDs (GP15, GP14) and Buttons (GP16, GP17) to ensure consistency across 2500 projects.
- **Validation Logic**: Split "Human Rules" from "Machine Schema" to enable CI/CD.

### Fixed
- **Ambiguity**: Removed overlap between sections (e.g., pins only in Wiring, variable descriptions only in Variables).
