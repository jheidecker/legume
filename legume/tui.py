import sys
sys.path.insert(0, '/Users/jheidecker/Documents/legume/plemmy')
from plemmy import LemmyHttp
from plemmy.responses import GetPostResponse
from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Button, Footer, Header, Static, MarkdownViewer

srv = LemmyHttp("https://lemmy.management")

def get_first_post():
    return "Hello World"

class PostTitle(Static):
    """TEST"""

class Post(Static):
    def compose(self) -> ComposeResult:
        post = srv.get_post(id=2035633)
        response = GetPostResponse(post)
        post = response.post_view.post
        post_body = post.body
        yield MarkdownViewer(post_body)
        yield Button("UpDoot", id="upvote")
        yield Button("DownDoot", id="downvote")


class Legume(App):

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield ScrollableContainer(Post())

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

    


if __name__ == "__main__":
    app = Legume()
    app.run()