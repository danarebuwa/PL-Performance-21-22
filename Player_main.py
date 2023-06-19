import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import seaborn as sns
pd.options.display.max_columns = None
from mplsoccer import Pitch, VerticalPitch
import plotly.graph_objects as go
import plotly.express as px
import math


#Allow for full tables to be shown
pd.options.display.max_columns = None
pd.options.display.max_rows = None


st.set_page_config(layout="wide")

#create main header "Premier League Player Analysis"
st.title("Premier League Player Rating and Grouping")

#create a sidebar


pl_df = pd.read_csv('pl_stats_cleaned.csv')
#in pl_df remove anything "/" in the player column 
pl_df['Player'] = pl_df['Player'].str.split('\\') .str[0] 
#in pl_df nation column remove anything before the first capital letter
pl_df['Nation'] = pl_df['Nation'].str.split(' ') .str[1]
#make all pl_df nation capitalized
pl_df['Nation'] = pl_df['Nation'].str.upper()
pl_df['Pos'] = pl_df['Pos'].str[:2]



pl_prev_df = pd.read_csv('pl_stats_2020.csv')
pl_prev_df['Player'] = pl_prev_df['Player'].str.split('\\') .str[0]
pl_prev_df['Nation'] = pl_prev_df['Nation'].str.split(' ') .str[1]
pl_prev_df['Nation'] = pl_prev_df['Nation'].str.upper()

#Shooting dataframe 2020-21
pl_shoot_prev_df = pd.read_csv('pl_prev_shooting.csv')
pl_shoot_prev_df['Player'] = pl_prev_df['Player'].str.split('\\') .str[0]
pl_shoot_prev_df['Nation'] = pl_prev_df['Nation'].str.split(' ') .str[1]
pl_shoot_prev_df['Nation'] = pl_prev_df['Nation'].str.upper()

#Shooting dataframe 2021-22
pl_shoot_df = pd.read_csv('pl_shooting_stats.csv')
pl_shoot_df['Player'] = pl_shoot_df['Player'].str.split('\\') .str[0]
pl_shoot_df['Nation'] = pl_shoot_df['Nation'].str.split(' ') .str[1]
pl_shoot_df['Nation'] = pl_shoot_df['Nation'].str.upper()

pl_pass_prev_df = pd.read_csv('pl_pass_prev.csv')
pl_pass_prev_df['Player'] = pl_pass_prev_df['Player'].str.split('\\') .str[0]
pl_pass_prev_df['Nation'] = pl_pass_prev_df['Nation'].str.split(' ') .str[1]
pl_pass_prev_df['Nation'] = pl_pass_prev_df['Nation'].str.upper()

pl_pass = pd.read_csv('pl_pass_stats.csv')
#in pi_pass player column remove anything after "\"
pl_pass['Player'] = pl_pass['Player'].str.split('\\').str[0]
pl_pass['Pos'] = pl_pass['Pos'].str[:2]
#pl_pass


pl_poss_prev = pd.read_csv('pl_possesion_2020.csv')
pl_poss_prev['Player'] = pl_poss_prev['Player'].str.split('\\') .str[0]
pl_poss_prev['Nation'] = pl_poss_prev['Nation'].str.split(' ') .str[1]
pl_poss_prev['Nation'] = pl_poss_prev['Nation'].str.upper()
pl_poss_prev['Pos'] = pl_poss_prev['Pos'].str[:2]

pl_poss = pd.read_csv('pl_possesion.csv')
#in pi_poss player column remove anything after "\"
pl_poss['Player'] = pl_poss['Player'].str.split('\\').str[0]
pl_poss['Pos'] = pl_poss['Pos'].str[:2]




pl_def_prev = pd.read_csv('pl_defense_prev.csv')
pl_def_prev['Player'] = pl_def_prev['Player'].str.split('\\') .str[0]
pl_def_prev['Nation'] = pl_def_prev['Nation'].str.split(' ') .str[1]
pl_def_prev['Nation'] = pl_def_prev['Nation'].str.upper()

pl_def = pd.read_csv('pl_defense.csv')
#in pl_def player column remove anything after "\"
pl_def['Player'] = pl_def['Player'].str.split('\\').str[0]
pl_def['Pos'] = pl_def['Pos'].str[:2]

pl_sca_gca_prev = pd.read_csv('pl_sca_gca_prev.csv')
pl_sca_gca_prev['Player'] = pl_sca_gca_prev['Player'].str.split('\\') .str[0]
pl_sca_gca_prev['Nation'] = pl_sca_gca_prev['Nation'].str.split(' ') .str[1]
pl_sca_gca_prev['Nation'] = pl_sca_gca_prev['Nation'].str.upper()



