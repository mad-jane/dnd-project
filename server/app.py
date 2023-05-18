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


if __name__ == '__main__':
    app.run(port=5555, debug=True)