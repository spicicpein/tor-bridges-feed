# tor-bridges-feed

Personal bridge feed for use as a `bridge_source.urls` entry in
[tor-bundle-windows](https://github.com/spicicpein/tor-bundle-windows).

Runs daily, pulls Tor Browser's current default obfs4/webtunnel bridges,
publishes them as `bridges.json`. Raw URL to use in your config:

```
https://raw.githubusercontent.com/spicicpein/tor-bridges-feed/main/bridges.json
```
