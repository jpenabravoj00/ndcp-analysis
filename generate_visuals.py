import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Set style
sns.set_theme(style="whitegrid", font="sans-serif")
plt.rcParams['figure.autolayout'] = True

images_dir = "images"
os.makedirs(images_dir, exist_ok=True)

# Load cleaned dataset
cleaned_data_filename = "ndcp_2008-2022_cleaned.csv"
df = pd.read_csv(cleaned_data_filename, dtype={'county_fips_code': str})
print(f"Loaded {df.shape[0]} rows and {df.shape[1]} columns.")

# -------------------------------------------------------------
# Chart 1: National & Florida Temporal Trend (2008-2022)
# -------------------------------------------------------------
price_trends_df = df.dropna(subset=['mcinfant'])
national_avg = price_trends_df.groupby('studyyear')['mcinfant'].mean().reset_index()
florida_avg = price_trends_df[price_trends_df['state_name'] == 'Florida'].groupby('studyyear')['mcinfant'].mean().reset_index()

plt.figure(figsize=(11, 6), dpi=300)
plt.plot(national_avg['studyyear'], national_avg['mcinfant'], marker='o', linewidth=2.5, markersize=7, color='#1E40AF', label='National Median Care Cost')
if not florida_avg.empty:
    plt.plot(florida_avg['studyyear'], florida_avg['mcinfant'], marker='s', linewidth=2.5, markersize=7, linestyle='--', color='#DC2626', label='Florida Baseline Average')

plt.title('Infant Center-Based Care Weekly Cost Trends (2008–2022)', fontsize=15, fontweight='bold', pad=15)
plt.xlabel('Study Year', fontsize=12, fontweight='bold')
plt.ylabel('Average Weekly Price ($ USD)', fontsize=12, fontweight='bold')
plt.xticks(national_avg['studyyear'], rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('${x:,.0f}'))
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(frameon=True, facecolor='white', framealpha=0.9, fontsize=11, loc='upper left')

start_val = national_avg.iloc[0]['mcinfant']
end_val = national_avg.iloc[-1]['mcinfant']
pct_change = ((end_val - start_val) / start_val) * 100
plt.annotate(f'+{pct_change:.1f}% Growth\n(${start_val:.0f} → ${end_val:.0f}/wk)',
             xy=(national_avg.iloc[-1]['studyyear'], end_val),
             xytext=(national_avg.iloc[-1]['studyyear'] - 3.2, end_val - 20),
             arrowprops=dict(facecolor='#1E40AF', shrink=0.08, width=1.5, headwidth=6),
             fontweight='bold', color='#1E40AF', fontsize=10,
             bbox=dict(boxstyle="round,pad=0.3", fc="#EFF6FF", ec="#1E40AF", lw=1))

plt.tight_layout()
chart1_path = os.path.join(images_dir, "national_infant_cost_trends.png")
plt.savefig(chart1_path, dpi=300)
plt.close()
print(f"Saved: {chart1_path}")

# -------------------------------------------------------------
# Chart 2: State-Level Geographic Price Disparities
# -------------------------------------------------------------
avg_price_by_state = price_trends_df.groupby('state_name')['mcinfant'].mean().sort_values(ascending=False).reset_index()
nat_mean = price_trends_df['mcinfant'].mean()

plt.figure(figsize=(12, 14), dpi=300)
colors = ['#EF4444' if state == 'Florida' else ('#1E3A8A' if price > nat_mean else '#60A5FA') for state, price in zip(avg_price_by_state['state_name'], avg_price_by_state['mcinfant'])]

bars = plt.barh(avg_price_by_state['state_name'], avg_price_by_state['mcinfant'], color=colors, height=0.7)
plt.axvline(nat_mean, color='#B91C1C', linestyle='--', linewidth=1.5, label=f'National Benchmark (${nat_mean:.1f}/wk)')

plt.title('Geographic Disparities in Weekly Infant Childcare Costs by State', fontsize=15, fontweight='bold', pad=15)
plt.xlabel('Average Weekly Infant Care Price ($ USD)', fontsize=12, fontweight='bold')
plt.ylabel('State / Territory', fontsize=12, fontweight='bold')
plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter('${x:,.0f}'))
plt.gca().invert_yaxis()
plt.legend(loc='lower right', fontsize=11, frameon=True, facecolor='white')
plt.tight_layout()

