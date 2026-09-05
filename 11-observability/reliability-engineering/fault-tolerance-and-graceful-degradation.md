# Fault Tolerance & Graceful Degradation Architecture

## Executive Summary

When a downstream dependency (e.g., Personalization Recommendation Engine) fails:
- **Catastrophic Design**: The entire checkout page throws HTTP 500; the user cannot purchase.
- **Graceful Degradation Design**: The checkout page catches the timeout; gracefully hides the recommendations widget or renders a static cache of popular items; the checkout transaction succeeds.
