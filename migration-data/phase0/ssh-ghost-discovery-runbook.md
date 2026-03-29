# SSH Ghost Discovery Runbook
**Last updated:** 2026-03-29  
**Owner:** Sevro (Backend & Migration Dev)  
**Status:** Read-only inspection only — no configuration changes  
**Target:** Ubuntu / DigitalOcean droplet with Ghost  

---

## What This Runbook Does

Locates Ghost installation directories, active content folder, config files, theme location, and service info over SSH. After each block, success looks like specific output you can spot-check. At the end, you'll have a complete runtime inventory to share back to the squad.

---

## ⚠️ Prerequisites

- SSH access already working (you confirmed `it worked`)
- SSH user and host known (e.g., `user@host` or `root@192.168.x.x`)
- Local `migration-data/phase0/` workspace already created

---

## STEP 1: Preflight — Confirm Session & Permissions

**Run this first to verify who you are and where you are:**

```bash
whoami
pwd
id
```

**What success looks like:**
- `whoami` prints the SSH user (e.g., `root` or `ubuntu` or your username)
- `pwd` shows you're in a home or app directory (e.g., `/root` or `/home/ubuntu`)
- `id` shows group memberships; if you're not root, note whether you're in `sudo` group

**If you're not root and `id` does not list `sudo` group:** you may need `sudo` for some later steps. Proceed; we'll call it out.

---

## STEP 2: Find Ghost Process & Service Type

**Check if Ghost is running via systemd (most common on Ubuntu/DO):**

```bash
sudo systemctl status ghost
```

**If that fails, check for PM2:**

```bash
pm2 list
```

**If that also fails, look for Node processes directly:**

```bash
ps aux | grep -i ghost | grep -v grep
```

**What success looks like:**
- **systemd:** `systemctl` output shows `Active: active (running)` and a service description with path or user hints
- **PM2:** `pm2 list` shows a Ghost app with status, uptime, and PID
- **Manual:** `ps aux` shows a Node process with `ghost` in the command line or working directory

**If none of these find Ghost, stop and report:** "Cannot locate Ghost process via systemd, PM2, or ps. Ghost may not be running or installed."

---

## STEP 3: Locate Ghost Installation Directory

**Start with common locations (try each in order):**

```bash
ls -la /var/www/ghost/current/ 2>/dev/null || echo "Not at /var/www/ghost/current"
```

```bash
ls -la /home/*/ghost/ 2>/dev/null || echo "Not at /home/*/ghost/"
```

```bash
ls -la /opt/ghost/ 2>/dev/null || echo "Not at /opt/ghost/"
```

**If systemd service exists, extract the path from the service file:**

```bash
sudo grep -i "ExecStart\|WorkingDirectory" /etc/systemd/system/ghost.service 2>/dev/null || echo "No ghost.service file"
```

**If PM2 process exists, check PM2 config:**

```bash
pm2 show ghost 2>/dev/null | grep -i "cwd\|script" || echo "No PM2 ghost process"
```

**What success looks like:**
- You have a single directory path like `/var/www/ghost/` or `/home/ubuntu/ghost/` where you can see:
  - `package.json`
  - `content/` subdirectory
  - `config.production.json` or similar

**Hard stop:** If you find multiple candidates (e.g., `/var/www/ghost/` and `/home/ubuntu/ghost-backup/`), ask which one is currently active. Default to what the systemd/PM2 service points to.

**Record this path:** Save it as `$GHOST_HOME` for the next steps.

---

## STEP 4: Confirm Content Directory & Image Inventory

**Navigate into Ghost home and check content structure:**

```bash
ls -la $GHOST_HOME/content/
```

**What success looks like:**
- You see subdirectories like `images/`, `files/`, `media/`, `themes/`, etc.
- `images/` exists (this is critical for Phase 0 backup)

**Count the images (used for the manifest):**

```bash
find $GHOST_HOME/content/images -type f | wc -l
du -sh $GHOST_HOME/content/images
```