chart2_path = os.path.join(images_dir, "state_cost_disparities.png")
plt.savefig(chart2_path, dpi=300)
plt.close()
print(f"Saved: {chart2_path}")

# -------------------------------------------------------------
# Chart 3: Econometric Correlation (Income vs Childcare Cost)
# -------------------------------------------------------------
corr_df = df[['mcinfant', 'mhi_2022', 'state_name']].dropna()
florida_corr = corr_df[corr_df['state_name'] == 'Florida']
other_corr = corr_df[corr_df['state_name'] != 'Florida']

plt.figure(figsize=(11, 7), dpi=300)
plt.scatter(other_corr['mhi_2022'], other_corr['mcinfant'], color='#94A3B8', alpha=0.35, s=25, label='US Counties')

if not florida_corr.empty:
    plt.scatter(florida_corr['mhi_2022'], florida_corr['mcinfant'], color='#DC2626', alpha=0.85, s=55, edgecolors='black', linewidth=0.5, label='Florida Counties')

m, b = np.polyfit(corr_df['mhi_2022'], corr_df['mcinfant'], 1)
x_vals = np.linspace(corr_df['mhi_2022'].min(), corr_df['mhi_2022'].max(), 100)
plt.plot(x_vals, m*x_vals + b, color='#1E40AF', linestyle='-', linewidth=2.5, label=f'OLS Trend (r = {corr_df["mcinfant"].corr(corr_df["mhi_2022"]):.2f})')

plt.title('County Median Household Income vs. Weekly Infant Care Costs', fontsize=15, fontweight='bold', pad=15)
plt.xlabel('Median Household Income (2022 Adjusted $ USD)', fontsize=12, fontweight='bold')
plt.ylabel('Median Weekly Infant Care Price ($ USD)', fontsize=12, fontweight='bold')

# Formatting axes with commas and dollar signs
plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter('${x:,.0f}'))
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('${x:,.0f}'))

plt.legend(frameon=True, facecolor='white', framealpha=0.9, fontsize=11, loc='upper left')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

chart3_path = os.path.join(images_dir, "income_vs_childcare_cost_correlation.png")
plt.savefig(chart3_path, dpi=300)
plt.close()
print(f"Saved: {chart3_path}")

# -------------------------------------------------------------
# Standalone Interactive HTML Report (Plotly) - EXACT MATCHING DESIGN
# -------------------------------------------------------------

# Fig 1: Exact matching colors (#1E40AF for National, #DC2626 dashed for Florida)
fig1 = go.Figure()
fig1.add_trace(go.Scatter(
    x=national_avg['studyyear'], y=national_avg['mcinfant'],
    mode='lines+markers', name='National Median Care Cost',
    line=dict(color='#1E40AF', width=3),
    marker=dict(size=8, symbol='circle'),
    hovertemplate='<b>Year %{x}</b><br>National Average: $%{y:.2f}/wk<extra></extra>'
))
if not florida_avg.empty:
    fig1.add_trace(go.Scatter(
        x=florida_avg['studyyear'], y=florida_avg['mcinfant'],
        mode='lines+markers', name='Florida Baseline Average',
        line=dict(color='#DC2626', width=3, dash='dash'),
        marker=dict(size=8, symbol='square'),
        hovertemplate='<b>Year %{x}</b><br>Florida Average: $%{y:.2f}/wk<extra></extra>'
    ))
fig1.update_layout(
    title=dict(text='<b>Infant Center-Based Care Weekly Cost Trends (2008–2022)</b>', font=dict(size=16, color='#0F172A')),
    xaxis=dict(title='<b>Study Year</b>', tickmode='linear', tick0=2008, dtick=1, gridcolor='#E2E8F0'),
    yaxis=dict(title='<b>Average Weekly Price ($ USD)</b>', tickprefix='$', tickformat=',.0f', gridcolor='#E2E8F0'),
    template='plotly_white',
    hovermode='x unified',
    legend=dict(x=0.02, y=0.98, bgcolor='rgba(255,255,255,0.9)', bordercolor='#CBD5E1', borderwidth=1),
    margin=dict(l=50, r=40, t=60, b=50)
)

