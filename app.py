# Dependencies
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.sql import func
from sqlalchemy import desc
from flask import Flask, jsonify, render_template
from flask_cors import CORS

# Connect to postgresql
engine = create_engine("postgresql://postgres:postgres@localhost:5432/Project3")

# Automap tables 
Base=automap_base()
Base.prepare(autoload_with=engine)
RegSeason=Base.classes.regsea_22

# Initialize Flask
app=Flask(__name__, template_folder='')
CORS(app)

## Welcome Page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/help')
def help():
    return(
        f'Available Pages:<br/>'
        f'/api/EfficientScorers<br/>'
        f'/api/RegEliteScorers<br/>'
        f'/api/Efficient3PShooters<br/>'
        f'/api/EfficientFTs<br/>'
        f'/api/DefensivePlayers<br/>'
        f'/api/ShotBlockers<br/>'
        f'/api/Youngsters<br/>'
        f'/api/PlayerDicts<br/>'
    )

# Efficient Scorers Page
@app.route('/api/RegEfficientScorers')
def EfficientScore():
    # Link back to Project3 DB
    session=Session(bind=engine)
    """League Average True Shooting is 52.7%"""
    Efficient_Scorers=session.query(RegSeason).order_by(desc(RegSeason.ts_per)).\
    filter(RegSeason.ts_per>0.527).\
    filter(RegSeason.gamesplayed>41).\
    filter(RegSeason.team!='TOT').\
    filter(RegSeason.fga>5)
    results=[{"id":scorer.id, "player": scorer.player, "Minutes Played":scorer.minutesplayed, "pts": scorer.pts, "ts_per":(scorer.ts_per*100)} for scorer in Efficient_Scorers]

    print(results)
    
    # End connection
    session.close()
    return jsonify(results)

# Efficient Scorers Page
@app.route('/api/RegEliteScorers')
def EliteScore():
    # Link back to Project3 DB
    session=Session(bind=engine)
    """League Average True Shooting is 52.7%"""
    Elite_Scorers=session.query(RegSeason).order_by(desc(RegSeason.ts_per)).\
    filter(RegSeason.ts_per>0.527).\
    filter(RegSeason.gamesplayed>41).\
    filter(RegSeason.pts>19.9).\
    filter(RegSeason.team!='TOT').\
    filter(RegSeason.fga>5)
    results=[{"id":elite.id, "player": elite.player, "Minutes Played":elite.minutesplayed, "pts": elite.pts, "ts_per":(elite.ts_per*100)} for elite in Elite_Scorers]

    print(results)
    
    # End connection
    session.close()
    return jsonify(results)

@app.route('/api/RegEfficient3PShooters')
def Efficient3PShooters():
    # Link back to Project3 DB
    session=Session(bind=engine)
    """League Average 3P Shooting is 35.4%"""
    Efficient_Shooters=session.query(RegSeason).order_by(desc(RegSeason.threeper)).\
    filter(RegSeason.ts_per>0.527).\
    filter(RegSeason.gamesplayed>41).\
    filter(RegSeason.team!='TOT').\
    filter(RegSeason.fga>5).\
    filter(RegSeason.threepa>3.5).\
    filter(RegSeason.threeper>.354)
    results=[{"id":shooter.id, "player": shooter.player, "pts": shooter.pts, "fga": shooter.fga, "3PM": shooter.threepm, "3PA": shooter.threepa, "3P%": (shooter.threeper*100), "ts_per":(shooter.ts_per*100)} for shooter in Efficient_Shooters]

    print(results)
    
    # End connection
    session.close()
    return jsonify(results)

@app.route('/api/EfficientFT')
def EfficientFT():
    # Link back to Project3 DB
    session=Session(bind=engine)

    Efficient_FT=session.query(RegSeason).order_by(desc(RegSeason.ft_per)).\
    filter(RegSeason.ts_per>0.527).\
    filter(RegSeason.gamesplayed>41).\
    filter(RegSeason.team!='TOT').\
    filter(RegSeason.fta>4).\
    filter(RegSeason.ft_per>0.795)
    results=[{"id":shooter.id, "player": shooter.player, "pts": shooter.pts, "FT": shooter.ft, "FTA": shooter.fta, "FT%": (shooter.ft_per*100), "ts_per":(shooter.ts_per*100)} for shooter in Efficient_FT]
    
    print(results)
    
    # End connection
    session.close()
    return jsonify(results)

@app.route('/api/DefPlayers')
def DefPlayers():
    # Link back to Project3 DB
    session=Session(bind=engine)

    Defensive_Players=session.query(RegSeason).\
    filter(RegSeason.gamesplayed>41).\
    filter(RegSeason.team!='TOT').\
    filter(RegSeason.stl>.999).\
    filter(RegSeason.blk>.499)
    results=[{"id":defender.id, "player": defender.player, "Minutes Played": defender.minutesplayed, "STL": defender.stl, "BLK": defender.blk, "DRB": defender.drb} for defender in Defensive_Players]
    
    print(results)
    
    # End connection
    session.close()
    return jsonify(results)

@app.route('/api/ShotBlockers')
def ShotBlockers():
    # Link back to Project3 DB
    session=Session(bind=engine)

    Shot_Blockers=session.query(RegSeason).order_by(desc(RegSeason.blk)).\
    filter(RegSeason.gamesplayed>41).\
    filter(RegSeason.team!='TOT')
    results=[{"id":blocker.id, "player": blocker.player, "Minutes Played": blocker.minutesplayed, "BLK": blocker.blk, "DRB": blocker.drb} for blocker in Shot_Blockers]
    
    print(results)
    
    # End connection
    session.close()
    return jsonify(results)

@app.route('/api/Youngsters')
def Young():
    # Link back to Project3 DB
    session=Session(bind=engine)

    Young=session.query(RegSeason).order_by(desc(RegSeason.age)).\
    filter(RegSeason.gamesplayed>41).\
    filter(RegSeason.team!='TOT').\
    filter(RegSeason.age<23)
    results=[{"id":rookie.id, "player": rookie.player, "Age": rookie.age, "Minutes Played": rookie.minutesplayed, "PTS": rookie.pts,"three_per": (rookie.threeper*100), "FT_per": (rookie.ft_per*100),"TS_per": (rookie.ts_per*100), "AST": rookie.ast} for rookie in Young]
    
    print(results)
    
    # End connection
    session.close()
    return jsonify(results)

@app.route("/api/PlayerDicts")
def playerdicts():
    session=Session(bind=engine)
    results=[pd.__dict__ for pd in session.query(RegSeason).order_by(RegSeason.player)]
    for result in results:
        del result['_sa_instance_state']
    session.close()

    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True) 