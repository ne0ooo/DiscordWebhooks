from Discord import Webhook
from Discord import Embed

hook = Webhook('Your Discord Webhook URL here') # Create the webhook object

hook.send_message("Yay") # Send a message

embed = Embed()
embed.color = 12515
embed.fields = [Embed.create_field("A", "b", True)]
embed.author_name = "author"
embed.author_icon_url = "ImageUrl"
embed.description = "description"

hook.send_embeds(embed) # Send the embed (up to ten per message)

