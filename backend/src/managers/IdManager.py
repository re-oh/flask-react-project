class IdManager:
  def __init__(self, startCount: int) -> None:
    self.count = startCount


  def genId(self) -> int:
    self.count += 1
    return self.count
