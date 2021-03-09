from discord_webhook import DiscordWebhook, DiscordEmbed
import time

def spam():
  webhook = DiscordWebhook(url='WEBHOOK_URL', content='@everyone')

  ## replace WEBHOOK_URL with your webhook url

  response = webhook.execute()

while True:
  spam()
  time.sleep(1) ## replace 1 with number of seconds you want per post (keep 1 as default due to being rate limited)
