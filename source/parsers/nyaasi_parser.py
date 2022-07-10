from bs4 import BeautifulSoup

from parsers.parser_base import ParserBase
from model.episode import Episode
from model.config.series_config import SeriesConfig
import re

class NyaaSiParser(ParserBase):

  def parse(self, seriesConfig: SeriesConfig, htmlContent: BeautifulSoup) -> 'list[Episode]':
    episodeNumberRegex = seriesConfig.episodeNumberRegex
    episodes = []
    episodeRows = htmlContent.select(".torrent-list tbody tr")

    for episodeRow in episodeRows:
      episodeNumber = 0
      title = magnetLink = torrentLink = ""
      titleElement = episodeRow.select_one("td:nth-child(2) a:last-child")
      torrentLinkElement = episodeRow.select_one("td:nth-child(3) a:first-child")
      magnetLinkElement = episodeRow.select_one("td:nth-child(3) a:nth-child(2)")

      if (titleElement):
        title = titleElement.text
        episodeNumberRegexResult = re.search(episodeNumberRegex, title)

        if (episodeNumberRegexResult is not None):
          episodeNumber = int(episodeNumberRegexResult.group(1))

      if (torrentLinkElement):
        torrentLink = torrentLinkElement["href"]

      if (magnetLinkElement):
        magnetLink = magnetLinkElement["href"]


      episode = Episode(title, magnetLink, torrentLink, number = episodeNumber)
      episodes.append(episode)
    
    return episodes