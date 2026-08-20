# Twitter Cards for 6 Exchanges

Bilingual (CN/EN) landing pages + `summary_large_image` cards for Twitter sharing.

## Live links

| Exchange | CN | EN |
|---|---|---|
| Binance | https://shirley44198-creator.github.io/twitter-cards/binance/ | https://shirley44198-creator.github.io/twitter-cards/binance/en/ |
| OKX | https://shirley44198-creator.github.io/twitter-cards/okx/ | https://shirley44198-creator.github.io/twitter-cards/okx/en/ |
| Bybit | https://shirley44198-creator.github.io/twitter-cards/bybit/ | https://shirley44198-creator.github.io/twitter-cards/bybit/en/ |
| Bitget | https://shirley44198-creator.github.io/twitter-cards/bitget/ | https://shirley44198-creator.github.io/twitter-cards/bitget/en/ |
| BIT | https://shirley44198-creator.github.io/twitter-cards/bit/ | https://shirley44198-creator.github.io/twitter-cards/bit/en/ |
| MSX | https://shirley44198-creator.github.io/twitter-cards/msx/ | https://shirley44198-creator.github.io/twitter-cards/msx/en/ |

## Cache-busting

Twitter caches both page and image aggressively. To force a refresh after redesigning the card:

1. Bump `VER` in `gen_twitter_cards.py`.
2. Re-generate and re-deploy. This changes the image filename (e.g. `card-cn-v4.png`).
3. When sharing on Twitter, append a fresh query parameter like `?v=5` to the landing URL.

## Generate locally

```bash
python gen_twitter_cards.py
```
