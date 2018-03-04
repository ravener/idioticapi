import aiohttp

class NotAvailable(Exception):
    pass

class Client:
    def __init__(self, token, dev=False, session=None):
        self.token = token
        self.dev = dev
        self.headers = {
        	"Authorization" if self.dev else "token": self.token
        }
        self.base_url = "https://dev.anidiots.guide" if self.dev else "https://api.anidiots.guide"
        self.session = aiohttp.ClientSession() if session is None else session
        
    async def _get(self, endpoint, query):
        async with self.session.get("{}{}{}".format(self.base_url, endpoint, query), headers=self.headers) as resp:
            data = await resp.json()
        return bytes(data["data"]["data"])
        
    async def blame(self, text):
        return await self._get("/generators/blame" if self.dev else "/blame", "?name={}".format(text))
        
    async def triggered(self, image_url):
        return await self._get("/generators/triggered" if self.dev else "/triggered", "?avatar={}".format(image_url))
       
    async def wanted(self, avatar):
        return await self._get("/generators/wanted" if self.dev else "/wanted", "?avatar={}".format(avatar))
    
    async def missing(self, avatar, text):
        if not self.dev:
            raise NotAvailable("Missing endpoint is disabled while in production")
        return await self._get("/generators/missing", "?avatar={}&text={}".format(avatar, text))
    
    async def pls(self, name):
        return await self._get("/generators/pls" if self.dev else "/pls", "?name={}".format(name))
        
    def __repr__(self):
        return "<IdioticAPI Client>"
    
    def __str__(self):
        return "<IdioticAPI Client, dev={}, url={}>".format(self.dev, self.base_url)
    
    async def snapchat(self, text):
        return await self._get("/generators/snapchat" if self.dev else "/snapchat", "?text={}".format(text))
    
    async def achievement(self, avatar, text):
        return await self._get("/generators/achievement" if self.dev else "/achievement","?avatar={}&text={}".format(avatar, text))
        
    async def the_search(self, avatar, text):
        return await self._get("/generators/thesearch" if self.dev else "/thesearch", "?avatar={}&text={}".format(avatar, text))
       
    async def beautiful(self, avatar):
        return await self._get("/generators/beautiful" if self.dev else "/beautiful", "?avatar={}".format(avatar))
       
    async def facepalm(self, avatar):
        return await self._get("/generators/facepalm" if self.dev else "/facepalm", "?avatar={}".format(avatar))
   
    async def respect(self, avatar):
        return await self._get("/generators/respect" if self.dev else "/facepalm", "?avatar={}".format(avatar))
       
    async def stepped(self, avatar):
        return await self._get("/generators/stepped" if self.dev else "/stepped", "?avatar={}".format(avatar))
       
    async def tatto(self, avatar):
        return await self._get("/generators/tatto" if self.dev else "/tatto", "?avatar={}".format(avatar))
       
    async def vault_boy(self, avatar):
        return await self._get("/generators/vault" if self.dev else "/vault", "?avatar={}".format(avatar))
       
    async def challenger(self, avatar):
        if not self.dev:
            raise NotAvailable("Challenger endpoint is disabled while in production")
        return await self._get("/generators/challenger", "?avatar={}".format(avatar))
       
    async def bat_slap(self, slapper, slapped):
        return await self._get("/generators/batslap" if self.dev else "/batslap", "?slapper={}&slapped={}".format(slapper, slapped))
       
    async def superpunch(self, puncher, punched):
        return await self._get("/generators/superpunch" if self.dev else "/superpunch", "?puncher={}&punched={}".format(puncher, punched))
       
    async def slap(self, slapper, slapped):
        return await self._get("/generators/slap" if self.dev else "/slap", "?slapper={}&slapped={}".format(slapper, slapped))
   
    async def karen(self, avatar):
        if not self.dev:
            raise NotAvailable("Karen endpoint is disabled while in production")
        return await self._get("/generators/karen", "?avatar={}".format(avatar))
       
    async def steam(self, avatar, text):
        if not self.dev:
            raise NotAvailable("Steam endpoint is disabled while in production")
        return await self._get("/generators/steam", "?avatar={}&text={}".format(avatar, text))
       
    async def crush(self, crusher, crush):
        return await self._get("/generators/crush" if self.dev else "/crush","?crusher={}&crush={}".format(crushed, crush))
       
    async def welcome(self, avatar, is_bot, usertag, guild, version="gearz"):
        return self._get("/greetings/{}_welcome".format(version) if self.dev else "/{}_welcome".format(version), "?guild={}&bot={}&usertag={}&avatar={}".format(guild, is_bot, usertag, avatar))
       