pl_sca_gca = pd.read_csv('pl_sca_gca_stats.csv')
#in pl_sca_gca player column remove anything after "\"
pl_sca_gca['Player'] = pl_sca_gca['Player'].str.split('\\').str[0]
pl_sca_gca['Pos'] = pl_sca_gca['Pos'].str[:2]

pl_gk_prev = pd.read_csv('pl_gk_stats_2020.csv')
#in pl_gk player column remove anything after "\"
pl_gk_prev['Player'] = pl_gk_prev['Player'].str.split('\\').str[0]
pl_gk_prev['Pos'] = pl_gk_prev['Pos'].str[:2]

pl_gk = pd.read_csv('pl_gk_stats.csv')
#in pl_gk player column remove anything after "\"
pl_gk['Player'] = pl_gk['Player'].str.split('\\').str[0]
pl_gk['Nation'] = pl_gk['Nation'].str.split(' ') .str[1]
pl_gk['Nation'] = pl_gk['Nation'].str.upper()
pl_gk['Pos'] = pl_gk['Pos'].str[:2]

pl_adv_gk_prev = pd.read_csv('pl_adv_gk_2020.csv')
#in pl_adv_gk player column remove anything after "\"
pl_adv_gk_prev['Player'] = pl_adv_gk_prev['Player'].str.split('\\').str[0]
pl_adv_gk_prev['Pos'] = pl_adv_gk_prev['Pos'].str[:2]



pl_adv_gk = pd.read_csv('pl_adv_gk.csv')
#in pl_adv_gk player column remove anything after "\"
pl_adv_gk['Player'] = pl_adv_gk['Player'].str.split('\\').str[0]
pl_adv_gk['Nation'] = pl_adv_gk['Nation'].str.split(' ') .str[1]
pl_adv_gk['Nation'] = pl_adv_gk['Nation'].str.upper()
pl_adv_gk['Pos'] = pl_adv_gk['Pos'].str[:2]




#miscellaneous stats 2020
pl_misc_prev = pd.read_csv('pl_misc_2020.csv')
pl_misc_prev['Player'] = pl_misc_prev['Player'].str.split('\\') .str[0]
pl_misc_prev['Nation'] = pl_misc_prev['Nation'].str.split(' ') .str[1]

#miscellaneous stats 
pl_misc = pd.read_csv('pl_misc.csv')
#in pl_misc player column remove anything after "\"
pl_misc['Player'] = pl_misc['Player'].str.split('\\').str[0]
pl_misc['Pos'] = pl_misc['Pos'].str[:2]


#merge the following dataframes pl_df, pl_pass, pl_poss, pl_def, pl_sca_gca
pl_df = pd.merge(pl_df, pl_pass, on='Player')
pl_df = pl_df.drop(columns=['Matches_x', 'Matches_y', 'Rk_y', 'Nation_y', 'Pos_y', 'Squad_y', 'Age_y', 'Born_y', '90s_y','Rk_x', 'Nation_x', 'Pos_x', 'Squad_x', 'Age_x', 'Born_x', '90s_x', 'Gls.1','Ast.1','Ast_y','Matches_y','Matches_x','xA_x','xG.1','xA.1','Att_x','xA_y'])
pl_df = pd.merge(pl_df, pl_poss, on='Player')
pl_df = pl_df.drop(columns=['Matches_x', 'Matches_y', 'Rk_y', 'Nation_y', 'Pos_y', 'Squad_y', 'Age_y', 'Born_y', '90s_y','Rk_x', 'Nation_x', 'Pos_x', 'Squad_x', 'Age_x', 'Born_x', '90s_x', 'Gls.1','Ast.1','Ast_y', 'Ast_x','Matches','Matches_y','Matches_x','xA_x','xG.1','xA.1','Att_x','TotDist_x','PrgDist_x','xA_y','1/3_x','Prog_x'])
pl_df = pd.merge(pl_df, pl_def, on='Player')
pl_df = pl_df.drop(columns=['Matches_x', 'Matches_y', 'Rk_y', 'Nation_y', 'Pos_y', 'Squad_y', 'Age_y', 'Born_y', '90s_y','Rk_x', 'Nation_x', 'Pos_x', 'Squad_x', 'Age_x', 'Born_x', '90s_x', 'Gls.1','Ast.1','Ast_y', 'Ast_x','Matches','Matches_y','Matches_x','xA_x','xG.1','xA.1','Att_x','TotDist_x','PrgDist_x','xA_y','1/3_x','Prog_x'])
pl_df = pd.merge(pl_df, pl_sca_gca, on='Player')
pl_df = pl_df.drop(columns=['Matches_x', 'Matches_y', 'Rk_y', 'Nation_y', 'Pos_y', 'Squad_y', 'Age_y', 'Born_y', '90s_y','Rk_x', 'Nation_x', 'Pos_x', 'Squad_x', 'Age_x', 'Born_x', '90s_x', 'Gls.1','Ast.1','Ast_y', 'Ast_x','Matches','Matches_y','Matches_x','xA_x','xG.1','xA.1','Att_x','TotDist_x','PrgDist_x','xA_y','1/3_x','Prog_x'])
#pl_df = pd.merge(pl_df, pl_shoot_df, on='Player')


