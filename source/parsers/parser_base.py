from abc import ABC, abstractclassmethod

from bs4 import BeautifulSoup
from model.episode import Episode
from model.config.series_config import SeriesConfig

class ParserBase(ABC):

  @abstractclassmethod
  def parse(seriesConfig: SeriesConfig, htmlContent: BeautifulSoup) -> 'list[Episode]':
    pass