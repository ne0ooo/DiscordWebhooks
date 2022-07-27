import requests


class Embed():
    def __init__(self):
        self._footer = {"text": None, "icon_url": None}
        self._thumbnail = {"url": None}
        self._author = {"name": None, "url": None, "icon_url": None}
        self._fields = []


    @property
    def title(self) -> str:
        return self._title


    @title.setter
    def title(self, title: str):
        if len(title) > 256:
            raise ValueError("title cannot exceed 256 characters")
        self._title = title

    
    @property
    def description(self) -> str:
        return self._description


    @description.setter
    def description(self, description: str):
        if len(description) > 4096:
            raise ValueError("description cannot exceed 4096 characters")
        self._description = description


    @property
    def color(self) -> int:
        return self._color

    
    @color.setter
    def color(self, integer_color: int):
        self._color = integer_color


    @property
    def url(self) -> str:
        return self._url


    @url.setter
    def url(self, url: str):
        self._url = url


    @property
    def footer_text(self) -> str:
        return self._footer["text"]


    @footer_text.setter
    def footer_text(self, footer_text: str):
        if len(footer_text) > 2048:
            raise ValueError("footer_text cannot exceed 2048 characters")
        self._footer["text"] = footer_text
    

    @property
    def footer_icon(self) -> str:
        return self._footer["icon_url"]

    
    @footer_icon.setter
    def footer_icon(self, footer_icon_url: str):
        self._footer["icon_url"] = footer_icon_url
    

    @property
    def thumbnail_icon_url(self) -> str:
        return self._thumbnail["url"]


    @thumbnail_icon_url.setter
    def thumbnail_icon_url(self, icon_url: str):
        self._thumbnail["url"] = icon_url


    @property
    def author_name(self) -> str:
        return self._author["name"]


    @author_name.setter
    def author_name(self, author_name: str):
        if len(author_name) > 256:
            raise ValueError("author_name cannot exceed 256 characters")
        self._author["name"] = author_name


    @property
    def author_url(self) -> str:
        return self._author["url"]


    @author_url.setter
    def author_url(self, author_url: str):
        self._author["author_url"] = author_url


    @property
    def author_icon_url(self) -> str:
        return self._author["icon_url"]


    @author_icon_url.setter
    def author_icon_url(self, author_icon_url: str):
        self._author["icon_url"] = author_icon_url


    @property
    def fields(self) -> dict:
        return self._fields

    
    @fields.setter
    def fields(self, fields: list[dict]):
        for field in fields:
            if len(field["name"]) > 256:
                raise ValueError("name in fields cannot exceed 256 characters")
            if len(field["value"]) > 1024:
                raise ValueError("value in fields cannot exceed 1024 characters")
        self._fields = fields


    def create_field(name: str, value: str, inline: bool) -> dict:
        if len(name) > 256:
            raise ValueError("name in fields cannot exceed 256 characters")
        if len(value) > 1024:
            raise ValueError("value in fields cannot exceed 1024 characters")
        return {"name": name, "value": value, "inline": inline}


class Webhook():
    def __init__(self,  webhook_url: str, name: str = None, avatar_url: str = None):
        self.webhook_url = webhook_url
        self.name = name
        self.avatar_url = avatar_url


    def send_message(self, message: str):
        if len(message) > 2000:
            raise ValueError("message cannot exceed 2000 characters")
        data = {
            "content": message,
            "username": self.name,
            "avatar_url": self.avatar_url
            }
        requests.post(self.webhook_url, json=data)


    def send_embeds(self, *embeds: Embed):
        if len(embeds) > 10:
            raise ValueError("amount of embeds cannot exceed 10 per message")

        data = {
            "username": self.name,
            "avatar_url": self.avatar_url,
            "embeds": [{k.strip('_'): v for (k, v)  in embed.__dict__.items()} for embed in embeds]
        } 

        # In "embeds" we create a list for every argument passed in embeds
        # we then turn it into a dictionary, and lastly we strip the underscore
        # from the variable name, or the key in order for discord's api
        # to properly accept it
        
        r = requests.post(self.webhook_url, json=data)
