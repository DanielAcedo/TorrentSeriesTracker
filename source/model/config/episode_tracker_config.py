class EpisodeTrackerConfig:
  name: str
  lastEpisodeScraped: int

  def __init__(self, name, lastEpisodeScraped):
    self.name = name
    self.lastEpisodeScraped = lastEpisodeScraped