
# pip install python-frontmatter
import os, frontmatter, re, unicodedata

tag_page_dir='_pages/tag'

cur_path = os.path.dirname(os.path.realpath(__file__))
tags = []

def slugify(value):
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub('[^\w\s-]', '', value.replace('.','-')).strip().lower()
    return re.sub('[-\s]+', '-', value)

for root, dirs, files in os.walk(cur_path, topdown=False):
    pages = [os.path.join(root, fi) for fi in files if fi.endswith(".md")]

    for p in pages:
        post = frontmatter.load(p)
        if 'tags' in post.keys():
            post_tags = post['tags']
            for tag in post_tags:
                if not tag in tags:
                    tags.append(tag)

tag_pages_dir = os.path.join(cur_path, tag_page_dir)
tag_pages = [f for f in os.listdir( tag_pages_dir ) if os.path.isfile( os.path.join(tag_pages_dir, f) ) and f.endswith(".md")]

for t in tags:
    tag_slug = slugify(t)
    tag_page_name = tag_slug + '.md'
    tag_page_fname = os.path.join( tag_pages_dir, tag_page_name )
    if not os.path.isfile( tag_page_fname ):
        # print( tag_page )
        # Build tag page content
        tag_page_content = []
        tag_page_content.append( "---")
        #print("title: {0} Tag Archives".format(t.title()))
        tag_page_content.append( "title: {0} Tag Archives".format(t.title()) )
        tag_page_content.append( "desc: All posts tagged {0}.".format(t) )
        tag_page_content.append( "permalink: /tag/{0}/".format(tag_slug) )
        tag_page_content.append( "tag_title: '{0}'".format(t) )
        tag_page_content.append( "---")
        tag_page_content.append( "{% include tagloop.html tag=page.tag_title %}")
        content = "\n".join( tag_page_content )
        with open( tag_page_fname, "w" ) as tag_page:
            tag_page.write(content)
            print( "Created tag page: {0}".format( tag_page_name ) )

print("Finished.")
print("Press Enter to Exit.")
input()

