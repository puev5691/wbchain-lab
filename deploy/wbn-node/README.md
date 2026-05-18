# WBN/TERA2 node deployment bundle

Кратко:
этот каталог фиксирует восстановление фактического WBN/TERA2 deployment bundle (дистрибутива развёртывания) по существующей публичной ноде ЭРэФия.

Статус: recovery_skeleton, не final installer.

## Что подтверждено аудитом ЭРэФии

Подтверждённая нода:

- label: ЭРэФия
- hostname: ruvds-ygo0w
- public IP: 194.87.107.135
- OS: Ubuntu 24.04.4 LTS
- service: wbn-tera2-node.service
- service status in audit: active/running
- user: pev5691
- working directory: /home/pev5691/wbn-tera2-lab/tera2/Source
- command: /usr/bin/node run-node.js NOPSWD NOAUTOUPDATE
- logs:
  - /home/pev5691/wbn-tera2-lab/logs/wbn-tera2-node.out.log
  - /home/pev5691/wbn-tera2-lab/logs/wbn-tera2-node.err.log
- source origin: https://gitlab.com/terafoundation/tera2.git
- source commit: 6cc2061c12986bbaea182786c42d89fd979eeb33

Observed listeners:

- 30000/tcp: WBN/TERA2 P2P
- 8780/tcp: public web/wallet/API process
- 8781/tcp: node/internal HTTP/API process

Observed child processes:

- run-node.js NOPSWD NOAUTOUPDATE
- ./process/web-process.js READONLYDB MODE:MAIN_JINN STARTNETWORK:1778186522932 PATH:../DATA/ HOSTING:8780 NOPSWD
- ./process/tx-process.js READONLYDB MODE:MAIN_JINN STARTNETWORK:1778186522932 PATH:../DATA/ HOSTING:8780 NOPSWD
- ./process/pow-process.js MODE:MAIN_JINN STARTNETWORK:1778186522932 PATH:../DATA/ HOSTING:8780 NOPSWD

## Что пока НЕ подтверждено

Нельзя считать финальным установщиком, пока не извлечены и очищены:

- DATA/config или аналогичный WBN runtime config;
- параметры shard/network, если они задаются не только кодом;
- способ первичной настройки STARTNETWORK=1778186522932;
- способ задания SHARD_NAME=WBN / NETWORK=WELLBEING, если они не встроены в исходники;
- bootstrap peers;
- mining mode;
- wallet/private-key boundary;
- различия между ЭРэФией и Буржуинией.

## Правило дальнейших установок

Дальнейшие установки должны идти через этот GitHub-каталог только после того, как:

1. снят дополнительный sanitized runtime audit с ЭРэФии;
2. снят аналогичный audit с Буржуинии;
3. подтверждён общий deployment contour;
4. создан final installer;
5. installer проверен на чистой ноде.

## Структура каталога

- docs/recovery-errefiya-audit-summary.md — что восстановлено из архива ЭРэФии.
- systemd/wbn-tera2-node.service.template — шаблон systemd-службы по факту ЭРэФии.
- install/install-wbn-node-recovery-skeleton.sh — осторожный каркас установки, не финальный production installer.
- verify/verify-wbn-node.sh — проверочный скрипт состояния ноды.

## Stop-condition

Если отсутствует подтверждённый WBN runtime config, установка должна останавливаться до развертывания service.

Нельзя делать вид, что официальный upstream TERA2 сам по себе уже является WBN-шардом, если WBN-параметры задавались отдельными файлами или ручной настройкой.

## Служебный хвост

КТО: ШАРДОВИК / ChatGPT
ДЛЯ ЧЕГО: начать перенос фактического WBN/TERA2 deployment contour в GitHub
СТАТУС: recovery_skeleton
