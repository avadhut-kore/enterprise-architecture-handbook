# HL7 v2 Architecture and MLLP Transport Protocol

## 1. Message Structure: Segments, Fields, and Delimiters
HL7 v2 uses pipe-and-hat ASCII formatting with standardized encoding characters:
- Field Separator: `|` (Pipe)
- Component Separator: `^` (Hat)
- Subcomponent Separator: `&` (Ampersand)
- Repetition Separator: `~` (Tilde)
- Escape Character: `\` (Backslash)

## 2. Minimal Lower Layer Protocol (MLLP)
Because raw TCP streams do not provide message boundaries, HL7 v2 transmits packets wrapped in MLLP framing characters:
- **Start Block**: Single byte `0x0B` (`<VT>`).
- **Data Payload**: ASCII / UTF-8 HL7 text.
- **End Block**: Two bytes `0x1C` (`<FS>`) followed by `0x0D` (`<CR>`).