#pl_df_prev = pd.merge(pl_df_prev, pl_misc_prev, on='Player')


#drop the following columns from pl_df Matches_x', 'Rk_y', 'Nation_y', 'Pos_y', 'Squad_y', 'Age_y', 'Born_y', '90s_y'
#pl_df = pl_df.drop(columns=['Matches_x', 'Matches_y', 'Rk_y', 'Nation_y', 'Pos_y', 'Squad_y', 'Age_y', 'Born_y', '90s_y','Rk_x', 'Nation_x', 'Pos_x', 'Squad_x', 'Age_x', 'Born_x', '90s_x', 'Gls.1','Ast.1','Ast_y', 'Ast_x','Matches','Matches_y','Matches_x','xA_x','xG.1','xA.1','Att_x','TotDist_x','PrgDist_x','xA_y','1/3_x','Prog_x'])
#pl_df_prev = pl_df_prev.drop(columns=['Matches_x', 'Rk_y', 'Nation_y', 'Pos_y', 'Squad_y', 'Age_y', 'Born_y', '90s_y','Rk_x', 'Nation_x', 'Pos_x', 'Squad_x', 'Age_x', 'Born_x', '90s_x', 'Gls.1','Ast.1','Ast_y', 'Ast_x','Matches','Matches_y','Matches_x','xA_x','xG.1','xA.1','Att_x','TotDist_x','PrgDist_x','xA_y','1/3_x','Prog_x'])






#Create list of columns to sum, then assign the sum to a new column
gk_list = ['PSxG', '/90', 'Cmp%', 'AvgDist']
pl_adv_gk['Sum PSxG'] = pl_adv_gk[gk_list].sum(axis=1)
SCA_list = ['SCAPassLive','SCAPassDead','SCADrib','SCASh','SCAFld']
pl_df['Sum SCA'] = pl_df[SCA_list].sum(axis=1)
GCA_list = ['GCAPassLive','GCAPassDead','GCADrib','GCASh','GCAFld']
pl_df['Sum GCA'] = pl_df[GCA_list].sum(axis=1)
poss_list = ['Def Pen', 'Def 3rd_x', 'Mid 3rd_x', 'Att 3rd_x', 'Att Pen']
pl_df['Sum Poss'] = pl_df[poss_list].sum(axis=1)
defence_list = ['Tkl', 'Def 3rd_y', 'Mid 3rd_y', 'Att 3rd_y', 'Blocks']
pl_df['Sum Defence'] = pl_df[defence_list].sum(axis=1)
pass_list = ['Cmp.1', 'Cmp.2', 'Cmp.3', 'Prog_y']
pl_df['Sum Pass'] = pl_df[pass_list].sum(axis=1)
#shooting_list = ['Sh/90', 'SoT/90', 'xG', 'npxG']
#pl_df['Sum Shoot'] = pl_df[shooting_list].sum(axis=1)

#Create Pass SCA ratio new column
pl_adv_gk['GK Ratio'] = pl_adv_gk['PSxG'] / pl_adv_gk['Sum PSxG']
pl_df['Pass SCA Ratio'] = pl_df['SCAPassLive']/pl_df['Sum SCA']
pl_df['Pass GCA Ratio'] = pl_df['GCAPassLive']/pl_df['Sum GCA']
pl_df['Poss Ratio'] = pl_df['Live']/pl_df['Sum Poss']
pl_df['Defence Ratio'] = pl_df['TklW']/pl_df['Sum Defence']
pl_df['Pass Ratio'] = pl_df['Cmp']/pl_df['Sum Pass']
#pl_df['Shoot Ratio'] = pl_df['Sh/90']/pl_df['Sum Shoot']

gk_cols_list = [each + ' Ratio' for each in gk_list]
for idx, val in enumerate(gk_cols_list):
    pl_adv_gk[val] = pl_adv_gk[gk_list[idx]] / pl_adv_gk['Sum PSxG']
SCA_cols_list = [each + ' Ratio' for each in SCA_list]
for idx, val in enumerate(SCA_cols_list):
    pl_df[val] = pl_df[SCA_list[idx]]/pl_df['Sum SCA']
GCA_cols_list = [each + ' Ratio' for each in GCA_list]
for idx, val in enumerate(GCA_cols_list):
    pl_df[val] = pl_df[GCA_list[idx]]/pl_df['Sum GCA']
