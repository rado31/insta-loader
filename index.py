from instaloader import Instaloader, Post


loader = Instaloader()

post = Post.from_shortcode(loader.context, 'CwnrCzMBL1y')
loader.download_post(post, 'CwnrCzMBL1y')