**What success looks like:**
- First command prints a number (count of image files)
- Second command prints a size like `2.3G` or `145M`

**If `images/` does not exist or is empty:** Note this. Ghost may be using external CDN or storage. Proceed to step 5.

**Record:** Image count and directory size for the manifest.

---

## STEP 5: Locate & Inspect Ghost Config File

**Look for config in the Ghost home directory:**

```bash
ls -la $GHOST_HOME/config.*.json
```

**What success looks like:**
- You see at least `config.production.json` (common) or `config.json`
- File is readable by your current user

**Read the config (do NOT copy it yet; just inspect):**

```bash
head -30 $GHOST_HOME/config.production.json
```

**What to look for in output:**
- Database section: `"mysql"` (uses MySQL) or `"sqlite3"` (uses SQLite)?
- Storage section: Is there a local `"local"` storage or external S3/CDN reference?
- If MySQL: capture the database connection string (you may see `database: "ghost"` and `host: "localhost"` or IP)

**If config file is not readable without sudo:** Note this — you'll need sudo for backup later.

**Record:** Database type (MySQL/SQLite) and whether storage is local or external.

---

## STEP 6: Check for Nginx/Site Config

**Look for Nginx site config (Ghost is usually behind Nginx on DO):**

```bash
ls -la /etc/nginx/sites-enabled/ | grep -i ghost
```

```bash
ls -la /etc/nginx/sites-available/ | grep -i ghost
```

**If found, inspect the active config:**

```bash
cat /etc/nginx/sites-enabled/*ghost* 2>/dev/null | head -40
```

**What success looks like:**
- You see an Nginx server block with:
  - `server_name` (your domain)
  - `proxy_pass http://localhost:2368` (or similar Ghost port)
  - SSL paths (`ssl_certificate`, `ssl_key`)

**If no Nginx config found:** Ghost may be accessible directly (less common). Proceed.

**Record:** Nginx config path and domain name.

---

## STEP 7: Locate Active Theme

**Check what theme is currently active:**

```bash
ls -la $GHOST_HOME/content/themes/
```

**What success looks like:**
- You see multiple theme directories (e.g., `default/`, `casper/`, `custom-theme/`)
- Most recent or largest directory is likely active

**Check Ghost config to confirm active theme:**

```bash
grep -i "theme" $GHOST_HOME/config.production.json
```

**What success looks like:**
- You see a key like `"theme": "casper"` or `"theme": "custom-theme"`

**Check if the active theme has custom code:**

```bash
find $GHOST_HOME/content/themes/ACTIVE_THEME_NAME -name "*.js" -o -name "*.hbs" | head -10
```

**Record:** Active theme name and whether it has custom partials/JavaScript.

---

## STEP 8: Database Engine & Size Check

**Confirm database type (from config in step 5, or run):**

```bash
file $GHOST_HOME/content/data/ghost.db 2>/dev/null && echo "SQLite detected" || echo "Likely MySQL"
```

**If MySQL, check if it's listening locally:**

```bash
sudo netstat -tlnp 2>/dev/null | grep -i mysql || netstat -tlnp 2>/dev/null | grep -i mysql || echo "netstat may need sudo"
```

**If SQLite, get database size:**

```bash
ls -lh $GHOST_HOME/content/data/ghost.db 2>/dev/null || echo "No SQLite database found"
```

**What success looks like:**
- For SQLite: file size printed (e.g., `145M`)
- For MySQL: port 3306 shown in netstat output, or note that you cannot see it without sudo

**Record:** Database engine type and size.

---

## STEP 9: Verify SSH User & Permissions for Backup Steps

**Check current user's home directory (for key storage):**

```bash
echo $HOME
ls -la ~/.ssh/ 2>/dev/null | head -5 || echo "No .ssh directory yet (can create it)"
```

**Check if you have read access to the Ghost directory:**

```bash
test -r $GHOST_HOME/config.production.json && echo "Config is readable" || echo "Config NOT readable (may need sudo)"
```