# Fig 2: Matching custom color list (Red for Florida, Dark Navy #1E3A8A for above avg, Light Blue #60A5FA for below avg)
bar_df = avg_price_by_state.sort_values(by='mcinfant', ascending=True)
bar_colors = ['#EF4444' if state == 'Florida' else ('#1E3A8A' if price > nat_mean else '#60A5FA') for state, price in zip(bar_df['state_name'], bar_df['mcinfant'])]

fig2 = go.Figure()
fig2.add_trace(go.Bar(
    x=bar_df['mcinfant'],
    y=bar_df['state_name'],
    orientation='h',
    marker=dict(color=bar_colors),
    hovertemplate='<b>%{y}</b><br>Average Weekly Cost: $%{x:.2f}<extra></extra>',
    showlegend=False
))
# Add national benchmark vertical line
fig2.add_vline(
    x=nat_mean, line_width=2, line_dash='dash', line_color='#B91C1C',
    annotation_text=f'National Benchmark (${nat_mean:.1f}/wk)',
    annotation_position='bottom right',
    annotation_font=dict(color='#B91C1C', size=11, family='Inter')
)
fig2.update_layout(
    title=dict(text='<b>Geographic Disparities in Weekly Infant Childcare Costs by State</b>', font=dict(size=16, color='#0F172A')),
    xaxis=dict(title='<b>Average Weekly Infant Care Price ($ USD)</b>', tickprefix='$', tickformat=',.0f', gridcolor='#E2E8F0'),
    yaxis=dict(title='<b>State / Territory</b>', gridcolor='#E2E8F0', dtick=1),
    template='plotly_white',
    height=950,
    margin=dict(l=120, r=40, t=60, b=50)
)

# Fig 3: Matching scatter (Other counties gray #94A3B8, Florida counties red #DC2626 with outline, Navy OLS line #1E40AF)
fig3 = go.Figure()
# US Counties (other)
fig3.add_trace(go.Scatter(
    x=other_corr['mhi_2022'],
    y=other_corr['mcinfant'],
    mode='markers',
    marker=dict(color='#94A3B8', opacity=0.35, size=6),
    text=other_corr['state_name'],
    hovertemplate='<b>%{text}</b><br>Median Income: $%{x:,.0f}<br>Weekly Cost: $%{y:.2f}<extra></extra>',
    name='US Counties'
))
# Florida Counties
if not florida_corr.empty:
    fig3.add_trace(go.Scatter(
        x=florida_corr['mhi_2022'],
        y=florida_corr['mcinfant'],
        mode='markers',
        marker=dict(color='#DC2626', opacity=0.9, size=9, line=dict(color='#000000', width=0.8)),
        text=florida_corr['state_name'],
        hovertemplate='<b>Florida County</b><br>Median Income: $%{x:,.0f}<br>Weekly Cost: $%{y:.2f}<extra></extra>',
        name='Florida Counties'
    ))