poss_cols_list = [each + ' Ratio' for each in poss_list]
for idx, val in enumerate(poss_cols_list):
    pl_df[val] = pl_df[poss_list[idx]]/pl_df['Sum Poss']
defence_cols_list = [each + ' Ratio' for each in defence_list]
for idx, val in enumerate(defence_cols_list):
    pl_df[val] = pl_df[defence_list[idx]]/pl_df['Sum Defence']
pass_cols_list = [each + ' Ratio' for each in pass_list]
for idx, val in enumerate(pass_cols_list):
    pl_df[val] = pl_df[pass_list[idx]]/pl_df['Sum Pass']
#shooting_cols_list = [each + ' Ratio' for each in shooting_list]
#for idx, val in enumerate(shooting_cols_list):
    #pl_df[val] = pl_df[shooting_list[idx]]/pl_df['Sum Shoot']

pl_adv_gk['Sum PSxG'] = pl_adv_gk[gk_cols_list].sum(axis=1)
pl_df['Sum SCA Ratio'] = pl_df[SCA_cols_list].sum(axis=1)
pl_df['Sum GCA Ratio'] = pl_df[GCA_cols_list].sum(axis=1)
pl_df['Sum Poss Ratio'] = pl_df[poss_cols_list].sum(axis=1)
pl_df['Sum Defence Ratio'] = pl_df[defence_cols_list].sum(axis=1)
pl_df['Sum Pass Ratio'] = pl_df[pass_cols_list].sum(axis=1)
#pl_df['Sum Shoot Ratio'] = pl_df[shooting_cols_list].sum(axis=1)

#in pl_df sum sca ratio column remove column with 0 values
pl_adv_gk = pl_adv_gk[pl_adv_gk['Sum PSxG'] != 0]
pl_df = pl_df[pl_df['Sum SCA Ratio'] != 0]
pl_df = pl_df[pl_df['Sum GCA Ratio'] != 0]
pl_df = pl_df[pl_df['Sum Poss Ratio'] != 0]
pl_df = pl_df[pl_df['Sum Defence Ratio'] != 0]
pl_df = pl_df[pl_df['Sum Pass Ratio'] != 0]
#pl_df = pl_df[pl_df['Sum Shoot Ratio'] != 0]

#in pl_df players column remove rows with the same values
pl_df = pl_df.drop_duplicates(subset='Player')

#in sidebar "select a team" dropdown menu from pl_df
with st.sidebar:
    st.image(
        "premierleague.png",
        use_column_width=True)
    with st.form('Form1'):
        team = st.selectbox(
            'Select a team',
            pl_df['Squad'].unique())
        player = st.selectbox(
            'Select a player',
            (pl_df[pl_df['Squad'] == team]['Player'].unique()))
       
        mlplayer = pl_df[pl_df['Player'] == player]
        #using K means clustering to cluster players based on attributes
        #if player is a GK then cluster based on GK attributes
    
        player_df = pl_df[pl_df['Pos'] == mlplayer['Pos'].iloc[0]]
        
        km = KMeans(n_clusters=5, init='random', random_state=0)
        #y_km_gk = km.fit_predict(gk_df[gk_cols_list])
        y_km_sca = km.fit_predict(player_df[SCA_cols_list])
        y_km_gca = km.fit_predict(player_df[GCA_cols_list])
        y_km_poss = km.fit_predict(player_df[poss_cols_list])
        y_km_pass = km.fit_predict(player_df[pass_cols_list])
        y_km_def = km.fit_predict(player_df[defence_cols_list])
        #y_km_shoot = km.fit_predict(player_df[shoot_cols_list])

        #gk_df['PSxG'] = y_km_gk
        player_df['SCA'] = y_km_sca
        player_df['GCA'] = y_km_gca
        player_df['Poss'] = y_km_poss
        player_df['Pass'] = y_km_pass
        player_df['Defence'] = y_km_def
        #player_df['Cluster Shoot'] = y_km_shoot
        player_df_pass = player_df[player_df['Pass'] == player_df['Pass'].iloc[0]]   
        player_df_sca = player_df[player_df['SCA'] == player_df['SCA'].iloc[0]]
        player_df_gca = player_df[player_df['GCA'] == player_df['GCA'].iloc[0]]
        player_df_poss = player_df[player_df['Poss'] == player_df['Poss'].iloc[0]]
        player_df_def = player_df[player_df['Defence'] == player_df['Defence'].iloc[0]]
        #gk_df_pass = gk_df[gk_df['PSxG'] == gk_df['PsxG'].iloc[0]]
        #rating = st.slider(
            #'Select a Rating',0,100,50)
        
        passing = player_df_pass[['Player', 'MP', 'Starts', 'Min', 'Pass']]
        passing = passing.rename(columns={'Pass': 'Passing'})
        shooting = player_df_sca[['Player', 'MP', 'Starts', 'Min', 'SCA']]
        shooting = shooting.rename(columns={'SCA': 'Shooting'})
        defending = player_df_def[['Player', 'MP', 'Starts', 'Min', 'Defence']]
        defending = defending.rename(columns={'Defence': 'Defending'})
        gca = player_df_gca[['Player', 'MP', 'Starts', 'Min', 'GCA']]
        gca = gca.rename(columns={'GCA': 'Goal Creation'})
        poss = player_df_poss[['Player', 'MP', 'Starts', 'Min', 'Poss']]
        poss = poss.rename(columns={'Poss': 'Possession'})
        #gk = gk_df_pass[['Player', 'MP', 'Starts', 'Min', 'PSxG']]
        #gk = gk_df_pass.rename(columns={'PSxG': 'Goal Keeping'})


        group = st.selectbox(
            #when passing is selected just show the player name and 
            'Select attribute to find similar players',
            ('Shooting', 'Passing', 'Defending', 'Goal Creation', 'Possession'))
        
        #if 'Cluster Shoot' in group:
            #st.write(shoot)


    

    
        submitted = st.form_submit_button('Run')
        # team = st.sidebar.selectbox('Select a Team',(pl_df['Squad'].unique()))
