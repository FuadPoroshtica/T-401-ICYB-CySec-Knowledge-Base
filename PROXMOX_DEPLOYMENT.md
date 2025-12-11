# Proxmox LXC Deployment

## 🎉 Deployment Complete!

Your CySec Knowledge Base wiki has been successfully deployed to Proxmox!

## 📊 Container Details

- **Container ID**: 116
- **Hostname**: cysec-wiki
- **IP Address**: 192.168.148.134
- **OS**: Debian 12 (Bookworm)
- **Memory**: 1GB
- **CPU Cores**: 2
- **Disk**: 8GB

## 🌐 Access Information

**Wiki URL**: http://192.168.148.134

You can access the wiki from any device on your network at this address.

**Root Password**: WikiPass2024!

## 📦 Installed Software

- Python 3.11
- MkDocs 1.6.1
- MkDocs Material Theme 9.7.0
- Nginx 1.22.1
- Git
- curl

## 🔄 Updating the Wiki

### Method 1: Using the Update Script (Recommended)

If you make changes to the wiki content, you can update it with:

```bash
# 1. Copy new files to Proxmox host
cd /home/fuad/Documents/T-401-ICYB-CySec-Knowledge-Base
tar czf /tmp/wiki-content.tar.gz --exclude='site' --exclude='docs_mkdocs' --exclude='.git' .
scp /tmp/wiki-content.tar.gz root@192.168.148.254:/tmp/

# 2. Update container
ssh root@192.168.148.254 "pct push 116 /tmp/wiki-content.tar.gz /tmp/wiki-update.tar.gz"
ssh root@192.168.148.254 "pct exec 116 -- bash -c 'cd /var/www/wiki && tar xzf /tmp/wiki-update.tar.gz && rm /tmp/wiki-update.tar.gz'"

# 3. Rebuild wiki
ssh root@192.168.148.254 "pct exec 116 -- /usr/local/bin/update-wiki.sh"
```

### Method 2: Quick Update Script

Save this as `update-proxmox-wiki.sh` in your local repository:

```bash
#!/bin/bash
set -e

echo "📦 Packaging wiki content..."
cd /home/fuad/Documents/T-401-ICYB-CySec-Knowledge-Base
tar czf /tmp/wiki-content.tar.gz --exclude='site' --exclude='docs_mkdocs' --exclude='.git' .

echo "📤 Uploading to Proxmox..."
scp /tmp/wiki-content.tar.gz root@192.168.148.254:/tmp/

echo "📥 Extracting in container..."
ssh root@192.168.148.254 "pct push 116 /tmp/wiki-content.tar.gz /tmp/wiki-update.tar.gz"
ssh root@192.168.148.254 "pct exec 116 -- bash -c 'cd /var/www/wiki && tar xzf /tmp/wiki-update.tar.gz && rm /tmp/wiki-update.tar.gz'"

echo "🏗️  Rebuilding wiki..."
ssh root@192.168.148.254 "pct exec 116 -- /usr/local/bin/update-wiki.sh"

echo "✅ Wiki updated successfully!"
echo "Visit: http://192.168.148.134"
```

## 🔧 Container Management

### Start/Stop/Restart Container

```bash
# Start
ssh root@192.168.148.254 "pct start 116"

# Stop
ssh root@192.168.148.254 "pct stop 116"

# Restart
ssh root@192.168.148.254 "pct restart 116"

# Status
ssh root@192.168.148.254 "pct status 116"
```

### Access Container Shell

```bash
ssh root@192.168.148.254 "pct enter 116"
```

### View Nginx Logs

```bash
ssh root@192.168.148.254 "pct exec 116 -- tail -f /var/log/nginx/access.log"
ssh root@192.168.148.254 "pct exec 116 -- tail -f /var/log/nginx/error.log"
```

## 🛠️ Troubleshooting

### Wiki not loading

```bash
# Check nginx status
ssh root@192.168.148.254 "pct exec 116 -- systemctl status nginx"

# Restart nginx
ssh root@192.168.148.254 "pct exec 116 -- systemctl restart nginx"
```

### Rebuild wiki manually

```bash
ssh root@192.168.148.254 "pct exec 116 -- bash -c 'cd /var/www/wiki && /usr/local/bin/update-wiki.sh'"
```

### Check container resources

```bash
ssh root@192.168.148.254 "pct status 116"
ssh root@192.168.148.254 "pct exec 116 -- df -h"
ssh root@192.168.148.254 "pct exec 116 -- free -m"
```

## 📝 File Locations in Container

- Wiki content: `/var/www/wiki/`
- Built site: `/var/www/wiki/site/`
- Nginx config: `/etc/nginx/sites-available/wiki`
- Update script: `/usr/local/bin/update-wiki.sh`
- Nginx logs: `/var/log/nginx/`

## 🔒 Security Considerations

1. **Change the root password** on first login
2. Consider setting up **SSH key authentication**
3. Configure a **firewall** if exposing to external networks
4. Set up **SSL/TLS with Let's Encrypt** if using a domain name
5. Enable **automatic security updates**

## 🌟 Features

- ✅ Fast static site serving via Nginx
- ✅ Material Design theme with dark/light mode
- ✅ Full-text search
- ✅ Mobile responsive
- ✅ Easy to update
- ✅ Low resource usage (~100MB RAM when idle)

---

**Deployed on**: December 11, 2025
**Proxmox Version**: 8.4.14
**Container OS**: Debian 12 Bookworm