# OLS Regression Trend line
reg_x = np.linspace(corr_df['mhi_2022'].min(), corr_df['mhi_2022'].max(), 100)
reg_y = m * reg_x + b
fig3.add_trace(go.Scatter(
    x=reg_x,
    y=reg_y,
    mode='lines',
    line=dict(color='#1E40AF', width=3),
    name=f'OLS Trend (r = {corr_df["mcinfant"].corr(corr_df["mhi_2022"]):.2f})',
    hoverinfo='skip'
))
fig3.update_layout(
    title=dict(text='<b>County Median Household Income vs. Weekly Infant Care Costs</b>', font=dict(size=16, color='#0F172A')),
    xaxis=dict(title='<b>Median Household Income (2022 Adjusted $ USD)</b>', tickprefix='$', tickformat=',.0f', gridcolor='#E2E8F0'),
    yaxis=dict(title='<b>Median Weekly Infant Care Price ($ USD)</b>', tickprefix='$', tickformat=',.0f', gridcolor='#E2E8F0'),
    template='plotly_white',
    legend=dict(x=0.02, y=0.98, bgcolor='rgba(255,255,255,0.9)', bordercolor='#CBD5E1', borderwidth=1),
    margin=dict(l=50, r=40, t=60, b=50)
)

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>National Database of Childcare Prices (NDCP) - Interactive Intelligence Report</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>body {{ font-family: 'Inter', sans-serif; }}</style>
</head>
<body class="bg-slate-50 text-slate-800 antialiased">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
        <!-- Header -->
        <header class="mb-10 pb-6 border-b border-slate-200">
            <div class="flex flex-wrap items-center justify-between gap-4">
                <div>
                    <span class="inline-block px-3 py-1 bg-emerald-100 text-emerald-800 text-xs font-bold rounded-full uppercase tracking-wider mb-2">Interactive Data Intelligence Product</span>
                    <h1 class="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight">National Childcare Affordability & Labor Market Analysis</h1>
                    <p class="mt-2 text-slate-600 text-base sm:text-lg">Author: <span class="font-semibold text-slate-900">José I. Peña Bravo, PhD</span> • Open-Access US DOL NDCP (2008–2022)</p>
                </div>
                <div class="flex gap-3">
                    <a href="https://github.com/jpenabravoj00/ndcp-analysis" target="_blank" class="inline-flex items-center px-4 py-2 bg-slate-900 hover:bg-slate-800 text-white text-sm font-semibold rounded-lg shadow-sm transition">
                        View GitHub Repo
                    </a>
                </div>
            </div>
        </header>

        <!-- KPI Cards -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
            <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
                <p class="text-sm font-medium text-slate-500 uppercase tracking-wider">Overall Price Growth (2008-2022)</p>
                <p class="text-3xl font-extrabold text-blue-600 mt-2">+{pct_change:.1f}%</p>
                <p class="text-xs text-slate-500 mt-1">National average weekly infant care surge from ${start_val:.0f} to ${end_val:.0f}/wk</p>
            </div>
            <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
                <p class="text-sm font-medium text-slate-500 uppercase tracking-wider">Income vs Cost Elasticity</p>
                <p class="text-3xl font-extrabold text-emerald-600 mt-2">r = {corr_df["mcinfant"].corr(corr_df["mhi_2022"]):.2f}</p>
                <p class="text-xs text-slate-500 mt-1">Strong positive correlation between median household income & care costs</p>
            </div>
            <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
                <p class="text-sm font-medium text-slate-500 uppercase tracking-wider">National Average Cost</p>
                <p class="text-3xl font-extrabold text-slate-900 mt-2">${nat_mean:.1f}<span class="text-base text-slate-500 font-normal"> /wk</span></p>
                <p class="text-xs text-slate-500 mt-1">Annualized care benchmark across all reporting US counties</p>
            </div>
        </div>

        <!-- Interactive Visualizations -->
        <div class="space-y-10">
            <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
                <h2 class="text-xl font-bold text-slate-900 mb-2">1. Temporal Trajectory: National & State Benchmark</h2>
                <p class="text-sm text-slate-500 mb-4">Hover over any data point to inspect exact year-by-year price points.</p>
                <div id="chart-trend" class="w-full h-96"></div>
            </div>

            <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
                <h2 class="text-xl font-bold text-slate-900 mb-2">2. Geographic Disparities across US States</h2>
                <p class="text-sm text-slate-500 mb-4">States are color-coded: Dark Blue (Above National Benchmark), Light Blue (Below Benchmark), and Red (Florida).</p>
                <div id="chart-disparity" class="w-full" style="height: 800px;"></div>
            </div>

            <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
                <h2 class="text-xl font-bold text-slate-900 mb-2">3. Econometric Correlation: Household Income vs Childcare Cost</h2>
                <p class="text-sm text-slate-500 mb-4">Interactive scatter plot showing thousands of US counties with Florida highlighted in red.</p>
                <div id="chart-correlation" class="w-full h-96"></div>
            </div>
        </div>

        <!-- Footer -->
        <footer class="mt-12 pt-6 border-t border-slate-200 text-center text-sm text-slate-500">
            <p>© José I. Peña Bravo, PhD | Analysis of National Database of Childcare Prices (NDCP 2008–2022)</p>
        </footer>
    </div>

    <script>
        const fig1Data = {fig1.to_json()};
        const fig2Data = {fig2.to_json()};
        const fig3Data = {fig3.to_json()};

        Plotly.newPlot('chart-trend', fig1Data.data, fig1Data.layout, {{responsive: true}});
        Plotly.newPlot('chart-disparity', fig2Data.data, fig2Data.layout, {{responsive: true}});
        Plotly.newPlot('chart-correlation', fig3Data.data, fig3Data.layout, {{responsive: true}});
    </script>
</body>
</html>
"""

report_path = "ndcp_interactive_report.html"
with open(report_path, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"Saved interactive report: {report_path}")
