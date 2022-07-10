class Episode:
  series = ""
  number = 0
  magnetLink = ""
  torrentLink = ""

  def __init__(self, series, magnetLink, torrentLink, number = 0):
    self.series = series
    self.magnetLink = magnetLink
    self.torrentLink = torrentLink
    self.number = number