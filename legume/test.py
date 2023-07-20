import sys
sys.path.insert(0, '/Users/jheidecker/Documents/legume/plemmy')
from plemmy import LemmyHttp
from plemmy.responses import GetSiteResponse

srv = LemmyHttp("https://lemmy.management")

site = srv.get_site()
response = GetSiteResponse(site)
print(response.discussion_languages)