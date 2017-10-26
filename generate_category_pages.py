
# pip install python-frontmatter
import os, frontmatter, re, unicodedata

tag_page_dir='_pages/category'
tag_feed_dir='_pages/category/feeds'

cur_path = os.path.dirname( os.path.realpath(__file__) )
tag_pages_dir = os.path.join( cur_path, tag_page_dir )
tag_feeds_dir = os.path.join( cur_path, tag_feed_dir )

tags = []

def slugify(value):
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub('[^\w\s-]', '', value.replace('.','-')).strip().lower()
    return re.sub('[-\s]+', '-', value)

for root, dirs, files in os.walk(cur_path, topdown=False):
    pages = [os.path.join(root, fi) for fi in files if fi.endswith(".md")]

    for p in pages:
        post = frontmatter.load(p)
        if 'category' in post.keys():
            if isinstance(post['category'], list):
                post_tags = post['category']
                for tag in post_tags:
                    if not tag in tags:
                        tags.append(tag)
            else:
                tags.append( post['category'] )

tags.extend( [cat for cat in os.listdir( cur_path ) if os.path.isdir( os.path.join(cur_path, cat)) and not cat.startswith("_") and not cat.startswith(".") ] )

tag_pages = [f for f in os.listdir( tag_pages_dir ) if os.path.isfile( os.path.join(tag_pages_dir, f) ) and f.endswith(".md")]

for t in tags:
    tag_slug = slugify(t)
    tag_page_name = tag_slug + '.md'
    tag_feed_name = tag_slug + '.xml'
    tag_page_fname = os.path.join( tag_pages_dir, tag_page_name )
    tag_feed_fname = os.path.join( tag_feeds_dir, tag_feed_name )

    # Create tag index page
    if not os.path.isfile( tag_page_fname ):
        # print( tag_page )
        # Build tag page content
        tag_page_content = []
        tag_page_content.append( "---")
        #print("title: {0} Tag Archives".format(t.title()))
        tag_page_content.append( "title: {0} Category Archives".format(t.title()) )
        tag_page_content.append( "desc: All posts filed under {0}.".format(t) )
        tag_page_content.append( "permalink: /category/{0}/".format(tag_slug) )
        tag_page_content.append( "category_title: '{0}'".format(t) )
        tag_page_content.append( "---")
        tag_page_content.append( "{% include catloop.html cat=page.category_title %}")
        tag_page_content.append( " ")
        content = "\n".join( tag_page_content )
        with open( tag_page_fname, "w" ) as tag_page:
            tag_page.write(content)
            print( "Created category page: {0}".format( tag_page_name ) )

    # Create tag feed page
    if not os.path.isfile( tag_feed_fname ):
        # Build up feed page content
        tag_feed_content = []
        tag_feed_content.append( "---" )
        tag_feed_content.append( "layout: feed-category " )
        tag_feed_content.append( "permalink: /category/{0}/feed/".format(tag_slug) )
        tag_feed_content.append( "category_title: '{0}'".format(t) )
        tag_feed_content.append( "---" )
        tag_feed_content.append( " " )
        content = "\n".join( tag_feed_content )

        # Write content to file
        with open( tag_feed_fname, "w" ) as tag_feed:
            tag_feed.write(content)
            print( "Created category feed page: {0}".format( tag_feed_fname ) )


print("Finished.")
print("Press Enter to Exit.")
input()

