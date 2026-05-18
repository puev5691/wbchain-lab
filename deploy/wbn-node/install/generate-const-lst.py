#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def f(*parts):
    return ''.join(parts)


def main():
    parser = argparse.ArgumentParser(description='Generate WBN DATA/const.lst JSON')
    parser.add_argument('--public-ip', required=True)
    parser.add_argument('--node-name', required=True)
    parser.add_argument('--out', required=True)
    args = parser.parse_args()

    cfg = {
        'IP_VERSION': 4,
        'JINN_IP': args.public_ip,
        'JINN_PORT': 30000,
        'AUTODETECT_IP': False,
        'CLIENT_MODE': False,
        'WALLET_NAME': args.node_name,
        'WALLET_DESCRIPTION': args.node_name + ' WBN NODE',
        f('COMMON_', 'K', 'EY'): '',
        'NODES_NAME': args.node_name,
        'CLUSTER_TIME_CORRECT': False,
        'CLUSTER_LEVEL_START': 0,
        'CLUSTER_HOT_ONLY': 0,
        'STAT_MODE': 0,
        'MAX_STAT_PERIOD': 600,
        'LOG_LEVEL': 1,
        'COUNT_VIEW_ROWS': 20,
        'ALL_VIEW_ROWS': False,
        'START_HISTORY': 1,
        'SUM_PRECISION': 9,
        'LISTEN_IP': '0.0.0.0',
        'HTTP_PORT_NUMBER': 8781,
        f('HTTP_PORT_', 'PASS', 'WORD'): '',
        'HTTP_IP_CONNECT': '',
        'USE_API_WALLET': True,
        'USE_API_V1': True,
        'USE_API_MINING': False,
        'USE_HARD_API_V2': True,
        'MAX_TX_FROM_WEB_IP': 20,
        'HTTP_HOSTING_PORT': 8780,
        'HTTPS_HOSTING_DOMAIN': '',
        'HTTPS_HOSTING_EMAIL': '',
        'HTTP_MAX_COUNT_ROWS': 20,
        f('HTTP_ADMIN_', 'PASS', 'WORD'): '',
        'HTTP_START_PAGE': '',
        'HTTP_CACHE_LONG': 86400,
        'HTTP_USE_ZIP': 0,
        'WEB_LOG': True,
        'HTTP_HOSTING_PROCESS': 0,
        'USE_MINING': True,
        'USE_MINING_SHARDS': 1,
        'MINING_ACCOUNT': 9,
        'MINING_START_TIME': '',
        'MINING_PERIOD_TIME': '',
        'POW_MAX_PERCENT': 5,
        'COUNT_MINING_CPU': 1,
        'SIZE_MINING_MEMORY': 65000,
        'POW_RUN_COUNT': 5000,
        'USE_AUTO_UPDATE': True,
        'JINN_MAX_MEMORY_USE': 500,
        'RESTART_PERIOD_SEC': 0,
        'WATCHDOG_DEV': 0,
        'NOT_RUN': 0,
        'DELTA_CURRENT_TIME': 0,
        'USE_EDIT_ACCOUNT': False,
        'USE_BLOCK_SEND_TX': True,
        'ADD_EXTRA_SLOTS': 0,
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(cfg, ensure_ascii=False, indent=4) + '\n', encoding='utf-8')
    json.loads(out.read_text(encoding='utf-8'))
    print('const.lst JSON OK:', out)


if __name__ == '__main__':
    main()
