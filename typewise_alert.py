
coolingType_List = {'PASSIVE_COOLING':{lowerLimit: 0, upperLimit: 35}, 'HI_ACTIVE_COOLING':{lowerLimit: 0, upperLimit: 45}, 'MED_ACTIVE_COOLING':{lowerLimit: 0, upperLimit: 40}}

breach_Type_Msg = {'TOO_LOW' : 'too low', 'TOO_HIGH' : 'too high', 'NORMAL' : 'normal'}

def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'

def classify_temperature_breach(coolingType, temperatureInC):
  if coolingType in coolingType_List and temperatureInC is not None:
    range = coolingType_List[coolingType]
    return infer_breach(temperatureInC, range['lowerLimit'], range['upperLimit'])
  else:
    return print("Please enter correct Input")

def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')
  return True

def send_to_console(breachType):
  print(f'BreachType is:, {breachType}')
  return True

def send_to_email(breachType):
  recepient = "a.b@c.com"
  print(f'To: {recepient}')
  print('Hi, the temperature is ', breach_Type_Msg[breachType])
  return True

alert_Target_Type = {"TO_CONTROLLER": send_to_controller, "TO_EMAIL" : send_to_email, "TO_CONSOLE" : send_to_console }

def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType =\
    classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  if breachType != "NORMAL":
    return alert_Target_Type[alertTarget](breachType)
  
