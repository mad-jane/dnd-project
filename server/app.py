from flask import request, session, make_response, jsonify
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from config import app, db, api
from models import User, Campaign, CampaignUser, CampaignCharacter, Character

class Campaigns(Resource):
    
    def get(self):
        campaigns = Campaign.query.all()
        campaigns_dict_list = [campaign.to_dict() for campaign in campaigns]
        
        response = make_response(
            campaigns_dict_list,
            200
        )
        
        return response
    
    def post(self):
        data = request.get_json()
        
        try:
            campaign = Campaign(
                title=data['title'],
                game_master=data['game_master']
            )
            
            db.session.add(campaign)
            db.session.commit()
            
        except Exception as ex:
            return make_response({
                'errors': [ex.__str__()]
            }, 422)
            
        response = make_response(
            campaign.to_dict(),
            201
        )
        
        return response

api.add_resource(Campaigns, '/campaigns')

class CampaignsById(Resource):
    
    def get(self, id):
        campaign = Campaign.query.filter_by(id=id).first()
        
        if not campaign:
            return make_response({
                'error': 'campaign not found.'
            }, 404)
            
        campaign_dict = campaign.to_dict(rules = ('characters',))
        
        response = make_response(
            campaign_dict,
            200
        )
        
        return response
    
    def patch(self, id):
        campaign = Campaign.query.filter_by(id=id).first()
        data = request.get_json()
        
        for attr in data:
            setattr(campaign, attr, data[attr])
            
        db.session.add(campaign)
        db.session.commit()
        
        response = make_response(
            campaign.to_dict(),
            202
        )
        
        return response
    
    def delete(self, id):
        campaign = Campaign.query.filter_by(id=id).first()
        
        if not campaign:
            return make_response({
                'error': 'campaign not found.'
            }, 404)
        
        db.session.delete(campaign)
        db.session.commit()

api.add_resource(CampaignsById, '/campaigns<int:id>')

class CampaignUsers(Resource):
    
    def post(self):
        data = request.get_json()
        
        try:
            campaign_user = CampaignUser(
                user_id=data['user_id'],
                campaign_id=data['campaign_id']
            )
            
            db.session.add(campaign_user)
            db.session.commit()
            
        except Exception as ex:
            return make_response({
                'errors': [ex.__str__()]
            }, 422)
        
        response = make_response(
            campaign_user.campaign.to_dict(),
            201
        )
        
        return response

api.add_resource(CampaignUsers, '/campaign_users')

class CampaignCharacters(Resource):
    
    def post(self):
        data = request.get_json()
        
        try:
            campaign_character = CampaignCharacter(
                character_id=data['character_id'],
                campaign_id=data['campaign_id']
            )
            
            db.session.add(campaign_character)
            db.session.commit()
            
        except Exception as ex:
            return make_response({
                'errors': [ex.__str__()]
            }, 422)
        
        response = make_response(
            campaign_character.campaign.to_dict(),
            201
        )
        
        return response
    
api.add_resource(CampaignCharacters, '/campaign_characters')

class Characters(Resource):
    
    def get(self):
        characters = Character.query.all()
        characters_dict_list = [character.to_dict() for character in characters]
        
        response = make_response(
            characters_dict_list,
            200
        )
    
    def post(self):
        data = request.get_json()
        try:
            character = Character(
                name=data['name'],
                race=data['race'],
                c_class=data['c_class'],
                level=data['level']
            )
            
            db.session.add(character)
            db.session.commit()
        
        except Exception as ex:
            return make_response({
                'errors': [ex.__str__()]
            }, 422)
            
        response = make_response(
            character.to_dict(),
        201
        )
        
        return response

api.add_resource(Characters, '/characters')

class CharactersById(Resource):
    
    def get(self, id):
        character = Character.query.filter_by(id=id).first()
        
        if not character:
            return make_response({
                'error': 'character not found.'
            }, 404)
        
        response = make_response(
            character.to_dict(),
            200
            )
        
        return response
    
    def patch(self, id):
        character = Character.query.filter_by(id=id).first()
        data = request.get_json()
        
        for attr in data:
            setattr(character, attr, data[attr])
        
        db.session.add(character)
        db.session.commit()
        
        response = make_response(
            character.to_dict(),
            202
        )
        
        return response
    
    def delete(self, id):
        character = Character.query.filter_by(id=id).first()
        
        if not character:
            return make_response({
                'error': 'character not found.'
            }, 404)
            
        db.session.delete(character)
        db.session.commit()

api.add_resource(CharactersById, '/characters<int:id>')

class Users(Resource):
    
    def get(self):
        users = User.query.all()
        users_dict_list = [user.to_dict() for user in users]
        
        response = make_response(
            users_dict_list,
            200
        )
        
        return response

api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run(port=5555, debug=True)