**Check if you need sudo for database:**

```bash
sudo ls -la /var/lib/mysql/ghost/ 2>/dev/null | head -2 && echo "MySQL accessible via sudo" || echo "MySQL not accessible or not local"
```

**Record:** Current SSH user, whether sudo is available, and which files/dirs need sudo for reading.

---

## STEP 10: Compile Runtime Inventory

**Run this final block to create a complete snapshot (copy the output to the runbook summary below):**

```bash
cat << 'EOF'
=== GHOST DISCOVERY SUMMARY ===
GHOST_HOME: $GHOST_HOME
SSH_USER: $(whoami)
TIMESTAMP: $(date -u +%Y-%m-%dT%H:%M:%SZ)
UNAME: $(uname -a)
GHOST_PROCESS: $(ps aux | grep -i "node.*ghost\|pm2.*ghost" | grep -v grep | head -1)
SYSTEMD_STATUS: $(sudo systemctl is-active ghost 2>/dev/null || echo "N/A")
CONFIG_FILE: $(ls -lh $GHOST_HOME/config.production.json 2>/dev/null | awk '{print $9, $5}' || echo "NOT FOUND")
DATABASE_TYPE: $(grep -o '"database":"[^"]*' $GHOST_HOME/config.production.json 2>/dev/null | cut -d'"' -f4 || echo "UNKNOWN")
CONTENT_IMAGES_SIZE: $(du -sh $GHOST_HOME/content/images 2>/dev/null | awk '{print $1}' || echo "N/A")
CONTENT_IMAGES_COUNT: $(find $GHOST_HOME/content/images -type f 2>/dev/null | wc -l || echo "N/A")
ACTIVE_THEME: $(grep -o '"theme":"[^"]*' $GHOST_HOME/config.production.json 2>/dev/null | cut -d'"' -f4 || echo "UNKNOWN")
NGINX_CONFIG: $(ls /etc/nginx/sites-enabled/*ghost* 2>/dev/null | head -1 || echo "NOT FOUND")
NGINX_DOMAIN: $(grep "server_name" /etc/nginx/sites-enabled/*ghost* 2>/dev/null | head -1 || echo "NOT FOUND")
PERMISSIONS_CHECK: $(test -r $GHOST_HOME/config.production.json && echo "Can read config" || echo "Cannot read config (need sudo?)")
SUDO_AVAILABLE: $(sudo -n true 2>/dev/null && echo "YES" || echo "NO or requires password")
=== END SUMMARY ===
EOF
```

**Copy the output block and paste it here for the squad:**

---

## Success Checklist

After running all 10 steps, you should have:

- [ ] **Ghost home directory** identified and verified
- [ ] **Content/images** counted and sized
- [ ] **Config file** located and database type confirmed
- [ ] **Active theme** identified
- [ ] **Nginx/site config** found (or noted as absent)
- [ ] **SSH user & permissions** documented
- [ ] **Runtime inventory** (final block output) copied and ready to share

---

## Hard Stop Conditions

**Do NOT proceed to Phase 0 raw backup until you can answer:**

1. **Where is Ghost installed?** (exact path)
2. **What database does it use?** (MySQL, SQLite, or unknown?)
3. **Do you have read access to config, content, and DB files?** (or do you need sudo?)
4. **Are images stored locally or on a CDN?** (if CDN, which one?)
5. **Is Ghost currently running?** (systemd, PM2, or manual?)

If any of these are unclear, stop and ask for help. Do not guess.

---

## Next Steps (for Sevro)

Once Romulus runs this walkthrough and pastes back the runtime inventory:
1. Validate counts against Ghost metadata
2. Update `migration-data/phase0/manifests/runtime-inventory.txt`
3. Confirm with Mustang that Phase 0 scope is achievable
4. Move to Phase 0 raw capture steps (admin export, DB backup, image download, etc.)

---

**End of runbook.**
