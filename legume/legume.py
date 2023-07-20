
import sys
sys.path.insert(0, '/Users/jheidecker/Documents/legume/plemmy')
from plemmy import LemmyHttp
from plemmy.responses import GetPostResponse

srv = LemmyHttp("https://lemmy.management")

post = srv.get_post(id=2035633)
response = GetPostResponse(post)
post = response.post_view.post
post_body = post.body