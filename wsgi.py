from dateutil import tz
from tamildhool import app
from flask import render_template, redirect, session, request, send_from_directory, make_response, url_for, Response
from tamildhool.models import Video,VideoPage,Movies,VideoCategory,VideoTrending, VideoTracking
# from tamildhool.video.views import Video_BluePrint
# from tamildhool.video_page.views import VideoPage_Blueprint
import datetime
from urllib.parse import urlparse, urlunparse
from tamildhool import db
import re
import math
utc_tz = tz.gettz('UTC')
india_tz = tz.gettz('Asia/Kolkata')

@app.route('/robots.txt')
@app.route('/ads.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

def urlsluggeneratorvideoview(string):
    return re.sub(' +', '-', string).lower()
    
def urlsluggenerator(string):
    return re.sub(' +', '-', string).lower()

def videoPageProfileContent(msg,videodate):
    msg = msg.replace('[slashformat]', str(videodate.strftime("%d/%m/%Y"))+' tamildhool, ')
    msg = msg.replace('[dashformat]', str(videodate.strftime("%d-%m-%Y"))+' tamildhool, ')
    msg = msg.replace('[namedformat]', str(videodate.strftime("%d %B %Y"))+' tamildhool, ')
    msg = msg.replace('[dotformat]', str(videodate.strftime("%d.%m.%Y"))+' tamildhool, ')
    return msg

@app.before_request
def redirect_nonwww():
    """Redirect non-www requests to www."""
    urlparts = urlparse(request.url)
    if urlparts.netloc == 'tamildhool.xyz':
        urlparts_list = list(urlparts)
        urlparts_list[1] = 'www.tamildhool.xyz'
        return redirect(urlunparse(urlparts_list), code=301)

def videoPageProfileContentPage(msg):
    msg = msg.replace('[slashformat]', '')
    msg = msg.replace('[dashformat]', '')
    msg = msg.replace('[namedformat]', '')
    msg = msg.replace('[dotformat]', '')
    return msg

def get_page_count():
    return 20

def gettamildescription():
    return 'sun tv serial & shows , vijay tv serial & Shows, Zee Tamil Serial & Shows, Latest Serials, free serials , online free'

def gettamiltitle():
    return 'sun tv serial tamil,vijay tv serial,Zee Tamil Serial,free serials, online free,tamil serials'

@app.route('/page/', defaults={"page": 1})
@app.route('/page/<int:page>')
def gethometamilpages(page):
    per_page = get_page_count()
    getpagelist = [mk.Id for mk in VideoPage.query.filter(VideoPage.VideoCategory.in_([1, 2, 3])).all()]
    if request.args.get('q'):
        searchcontent = "%{}%".format(request.args.get('q'))
        return render_template('tamil.html', data1=Video.query.filter(Video.VideoTitle.like(searchcontent), Video.VideoPage.in_(getpagelist)).order_by(Video.Id.desc()).paginate(page,per_page,error_out=False), currentdate=datetime, description=gettamildescription(), title=gettamiltitle(), videoviewurl='/tamil')
    else:
        return render_template('tamil.html', data1=Video.query.filter(Video.VideoPage.in_(getpagelist)).order_by(Video.Id.desc()).paginate(page,per_page,error_out=False), currentdate=datetime, q='', description=gettamildescription(), title=gettamiltitle(), videoviewurl='/tamil')

@app.route('/')
def homepagetamil():
    per_page = get_page_count()
    getpagelist = [mk.Id for mk in VideoPage.query.filter(VideoPage.VideoCategory.in_([1, 2, 3])).all()]
    if request.args.get('q'):
        searchcontent = "%{}%".format(request.args.get('q'))
        return render_template('tamil.html', data1=Video.query.filter(Video.VideoTitle.like(searchcontent), Video.VideoPage.in_(getpagelist)).order_by(Video.Id.desc()).paginate(1,per_page,error_out=False), currentdate=datetime, description=gettamildescription(), title=gettamiltitle(), videoviewurl='/tamil')
    else:
        return render_template('tamil.html', data1=Video.query.filter(Video.VideoPage.in_(getpagelist)).order_by(Video.Id.desc()).paginate(1,per_page,error_out=False), currentdate=datetime, q='', description=gettamildescription(), title=gettamiltitle(), videoviewurl='/tamil')

@app.route('/cs/', defaults={"videopage": 1, "pageid": 1})
@app.route('/cs/<videopage>/<int:pageid>')
@app.route('/cs/<videopage>')
def homechanneltamil(videopage,pageid=1):
    if(videopage == 'sun-tv'):
        categoryid = 2
        title = 'suntv, sun tv, sun tv serials, free online, sun tv shows, serials,show'
        pagename = 'Sun Tv'
    elif (videopage == 'vijay-tv'):
        categoryid = 1
        title = 'vijaytv, vijay tv, vijay tv serials, free online, vijay tv shows, serials,show'
        pagename = 'Vijay Tv'
    elif (videopage == 'zee-tamil'):
        categoryid = 3
        title = 'zee tamiltv, zee tamil tv, zee tamil tv serials, free online, zee tamil tv shows, serials,show'
        pagename = 'Zee Tamil'
    else:
        return render_template('404.html'), 404
    per_page = get_page_count()
    getpagelist = [mk.Id for mk in VideoPage.query.filter(VideoPage.VideoCategory.in_([categoryid])).all()]
    if request.args.get('q'):
        searchcontent = "%{}%".format(request.args.get('q'))
        return render_template('tamil.html', data1=Video.query.filter(Video.VideoTitle.like(searchcontent), Video.VideoPage.in_(getpagelist)).order_by(Video.Id.desc()).paginate(1,per_page,error_out=False), currentdate=datetime, description=title, title=title, videoviewurl='/tamil')
    else:
        return render_template('tamil.html', data1=Video.query.filter(Video.VideoPage.in_(getpagelist)).order_by(Video.Id.desc()).paginate(1,per_page,error_out=False), currentdate=datetime, q='', description=title, title=title, videoviewurl='/tamil')
    
@app.route('/v/<videoid>/<urlslug>')
def homevideoview(videoid, urlslug):
    if request.headers.getlist("X-Forwarded-For"):
       ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr
    insertdata = VideoTracking(
        Id=0, VideoId=videoid, Ip=ip, CreatedAt=datetime.datetime.now())
    db.session.add(insertdata)
    db.session.commit()
    videodata = Video.query.filter_by(Id=videoid).first()
        
    if(videodata != None):
        if(int(videodata.VideoType) == 1 ):
            videopagedata = VideoPage.query.filter_by(Id=videodata.VideoPage).first()  
            if(videopagedata.VideoCategory == 1):
                link = 'vijay-tv'
                channelname = 'Vijay Tv Serials'
                pagename = 'Vijay Tv Serials & Shows'
            elif (videopagedata.VideoCategory == 2):
                link = 'sun-tv'
                channelname = 'Sun Tv Serials'
                pagename = 'Sun Tv Serials & Shows'
            elif (videopagedata.VideoCategory == 3):
                link = 'zee-tamil'
                channelname = 'Zee Tamil Tv Serials'
                pagename = 'Zee Tamil Tv Serials & Shows'
            getmsgcontent = videoPageProfileContent(videopagedata.Profile,videodata.VideoDate)
            return render_template('videoview.html', data=videodata, otherepisodes=Video.query.filter_by(VideoPage=videodata.VideoPage).order_by(Video.Id.desc()).limit(4).all(), title=videodata.VideoTitle, description=videoPageProfileContent(videopagedata.Description, videodata.VideoDate), getmsgcontent=getmsgcontent, videopagedata=videopagedata, videoviewurl=url_for('homevideoview', videoid=videodata.Id, urlslug=urlsluggeneratorvideoview(videodata.VideoTitle)),link=link,pagename=pagename,channelname=channelname)
        else:
            videopagedata = VideoPage.query.filter_by(Id=videodata.VideoPage).first()    
            return render_template('video/subvideo.html', data=videodata, otherepisodes=Video.query.filter_by(VideoPage=videodata.VideoPage).order_by(Video.Id.desc()).limit(4).all(), title=videodata.VideoTitle, description=videoPageProfileContent(videodata.Description, videodata.VideoDate), getmsgcontent='', videoviewurl=url_for('homevideoview', videoid=videodata.Id, urlslug=urlsluggeneratorvideoview(videodata.VideoTitle))) 
    else:
        return render_template('404.html'), 404

@app.route('/s/', defaults={"videopage": 1, "pageid": 1})
@app.route('/s/<videopage>/<int:pageid>')
@app.route('/s/<videopage>')
def homeserialpage(videopage, pageid = 1):
    if(videopage == 'sun-tv'):
        categoryid = 2
        title = 'suntv, sun tv, sun tv serials, free online, sun tv shows, serials,show'
        pagename = 'Sun Tv'
    elif (videopage == 'vijay-tv'):
        categoryid = 1
        title = 'vijaytv, vijay tv, vijay tv serials, free online, vijay tv shows, serials,show'
        pagename = 'Vijay Tv'
    elif (videopage == 'zee-tamil'):
        categoryid = 3
        title = 'zee tamiltv, zee tamil tv, zee tamil tv serials, free online, zee tamil tv shows, serials,show'
        pagename = 'Zee Tamil'
    else:
        return render_template('404.html'), 404
    per_page = get_page_count()
    if request.args.get('q'):
        searchcontent = "%{}%".format(request.args.get('q'))
        return render_template('channelpage.html', datapage=VideoPage.query.filter(VideoPage.PageName.like(searchcontent),VideoPage.VideoCategory.in_([categoryid])).order_by(VideoPage.Id.desc()).paginate(pageid,per_page,error_out=False), title=title, description=title,pagename=pagename,videopagenameforslug=videopage)
    else:
        return render_template('channelpage.html', datapage=VideoPage.query.filter(VideoPage.VideoCategory.in_([categoryid])).order_by(VideoPage.Id.desc()).paginate(pageid,per_page,error_out=False), title=title, description=title,pagename=pagename,videopagenameforslug=videopage)
        

@app.route('/p/', defaults={"videopageid": 1,"urlslug":"","pageid": 1})
@app.route('/p/<videopageid>/<urlslug>/<int:pageid>')
@app.route('/p/<videopageid>/<urlslug>')
def homevideopage(videopageid,urlslug, pageid=1):
    per_page = get_page_count()
    videopagedata = VideoPage.query.filter_by(Id=videopageid).first()
    if videopagedata != None:
        description = videoPageProfileContentPage(videopagedata.Description)
        if request.args.get('q'):
            searchcontent = "%{}%".format(request.args.get('q'))
            return render_template('videoindex.html', datapage=Video.query.filter(Video.VideoTitle.like(searchcontent),Video.VideoPage.in_([videopageid])).order_by(Video.Id.desc()).paginate(pageid,per_page,error_out=False), videopageid=videopageid, title=videopagedata.PageName, keywords=videopagedata.Keywords, description=description, videopagenameforslug=urlsluggenerator(videopagedata.PageName))
        else:
            return render_template('videoindex.html', datapage=Video.query.filter(Video.VideoPage.in_([videopageid])).order_by(Video.Id.desc()).paginate(pageid,per_page,error_out=False), videopageid=videopageid, title=videopagedata.PageName, keywords=videopagedata.Keywords, description=description, videopagenameforslug=urlsluggenerator(videopagedata.PageName))
    else:
        return render_template('404.html'), 404

@app.route("/sitemap.xml")
def sitemap_index_1():
    dynamic_urls = list()
    getpagelist = [mk.Id for mk in VideoPage.query.filter(VideoPage.VideoCategory.in_([1, 2, 3])).all()]
    blog_posts = Video.query.filter(Video.VideoPage.in_(getpagelist)).order_by(Video.Id.desc()).all()
    for post in blog_posts:
        date_string = post.CreatedAt.strftime("%Y-%m-%dT%H:%M:%S+00:00")
        url = {
            "loc":  url_for('homevideoview', videoid=post.Id, urlslug=urlsluggenerator(post.VideoTitle), _external=True, _scheme='https'),
            "lastmod": date_string
        }
        dynamic_urls.append(url)
    xml_sitemap = render_template("sitemap.xml", dynamic_urls=dynamic_urls)
    response = make_response(xml_sitemap)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.errorhandler(404) 
def not_found(e): 
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True)
    
