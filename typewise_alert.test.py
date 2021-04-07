import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    self.assertTrue(typewise_alert.infer_breach(100, 0, 45) == 'TOO_HIGH')
    self.assertTrue(typewise_alert.infer_breach(25, 0, 40) == 'NORMAL')
    
  def test_check_if_input_data_is_valid(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', 80))
    self.assertFalse(typewise_alert.classify_temperature_breach(None, 40))
    self.assertFalse(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING', None))
    self.assertFalse(typewise_alert.classify_temperature_breach('COOLING', 80))
        
  def test_alert_breaches(self):
    typewise_alert.check_and_alert('TO_CONTROLLER', {'coolingType': 'PASSIVE_COOLING'}, 120)
    typewise_alert.check_and_alert('TO_EMAIL', {'coolingType': 'HI_ACTIVE_COOLING'}, -20)
    typewise_alert.check_and_alert('TO_CONSOLE', {'coolingType': 'MED_ACTIVE_COOLING'}, 90)

if __name__ == '__main__':
  unittest.main()
