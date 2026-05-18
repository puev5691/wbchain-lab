# WBN deployment bundle

Кратко:
этот каталог содержит восстановленный deployment bundle (дистрибутив развёртывания) WBN/TERA2 shard cluster.

Статус:
working operational deployment bundle.

## Архитектура

WBN строится как:

- upstream tera2;
- DATA/shard.js;
- DATA/const.lst;
- bootstrap peer graph;
- START_NETWORK_DATE;
- systemd runtime.

## Ключевой identity layer

Файл:

    DATA/shard.js

Ключевые параметры:

- NETWORK = WELLBEING
- SHARD_NAME = WBN
- START_NETWORK_DATE = 1778186522932
- SeedServerArr

## Bootstrap peer

Текущий bootstrap peer:

    185.39.19.240:30000

## Порты

- 30000/tcp — JINN P2P
- 8780/tcp — wallet/web UI
- 8781/tcp — internal/API layer

## Что нельзя публиковать

Никогда не публиковать:

- DATA/WALLET/*
- DB/*
- BlockChain/*
- private keys
- wallet config
- runtime secrets

## Deployment flow

1. Prepare Ubuntu host.
2. Install nodejs/npm.
3. Clone tera2.
4. Checkout confirmed commit.
5. Apply WBN identity layer.
6. Configure const.lst.
7. Install systemd service.
8. Open ports.
9. Start node.
10. Verify peer sync.

## Проверка

Открыть:

    http://IP:8780/

API:

    http://IP:8780/GetCurrentInfo

Проверить:

- NETWORK = WELLBEING
- SHARD_NAME = WBN
- block height
- peers
- sync progress

## Что уже подтверждено

Подтверждено:

- clean third-node deployment;
- WBN identity sync;
- peer graph connectivity;
- operational reproducibility;
- GUI/web wallet on 8780;
- mining runtime startup;
- public API response through 8780.

## Структура каталога

- configs/shard.js — shard identity layer.
- configs/const.template.lst — sanitized runtime config template.
- systemd/wbn-tera2-node.service — systemd service.
- install/install-third-node.sh — deployment installer.

## Служебный хвост

КТО: ШАРДОВИК / ChatGPT
ДЛЯ ЧЕГО: canonical WBN deployment bundle after successful third-node deployment
СТАТУС: working
