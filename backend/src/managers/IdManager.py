class IdManager:
  def __init__(self, startCount: int) -> None:
    self.count = startCount


  def genId(self, users: list[dict]) -> int:
    if len(users) > self.count:
      return self.count + 1
    elif len(users) == self.count:
      return len(users) + 1
    else:
      return self.count + 1
