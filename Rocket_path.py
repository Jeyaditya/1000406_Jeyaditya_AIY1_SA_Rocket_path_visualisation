import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

# --- STAGE 1 & 2: App Setup & Data Preprocessing ---
st.set_page_config(page_title="Rocket Path Visualization", layout="wide", page_icon="🚀")
st.title("🚀 Aerospace Mission Control & Flight Simulator")

@st.cache_data
def load_and_clean_data():
    # Load the specific dataset provided
    df = pd.read_csv('rocket_data.csv')
    
    # FIX: Explicitly set dayfirst=True for DD-MM-YYYY format
    df['Launch Date'] = pd.to_datetime(df['Launch Date'], dayfirst=True)
    
    # Ensure numerical columns are correctly typed
    numeric_cols = [
        'Distance from Earth (light-years)', 'Mission Duration (years)', 
        'Mission Cost (billion USD)', 'Scientific Yield (points)', 
        'Mission Success (%)', 'Fuel Consumption (tons)', 'Payload Weight (tons)'
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        
    return df

try:
    df = load_and_clean_data()
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# --- SIDEBAR: Control Center ---
st.sidebar.header("🛠️ Mission Configuration")

# Filters
target_type = st.sidebar.multiselect("Select Target Type", options=df['Target Type'].unique(), default=df['Target Type'].unique())
vehicle_type = st.sidebar.multiselect("Select Launch Vehicle", options=df['Launch Vehicle'].unique(), default=df['Launch Vehicle'].unique())
success_threshold = st.sidebar.slider("Minimum Success Rate (%)", 0, 100, 0)

# Filter Data
filtered_df = df[
    (df['Target Type'].isin(target_type)) & 
    (df['Launch Vehicle'].isin(vehicle_type)) & 
    (df['Mission Success (%)'] >= success_threshold)
]

# --- STAGE 2: Data Visualization & EDA ---
st.header("📊 Mission Data Analysis")

# KPI Summary
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Missions", len(filtered_df))
col2.metric("Avg Success Rate", f"{filtered_df['Mission Success (%)'].mean():.1f}%")
col3.metric("Total Cost", f"${filtered_df['Mission Cost (billion USD)'].sum():,.0f}B")
col4.metric("Avg Payload", f"{filtered_df['Payload Weight (tons)'].mean():.1f} Tons")

tab1, tab2, tab3 = st.tabs(["Performance Trends", "Financial Analysis", "Correlations"])

with tab1:
    st.subheader("Payload vs. Fuel Efficiency")
    fig1 = px.scatter(filtered_df, x="Payload Weight (tons)", y="Fuel Consumption (tons)", 
                     color="Launch Vehicle", size="Scientific Yield (points)",
                     hover_name="Mission Name", trendline="ols",
                     template="plotly_dark")
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    st.subheader("Mission Cost Distribution by Vehicle")
    fig2 = px.box(filtered_df, x="Launch Vehicle", y="Mission Cost (billion USD)", 
                 color="Launch Vehicle", template="plotly_dark")
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.subheader("Mathematical Correlation Matrix")
    # Using specific numerical columns for heatmap
    corr_df = filtered_df[['Distance from Earth (light-years)', 'Mission Duration (years)', 
                           'Mission Cost (billion USD)', 'Scientific Yield (points)', 
                           'Fuel Consumption (tons)', 'Payload Weight (tons)']].corr()
    
    fig_heat, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr_df, annot=True, cmap='RdBu', center=0, ax=ax)
    plt.title("Correlation Between Spacecraft Metrics")
    st.pyplot(fig_heat)

# --- STAGE 3: Rocket Path Simulation (Calculus & Physics) ---
st.divider()
st.header("☄️ Rocket Path Simulation Engine")
st.write("""
This engine calculates the vertical trajectory using **Differential Equations** and **Newton's Second Law** ($F = ma$).
As the rocket burns fuel, its mass ($m$) decreases, which changes the acceleration ($a$) over time.
""")



with st.expander("🔧 Simulation Physics Parameters"):
    c1, c2, c3 = st.columns(3)
    user_thrust = c1.number_input("Engine Thrust (kN)", value=4000, step=500)
    user_payload = c2.slider("Simulation Payload (Tons)", 5, 150, 50)
    user_fuel = c3.slider("Fuel Load (Tons)", 50, 1000, 500)
    
    # Constants
    g = 9.81  # Gravity (m/s^2)
    burn_rate = 2.5 # Tons of fuel burned per second
    dry_mass = 40 # Structural mass of the rocket

# Numerical Integration (Euler Method)
def simulate_flight(thrust_kn, payload_t, fuel_t, structural_t, burn_r):
    dt = 0.5 # half-second intervals
    t_max = 500
    
    # Initialize variables
    time, alt, vel, mass = [0], [0], [0], [structural_t + payload_t + fuel_t]
    current_fuel = fuel_t
    
    for _ in range(int(t_max/dt)):
        m = mass[-1]
        v = vel[-1]
        h = alt[-1]
        
        # Calculate Forces
        # T is thrust, W is weight (m*g), D is drag
        thrust = (thrust_kn / 10) if current_fuel > 0 else 0 
        weight = m * g
        drag = 0.5 * 0.5 * (v**2) * np.exp(-h/10000) # Density drops with altitude
        
        # Acceleration a = (T - W - D) / m
        net_force = (thrust * 1000) - weight - drag
        a = net_force / m
        
        # Update motion (v = v0 + at; h = h0 + vt)
        new_v = v + a * dt
        new_h = h + new_v * dt
        
        if new_h < 0: break # Simulation ends if rocket crashes or doesn't lift
            
        time.append(time[-1] + dt)
        alt.append(new_h)
        vel.append(new_v)
        
        if current_fuel > 0:
            current_fuel -= burn_r * dt
            mass.append(m - burn_r * dt)
        else:
            mass.append(m)
            
    return pd.DataFrame({"Time": time, "Altitude": alt, "Velocity": vel})

if st.button("🚀 Launch Simulation"):
    sim_data = simulate_flight(user_thrust, user_payload, user_fuel, dry_mass, burn_rate)
    
    if len(sim_data) > 1:
        fig_sim = go.Figure()
        fig_sim.add_trace(go.Scatter(x=sim_data["Time"], y=sim_data["Altitude"], 
                                     line=dict(color='#00f2ff', width=3)))
        fig_sim.update_layout(title="Simulated Flight Path: Altitude vs Time", 
                             xaxis_title="Seconds", yaxis_title="Altitude (Meters)",
                             template="plotly_dark")
        st.plotly_chart(fig_sim, use_container_width=True)
        
        st.success(f"Maximum Altitude Reached: {max(sim_data['Altitude']):,.2f} meters")
    else:
        st.error("Launch Failed: Thrust is insufficient to lift the current mass. Increase Thrust or decrease Payload.")

st.markdown("---")
st.caption("Developed for the Summative Assessment: Mathematics for AI-I")
