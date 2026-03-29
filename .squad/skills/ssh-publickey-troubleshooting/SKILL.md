---
name: "ssh-publickey-troubleshooting"
description: "How to guide a user through low-risk diagnosis of SSH Permission denied (publickey) failures"
domain: "access-debugging"
confidence: "high"
source: "observed"
---

## Context

Use this when a user is trying to connect manually over SSH and gets `Permission denied (publickey)`. The goal is to diagnose the blocker without asking for secrets, changing server config blindly, or skipping straight to risky fixes.

## Patterns

### Translate the error plainly

- Explain that the network path likely works, but the server rejected every key the client offered.
- Make it clear this is usually an identity mismatch, not a server outage.

### Start with local evidence only

- First inspect `~/.ssh/*.pub` so the user can see whether they even have public keys locally.
- Then inspect agent state with `ssh-add -l` to see whether SSH will offer any loaded identities automatically.
- Keep the first batch to 2-4 safe read-only commands.

### Tell the user what to look for after each command

- Missing `.pub` files usually means no usable keypair is present.
- `The agent has no identities` means keys exist but are not currently loaded into the SSH agent.
- Seeing a key fingerprint in the agent output means the agent is loaded; the next questions become username, authorized_keys, and which key the server expects.

### Branch the diagnosis explicitly

- Wrong username: `root`, `ghost`, `deploy`, and personal usernames are not interchangeable.
- Missing keypair: user has no local SSH key material.
- Wrong key file: user has a key, but SSH is offering a different one than the server trusts.
- Agent not loaded: key exists on disk but is not being offered.
- Server not authorized: the public key is not in the target account's `~/.ssh/authorized_keys` or access is configured for another user/account.

### Escalate only after the read-only checks

- If the first batch is inconclusive, move to `ssh -v user@host` or `ssh -i ~/.ssh/<key> -v user@host` to see which keys are offered and rejected.
- Do not tell the user to regenerate keys or edit server files until the evidence points there.

## Examples

- Good: `ls -la ~/.ssh && find ~/.ssh -maxdepth 1 -type f \( -name "*.pub" -o -name "id_*" \) | sort` followed by a note about expected key filenames.
- Good: `ssh-add -l` followed by interpretation of `The agent has no identities`.
- Bad: telling the user to disable host key checking or chmod random files on the server before confirming the client is offering the right key.

## Anti-Patterns

- Asking the user to paste private key contents
- Treating `Permission denied (publickey)` as proof the host is down
- Assuming the SSH username matches the blog or OS username without verification
- Jumping straight to server-side changes before checking local key and agent state
