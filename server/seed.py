from random import randint, choice as rc
from faker import Faker
from app import app
from models import db, Campaign, CampaignCharacter, Character, CampaignUser, User

users_names = [{
    'name': 'John Rhys-Davies',
    'username': 'battlebeard',
    'profile_pic': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstatic3.srcdn.com%2Fwordpress%2Fwp-content%2Fuploads%2F2019%2F12%2Fgimli-destroys-ring.jpg&f=1&nofb=1&ipt=28eeb29cebcf32cc52eceebf1e159053942b71a339365eadcca158296fdc23fc&ipo=images',
    'user_id': '1'
}, {
    'name': 'Viggo Mortensen',
    'username': 'rangerdude',
    'profile_pic': 'https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fimages6.fanpop.com%2Fimage%2Fphotos%2F34500000%2FAragorn-in-the-Fellowship-of-the-Ring-aragorn-34519237-563-831.jpg&f=1&nofb=1&ipt=5a79444ee09bde03d6fa800652579f3723729fffa0cdb8a9c8195162d8ffb81c&ipo=images',
    'user_id': '2'
}, {
    'name': 'Orlando Bloom',
    'username': 'prince_of_mirkwood',
    'profile_pic': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ffsmedia.imgix.net%2F37%2Fc9%2Fed%2F8e%2F25c7%2F4e94%2Fb8b7%2Fb8114a7ec052%2Forlando-bloom-as-legolas-in-lord-of-the-rings.jpeg%3Frect%3D0%2C0%2C881%2C660%26dpr%3D1.5%26auto%3Dformat%2Ccompress%26q%3D75&f=1&nofb=1&ipt=32402f8046a0d0cf6994388f41b73bf6e08d91de5421f9379197bdee2b19fab7&ipo=images',
    'user_id': '3'
}, {
    'name': 'Ian McKellen',
    'username': 'gandalf_the_great',
    'profile_pic': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F36%2Fd1%2F96%2F36d1966ae18bfbc2531cbf9a0d7ecc07.jpg&f=1&nofb=1&ipt=f7439a18f7d214888a89ee6dc31a08b36937fa6af08d2a61e858cd2cce3c38b9&ipo=images',
    'user_id': '4'
}, {
    'name': 'Sean Bean',
    'username': 'broromir',
    'profile_pic': 'https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fimages2.fanpop.com%2Fimages%2Fphotos%2F5500000%2FBoromir-boromir-5599648-700-544.jpg&f=1&nofb=1&ipt=335c413830bbadee91b569f3bdc02ca78021208dab8a2cc0dff81483d0cab875&ipo=images',
    'user_id': '5'
}, {
    'name': 'Elijah Wood',
    'username': 'i_wear_wigs',
    'profile_pic': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F81%2F7c%2Fa2%2F817ca2d85101b9c21fbbaeece59df1ff.jpg&f=1&nofb=1&ipt=0a1424451db3930c869d58d0e257291a39cea396d812b39b875c4ff3c8b708f7&ipo=images',
    'user_id': '6'
}, {
    'name': 'Sean Astin',
    'username': 'gamgee_the_gardener',
    'profile_pic': 'https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fimages2.fanpop.com%2Fimage%2Fphotos%2F12000000%2FSamwise-Gamgee-samwise-gamgee-12089146-960-404.jpg&f=1&nofb=1&ipt=724a1d1d30e6ffda209db9bdf6e62dc26121783e174eea1bc5a6ef7e85ab6355&ipo=images',
    'user_id': '7'
}, {
    'name': 'Billy Boyd',
    'username': 'yaboy_pippin',
    'profile_pic': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F3b%2F44%2Fc1%2F3b44c1b3c5be7dda5cd666d16196cd49.jpg&f=1&nofb=1&ipt=51b6339955a07ac454855d25ba93ffd00599c5de259db13f5f3927915c3af3a7&ipo=images',
    'user_id': '8'
}, {
    'name': 'Dom Monaghan',
    'username': 'tallest_hobbit',
    'profile_pic': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.ZJ-diZ0qyMjSP63LNQcyFAAAAA%26pid%3DApi&f=1&ipt=c3de1ecababf005a7d45a2133e9210404ceb183873725dfe4c1f4ac659b9a7a5&ipo=images',
    'user_id': '9'
}, {
    'name': 'Jay',
    'username': 'pb_n_jay',
    'profile_pic': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwallpapercave.com%2Fwp%2Fwp9566448.jpg&f=1&nofb=1&ipt=a9f1ef4539891492e1fda043cbaa854771fe4b187f7fa5dd09bd066a5a4daa68&ipo=images',
    'user_id': '10'
}, {
    'name': 'Seth',
    'username': 'yoshimishep',
    'profile_pic': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwallpapercave.com%2Fwp%2Fwp9566448.jpg&f=1&nofb=1&ipt=a9f1ef4539891492e1fda043cbaa854771fe4b187f7fa5dd09bd066a5a4daa68&ipo=images',
    'user_id': '11'
}, {
    'name': 'Mars',
    'username': 'marscd',
    'profile_pic': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwallpapercave.com%2Fwp%2Fwp9566448.jpg&f=1&nofb=1&ipt=a9f1ef4539891492e1fda043cbaa854771fe4b187f7fa5dd09bd066a5a4daa68&ipo=images',
    'user_id': '12'
}, {
    'name': 'Isabella',
    'username': 'bella_flo',
    'profile_pic': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwallpapercave.com%2Fwp%2Fwp9566448.jpg&f=1&nofb=1&ipt=a9f1ef4539891492e1fda043cbaa854771fe4b187f7fa5dd09bd066a5a4daa68&ipo=images',
    'user_id': '13'
}, {
    'name': 'Clara',
    'username': 'clarademeanor',
    'profile_pic': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwallpapercave.com%2Fwp%2Fwp9566448.jpg&f=1&nofb=1&ipt=a9f1ef4539891492e1fda043cbaa854771fe4b187f7fa5dd09bd066a5a4daa68&ipo=images',
    'user_id': '14'
}, {
    'name': 'Liam',
    'username': 'godthedm',
    'profile_pic': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwallpapercave.com%2Fwp%2Fwp9566448.jpg&f=1&nofb=1&ipt=a9f1ef4539891492e1fda043cbaa854771fe4b187f7fa5dd09bd066a5a4daa68&ipo=images',
    'user_id': '15'
},{
    'name': 'Griffin Mcelroy',
    'username': 'crunchy_banana',
    'profile_pic': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ytimg.com%2Fvi%2FTvwz1809v94%2Fmaxresdefault.jpg&f=1&nofb=1&ipt=c641c9ef9500621068837297128336e5bcca9f9856b90e9d43b434d7d3ddc4c1&ipo=images',
    'user_id': '16'
},{
    'name': 'Clint McElroy',
    'username': 'radio_genius',
    'profile_pic': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette.wikia.nocookie.net%2Fpodcastdb%2Fimages%2F5%2F5b%2FClint_McElroy-0.jpg%2Frevision%2Flatest%3Fcb%3D20170513005815&f=1&nofb=1&ipt=5729a399ebed752b2c17bc74399eec4f02fab99ae298c80fa377ca29aa0c47d7&ipo=images',
    'user_id': '17'
},{
    'name': 'Travis McElroy',
    'username': 'goof',
    'profile_pic': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fjococruise.com%2Fwp-content%2Fuploads%2F2007%2F09%2Ftravis3.jpg&f=1&nofb=1&ipt=1095acdc16ed5c20f86ec49be2cb4ea24923111795d96c021af640fc1b48b8f2&ipo=images',
    'user_id': '18'
},{
    'name': 'Justin McElroy',
    'username': 'hoopsmcgee',
    'profile_pic': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpodcasts.voxmedia.com%2Fperch%2Fresources%2Fjustin-mcelroy-color.jpg&f=1&nofb=1&ipt=f18bf767e08c55e200c2674cca47f7c6091e5a6998a2523be189e7fbde2cd786&ipo=images',
    'user_id': '19'
},{
    'name': 'J.R.R. Tolkien',
    'username': 'the_tolkien',
    'profile_pic': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpodcasts.voxmedia.com%2Fperch%2Fresources%2Fjustin-mcelroy-color.jpg&f=1&nofb=1&ipt=f18bf767e08c55e200c2674cca47f7c6091e5a6998a2523be189e7fbde2cd786&ipo=images',
    'user_id': '20'
}]

