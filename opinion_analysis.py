from bs4 import BeautifulSoup
import urllib
import pycurl
import cStringIO
import ast

sentiments = []

def crawler(website):
    if website == "techcrunch":
        ur = urllib.urlopen("https://www.facebook.com/plugins/comments.php?channel_url=http%3A%2F%2Fstatic.ak.facebook.com%2Fconnect%2Fxd_arbiter.php%3Fversion%3D11%23cb%3Df30432051b812ae%26origin%3Dhttp%253A%252F%252Ftechcrunch.com%252Ff3c5c958a276ea2%26domain%3Dtechcrunch.com%26relation%3Dparent.parent&href=http%3A%2F%2Ftechcrunch.com%2F2012%2F09%2F12%2Fapple-iphone-5-official%2F&locale=en_US&numposts=25&sdk=joey&width=630")
        soup = BeautifulSoup(ur.read())
        posts = soup.select(".postText")#soup.find_all('a', class_="uiHeaderActions rfloat")
    elif website == "cnet":
        ur = urllib.urlopen('http://news.cnet.com/8614-13579_3-57512089.html?assetTypeId=12&nomesh&formCommunityId=2070&formTargetCommunityId=2070')
        #another link to be processed: http://www.cnet.com/8614-6452_7-35022502.html?assetTypeId=2&nomesh&communityId=2177&targetCommunityId=2177&formCommunityId=2177&formTargetCommunityId=2177
        soup = BeautifulSoup(ur.read())
        posts = soup.select(".commentBody")#soup.find_all('a', class_="uiHeaderActions rfloat")
    print "no comments: %d" % len(posts)
    for post in posts:
        #print type(post)
        print post.renderContents()
        
def compute_sentiments(data_file_name):
    f = open(data_file_name)
    lines = f.readlines()
    #c.setopt(c.CONNECTTIMEOUT, 5)
    #c.setopt(c.TIMEOUT, 8)
    cnt = 0
    for line in lines:
        try:
            cnt += 1
            buf = cStringIO.StringIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'http://text-processing.com/api/sentiment/')
            c.setopt(c.WRITEFUNCTION, buf.write)
            postdata = ''
            postdata = 'text=' + line[:-1]
            #print postdata
            c.setopt(c.POSTFIELDS, postdata)
            c.perform()
            val = buf.getvalue()
            #print repr(val)
            #data = json.loads(val)
            data = ast.literal_eval(val)
            #print data
            #pprint(data)
            data["post"] = line[:-1]
            sentiments.append(data)
            buf.close()
        except pycurl.error, error:
            errno, errstr = error
            print "An error occured: ", errstr
    f.close()
    print cnt
#First step, you should crawl the desired website
crawler("techcrunch")
#Second, we do sentiment analysis for our comments
#compute_sentiments("cnet_data_iphone5")
#g = open("cnet_jason_sentiments_iphone5", 'a')
#for sent in sentiments:
#    print sent
#    g.write(str(sent) + '\n')
#g.close()