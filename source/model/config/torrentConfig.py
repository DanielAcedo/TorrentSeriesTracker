class TorrentConfig:
  serverUri = ""
  port = 0
  user = ""
  password = ""

  def __init__(self, serverUri, port, user, password):
    self.serverUri = serverUri
    self.port = port
    self.user = user
    self.password = password