campaigns_list = [
    {
    'title': 'The Lord of the Rings',
    'game_master': 'J.R.R. Tolkien',
    'user_id': '20',
    'campaign_id': '1'
    },{
    'title': 'Rupture',
    'game_master': 'Liam',
    'user_id': '15',
    'campaign_id': '2'
    },{
    'title': 'The Adventure Zone: Balance',
    'game_master': 'Griffin McElroy',
    'user_id': '16',
    'campaign_id': '3'
    }
]

characters_list = [
    {
    'name': 'Angus McDonald',
    'race': 'human',
    'c_class': 'sorcerer',
    'level': '8',
    'campaign_id': '1',
    'user_id': '16'
    },{
    'name': 'Taako Taaco',
    'race': 'elf',
    'c_class': 'wizard',
    'level': '20',
    'user_id': '19'
    },{
    'name': 'Magnus Burnsides',
    'race': 'human',
    'c_class': 'fighter',
    'level': '20',
    'user_id': '18'
    },{
    'name': 'Lucretia',
    'race': 'human',
    'c_class': 'sorcerer',
    'level': '20',
    'user_id': '16'
    },{
    'name': 'Lup Taaco',
    'race': 'elf',
    'c_class': 'wizard',
    'level': '20',
    'user_id': '16'
    },{
    'name': 'Barry Bluejeans',
    'race': 'human',
    'c_class': 'fighter',
    'level': '20',
    'user_id': '16'
    },{
    'name': 'Merle Highchurch',
    'race': 'dwarf',
    'c_class': 'cleric',
    'level': '20',
    'user_id': '17'
    },{
    'name': 'Koda',
    'race': 'dwarf',
    'c_class': 'fighter',
    'level': '8',
    'user_id': '10'
    },{
    'name': 'Yoshi',
    'race': 'aasimar',
    'c_class': 'paladin',
    'level': '9',
    'user_id': '12'
    },{
    'name': 'Aera',
    'race': 'aarakocra',
    'c_class': 'bard',
    'level': '8',
    'user_id': '11'
    },{
    'name': 'Halfoff TodayOnly',
    'race': 'Kenku',
    'c_class': 'rogue',
    'level': '9',
    'user_id': '14'
    },{
    'name': 'Willow',
    'race': 'gnome',
    'c_class': 'druid',
    'level': '9',
    'user_id': '13'
    },{
    'name': 'Frodo Baggins',
    'race': 'hobbit',
    'c_class': 'rogue',
    'level': '12',
    'user_id': '6'
    },{
    'name': 'Gandalf',
    'race': 'ainur',
    'c_class': 'wizard/fighter (multiclass)',
    'level': '20',
    'user_id': '4'
    },{
    'name': 'Sam Gamgee',
    'race': 'hobbit',
    'c_class': 'bard',
    'level': '12',
    'user_id': '7'
    },{
    'name': 'Aragorn',
    'race': 'dúnedain',
    'c_class': 'ranger',
    'level': '12',
    'user_id': '2'
    },{
    'name': 'Legolas',
    'race': 'elf',
    'c_class': 'fighter',
    'level': '12',
    'user_id': '3'
    },{
    'name': 'Gimli',
    'race': 'dwarf',
    'c_class': 'fighter/barbarian',
    'level': '12',
    'user_id': '1'
    },{
    'name': 'Boromir',
    'race': 'human',
    'c_class': 'fighter',
    'level': '12',
    'user_id': '5'
    },{
    'name': 'Merry Brandybuck',
    'race': 'hobbit',
    'c_class': 'rogue/fighter',
    'level': '12',
    'user_id': '8'
    },{
    'name': 'Pippin',
    'race': 'hobbit',
    'c_class': 'rogue/bard',
    'level': '12',
    'user_id': '9'
    },
]


def make_users():
    
    User.query.Delete()
    
    users = []
    
    for user_dict in users_names:
        user = User(
            name=user_dict['name'],
            username=user_dict['username'],
            profile_pic=user_dict['profile_pic']
        )
        users.append(user)
        
    db.session.add_all(users)
    db.session.commit()
    

def make_characters():
    
    Character.query.delete()
    users = User.query.with_entities(User.id).all()
    
    
    characters = []
    
    for character_dict in characters_list:
        character = Character(
            name=character_dict['name'],
            race=character_dict['race'],
            c_class=character_dict['c_class'],
            level=character_dict['level'],
            user_id=rc(users)[0]
        )
        characters.append(character)
        
    db.session.add_all(characters)
    db.session.commit()

def make_campaigns():
    
    Campaign.query.delete()
    campaigns = Campaign.query.with_entities(campaign.id).all()
    
    campaigns = []
    
    for campaign_dict in campaigns_list:
        campaign = Campaign(
            title=campaign_dict['title'],
            game_master=campaign_dict['game_master']
        )
    db.session.add_all(campaigns)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        make_campaigns()
        make_characters()
        make_users()