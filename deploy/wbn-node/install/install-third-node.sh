#!/usr/bin/env bash
set -euo pipefail

BASE="/home/pev5691/wbn-tera2-lab"
TERA="$BASE/tera2"
LOGS="$BASE/logs"
BACKUPS="$BASE/backups"

mkdir -p "$LOGS" "$BACKUPS"

sudo apt update
sudo apt install -y git curl rsync build-essential nodejs npm

if [ ! -d "$TERA/.git" ]; then
  git clone https://gitlab.com/terafoundation/tera2.git "$TERA"
fi

cd "$TERA"

git fetch --all
git checkout 6cc2061c12986bbaea182786c42d89fd979eeb33

cd "$TERA/Source"
npm install

mkdir -p "$TERA/DATA"

cp ../deploy/wbn-node/configs/shard.js "$TERA/DATA/shard.js"
cp ../deploy/wbn-node/configs/const.template.lst "$TERA/DATA/const.lst"

sudo cp ../deploy/wbn-node/systemd/wbn-tera2-node.service /etc/systemd/system/wbn-tera2-node.service

sudo ufw allow 30000/tcp comment 'WBN P2P'
sudo ufw allow 8780/tcp comment 'WBN HTTP HOSTING'
sudo ufw allow 8781/tcp comment 'WBN HTTP API'

sudo systemctl daemon-reload
sudo systemctl enable wbn-tera2-node.service
sudo systemctl restart wbn-tera2-node.service

sleep 15

systemctl status wbn-tera2-node.service --no-pager -l
ss -ltnp | grep -E '30000|8780|8781'
