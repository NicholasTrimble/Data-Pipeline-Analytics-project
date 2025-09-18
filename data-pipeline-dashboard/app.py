import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from src.analytics import compute_kpis

engine = create_engine('sqlite:///data/warehouse.db')

st.title("E-commerce Dashboard")

kpis = compute_kpis()
st.metric("Total Revenue", f"${kpis['total_revenue']:.2f}")
st.metric("Total Orders", kpis['total_orders'])
st.metric("AOV", f"${kpis['avg_order_value']:.2f}")  # fixed key
st.metric("Unique Users", kpis['unique_users'])


orders = pd.read_sql_table("orders", engine, parse_dates=["order_datetime"])
orders["date"] = pd.to_datetime(orders["order_datetime"]).dt.date
daily = orders.groupby("date")["total_price"].sum().reset_index()
st.line_chart(daily, x="date", y="total_price")