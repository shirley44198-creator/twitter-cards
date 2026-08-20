#!/usr/bin/env python3
"""Configure GitHub Pages URL - replace {{BASE_URL}} with actual address."""
import os

base = input("Your GitHub Pages URL (e.g. https://username.github.io/twitter-cards/): ").strip()
if not base.endswith('/'):
    base += '/'
if not base.startswith('http'):
    base = 'https://' + base

count = 0
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as fh:
                content = fh.read()
            if '{{BASE_URL}}' in content:
                content = content.replace('{{BASE_URL}}', base)
                with open(p, 'w', encoding='utf-8') as fh:
                    fh.write(content)
                count += 1
                print('  OK ' + p)

print()
print('Done! Replaced in ' + str(count) + ' files.')
print('Your base URL: ' + base)
print('Test link: ' + base + 'binance/')
