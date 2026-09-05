# Backup & Recovery Operations Architecture

## Executive Summary

1. **The 3-2-1-1-0 Backup Rule**:
   - **3** copies of critical data.
   - **2** different storage media types.
   - **1** copy located offsite in a secondary cloud region.
   - **1** copy stored **immutable (WORM Object Lock)**.
   - **0** errors on automated recovery restore drills.
2. **Automated Monthly Restore Testing**:
   - A scheduled CI/CD job spins up an ephemeral staging database, restores the latest production backup snapshot, executes synthetic integrity queries, and logs success before terminating.
