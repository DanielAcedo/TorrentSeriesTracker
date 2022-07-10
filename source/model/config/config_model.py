from model.config.series_config import SeriesConfig


class ConfigModel:
  series: 'list[SeriesConfig]'

  def __init__(self, series):
    self.series = series