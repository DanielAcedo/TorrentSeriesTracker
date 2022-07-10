# Torrent Series Tracker

Hello there, stranger!

Torrent Series Tracker (provisional name) is a simple program with the simple goal of keeping track of your ongoing series and automatically downloading them to your preferred torrent client.

The setup for the project should be quite easy at the moment, I'll think of adding some UI for the configuration part in the future 😊

**Disclaimer**: At the moment, only Nyaa.si is supported as a source for checking new torrent files, and only supported torrent client is Deluge.

## Setup

You will only need Python 3 to run the script, remember to setup a python virtual env and run `pip install -r requirements.txt` to install dependencies.

## Configuration

There are 3 configuration files that you need to setup before starting the program for the first time.

### series-config.json

This file is used by the program to know which series to keep track of, and how should it search for new episodes of it.

- **name**: Identifier for the series.
- **searchKeyWords**: search string to use in the scraped website to search for new episodes of the series.
- **episodeNumberRegex**: In case the website does not have a separate field for the episode number, this regex is used to extract the episode number from the title of episode. The first capturing group will be used to get the number.
- **downloadOutputFolder**: Folder where the files contained in the torrent will be downloaded to.

Example:

```json
{
  "series": [
    {
      "name": "kaguya-sama ultra-romantic",
      "searchKeyWords": "kaguya-sama s3 subsplease 1080p",
      "episodeNumberRegex": "- ([0-9]+)",
      "downloadOutputFolder": "C:\\plex\\Kaguya-sama love is war\\Kaguya-sama Love is War S03"
    }
  ]
}
```

### episode-tracker.json

Used to keep track of which episode was the last downloaded. This file should be automatically updated by the program every time it's run.

Example:

```json
[
  {
    "name": "kaguya-sama ultra-romantic",
    "lastEpisodeScraped": 5
  }
]
```

### torrent-config.json

Used to specify the torrent server address, port and auth information

Example:

```json
{
  "serverUri": "192.168.1.90",
  "port": 58846,
  "user": "yourTorrentUser",
  "password": "yourUserPassword"
}
```
