# models
from tamildhool import db
import datetime


# video page category

class VideoCategory(db.Model):
    
    __tablename__ = 'video_category'
    Id = db.Column(db.Integer, primary_key=True)
    OrderCol = db.Column(db.Integer)
    Name = db.Column(db.String(100))
    Image = db.Column(db.Text)
    Keywords = db.Column(db.Text)
    Description = db.Column(db.Text)
    CreatedAt = db.Column(db.DateTime)

    def __init__(self, Id, OrderCol, Name, Image, Keywords, Description, CreatedAt):
        self.Id = Id
        self.OrderCol = OrderCol
        self.Name = Name
        self.Image = Image
        self.Keywords = Keywords
        self.Description = Description
        self.CreatedAt = CreatedAt
        
# video views count
class VideoTracking(db.Model):
    
    __tablename__ = "video_tracking"
    Id = db.Column(db.Integer, primary_key=True)
    VideoId = db.Column(db.Integer)
    Ip = db.Column(db.String(15))
    CreatedAt = db.Column(db.DateTime)
    
    def ___init__(self,Id,VideoId,Ip,CreatedAt):
        self.Id = Id
        self.VideoId = VideoId
        self.Ip = Ip
        self.CreatedAt = CreatedAt


class TrendingTracking(db.Model):

    __tablename__ = "trending_tracking"
    Id = db.Column(db.Integer, primary_key=True)
    VideoId = db.Column(db.Integer)
    Ip = db.Column(db.String(15))
    CreatedAt = db.Column(db.DateTime)

    def ___init__(self, Id, VideoId, Ip, CreatedAt):
        self.Id = Id
        self.VideoId = VideoId
        self.Ip = Ip
        self.CreatedAt = CreatedAt



# movies
class Movies(db.Model):
    
    __tablename__ = 'movies'
    Id = db.Column(db.Integer, primary_key=True)
    OrderCol = db.Column(db.Integer)
    OverAllCol = db.Column(db.Integer)
    MovieTitle = db.Column(db.String(500))
    MovieLink = db.Column(db.String(500))
    MovieImage = db.Column(db.String(500))
    DirectLink = db.Column(db.String(500))
    TorrentLink = db.Column(db.String(500))
    Description = db.Column(db.Text)
    MovieDescription = db.Column(db.Text)
    KeyWords = db.Column(db.Text)
    CreatedAt = db.Column(db.DateTime)
    

# pages
class VideoPage(db.Model):
    
    __tablename__ = 'pages'
    
    Id = db.Column(db.Integer, primary_key=True)
    OrderCol = db.Column(db.Integer)
    VideoCategory = db.Column(db.Integer)
    PageName = db.Column(db.String(500))
    PageImage = db.Column(db.String(500))
    Keywords = db.Column(db.Text)
    Description = db.Column(db.Text)
    Profile = db.Column(db.Text)
    cast = db.Column(db.Text)
    story = db.Column(db.Text)
    CreatedAt = db.Column(db.DateTime)

    def __init__(self, Id, VideoCategory, OrderCol, PageName, PageImage, Keywords, Description, Profile, cast,story, CreatedAt):
        self.Id = Id
        self.VideoCategory = VideoCategory
        self.OrderCol = OrderCol
        self.PageName = PageName
        self.PageImage = PageImage
        self.Keywords = Keywords
        self.Description = Description
        self.Profile = Profile
        self.cast = cast
        self.story = story
        self.CreatedAt = CreatedAt
        
    def __repr__(self):
        return self.PageName

# video
class Video(db.Model):

    __tablename__ = 'video'
    
    Id = db.Column(db.Integer, primary_key=True)
    OrderCol = db.Column(db.Integer)
    OverAllCol = db.Column(db.Integer)
    VideoTitle = db.Column(db.String(500))
    VideoLink = db.Column(db.String(500))
    VideoLink2 = db.Column(db.String(500))
    VideoImage = db.Column(db.String(500))
    VideoPage = db.Column(db.Integer, db.ForeignKey('pages.Id'))
    Description = db.Column(db.Text)
    KeyWords = db.Column(db.Text)
    CreatedAt = db.Column(db.DateTime)
    VideoDate = db.Column(db.DateTime)
    VideoType = db.Column(db.String(50))
    videpagedetails = db.relationship("VideoPage", backref=db.backref("pages", uselist=False))
    
    def __init__(self,Id,OrderCol,OverAllCol,VideoTitle,VideoLink,VideoLink2,VideoImage,VideoPage,Description,KeyWords,CreatedAt,VideoDate,VideoType):
        self.Id = Id
        self.OrderCol = OrderCol
        self.OverAllCol = OverAllCol
        self.VideoTitle = VideoTitle
        self.VideoLink = VideoLink
        self.VideoLink2 = VideoLink2
        self.VideoImage = VideoImage
        self.VideoPage = VideoPage
        self.Description = Description
        self.KeyWords = KeyWords
        self.CreatedAt = CreatedAt
        self.VideoDate = VideoDate
        self.VideoType = VideoType
        
    def __repr__(self):
        return self.VideoTitle


class VideoTrending(db.Model):
    
    __tablename__ = 'trending_video'
    
    Id = db.Column(db.Integer, primary_key=True)
    OrderCol = db.Column(db.Integer)
    VideoTitle = db.Column(db.String(500))
    VideoLink = db.Column(db.String(500))
    VideoImage = db.Column(db.String(500))
    Description = db.Column(db.Text)
    KeyWords = db.Column(db.Text)
    CreatedAt = db.Column(db.DateTime)
    
    def __init__(self,Id,OrderCol,VideoTitle,VideoLink,VideoImage,Description,KeyWords,CreatedAt):
        self.Id = Id
        self.OrderCol = OrderCol
        self.VideoTitle = VideoTitle
        self.VideoLink = VideoLink
        self.VideoImage = VideoImage
        self.Description = Description
        self.KeyWords = KeyWords
        self.CreatedAt = CreatedAt
        
    def __repr__(self):
        return self.VideoTitle

class VideoType(db.Model):
        
    __tablename__ = 'video_type'
    Id = db.Column(db.Integer, primary_key=True)
    OrderCol = db.Column(db.Integer)
    Name = db.Column(db.String(100))
    Image = db.Column(db.Text)
    Keywords = db.Column(db.Text)
    Description = db.Column(db.Text)
    CreatedAt = db.Column(db.DateTime)

    def __init__(self, Id, OrderCol, Name, Image, Keywords, Description, CreatedAt):
        self.Id = Id
        self.OrderCol = OrderCol
        self.Name = Name
        self.Image = Image
        self.Keywords = Keywords
        self.Description = Description
        self.CreatedAt = CreatedAt
        