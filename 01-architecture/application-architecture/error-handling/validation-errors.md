# Validation Error Architecture

## 1. Accumulative Validation
Never return only the first validation error. Collect all field-level validation failures into a structured list so clients can correct their input in a single pass.
