
coolingType_List = {'PASSIVE_COOLING' : {min: 0, max: 35}, 
                    'HI_ACTIVE_COOLING' : {min: 0, max: 45}, 
                    'MED_ACTIVE_COOLING' : {min: 0, max: 40}}

breach_Type_Msg = {'TOO_LOW' : 'too low', 'TOO_HIGH' : 'too high', 'NORMAL' : 'normal'}

alert_Target_Type = {'TO_CONTROLLER' : send_to_controller, 'TO_EMAIL' : send_to_email}

def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'


def classify_temperature_breach(coolingType, temperatureInC):
  if (coolingType in coolingType_List):
    range = coolingType_List[coolingType]
    return infer_breach(temperatureInC, range['min'], range['max'])
  else:
    return infer_breach(temperatureInC, 0, 0)


def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType =\
    classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  alert_Target_Type[alertTarget](breachType)


def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')


def send_to_email(breachType):
  recepient = "a.b@c.com"
  print(f'To: {recepient}')
  print('Hi, the temperature is', breach_Type_Msg[breachType])
