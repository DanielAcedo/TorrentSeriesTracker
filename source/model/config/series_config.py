class SeriesConfig:
  name = ""
  searchKeyWords = ""
  episodeNumberRegex = ""
  downloadOutputFolder = ""

  def __init__(self, name, searchKeyWords, episodeNumberRegex, downloadOutputFolder):
    self.name = name
    self.searchKeyWords = searchKeyWords
    self.episodeNumberRegex = episodeNumberRegex
    self.downloadOutputFolder = downloadOutputFolder