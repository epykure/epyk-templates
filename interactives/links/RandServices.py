
from epyk.core.data import Received
from epyk.core.data import Sent


class InpRand(Sent):

  @property
  def seed(self):
    """
    gdgdg
    """
    return self.get()

  @property
  def n(self):
    """

    """
    return int(self.get())


class ResRand(Received):
  """

  """

  end_point = "randoms"
  data_sent = InpRand

  @property
  def s(self):
    """

    :rtype: InpRand
    """
    return super(ResRand, self).s

  @property
  def random(self):
    """

    """
    return self.get()

  @random.setter
  def random(self, value): self.set(value)
