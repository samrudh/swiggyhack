from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-316136715812-317008084406-397545707104-5b2ebf46de06b5d5a9b762bbd0f7f31f', #app verification token
							'xoxb-316136715812-397703476897-6OB44L0y1JMsrpHSSlp6m3vT', # bot verification token
							'gI4pjv8Pnsk5n1QHGsRv74Fs', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))