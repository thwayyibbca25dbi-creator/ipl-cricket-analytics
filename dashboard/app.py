

import streamlit as st

import pandas as pd

import plotly.graph_objects as go



# ================= PAGE CONFIG =================

st.set_page_config(

          page_title="IPL Matches Dashboard",

          page_icon="🏏",

          layout="wide"

)



# ================= DARK BLUE COLOUR THEME =================

st.markdown("""

<style>

/* Main background */

.stApp {

          background-color: #101B2D;

          color: #E8EEF7;

}



/* Main content */

.block-container {

          padding-top: 1.2rem;

          padding-bottom: 1rem;

          max-width: 1400px;

}



/* Headings */

h1 {

          color: #EAF2FF !important;

          font-size: 25px !important;

}



h2, h3 {

          color: #BBD0F0 !important;

}



p, label, .stMarkdown, .stCaption {

          color: #C4D0E0;

}



/* Metric cards */

div[data-testid="stMetric"] {

          background: #1B2B43;

          border: 1px solid #344B6B;

          border-radius: 10px;

          padding: 12px;

}



/* Custom cards */

div[data-testid="stPlotlyChart"] {

          background: #18263B;

          border: 1px solid #344B6B;

          border-radius: 10px;

          padding: 5px;

}



/* Tabs */

button[data-baseweb="tab"] {

          color: #B8C9E3;

}



button[data-baseweb="tab"][aria-selected="true"] {

          color: #8DB8FF;

}



/* Multiselect */

div[data-baseweb="select"] > div {

          background-color: #1B2B43;

          border-color: #405779;

          color: #E8EEF7;

}



/* Select menu text */

div[data-baseweb="popover"] {

          background-color: #1B2B43;

}



/* Buttons */

.stDownloadButton button {

          background-color: #315A91;

          color: white;

          border: 1px solid #527DB6;

          border-radius: 7px;

}



/* Dividers */

hr {

          border-color: #344B6B;

}

</style>

""", unsafe_allow_html=True)



# ================= COLOUR PALETTE =================

BLUE = "#6F9FE8"

ORANGE = "#F0A66A"

BG = "#18263B"

TEXT = "#DCE7F5"

GRID = "#34445B"



def chart_style(fig, height=220):

          fig.update_layout(

                    height=height,

                    paper_bgcolor=BG,

                    plot_bgcolor=BG,

                    font=dict(color=TEXT, size=10),

                    margin=dict(l=20, r=12, t=20, b=30),

                    legend=dict(

                              font=dict(color=TEXT),

                              bgcolor="rgba(0,0,0,0)"

                    )

          )

          fig.update_xaxes(

                    showgrid=False,

                    color=TEXT,

                    linecolor=GRID

          )

          fig.update_yaxes(

                    gridcolor=GRID,

                    zeroline=False,

                    color=TEXT,

                    linecolor=GRID

          )

          return fig



