from deluge_client import DelugeRPCClient
from model.episode import Episode
from model.config.series_config import SeriesConfig
from model.config.torrentConfig import TorrentConfig

def connectToClient(torrentConfig: TorrentConfig):
  return DelugeRPCClient(torrentConfig.serverUri, torrentConfig.port, torrentConfig.user, torrentConfig.password, True, True)

def uploadTorrentMagnet(torrentConfig: TorrentConfig, episode: Episode, episodeConfig: SeriesConfig):
  try:
    with connectToClient(torrentConfig) as client:
      client.call("core.add_torrent_magnet", episode.magnetLink, {"download_location": episodeConfig.downloadOutputFolder})
  except Exception as e:
    print(f"Error uploading torrent file for series {episodeConfig.name}, episode {episode.number}\n", e)
    raise