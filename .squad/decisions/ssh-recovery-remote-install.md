---
date: 2026-03-29
author: Sevro
title: SSH Key Recovery — Remote-Install Commands (Corrected)
---

# SSH Key Remote-Install: Safe Commands for DigitalOcean Console

**Confirm target account:** Is console logged in as <LOGIN_USER> or as root with <LOGIN_USER> elsewhere?

## Case A: Console logged in as <LOGIN_USER>

```bash
mkdir -p ~/.ssh && chmod 700 ~/.ssh
echo "<PASTE_PUBLIC_KEY_HERE>" >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

## Case B: Console logged in as root, SSH user is <LOGIN_USER>

```bash
sudo -u <LOGIN_USER> bash -c 'mkdir -p ~/.ssh && chmod 700 ~/.ssh'
echo "<PASTE_PUBLIC_KEY_HERE>" | sudo -u <LOGIN_USER> tee -a ~<LOGIN_USER>/.ssh/authorized_keys
sudo -u <LOGIN_USER> chmod 600 ~<LOGIN_USER>/.ssh/authorized_keys
```

## Verify from macOS

```bash
ssh -i ~/.ssh/id_blog_migration <LOGIN_USER>@<DROPLET_IP> "echo 'SSH OK'"
```

---

## Rationale

- **Case A** assumes you control the target account directly; uses `~` expansion for simplicity.
- **Case B** uses `sudo -u` to operate within the target user's home directory when console runs as root, avoiding permission/ownership issues.
- Both append (never clobber) with `>>` or `tee -a` for safety.
- Permissions: 700 on `~/.ssh/`, 600 on `authorized_keys` (standard SSH security).
