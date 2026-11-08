# Example PR description

This is a sample of the expected format and level of detail.

## What
Adds automatic retries with exponential backoff to the API client.

## Why
Transient network errors were failing whole jobs. Retrying a few times makes the client resilient without manual reruns.

## Changes
- Add `retry_with_backoff()` helper in `client/retry.py`
- Wrap all outgoing requests in the helper (max 3 attempts)
- Add unit tests covering success, retry and final failure
- Remove the unused `legacy_request()` function