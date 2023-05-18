from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from config import db

class Campaign(db.Model, SerializerMixin):
    __tablename__ = 'campaigns'
    serialize_rules = ('-created_at', '-updated_at')
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    game_master = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

@validates('title')
def validates_title(self, key, title):
    campaigns = Campaign.query.all()
    titles = [campaign.title for campaign in campaigns]
    if not title:
        raise ValueError('title must be provided.')
    elif title in titles:
        raise ValueError('title already exists.')
    return title

@validates('game_master')
def validates_game_master(self, key, game_master):
    campaigns = Campaign.query.all()
    game_masters = [campaign.game_master for campaign in campaigns]
    if not game_master:
        raise ValueError('game_master must be provided.')
    elif game_master in game_masters:
        raise ValueError('game_master already exists.')
    return game_master

class CampaignCharacter(db.Model, SerializerMixin):
    __tablename__ = 'campaign_characters'
    serialize_rules = ('-created_at', '-updated_at')
    
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'))
    # avatar = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

@validates('character_id')
def validates_character_id(self, key, character_id):
    characters = Character.query.all()
    ids = [character.id for character in characters]
    
    if not character_id:
        raise ValueError('character must be provided.')
    elif not character_id in ids:
        raise ValueError('character must exist.')
    return character_id

@validates('campaign_id')
def validates_campaign_id(self, key, campaign_id):
    campaigns = Campaign.query.all()
    ids = [campaign.id for campaign in campaigns]
    
    if not campaign_id:
        raise ValueError('campaign must be provided.')
    elif not campaign_id in ids:
        raise ValueError('campaign must exist.')
    return campaign_id

class CampaignUser(db.Model, SerializerMixin):
    __tablename__ = 'campaign_users'
    serialize_rules = ('-created_at', '-updated_at')
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
@validates('user_id')
def validates_user_id(self, key, user_id):
    users = User.query.all()
    ids = [user.id for user in users]
    
    if not user_id:
        raise ValueError('user must be provided.')
    elif not user_id in ids:
        raise ValueError('user must exist.')
    return user_id

@validates('campaign_id')
def validates_campaign_id(self, key, campaign_id):
    campaigns = Campaign.query.all()
    ids = [campaign.id for campaign in campaigns]
    
    if not campaign_id:
        raise ValueError('campaign must be provided.')
    elif not campaign_id in ids:
        raise ValueError('campaign must exist.')
    return campaign_id

class Character(db.Model, SerializerMixin):
    __tablename__ = 'characters'
    serialize_rules = ('-created_at', '-updated_at')
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    race = db.Column(db.String, nullable=False)
    c_class = db.Column(db.String, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

@validates('name')
def validates_name(self, key, name):
    if not name:
        raise ValueError('name must be provided.')
    return name

@validates('race')
def validates_race(self, key, race):
    if not race:
        raise ValueError('race must be provided.')
    return race

@validates('c_class')
def validates_class(self, key, c_class):
    if not c_class:
        raise ValueError('class must be provided.')
    return c_class

@validates('level')
def validates_level(self, key, level):
    if level < 0 and level >= 20:
        raise ValueError('level must be between 1 and 20.')
    return level

@validates('user_id')
def validates_user_id(self, key, user_id):
    users = User.query.all()
    ids = [user.id for user in users]
    
    if not user_id:
        raise ValueError('user must be provided.')
    elif not user_id in ids:
        raise ValueError('user must exist.')
    return user_id

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    serialize_rules = ('-created_at', '-updated_at')
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False, unique=True)
    profile_pic = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
@validates('username')
def validates_username(self, key, username):
    users = User.query.all()
    usernames = [user.username for user in users]
    if not username:
        raise ValueError('username must be provided.')
    elif username in usernames:
        raise ValueError('username already exists.')
    return username
