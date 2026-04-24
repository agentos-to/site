---
title: secrets
description: "Skills in the secrets category."
sidebar:
  label: Overview
  order: -1
---

**1** skills in `secrets`.

- [**1Password**](/skills/reference/secrets/onepassword/) — Credential provider backed by the 1Password CLI (`op`). Exposes Login and API-Credential vault items via `@provides(login_credentials)` and `@provides(api_key)` so skills' `login` tools can pull `{email, password}` or API keys without the user pasting anything