def card(title, value):
    # Keep the HTML compact so Streamlit renders it as a card, not visible CSS text.
    st.markdown(
        f'<div style="background-color:#1B2B43;border:1px solid #344B6B;'
        f'border-radius:10px;padding:12px;min-height:75px;">'
        f'<div style="font-size:10px;color:#A9BCD5;margin-bottom:8px;">{title}</div>'
        f'<div style="font-size:19px;font-weight:700;color:#EAF2FF;">{value}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )


# ================= DEMO DATA =================

# Replace these values with actual IPL CSV data

# to make the statistics accurate.



matches = pd.DataFrame({

          "season": [2019, 2019, 2020, 2020, 2021, 2021,

                                       2022, 2022, 2023, 2023, 2024, 2024],

          "team1": ["MI", "CSK", "MI", "DC", "CSK", "MI",

                                   "GT", "RR", "CSK", "GT", "KKR", "RCB"],

          "team2": ["CSK", "MI", "DC", "MI", "MI", "CSK",

                                   "RR", "GT", "GT", "CSK", "SRH", "CSK"],

          "winner": ["MI", "CSK", "MI", "DC", "CSK", "MI",

                                       "GT", "RR", "CSK", "GT", "KKR", "RCB"],

          "toss_winner": ["MI", "CSK", "MI", "DC", "CSK", "MI",

                                                  "GT", "RR", "CSK", "GT", "KKR", "RCB"],

          "toss_decision": ["bat", "field", "bat", "field",

                                                       "bat", "field", "bat", "field",

                                                       "bat", "field", "bat", "field"],

          "venue": ["Mumbai", "Delhi", "Dubai", "Abu Dhabi",

                                   "Chennai", "Mumbai", "Mumbai", "Pune",

                                   "Mumbai", "Chennai", "Chennai", "Bengaluru"],

          "first_score": [170, 155, 195, 175, 160, 180,

                                                  185, 190, 178, 165, 222, 187],

          "second_score": [165, 158, 185, 178, 155, 175,

                                                      180, 185, 170, 168, 210, 180],

          "first_wickets": [6, 8, 5, 7, 6, 4, 7, 5, 8, 6, 6, 9],

          "second_wickets": [8, 6, 7, 6, 8, 7, 8, 7, 9, 7, 8, 6]

})



# Sample over-by-over values for Tab 1

overs = list(range(1, 21))

srh_runs = [8,12,6,15,7,10,9,13,5,11,14,8,16,7,12,10,15,9,11,10]

rcb_runs = [6,10,12,8,11,7,13,9,14,6,10,12,8,15,7,11,9,13,10,9]

wickets = [0,1,0,2,1,0,1,1,0,2,1,0,1,2,0,1,1,0,2,1]



# ================= HEADER =================

st.title("🏏 IPL MATCHES DASHBOARD")

st.caption("IPL Match Analytics | Interactive dashboard")



tab1, tab2 = st.tabs([

          "📊 Tab 1 — Match Analysis",

          "📈 Tab 2 — Season Statistics"

])



# ==================================================

# TAB 1: MATCH ANALYSIS

# ==================================================

with tab1:

          st.subheader("Match Summary")



          c1, c2, c3 = st.columns(3)

          with c1:

                    card("RESULT", "SRH won by 8 runs")

          with c2:

                    card("1ST INNINGS — SRH", "208 / 7")

          with c3:

                    card("2ND INNINGS — RCB", "200 / 7")



          st.write("")

          st.subheader("Runs per over — innings comparison")



          fig1 = go.Figure()

          fig1.add_bar(

                    x=overs, y=srh_runs, name="SRH",

                    marker_color=BLUE

          )

          fig1.add_bar(

                    x=overs, y=rcb_runs, name="RCB",

                    marker_color=ORANGE

          )

          fig1.update_layout(

                    barmode="group",

                    xaxis_title="Over",

                    yaxis_title="Runs",

                    legend=dict(orientation="h", y=1.12, x=1,

                                                  xanchor="right")

          )

          chart_style(fig1, 250)

          st.plotly_chart(fig1, use_container_width=True)



          left, right = st.columns(2)



          with left:

                    st.subheader("Fours and sixes")

                    fig2 = go.Figure()

                    fig2.add_bar(

                              x=["SRH", "RCB"], y=[18, 15],

                              name="Fours", marker_color=BLUE

                    )

                    fig2.add_bar(

                              x=["SRH", "RCB"], y=[12, 13],

                              name="Sixes", marker_color=ORANGE

                    )

                    fig2.update_layout(

                              barmode="group",

                              legend=dict(orientation="h", y=1.12, x=1,

                                                            xanchor="right")

                    )

                    chart_style(fig2, 190)

                    st.plotly_chart(fig2, use_container_width=True)



          with right:

                    st.subheader("Toss: SRH won and chose to bat")

                    fig3 = go.Figure(go.Pie(

                              labels=["Chose to bat", "Chose to field"],

                              values=[1, 0],

                              hole=0.65,

                              marker_colors=[BLUE, ORANGE],

                              textinfo="none"

                    ))

                    fig3.update_layout(

                              height=190,

                              paper_bgcolor=BG,

                              font=dict(color=TEXT),

                              annotations=[dict(

                                        text="SRH", x=0.5, y=0.5,

                                        showarrow=False,

                                        font=dict(size=15, color="#EAF2FF")

                              )],

                              margin=dict(l=10, r=10, t=10, b=10)

                    )

                    st.plotly_chart(fig3, use_container_width=True)



          left, right = st.columns(2)



          with left:

                    st.subheader("Wickets by over")

                    fig4 = go.Figure(go.Bar(

                              x=overs, y=wickets,

                              marker_color=BLUE

                    ))

                    fig4.update_layout(

                              xaxis_title="Over",

                              yaxis_title="Wickets"

                    )

                    chart_style(fig4, 190)

                    st.plotly_chart(fig4, use_container_width=True)



          with right:

                    st.subheader("Runs by match phase")

                    phases = ["Powerplay", "Middle", "Death"]

                    fig5 = go.Figure()

                    fig5.add_bar(

                              x=phases, y=[65, 82, 61],

                              name="SRH", marker_color=BLUE

                    )

                    fig5.add_bar(

                              x=phases, y=[58, 85, 57],

                              name="RCB", marker_color=ORANGE

                    )

                    fig5.update_layout(

                              barmode="group",

                              xaxis_title="Match phase",

                              yaxis_title="Runs",

                              legend=dict(orientation="h", y=1.12, x=1,

                                                            xanchor="right")

                    )

                    chart_style(fig5, 190)

                    st.plotly_chart(fig5, use_container_width=True)



# ==================================================

# TAB 2: SEASON STATISTICS

# ==================================================

with tab2:

          st.subheader("Season Statistics")



          available_seasons = sorted(matches["season"].unique())

          selected_seasons = st.multiselect(

                    "Filter by season",

                    available_seasons,

                    default=available_seasons,

                    key="season_filter"

          )



          df = matches[matches["season"].isin(selected_seasons)].copy()



          if df.empty:

                    st.warning("Please select at least one season.")

          else:

                    total_matches = len(df)

                    total_runs = int(

                              df["first_score"].sum() + df["second_score"].sum()

                    )

                    highest_score = int(max(

                              df["first_score"].max(),

                              df["second_score"].max()

                    ))

                    average_score = (

                              df["first_score"].mean()

                              + df["second_score"].mean()

                    ) / 2



                    c1, c2, c3 = st.columns(3)

                    with c1:

                              card("MATCHES | SEASONS",

                                            f"{total_matches} | {df['season'].nunique()}")

                    with c2:

                              card("TOTAL RUNS", f"{total_runs:,}")

                    with c3:

                              card("HIGHEST INNINGS SCORE", str(highest_score))



                    st.write("")

                    st.subheader("Average innings score by season")



                    df["match_average"] = (

                              df["first_score"] + df["second_score"]

                    ) / 2



                    avg_season = df.groupby("season")["match_average"].mean()



                    fig6 = go.Figure(go.Bar(

                              x=avg_season.index.astype(str),

                              y=avg_season.values,

                              marker_color=BLUE

                    ))

                    fig6.update_layout(yaxis_title="Average runs")

                    chart_style(fig6, 230)

                    st.plotly_chart(fig6, use_container_width=True)



                    left, right = st.columns(2)



                    with left:

                              st.subheader("Chasing win rate by season")



                              # Simplified: assumes second innings is the chasing side.

                              df["chasing_won"] = (

                                        df["second_score"] > df["first_score"]

                              )

                              chase_rate = (

                                        df.groupby("season")["chasing_won"].mean() * 100

                              )



                              fig7 = go.Figure(go.Bar(

                                        x=chase_rate.index.astype(str),

                                        y=chase_rate.values,

                                        marker_color=BLUE

                              ))

                              fig7.update_layout(

                                        yaxis_title="Chasing wins (%)",

                                        yaxis=dict(range=[0, 100])

                              )

                              chart_style(fig7, 200)

                              st.plotly_chart(fig7, use_container_width=True)



                    with right:

                              st.subheader("Runs by season")



                              runs_season = df.groupby("season").agg(

                                        first=("first_score", "sum"),

                                        second=("second_score", "sum")

                              )



                              fig8 = go.Figure()

                              fig8.add_bar(

                                        x=runs_season.index.astype(str),

                                        y=runs_season["first"],

                                        name="First innings",

                                        marker_color=BLUE

                              )

                              fig8.add_bar(

                                        x=runs_season.index.astype(str),

                                        y=runs_season["second"],

                                        name="Second innings",

                                        marker_color=ORANGE

                              )

                              fig8.update_layout(

                                        barmode="group",

                                        yaxis_title="Runs",

                                        legend=dict(orientation="h", y=1.12, x=1,

                                                                      xanchor="right")

                              )

                              chart_style(fig8, 200)

                              st.plotly_chart(fig8, use_container_width=True)



                    left, right = st.columns(2)



                    with left:

                              st.subheader("Toss winners choose to bat or field")



                              toss_counts = df["toss_decision"].value_counts()



                              fig9 = go.Figure(go.Bar(

                                        x=toss_counts.index,

                                        y=toss_counts.values,

                                        marker_color=[

                                                  BLUE if decision == "bat" else ORANGE

                                                  for decision in toss_counts.index

                                        ]

                              ))

                              fig9.update_layout(yaxis_title="Matches")

                              chart_style(fig9, 210)

                              st.plotly_chart(fig9, use_container_width=True)



                    with right:

                              st.subheader("How teams win")



                              wins = df["winner"].value_counts()

                              win_percent = wins / wins.sum() * 100



                              top_teams = win_percent.head(2)

                              c1, c2 = st.columns(2)



                              if len(top_teams) >= 1:

                                        c1.metric(

                                                  f"{top_teams.index[0]} WINS",

                                                  f"{top_teams.iloc[0]:.0f}%"

                                        )

                              if len(top_teams) >= 2:

                                        c2.metric(

                                                  f"{top_teams.index[1]} WINS",

                                                  f"{top_teams.iloc[1]:.0f}%"

                                        )



                              fig10 = go.Figure(go.Pie(

                                        labels=wins.index,

                                        values=wins.values,

                                        hole=0.60,

                                        marker=dict(colors=[

                                                  BLUE if i % 2 == 0 else ORANGE

                                                  for i in range(len(wins))

                                        ])

                              ))

                              fig10.update_layout(

                                        height=210,

                                        paper_bgcolor=BG,

                                        plot_bgcolor=BG,

                                        font=dict(color=TEXT),

                                        margin=dict(l=10, r=10, t=10, b=10)

                              )

                              st.plotly_chart(fig10, use_container_width=True)



st.caption(

          "IPL Matches Dashboard | Sample data — replace with your IPL CSV files for accurate statistics."

)