#in sidebar "select a player", create a dropdown list of all players in selected team
        #player = st.sidebar.selectbox('Select a Player',(pl_df[pl_df['Squad'] == team]['Player'].unique()))

#create a slider to show player of certain rating
        #rating = st.sidebar.slider('Select a Rating',0,100,50)
        
#create st.expander to metric glossary
    with st.expander('Metric Glossary*'):
        st.write('**Rating**:')
        st.write('The rating of a player is the average of their individual metrics. The rating is calculated by taking the average of the individual metrics and multiplying it by 100.')
        st.write('**Cluster**:')
        st.write('The cluster is the group of players that have similar attributes. The cluster is calculated by taking the average of the individual metrics and multiplying it by 100.')
        st.write('**SCA/GCA**:')
        st.write('The SCA/GCA metric is the ratio of shots conceded to shots taken. The SCA/GCA metric is calculated by dividing the number of shots conceded by the number of shots taken.')
        st.write('**Possession**:')
        st.write('The Possession metric is the ratio of shots taken to shots conceded. The Possession metric is calculated by dividing the number of shots taken by the number of shots conceded.') 
        st.write('**Passing**:')
        st.write('The Passing metric is the ratio of passes made to passes received. The Passing metric is calculated by dividing the number of passes made by the number of passes received.')
        st.write('**Defense**:')
        st.write('The Defense metric is the ratio of shots blocked to shots taken. The Defense metric is calculated by dividing the number of shots blocked by the number of shots taken.')
        st.write('**Shooting**:')
        st.write('The Shooting metric is the ratio of shots taken to shots made. The Shooting metric is calculated by dividing the number of shots taken by the number of shots made.')
        st.write('**GCA**:')
        st.write('The GCA metric is the ratio of goals conceded to goals scored. The GCA metric is calculated by dividing the number of goals conceded by the number of goals scored.')
    
if not submitted:
    st.write('In this application, we will be scoring and providing a summary of each premier league player performance based on their stats. \n')
    st.write('This is stricly based on the 2021-22 season. \n')
    st.write('Statistics are collected from fbref.com. and statsbomb \n')
    st.write('The following is a list of all the stats we will be using to score players: \n')
    with st.expander('Credits*'):
        st.write('*This web application was created by:')
        st.write('*Daniel Bosun-Arebuwa ')
        st.write('Website: https://danielbosunarebuwa.github.io/')
        st.write('*Contact:')
    
