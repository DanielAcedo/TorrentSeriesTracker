import urllib.parse
import requests
from bs4 import BeautifulSoup
from parsers.nyaasi_parser import NyaaSiParser
from helper import writeToFile, readFile, serializeJson, deserializeJson
from constants import config_file, nyaa_url, episode_tracker_file, torrent_config_file
from model.config.config_model import ConfigModel
from model.config.series_config import SeriesConfig
from model.config.episode_tracker_config import EpisodeTrackerConfig
from model.config.torrentConfig import TorrentConfig
from torrent.torrent_uploader import uploadTorrentMagnet
from errors.not_found_error import NotFoundError

def loadEpisodeTracker() -> 'list[EpisodeTrackerConfig]':
  configText = readFile(episode_tracker_file)
  config = deserializeJson(configText)
  return config

def updateEpisodeTracker(seriesName: str, lastEpisode: int) -> None:
  episodeTrackerConfig = loadEpisodeTracker()
  episodeTrackerForSeries = next(filter(lambda o: o.name == seriesName, episodeTrackerConfig), None)

  if episodeTrackerForSeries is None:
    raise NotFoundError(f"No episode tracker found for series \"{seriesName}\"")

  episodeTrackerForSeries.lastEpisodeScraped = lastEpisode
  episodeTrackerJson = serializeJson(episodeTrackerConfig, True)
  writeToFile(episode_tracker_file, episodeTrackerJson)

def loadSeriesConfig() -> ConfigModel:
  configText = readFile(config_file)
  config = deserializeJson(configText)
  return config

def loadTorrentConfig() -> TorrentConfig:
  configText = readFile(torrent_config_file)
  config = deserializeJson(configText)
  return config

def loadEpisodes(seriesConfig: SeriesConfig, episodeTracker: EpisodeTrackerConfig, torrentConfig: TorrentConfig):
  queryParams = urllib.parse.quote(seriesConfig.searchKeyWords)
  url = f"{nyaa_url}?f=0&c=0_0&q={queryParams}&o=desc"

  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")

  parser = NyaaSiParser()
  episodes = parser.parse(seriesConfig, soup)

  fileContent = ""
  maxEpisode = episodeTracker.lastEpisodeScraped

  for episode in filter(lambda episode: episode.number > episodeTracker.lastEpisodeScraped, episodes):
    try:
      uploadTorrentMagnet(torrentConfig, episode, seriesConfig)
      maxEpisode = episode.number
      fileContent += f"{episode.series} | {episode.number} | {episode.magnetLink} | {episode.torrentLink}"+" \n"
    except Exception as e:
      print(f"Could not upload {seriesConfig.name} episode {episode.number}, skipping series...\n", f"Reason: {e}")
      break

  updateEpisodeTracker(seriesConfig.name, maxEpisode)
  writeToFile(f"{seriesConfig.name}.txt", fileContent)



config = loadSeriesConfig()
episodeTrackers = loadEpisodeTracker()
torrentConfig = loadTorrentConfig()

for seriesConfig in config.series:
  filteredEpisodeTrackers = [episodeTracker for episodeTracker in episodeTrackers if episodeTracker.name == seriesConfig.name]
  episodeTracker = filteredEpisodeTrackers[0] if len(filteredEpisodeTrackers) != 0 else EpisodeTrackerConfig(name=seriesConfig.name, lastEpisodeScraped=0)

  loadEpisodes(seriesConfig, episodeTracker, torrentConfig)

