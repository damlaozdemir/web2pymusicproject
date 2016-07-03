# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################
import datetime	
songs_data = [ {'id':1, "Singer's Name": "Rihanna", "Album": "Talk That Talk", "singerimg": "rihanna.jpg ","albumimg": "talkthattalk.jpg", "releaseyear": 2011,
'title':["You da One","Where Have You Been","We Found Love", "Talk That Talk","Cockiness (Love It)","Birthday Cake","We All Want Love","Drunk on Love","Roc Me Out","Watch n' Learn","Farewell " ]},
{'id':2, "Singer's Name": "Beyonce", "Album": "Dangerously in Love", "singerimg": "beyonce.jpg ","albumimg": "beyonce.jpg", "releaseyear": 2003,
'title':["Crazy In Love","Naughty Girl","That's How You Like It", "Baby Boy","Hip Hop Star","Be With You","Me, Myself and I","Yes","Signs","Speechless","The Closer I Get To You","Dangerously in Love 2","Beyonce(Interlude)","Gift From Virgo","Daddy"]},
{'id':3, "Singer's Name": "Chris Brown", "Album": "Chris Brown", "singerimg": "chris.jpg ","albumimg": "Chris_brown.jpg", "releaseyear": 2005,
'title':["Intro","Run It","Yo","Young Love","Cockiness (Love It)","Gimme That","Ya Man Ain't Me","Winner","Ain't No Way","What's My Name","Is This Love?","Poppin'-Main","Just Fine","Say Goodbye","Run It!(Remix)","Thank You"]},
{'id':4, "Singer's Name": "Jay Z", "Album": " Reasonable Doubt ", "singerimg": "Jay.jpg ","albumimg": "Reasonable_Doubt.jpg", "releaseyear": 1996,
'title':["Can't Knock the Hustle","Politics as Usual","Brooklyn's Finest", "Dead Presidents II","Feelin' It","D'Evils","22 Two's","Can I Live","Ain't No Nigga","Friend or Foe","Coming of Age","Cashmare Thoughts","Bring It On","Regrets"]},
{'id':5, "Singer's Name": "Cem Karaca", "Album": "Nerde Kalmıştık?", "singerimg": "karaca.jpg ","albumimg": "Nerde_Kalmistik.jpg", "releaseyear": 1992,
'title':["Raptiye Rap Rap","Islak Islak","Sen Duymadın","Bu Biçim", "Sen de Başını Alıp Gitme","Niyazi Köfteler","Karabağ","Herkes Gibisin","Nöbetçinin Türküsü ","Ömrüm","Suskunluk"]}
 ]
 
def index():
	return dict(msg={})
def about():
	return dict(msg={})
def music():
    rows = db(db.Songsdata.id >= 0).select()
    return dict(rows=rows)

	
def song():
	if request.args(0):
		rows=db(db.Songsdata.id ==request.args(0)).select().first()
		if rows:
			songs=db(db.song.Songsdataid==rows.id).select(db.song.songname, db.song.id)
			comments=db(db.comments.usersid==db.users.id).select(db.users.username,db.comments.datecomment,db.comments.comments)
		return dict(song=rows,songs=songs,comments=comments)
	else:
		return dict()
	

def addcomment():
	if request.args(0) and session.user:
		user=db(db.users.username==session.user.username).select().first()
		db.comments.insert(songid=request.args(0),usersid=user.id,comments=request.vars.text,datecomment=datetime.datetime.utcnow())
		address='/MusicProject/default/song/'+request.args(0)
		return redirect(address)
	return dict(msg={})	

	
def addalbum():
	return dict(grid=SQLFORM.grid(db.Songsdata,user_signature=False))

def addsong():
	return dict(grid=SQLFORM.grid(db.song,user_signature=False))
	
def addsinger():
	return dict(grid=SQLFORM.grid(db.singers,user_signature=False))
	
def top():
	return dict(msg={})
	
def report():
	return dict(msg={})
def bio():
	return dict(msg={})

	
def photos():
	rows = db(db.Songsdata).select()
	return dict(rows=rows)
	
def events():
	return dict(msg={})
def NewReleases():
	rows = db(db.Songsdata.releaseyear >= 2015 ).select()
	return dict(news=rows)
			
def play():
	if request.args(0) and session.user:
		rows = db(db.song.id==request.args(0)).select()
	return dict(rows = rows)


def user():
	

    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
	
def uploads():  
    return response.download(request, db)

def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