else:
    row2_1, row2_spacer1, row2_2, row2_spacer2, row2_3, row2_spacer3, row2_4 = st.columns(
    (1.5, .4, 1.6, .8, 1.6, .2, 2.6)
    )
    shootplayer = pl_shoot_df[pl_shoot_df['Player'] == player]
    shootprevplayer = pl_shoot_prev_df[pl_shoot_prev_df['Player'] == player]
    #with row2_1:
        #st.image(f'{player}.png', width=200)
    with row2_2:
        player2 = pl_df[pl_df['Player'] == player]
        #in player 2 nation column remove anything before the first capital letter
        player2['Nation'] = player2['Nation'].str.split(' ').str[0]
        #make all player nation capitalized
        player2['Nation'] = player2['Nation'].str.upper()
        st.write(f'Name: {player2["Player"].iloc[0]}')
        st.write(f'Nation: {player2["Nation"].iloc[0]}')
        st.write(f'Position: {player2["Pos"].iloc[0]}')
        st.write(f'Age: {player2["Age"].iloc[0]}')
    with row2_3:
        #if player pos is GK, then show gk stats
        playergk = pl_gk[pl_gk['Player'] == player]
        playergkprev = pl_gk_prev[pl_gk_prev['Player'] == player]
        standardplayer = pl_prev_df[pl_prev_df['Player'] == player]
        prevdefense = pl_def_prev[pl_def_prev['Player'] == player]
        possprev = pl_poss_prev[pl_poss_prev['Player'] == player]
        playermisc = pl_misc[pl_misc['Player'] == player]
        playermiscprev = pl_misc_prev[pl_misc_prev['Player'] == player]
        playerpass = pl_pass[pl_pass['Player'] == player]
        playerpassprev = pl_pass_prev_df[pl_pass_prev_df['Player'] == player]
        st.text("2021-22")
        if player2['Pos'].iloc[0] == 'GK':
            if player2["Player"].iloc[0] in prevdefense["Player"].values:
                st.metric(
                    label="Clean Sheets",
                    value=round(playergk["CS"].iloc[0],2),
                    #if player is in the top 10% of clean sheets, show a star
                    delta=round(playergk["CS"].iloc[0] - playergkprev["CS"].iloc[0],2),
            )
            else:
                st.metric(
                    label="Clean Sheets",
                    value=round(playergk["CS"].iloc[0])
            )
        elif player2['Pos'].iloc[0] == 'DF':
            if player2["Player"].iloc[0] in prevdefense["Player"].values:
                st.metric(
                    label="Tackle%",
                    value=round(player2["Tkl%"].iloc[0],2),
                    delta=round(player2["Tkl%"].iloc[0] - prevdefense["Tkl%"].loc[player2["Tkl%"].iloc[0]],2)
                )
            else:
                st.metric(
                    label="Tackle%",
                    value=round(player2["Tkl%"].iloc[0],2))
        elif player2['Pos'].iloc[0] == 'MF':
            if player2["Player"].iloc[0] in prevdefense["Player"].values:
                st.metric(
                    label="Successful Dribbles",
                    value=round(player2["Succ%"].iloc[0],2),
                    delta=round(player2["Succ%"].iloc[0] - possprev["Succ%"].iloc[0],2)
            )
            else:
                st.metric(
                    label="Successful Dribbles",
                    value=round(player2["Succ%"].iloc[0]))
        else:
            if player2["Player"].iloc[0] in prevdefense["Player"].values:
                st.metric(
                    label="Expected Goals + Assists",
                    value=round(player2["npxG+xA"].iloc[0]),
                    delta=round(player2["npxG+xA"].iloc[0] - standardplayer["npxG+xA"].iloc[0])
                    
                )
        
            else:
                st.metric(
                    label="Expected Goals + Assists",
                    value=round(player2["npxG+xA"].iloc[0]))
                    
        if player2['Pos'].iloc[0] == 'GK':
            if player2["Player"].iloc[0] in prevdefense["Player"].valuess:
                st.metric(
                    label="Save %",
                    value=round(playergk["Save%"].iloc[0]),
                    delta=round(playergk["Save%"].iloc[0] - playergkprev["Save%"].iloc[0])
            )
            else:
                st.metric(
                    label="Save %",
                    value=round(playergk["Save%"].iloc[0]))

        elif player2['Pos'].iloc[0] == 'DF':
            if player2["%"].iloc[0] in prevdefense["%"].values:
                st.metric(
                    label="Duels Won%",
                    value=round(player2["%"].iloc[0]),
                    delta=round(player2["%"].iloc[0] - prevdefense["%"].loc[player2["Player"].iloc[0]])
                )
            else:
                st.metric(
                    label="Duels Won%",
                    value=round(player2["%"].iloc[0])
                )
        elif player2['Pos'].iloc[0] == 'MF':
            if player2["Player"].iloc[0] in prevdefense["Player"].values:
                st.metric(
                    label="Progressive Carries",
                    value=round(player2["CProg"].iloc[0]),
                    delta=round(player2["CProg"].iloc[0] - possprev["Prog"].iloc[0]),
            )
            else:
                st.metric(
                    label="Progressive Carries",
                    value=round(player2["CProg"].iloc[0]))
        else:
            if player2["Player"].iloc[0] in prevdefense["Player"].values:
                st.metric(
                    label="Pass Completion%",
                    value=playerpass["Cmp%"].iloc[0],
                    delta=round(playerpass["Cmp%"].iloc[0] - playerpassprev["Cmp%"].iloc[0])
            )
            else:
                st.metric(
                    label="Pass Completion%",
                    value=playerpass["Cmp%"].iloc[0])

    with row2_4:
        playerpass = pl_pass[pl_pass['Player'] == player]
        playerpassprev = pl_pass_prev_df[pl_pass_prev_df['Player'] == player]
        advancedgk = pl_adv_gk[pl_adv_gk['Player'] == player]
        advancedgkprev = pl_adv_gk_prev[pl_adv_gk_prev['Player'] == player]
        playerscaprev = pl_sca_gca_prev[pl_sca_gca_prev['Player'] == player]
        st.text(f'GP: {player2["MP"].iloc[0]}')
        if player2['Pos'].iloc[0] == 'GK':
            if player2["Player"].iloc[0] in prevdefense["Player"].values:
                st.metric(
                    label="Goals Against Per 90",
                    value=playergk["GA90"].iloc[0],
                    delta=playergk["GA90"].iloc[0] - playergkprev["GA90"].iloc[0],
            )
            else:
                st.metric(
                    label="Goals Against Per 90",
                    value=playergk["GA90"].iloc[0]
            )
        elif player2['Pos'].iloc[0] == 'DF':
            if player2["Player"].iloc[0] in prevdefense["Player"].values:
                st.metric(
                label="Blocks",
                value=round(player2["Blocks"].iloc[0]),
                delta=round(player2["Blocks"].iloc[0] - prevdefense["Blocks"].iloc[0]),
            )
            else:
                st.metric(
                label="Blocks",
                value=round(player2["Blocks"].iloc[0]),
            )
        elif player2['Pos'].iloc[0] == 'MF':
            if player2["Player"].iloc[0] in prevdefense["Player"].values:
                st.metric(
                    label="Expected Goals + Assists",
                    value=player2["npxG+xA"].iloc[0],
                    delta=player2["npxG+xA"].iloc[0] - standardplayer["npxG+xA"].iloc[0],
            )
            else:
                st.metric(
                    label="Expected Goals + Assists",
                    value=player2["npxG+xA"].iloc[0],
            )
        else:
            if player2["Player"].iloc[0] in standardplayer["Player"].values:
                st.metric(
                    label="Expected Goals + Assists per 90",
                    value=player2["xG+xA"].iloc[0],
                    delta=round(player2["xG+xA"].iloc[0] - standardplayer["xG+xA"].iloc[0])
            )
            else:
                st.metric(
                label="Expected Goals + Assists per 90",
                value=player2["xG+xA"].iloc[0]
            )

   
        if player2['Pos'].iloc[0] == 'GK':
            if player2["Player"].iloc[0] in prevdefense["Player"].values:
                st.metric(
                    label="Launch %",
                    value=round(advancedgk["Launch%"].iloc[0]),
                    delta=round(advancedgk["Launch%"].iloc[0] - advancedgkprev["Launch%"].iloc[0]),
            )
            else:
                st.metric(
                    label="Launch %",
                    value=round(advancedgk["Launch%"].iloc[0]),
            )
        elif player2['Pos'].iloc[0] == 'DF':
            if playermisc["Player"].iloc[0] in prevdefense["Player"].values:
                st.metric(
                    label="Duels Won%",
                    value=round(playermisc["Won%"].iloc[0]),
                    delta=round(playermisc["Won%"].iloc[0] - playermiscprev["Won%"].iloc[0]),
            )
            else:
                st.metric(
                    label="Duels Won%",
                    value=round(playermisc["Won%"].iloc[0]),
            )
            
        elif player2['Pos'].iloc[0] == 'MF':
            if player2["Player"].iloc[0] in prevdefense["Player"].values:
                    st.metric(
                    label="Shot Creation per 90",
                    value=player2["SCA90"].iloc[0],
                    delta=round(player2["SCA90"].iloc[0] - playerscaprev["SCA90"].iloc[0]),
            )
        else:
            if player2["Player"].iloc[0] in playerscaprev["Player"].values:
                st.metric(
                    label="Goal Creation per 90",
                    value=player2["GCA90"].iloc[0],
                    delta=round(player2["GCA90"].iloc[0] - playerscaprev["GCA90"].iloc[0])
            )
            
            
            
    row3_1, row3_2,  = st.columns(
    (3,4)
    )
    with row3_1:
        st.text("Similar Players")
        player_df = pl_df[pl_df['Pos'] == player2['Pos'].iloc[0]]
        km = KMeans(n_clusters=5, init='random', random_state=0)
        y_km_sca = km.fit_predict(player_df[SCA_cols_list])
        y_km_gca = km.fit_predict(player_df[GCA_cols_list])
        y_km_poss = km.fit_predict(player_df[poss_cols_list])
        y_km_pass = km.fit_predict(player_df[pass_cols_list])
        y_km_def = km.fit_predict(player_df[defence_cols_list])
        #y_km_shoot = km.fit_predict(player_df[shoot_cols_list])

        player_df['SCA'] = y_km_sca
        player_df['GCA'] = y_km_gca
        player_df['Poss'] = y_km_poss
        player_df['Pass'] = y_km_pass
        player_df['Defence'] = y_km_def
        #player_df['Cluster Shoot'] = y_km_shoot
        player_df_pass = player_df[player_df['Pass'] == player_df['Pass'].iloc[0]]   
        player_df_sca = player_df[player_df['SCA'] == player_df['SCA'].iloc[0]]

        #st.dataframe(player_df_pass[['Player', 'MP', 'Starts', 'Min', 'SCA', 'GCA', 'Poss', 'Pass', 'Defence']])
        if 'Shooting' in group:
            st.write(shooting)
        if 'Passing' in group:
            st.write(passing)
        if 'Defending' in group:
            st.write(defending)
        if 'Goal Creation' in group:
            st.write(gca)
        if 'Possession' in group:
            st.write(poss)
        if 'Goalkeeping' in group:
            st.write(goalkeeping)
        
        #show in player_df in the same pass cluster
    
    with row3_2:
        hover_text = []
        bubble_size = []
        if player2['Pos'].iloc[0] == 'GK':
            for i in range(len(player_df)):
                hover_text.append(player_df['Player'].iloc[i])
                bubble_size.append(player_df['MP'].iloc[i])
            fig = go.Figure(data=[go.Scatter(x=player_df['xG'], y=player_df['xG+xA'],
            text=hover_text, mode='markers', marker=dict(size=bubble_size, color=player_df['SCA'], colorscale='Viridis', showscale=True))])
            fig.update_layout(title='Similarity of Players', xaxis_title='xG+xA', yaxis_title='Goals + Assists')
            #highlight the player
            fig.update_traces(marker=dict(color=player_df['SCA'],
                                            colorscale='Viridis',
                                            showscale=True,
                                            line=dict(color='rgb(0,0,0)', width=1)))

            st.plotly_chart(fig)

        elif player2['Pos'].iloc[0] == 'DF':
            for i in range(len(player_df)):
                hover_text.append(player_df['Player'].iloc[i])
                bubble_size.append(player_df['MP'].iloc[i])
            fig = go.Figure(data=[go.Scatter(x=player_df['Succ%'], y=player_df['Tkl+Int'],
            text=hover_text, mode='markers', marker=dict(size=bubble_size, color=player_df['SCA'], colorscale='Viridis', showscale=True))])
            fig.update_layout(title='Similarity of Players', xaxis_title='Successful Passes', yaxis_title='Tackles + Interceptions')
            #highlight the player
            fig.update_traces(marker=dict(color=player_df['SCA'],
                                            colorscale='Viridis',
                                            showscale=True,
                                            line=dict(color='rgb(0,0,0)', width=1)))

            st.plotly_chart(fig)

        elif player2['Pos'].iloc[0] == 'MF':
            for i in range(len(player_df)):
                hover_text.append(player_df['Player'].iloc[i])
                bubble_size.append(player_df['MP'].iloc[i])
            fig = go.Figure(data=[go.Scatter(x=player_df['KP'], y=player_df['GCA90'],
            text=hover_text, mode='markers', marker=dict(size=bubble_size, color=player_df['SCA'], colorscale='Viridis', showscale=True))])
            fig.update_layout(title='Similarity of Players', xaxis_title='xG+xA', yaxis_title='Goals + Assists')
            #highlight the player
            fig.update_traces(marker=dict(color=player_df['SCA'],
                                            colorscale='Viridis',
                                            showscale=True,
                                            line=dict(color='rgb(0,0,0)', width=1)))

            st.plotly_chart(fig)

        elif player2['Pos'].iloc[0] == 'FW':
            for i in range(len(player_df)):
                hover_text.append(player_df['Player'].iloc[i])
                bubble_size.append(player_df['MP'].iloc[i])
            fig = go.Figure(data=[go.Scatter(x=player_df['Gls'], y=player_df['xG'],
            text=hover_text, mode='markers', marker=dict(size=bubble_size, color=player_df['SCA'], colorscale='Viridis', showscale=True))])
            fig.update_layout(title='Similarity of Players', xaxis_title='xG+xA', yaxis_title='Goals + Assists')
            #highlight the player
            fig.update_traces(marker=dict(color=player_df['SCA'],
                                            colorscale='Viridis',
                                            showscale=True,
                                            line=dict(color='rgb(0,0,0)', width=1)))

            st.plotly_chart(fig)
        

        #st.write(player_df[player_df['Cluster'] == y_km[0]][['Player', 'MP', 'Starts', 'Cluster']])
        #st.write(player_df[['Player', 'MP', 'Starts', 'Min', 'Cluster']].sort_values(by=['Cluster', 'MP'], ascending=False))



        #player_df[player_df['Cluster'] == 2]
        
    

    #row4_1, row4_2 = st.columns(
    #(2.5, 0.6)
    #)
    #with row4_1:
        #using plotly bubble chart to show the similarity of the players
        #st.text("Similarity of Players")
        
            #player_df
